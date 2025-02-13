"""
Program for testing South African Reserve Bank quarterly projections model.

Created on Dec 22, 2023
@author: A.Goumilevski
"""
import os
import sys
import numpy as np
import datetime as dt
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))
working_dir = os.path.abspath(path + "/../../..")
sys.path.append(working_dir)
os.chdir(working_dir)

from snowdrop.src.utils.merge import merge
from snowdrop.src.misc.termcolor import cprint

def test(model_file = 'snowdrop/models/QPM/model_Lshocks.model',
         calib_file = 'snowdrop/data/QPM/QPMcalibration_dict.xlsx',
         data_file = 'snowdrop/data/QPM/history.csv'):

    from snowdrop.src.driver import run
    from snowdrop.src.driver import findSteadyStateSolution
    from snowdrop.src.utils.getIrisData import getIrisModel
    from snowdrop.src.driver import kalman_filter
    from snowdrop.src.numeric.solver.util import find_residuals
    from snowdrop.src.model.settings import SolverMethod
    from snowdrop.src.numeric.solver.linear_solver import solve
    from snowdrop.src.utils.equations import getVariablesPosition as getTopology
    from snowdrop.src.graphs.util import plotTimeSeries
    
    # Contains model parameters and standard deviation of shocks
    #calib_file = 'snowdrop/data/QPM/QPMcalibration_dict.xlsx' 
    # Model file
    #model_file = 'snowdrop/models/QPM/model_Lshocks.model' 
    # Historical data 
    #data_file = 'snowdrop/data/QPM/history.csv'
    
    fout = 'data/QPM/results.csv'     # Results are saved in this file
    output_variables = ['lgdp_gap','lgdp','lcpi','lcpi_core','dot4_cpi','rr','rn','dot_w','dot4_emp']      # List of variables that will be displayed
    decomp_variables = ['lz_gap','lgdp_gap','lemp_gap','rr_gap']  # List of variables for which decomposition plots are produced
    filtered = None
 
    # Path to model file
    file_path = os.path.abspath(os.path.join(working_dir, model_file))
    calib_path = os.path.abspath(os.path.join(working_dir, calib_file))
    hist_path = os.path.abspath(os.path.join(working_dir, data_file))
    fig_dir = os.path.abspath(os.path.join(working_dir, 'graphs'))
        
    # Path to model calibration file
    df = pd.read_excel(calib_path,"params")
    var = [x.strip() for x in df["var"]]
    val = [float(x) for x in df["value"]]
    calibration = dict(zip(var,val))
    
    #Path to shock std dev
    df = pd.read_excel(calib_path,"std")
    var = [x.strip() for x in df["var"]]
    val = [float(x) for x in df["value"]]
    stddev = dict(zip(var,val))
    calibration = {**calibration, **stddev}
    
    #---------- 1. Instantiate model 
    # Please use parameter 'use_cache' with caution...
    # If set to True it will read a model from a file neglecting calibrations and conditions settings.
    # If set to False it will save (aka serialize) this model in a file with the new set of conditions and calibration parameters.
    cprint("Parsing model file...\n","blue")
    model = getIrisModel(file_path,calibration=calibration,conditions={"fiscalswitch":False,"wedgeswitch":True}, 
                         use_cache=False,check=False,debug=False)
    #print(model)
    variables_names = model.symbols["variables"]
    n = len(variables_names)
    variables_values = model.calibration["variables"]
    var_labels = model.symbols["variables_labels"]
    param_names = model.symbols["parameters"]
    param_values = model.calibration["parameters"]
    params = dict(zip(param_names,param_values))
    #print(params)
    model.calibration["variables"] = np.zeros(len(variables_names))
    shock_names = model.symbols["shocks"]
    
    model.options["frequency"] = 1 # Quarterly
    # Steady state is computed as the numerical solution at the end of this time interval
    model.options["ss_interval"] = 400
    is_linear = model.isLinear
    
    #---------- 2. Compute steady state
    cprint("Computing steady state...\n","blue")
    ss_values, ss_growth = findSteadyStateSolution(model=model)
    ss = dict(zip(variables_names,ss_values))
    ss_gr = dict(zip(variables_names,ss_growth))
    print("Steady state:")
    print("-"*13)
    i = 0
    for x in sorted(variables_names):
        if not "_plus_" in x and not "_minus_" in x:
            i += 1
            lbl = None #var_labels[x] if x in var_labels else ""
            if bool(lbl):
                print(f"{i}: {lbl} -  {x} = ({ss[x]:.3f}, {ss_gr[x]:.3f})")
            else:
                print(f"{i}: {x} = ({ss[x]:.3f}, {ss_gr[x]:.3f})")
    print()
    
    # Set starting values
    ss_vars = [ss[x] if x in ss else variables_values[i] for i,x in enumerate(variables_names)]
    model.calibration["variables"] = ss_vars
    
    #---------- 3. Solve linear model
    # Compute reduced form transition and shock matrices.
    # If model is non-linear, then use steady state.
    
    cprint("Solving linearized model","blue")
    getTopology(model) 
    model.SOLVER = SolverMethod.Klein
    solve(model,steady_state=ss_values)
    

    # ---------------- 4. Run IRFs
    if True:
        cprint("\nRunning IRFs...\n","blue")
        model.options["range"] = ["2020-1-1","2030-1-1"]
        model.options["periods"] = ["2021-1-1"]
        
        shock_names = model.symbols["shocks"]
        n_shocks = len(shock_names)
        
        model.calibration["variables"] = ss_vars
        model.isLinear = is_linear
        
        # Define shocks
        shocks = [0.1]
        list_shocks = ['e_lgdp_gap']
        num_shocks = len(list_shocks)
        
        for i in range(num_shocks):
            # Set shocks
            shock_name = list_shocks[i]
            ind = shock_names.index(shock_name)
            shock_values = np.zeros(n_shocks)
            shock_values[ind] = shocks[i]
            model.options["shock_values"] = shock_values
            
            dates1,yy1 = \
            run(model=model,decomp_variables=decomp_variables,
                output_variables=output_variables,Solver="LBJ",
                fout=fout,Output=True,Plot=True,irf=True)
        
        
    # -----------5.  Run Kalman Filter and Smoother
    if True:
        cprint("Running Kalman filter and smoother...\n","blue")
        # Set simulation and filter ranges
        simulation_range = [[1990,1,1],[2023,1,1]]
        filter_range = [[2001,1,1],[2023,1,1]]
        model.options['range'] = simulation_range
        model.options['filter_range'] = filter_range
        model.options["shock_values"] = np.zeros(len(shock_names))
        start_filter = dt.date(*filter_range[0])
        end_filter = dt.date(*filter_range[1])
        start_simulation = dt.date(*simulation_range[0])
        end_simulation = dt.date(*simulation_range[1])
        
        # set path to a file with filtered results   
        smoother_path = os.path.abspath(os.path.join(working_dir,'../data/QPM/smoother_results.csv'))
    
        #Set variables starting values from historical data
        calib = model.calibration["variables"].copy()
        ss = dict(zip(variables_names,calib))
        model.setStartingValues(hist=hist_path,bTreatMissingObs=True,debug=False)
        #starting_values = dict(zip(variables_names,model.calibration["variables"]))
                
        # Get filtered and smoothed endogenous variables
        # We apply Kalman filter for linearized model
        model.isLinear = True
        yy2,dates2,epsilonhat,etahat = \
            kalman_filter(model=model,Output=True,Plot=False,fout=smoother_path,meas=hist_path,
                         #Filter="Diffuse",Smoother="Diffuse",Prior="Diffuse",
                         Filter="Durbin_Koopman",Smoother="Durbin_Koopman")
        # filtered results
        filtered = yy2[0]
        # smoothed results
        smoothed = yy2[-1]
        results = smoothed
        rows,columns = results.shape
        
        # Save filtration results
        dct = {}
        for j in range(columns):
            n = variables_names[j]
            data = results[:,j]
            m = min(len(data),len(dates2))
            ts = pd.Series(data[:m], dates2[:m])
            dct[n] = ts[start_filter:end_simulation]
    
        # Get shocks and residuals
        shocks = model.symbols['shocks']
        n_shk = len(shocks)
        res = find_residuals(model,results)
        m = min(len(dates2),len(data))
        if etahat is None:
            for j in range(n_shk):
                n = shocks[j]
                data = res[:,j]
                ts = pd.Series(data[:m], dates2[:m])
                dct[n] = ts[start_filter:end_simulation]
                dct[n+"_other"] = pd.Series(np.zeros(m), dates2[:m])[start_filter:end_simulation]
        else:
            for j in range(n_shk):
                n = shocks[j]
                data = etahat[:,j]
                m = min(len(data),len(dates2))
                ts = pd.Series(data[:m], dates2[:m])
                dct[n] = ts[start_filter:end_simulation]
                data = res[:,j]
                m = min(len(data),len(dates2))
                ts2 = pd.Series(data[:m], dates2[:m])
                dct[n+"_other"] = 0*(ts2-ts)[start_filter:end_simulation]
                    
        date = dt.datetime(*filter_range[1])
        filtered = [dct[n][date] for n in variables_names]
        
        # Read historical data
        ext = hist_path.split(".")[-1].lower()
        if ext == 'xlsx' or ext == 'xls':
            df = pd.read_excel(hist_path,header=0,index_col=0,parse_dates=True)
        else:
            df = pd.read_csv(filepath_or_buffer=hist_path,sep=',',header=0,index_col=0,parse_dates=True,infer_datetime_format=True)
       
        ### Plot results
        output_variables = [x for x in variables_names if "_gap" in x and x in var_labels]
        #output_variables = variables_names
        series = []; labels = []
        header = "Kalman_Filter"
        titles = [var_labels[k] for k in variables_names if k in output_variables and k in var_labels]
        for k in dct:
            if k in output_variables:
                arr = []
                lbls = ["filter ("+k+")"]
                if k in df.columns:
                    lbls.append("data")
                    val = df[k][start_filter:end_simulation]
                    # diff = (dct[k]-val)[:end_filter]
                    # shift = np.nanmean(diff)
                    # arr.append(dct[k]-shift)
                    arr.append(val)
                else:
                    arr.append(dct[k])
                series.append(arr)
                labels.append(lbls)
        
        plotTimeSeries(path_to_dir=fig_dir,header=header,titles=titles,labels=labels,series=series,sizes=[3,1],fig_sizes=(6,8),save=True)

        files = []
        outputFile = fig_dir+"/Gap Variables.pdf"
        list_names = [fig_dir+"/"+x for x in os.listdir(fig_dir) if x.startswith(header) and x.endswith(".pdf")]
        for f in list_names:
            files.append(f)
        merge(outputFile,files)
        
    # ---------------- 5. Impose user judgements
    #### Run forecast with tunes
    if True:
        cprint("Running forecasts with tunes...\n","blue")
        # Set simulation range
        model.options['range'] = ["2020-1-1","2028-1-1"]
        model.options["periods"] = ["2021-1-1"]
        rng = pd.date_range(start="2022-1-1",end="2028-1-1",freq='QS')
        model.isLinear = True
        model.anticipate = False
        
        # Set starting values
        model.calibration["variables"] = ss_vars if filtered is None else filtered
        
        # Swap endogenous and exogenous variables
        m = {}
        m['w_food'] = pd.Series([0.1714]*len(rng),rng)
        m['w_petr'] = pd.Series([0.0482]*len(rng),rng)
        m['w_elec'] = pd.Series([0.0363]*len(rng),rng)
        m['w_goodsx'] = pd.Series([0.2308]*len(rng),rng)
        m['w_serv'] = pd.Series([0.5132]*len(rng),rng)
        m['w_bfp'] = pd.Series([0.5094]*len(rng),rng)
        
        exog_shocks = ["e_w_food","e_w_petr","e_w_elec","e_w_goodsx","e_w_serv","e_w_bfp"]
        model.swap(var1=m,var2=exog_shocks)
        
        output_variables = ['w_food','w_petr','w_elec','w_goodsx','w_serv','w_bfp']      # List of variables that will be displayed
        decomp_variables = ['lgdp_gap','lemp_gap','w_petr','w_bfp']  # List of variables for which decomposition plots are produced
    
        # Define shocks
        shocks = [0.1]
        list_shocks = ['e_lgdp_gap']
        num_shocks = len(list_shocks)
        
        for i in range(num_shocks):
            # Set shocks
            shock_name = list_shocks[i]
            ind = shock_names.index(shock_name)
            shock_values = np.zeros(n_shocks)
            shock_values[ind] = shocks[i]
            model.options["shock_values"] = shock_values
            
            dates3,yy3 = run(model=model,output_variables=output_variables,
                              decomp_variables=decomp_variables,
                              fout=fout,Output=True,Plot=True,output_dir="out")
            
    print("\nDone!")

if __name__ == '__main__':
    """
    The main test program.
    """
    test()