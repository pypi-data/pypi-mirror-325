"""
Program for testing IMFE solver.

Created on Tue Sep 8, 2024
@author: A.Goumilevski
"""
import os,sys
import numpy as np
import pandas as pd
from textwrap import wrap
from datetime import datetime

path = os.path.dirname(os.path.abspath(__file__))
working_dir = os.path.abspath(path + "/../../..")
sys.path.append(working_dir)
os.chdir(working_dir)

from snowdrop.src.driver import run
from snowdrop.src.numeric.solver.nonlinear_solver import predict
from snowdrop.src.numeric.solver import nonlinear_solver
from snowdrop.src.utils import getImfeData as ds
from snowdrop.src.utils.getImfeData import get_model
from snowdrop.src.utils.getImfeData import getModelHash
from snowdrop.src.utils.getImfeData import get_frequencies
from snowdrop.src.utils.util import getExogenousSeries
#from snowdrop.src.utils.getImfeData import computeShocks
#from snowdrop.src.utils.getImfeData import solveOneVarEqs
from snowdrop.src.graphs.util import plotTimeSeries    
from snowdrop.src.utils.interface import saveModel
from snowdrop.src.utils.interface import loadModel
from snowdrop.src.utils.util import saveData
from snowdrop.src.utils.util import findVariableLag
from snowdrop.src.utils.util import findVariableLead
from snowdrop.src.utils.util import loadData 
from snowdrop.src.utils.equations import aggregateEqs
from snowdrop.src.numeric.solver.util import getOneVarEqsSolution
from snowdrop.src.misc.termcolor import cprint

def test(json_path=None,fpe_file=None,xl_path=None,save=False,debug=False):
    """
    Solves IMFE equations, saves results in excel file, displays forecasts of macroeconomic variables.

    Parameters
    ----------
    json_path : str, optional.
        Path to IMFE json directory.
    fpe_file : str, optional.
        Path to IMFE json fpe file.
    xl_path : str, optional.
        Path to excel directory containing extract from IMFE zip file.
    debug : bool, optional
        if True prints debug info. The default is False.

    Returns
    -------
    None.

    """
    fdir = working_dir+"/snowdrop/data/IMFE"
    fout_hist = os.path.join(fdir,"history") # Results are saved in this file
    fout_frcst = os.path.join(fdir,"forecast") # Results are saved in this file
    f_calib = os.path.join(fdir,"import.xlsx") # Parameters calibration file

    if not json_path is None: 
        json_path = os.path.join(fdir,json_path)
    elif not fpe_file is None: 
        fpe_file = os.path.join(fdir,fpe_file)
    elif not xl_path is None:  
        xl_path = os.path.join(fdir,xl_path)
            
    frequencies,m_aggr_variables,m_var_aggr = get_frequencies(json_path=json_path,xl_path=xl_path,fpe_file=fpe_file)
    cprint(f"\nFrequencies: {','.join(frequencies)}","blue")
    m_aggr = None; shock_names = None; shock_eqs = None; mh = {}
    
    
    for i,freq in enumerate(frequencies):
        
        cprint(f'\nRunning {freq.upper()} Frequency\n','cyan',attrs=['bold','underline'])
  
        if not json_path is None:
            fname = os.path.basename(json_path) 
            model_name,ext = os.path.splitext(fname)
            model_path = working_dir+"/snowdrop/models/IMFE/" + model_name + "_" + freq + ".bin"
        elif not fpe_file is None:
            fname = os.path.basename(fpe_file) 
            model_name,ext = os.path.splitext(fname)
            model_path = working_dir+"/snowdrop/models/IMFE/" + model_name + "_" + freq + ".bin"
        elif not xl_path is None:
            model_name = "imfe"
            model_path = working_dir+"/snowdrop/models/IMFE/" + model_name + "_" + freq + ".bin"
        fout_results = os.path.join(fdir,f"{model_name}/{freq}/results") # Results are saved in this file
           
        # Build hash of model variables, parameters, equations and hard data
        b_model_hash = getModelHash(json_path=json_path,xl_path=xl_path,fpe_file=fpe_file)
        b_model_exist = os.path.exists(model_path)
        
        # Load previous historic solution
        hist_path = fdir+"/"+model_name+"/"+freq+"/y_hist.json"
        if os.path.exists(hist_path):
            y = loadData(fdir+"/"+model_name+"/"+freq,"y_hist")
        else:
            y = None
            
        hist_path = fdir+"/"+model_name+"/"+freq+"/hist_variables_names.json"
        b_hist_exist = os.path.exists(hist_path)
        
        if not skipHistory or b_model_hash or not b_model_exist or not b_hist_exist:
                      
            ###-------- 1. Get IMFE model for historic interval
            cprint(f"\nCreating model for historic interval ({freq})...","blue")
            aggr_freq = None if i==0 else frequencies[i-1]
            model,lfunc,lvars,largs,one_var,exog,one_params,one_var_eqs,history_rng = get_model(json_path=json_path,fpe_file=fpe_file,bHist=True,freq=freq,aggr_freq=aggr_freq,m_aggr=m_aggr,f_calib=f_calib,bCompileAll=bCompileAll,debug=debug)
            if not m_aggr is None:
                model.setStartingValues(hist=m_aggr,bTreatMissingObs=False,debug=debug)
            if not y is None:
                model.y = np.squeeze(np.array(y))
                
            #print(model)
            hist_variables_names = model.symbols["variables"]
            hist_variables_values = model.calibration["variables"]
            mv = dict(zip(hist_variables_names,hist_variables_values))
            var_labels = model.symbols["variables_labels"]
            param_names = model.symbols["parameters"]
            param_values = model.calibration["parameters"]
            hist_mp = dict(zip(param_names,param_values))
            hist_me = model.calibration["exogenous"]
            #nv = len(hist_variables_names)
            hist_data = model.symbolic.exog_data
            hist_exog_data = model.symbolic.exog_data
            
            if compute_steady_state and model.y is None:
                from snowdrop.src.driver import findSteadyStateSolution
                cprint("\nComputing steady state for historical periods...","blue")
                # Steady state is computed as the numerical solution at the end of this time interval
                model.options["ss_interval"] = 10
                ss_values, ss_growth = findSteadyStateSolution(model=model)
                if debug:
                    ss = dict(zip(hist_variables_names,ss_values))
                    ss_gr = dict(zip(hist_variables_names,ss_growth))
                    print("Steady state:")
                    print("-"*13)
                    j = 0
                    for x in sorted(hist_variables_names):
                        if not "_plus_" in x and not "_minus_" in x:
                            j += 1
                            lbl = var_labels[x] if x in var_labels else ""
                            if bool(lbl):
                                print(f"{j}: {lbl}:\n     {x} = ({ss[x]:.3f}, {ss_gr[x]:.3f})")
                            else:
                                print(f"{j}: {x} = ({ss[x]:.3f}, {ss_gr[x]:.3f})")
                    
                # Set starting values
                model.calibration["variables"] = [1.e-5 if x==0 else x for x in ss_values]
                
            #---------- 2. Run historic simulations
            cprint("\nRunning historic simulations...","blue")
            if bCompileAll:
                y_hist,hist_rng = run(model=model,y0=model.y,fout=f"{fout_hist} ({freq}).csv",Output=False,Plot=False)              
            else:
                if model.y is None:
                    y = np.empty((model.T,len(hist_variables_names)))
                    y[:] = hist_variables_values
                else:
                    y = model.y
                y_hist = predict(model=model,T=model.T,y=y,params=param_values)
                y_hist[np.isnan(y_hist)+np.isinf(y_hist)] = ds.default_value
                frequency = pd.infer_freq(history_rng)
                hist_rng = pd.date_range(start=history_rng[0],periods=max(1,len(y)-2),freq=frequency)
            # First element id intial condition.  
            y_hist[0] = 2*y_hist[1]-y_hist[2] if len(y_hist)>2 else y_hist[1]
                            
            ###-------- 3. Get IMFE model for forecast interval
            cprint(f"\nCreating model for forecast interval ({freq})...","blue")
            model,lfunc,lvars,largs,one_var,exog,one_params,one_var_eqs,frcst_rng = get_model(json_path=json_path,fpe_file=fpe_file,bHist=False,freq=freq,f_calib=f_calib,bCompileAll=bCompileAll,debug=debug)  
            
            # Save model object
            saveModel(model_path,model)
            
            # Save historic data
            if not os.path.exists(fdir+"/"+model_name):
                os.mkdir(fdir+"/"+model_name)
            hist_start = ds.data_range_start; hist_end= ds.data_range_end
            forecast_start = ds.forecast_range_start; forecast_end = ds.forecast_range_end
            data = {"hist_variables_names":hist_variables_names,"y_hist":y_hist,"hist_rng":hist_rng,
                    "hist_me":hist_me, "hist_mp":hist_mp,"hist_data":hist_data,
                    "hist_exog_data":hist_exog_data,"frcst_rng":frcst_rng,"one_var_eqs":one_var_eqs, "lfunc":[one_var,exog,one_params,one_var_eqs],
                    "lvars":lvars,"largs":largs,"hist_start":hist_start,"hist_end":hist_end,
                    "forecast_start":forecast_start, "forecast_end":forecast_end,
                    "history_rng":history_rng}
            saveData(fdir+"/"+model_name+"/"+freq,**data)
        
        else:
            
            model = loadModel(model_path)
            args = ["hist_variables_names","y_hist","hist_rng","hist_me","hist_mp","hist_data","hist_exog_data",
                    "frcst_rng","one_var_eqs","lfunc","lvars","largs","hist_start","hist_end","forecast_start",
                    "forecast_end","history_rng"]
            hist_variables_names,y_hist,hist_rng,hist_me,hist_mp,hist_data,hist_exog_data,frcst_rng,one_var_eqs, \
                lfunc,lvars,largs,hist_start,hist_end,forecast_start,forecast_end,history_rng = \
                loadData(fdir+"/"+model_name+"/"+freq,*args)
            y_hist = np.array(y_hist)
        
        # Load previous forecast solution
        frcst_path = fdir+"/"+model_name+"/"+freq+"/y_frcst.json"
        if os.path.exists(frcst_path):
            y = loadData(fdir+"/"+model_name+"/"+freq,"y_frcst")
            model.y = np.squeeze(np.array(y))
        else:
            model.y = None
            
        exog_data = model.symbolic.exog_data
        forecast_variables_names = model.symbols["variables"]
        #forecast_variables_values = model.calibration["variables"]
        var_labels = model.symbols["variables_labels"]
        param_names = model.symbols["parameters"]
        param_values = model.calibration["parameters"].copy()
        mp = dict(zip(param_names,param_values))
                        
        for j,k in enumerate(hist_variables_names):
            mh[k] = pd.Series(y_hist[1:-1,j],hist_rng) 
        
        # Get exogenous data
        exog_names = model.symbols["exogenous"]
        k = next(iter(exog_data))
        index = exog_data[k].index
            
        #---------- 4. Set starting values
        model.setStartingValues(hist=mh,bTreatMissingObs=False,debug=debug)
        hist_values = model.calibration["variables"].copy()
        for j,v in enumerate(forecast_variables_names):
            if v in hist_variables_names:
                ind = hist_variables_names.index(v)
                hist_values[j] = y_hist[-1,ind]

        b = (hist_values == np.nan)
        if sum(b) > 0:
            not_set_var = [x for i,x in enumerate(forecast_variables_names) if b[i]]
            cprint(f"Initial conditions are not set for variables {not_set_var}")
        
        model.calibration["variables"] = hist_values
        mv = dict(zip(forecast_variables_names,hist_values))
    
        #---------- 5. Run one variable equations
        if len(largs) > 0:  
                
            m = dict(); T = len(frcst_rng)
            frequency = pd.infer_freq(hist_rng)
            start = str(forecast_start)+"-01-01"
            frcst_rng = pd.date_range(start=start,periods=T,freq=frequency)
            
            for x in exog_names+hist_variables_names:
                if x in mv:
                    v = mv[x]
                elif x in hist_me:
                    v = hist_me[x][-1]
                elif x in hist_mp:
                    v = hist_mp[x]
                elif x in hist_variables_names:
                    ind = hist_variables_names.index(x)
                    v = y_hist[-1,ind]
                elif x in exog_data:
                    v = exog_data[x].iloc[0]
                else:
                    v = ds.default_value
                    cprint(f"Initial value of {x} is not defined.  Assigning default value...","yellow")
                m[x] = v
            
            mOneVarEq = getOneVarEqsSolution(lvars,lfunc,largs,one_var_eqs,m,mp,exog_data,T)
     
            for v in lvars:
                if v in mOneVarEq:
                    exog_data[v] = pd.Series(mOneVarEq[v],frcst_rng)
                
        # Revision of Gyana debt projections
        if reviseProjections and "GUY" in fpe_file:
            exog_data["D"]["2025-01-01":"2027-01-01"] = [1.5,1.4,1.3]
            cprint("\n\nRevised Projections:\n","blue")
            print(f"D - {var_labels['D']}:") 
            print(exog_data["D"])
                
        model.symbolic.exog_data = exog_data     
        model.calibration["exogenous"] = getExogenousSeries(model)
        
        #---------- 6. Run forecast simulations 
        cprint("\nRunning forecast simulations...","blue")
        try:
            frequency = pd.infer_freq(hist_rng)
            start = str(forecast_start)+"-01-01"
            frcst_rng = pd.date_range(start=start,periods=max(1,model.T-2),freq=frequency)
            if len(model.symbolic.equations) > 0:
                if bCompileAll:
                    y,frcst_rng = run(model=model,y0=model.y,fout=f"{fout_frcst} ({freq}).csv",Plot=False,Output=False)
                else:
                    if model.y is None:
                        y = np.empty((model.T,len(forecast_variables_names)))
                        y[:] = hist_values
                    else:
                        y = model.y
                    y = predict(model=model,T=model.T,y=y,params=param_values)
            else:
                y = None
        
        except Exception as ex:
            cprint(f"Exception: {ex}","red")
            y = model.y
            if y is None: 
                return
            frequency = pd.infer_freq(hist_rng)
            start = hist_rng[-1] + pd.tseries.frequencies.to_offset(frequency)
            frcst_rng = pd.date_range(start=start,periods=len(y),freq=frequency)
            
            # Save forecast results
            if save:
                from snowdrop.src.utils.util import saveToExcel
                var_labels = model.symbols["variables_labels"]
                param_names = model.symbols["parameters"]
                param_values = model.calibration["parameters"].copy()
                saveToExcel(fname=fout_frcst,data=[y],variable_names=forecast_variables_names,
                            var_labels=var_labels,par_values=param_values,
                            par_names=param_names, #output_variables=output_variables,
                            rng=frcst_rng,Npaths=1)
            
        y_frcst = y
        #mf = dict(zip(forecast_variables_names,y_frcst.T))
        
        # Save forecast
        data = {"y_frcst":y_frcst}
        saveData(fdir+"/"+model_name+"/"+freq,**data)
        
        #---------- 7. Plot results 
        cprint("\nPloting results...","blue")
        variables = list(set(hist_variables_names + forecast_variables_names + lvars))
        variables = [x for x in variables if not "_minus_" in x and not "_plus_" in x]
        if output_variables is None:
            nplot = len(forecast_variables_names)
            Nplot = 12
        else:
            nplot = sum([1 if x in output_variables else 0 for x in variables])
            Nplot = 6
        
        end_hist = hist_rng[-1].year   
        for k in hist_data:
            years = [datetime.date(dt).year for dt in hist_data[k].index]
            b = [end_hist >= y >= hist_start for y in years]
            hist_data[k] = hist_data[k][b]
        
        highlight = [history_rng[0]+'-01-01',history_rng[-1]+'-01-01']
        start = f"{hist_start}-01-01"
        end_hist = f"{hist_end}-01-01"
        start_forecast = f"{forecast_start}-01-01"
        end = f"{forecast_end}-01-01"

        # # Compute shocks which are necessary to satisfy aggregation equations
        # if freq in m_aggr_variables:
        #     m_var = {}
        #     aggr_variables = m_aggr_variables[freq]
        #     if len(aggr_variables) > 0:
        #         for v in aggr_variables:
        #                 y1,y2 = None,None
        #                 if v in hist_variables_names:
        #                     ind1 = hist_variables_names.index(v)
        #                     y1 = pd.Series(y_hist[-1-len(hist_rng):-1,ind1],hist_rng) 
        #                 if v in forecast_variables_names:
        #                     ind2 = forecast_variables_names.index(v)
        #                     y2 = pd.Series(y_frcst[1:-1,ind2],frcst_rng) 
        #                     y2 = y2[start_forecast:]
        #                 if not y1 is None and not y2 is None:
        #                     y = pd.concat([y1,y2])
        #                     y_ = y[start:end]
        #                     m_var[v] = y_
                
        #     # Compute shocks as residuals of aggregation equations           
        #     shock_values = computeShocks(shock_eqs,m_var=m_var,m_aggr=m_aggr)
        #     m_shocks = dict(zip([x[:x.index("[")] for x in shock_names],shock_values))
            
        # # Save aggregated variables
        # m_aggr = {}
        # if len(frequencies) > 1 and i < len(frequencies)-1:
        #     aggr_variables = m_aggr_variables[freq]
        #     freq2 = frequencies[i+1]
            
        #     for v in aggr_variables:
        #         y1,y2 = None,None
        #         if v in hist_variables_names:
        #             ind1 = hist_variables_names.index(v)
        #             y1 = pd.Series(y_hist[-1-len(hist_rng):-1,ind1],hist_rng) 
        #             y1 = y1[:end_hist]
        #         if v in forecast_variables_names:
        #             ind2 = forecast_variables_names.index(v)
        #             y2 = pd.Series(y_frcst[1:-1,ind2],frcst_rng)
        #             y2 = y2[start_forecast:]
        #         elif v in lvars:
        #             y2 = exog_data[v]    
        #             y2 = y2[start_forecast:]
        #         if not y1 is None and not y2 is None:
        #             y = pd.concat([y1,y2])
        #         elif y1 is None and not y2 is None:
        #             if v in hist_data:
        #                 y1 = hist_data[v]
        #                 y1 = y1[:end_hist]
        #                 y = pd.concat([y1,y2])
        #             else:
        #                 y = y2
        #         elif not y1 is None and y2 is None:
        #             y2 = pd.Series([y_frcst[-1,ind2]]*len(frcst_rng),frcst_rng)                    
        #             y2 = y2[start_forecast:]
        #             y = pd.concat([y1,y2])
        #         else:
        #             y = None
        #         if not y is None:
        #             y_ = y[start:end]
        #             m_aggr[v] = y_.resample(freq2[0].upper()+'S').interpolate(method="time")
            
        #     # Define shocks names and equations
        #     var_aggr = [m_var_aggr[x] for x in m_var_aggr]
        #     shock_eqs,shock_names,new_exog_vars = aggregateEqs(variables=variables,aggregation=var_aggr,freq=freq2,aggr_freq=freq,m_aggr=m_aggr)
   

        my = dict(); m_all = dict(); m_descr = dict(); ii = iii = 0
        all_variables = variables + list(hist_exog_data.keys())
        for v in sorted(set(all_variables)):
            if output_variables is None or len(all_variables) <= 12 or v in output_variables:
                y1,y2 = None,None; descr = ""
                if v in hist_variables_names:
                    descr += " (history: computed"
                    ind1 = hist_variables_names.index(v)
                    y1 = pd.Series(y_hist[-2-len(hist_rng):-2,ind1],hist_rng) 
                    y1 = y1[:end_hist]
                elif v in hist_exog_data:
                    descr += " (history: data"
                    y1 = hist_exog_data[v]
                    y1 = y1[:end_hist]
                if v in forecast_variables_names:
                    descr += ", forecast: computed)"
                    ind2 = forecast_variables_names.index(v)
                    if len(frcst_rng) == 1:
                        y2 = pd.Series(y_frcst[-1,ind2],frcst_rng)  
                    elif len(frcst_rng) == len(y_frcst):
                        y2 = pd.Series(y_frcst[:,ind2],frcst_rng)  
                    else:
                        y2 = pd.Series(y_frcst[-1-len(frcst_rng):-1,ind2],frcst_rng)   
                    y2 = y2[start_forecast:]
                elif v in lvars:
                    descr += ", forecast: computed - one var eq)"
                    y2 = exog_data[v]    
                    y2 = y2[start_forecast:]
                elif v in exog_data:
                    descr += ", forecast: data)"
                    y2 = exog_data[v]    
                    y2 = y2[start_forecast:]
                if not y1 is None and not y2 is None:
                    y = pd.concat([y1,y2])
                elif y1 is None and not y2 is None:
                    if v in hist_data:
                        y1 = hist_data[v] 
                        y1 = y1[:end_hist]
                        y = pd.concat([y1,y2])
                    else:
                        y = y2
                elif not y1 is None and y2 is None:
                    y2 = pd.Series([y_frcst[-1,ind2]]*len(frcst_rng),frcst_rng) 
                    y2 = y2[start:]
                    y = pd.concat([y1,y2])
                else:
                    y = None
                if not y is None:
                    y_ = y[start:end]
                    m_all[v] = y_
                    my[v] = y_
                    m_descr[v] = descr
                    ii += 1
                    if ii%Nplot == 0 or ii == nplot:
                        iii += 1
                        header = f"{model_name} ({freq}) #{iii}"
                        labels = []
                        series = [[my[k]] for k in my]
                        titles = [str(var_labels[k])+" ("+k+")"+m_descr[k] if k in var_labels and not var_labels[k] is None else k+m_descr[k] for k in my]
                        titles = ["\n".join(wrap(x,50)) for x in titles]
                        path_to_dir = os.path.abspath(os.path.join(working_dir,"graphs"))
                        plotTimeSeries(path_to_dir=path_to_dir,header=header,titles=titles,labels=labels,series=series,highlight=highlight,save=True,stacked=False,ext="png")
                        my = dict()

        if save:
            df_all = pd.DataFrame(m_all)
            df_all.to_csv(f"{fout_results}.csv")
    
    print("Done!")
             
    
# Maximum number of iterations
nonlinear_solver.NITERATIONS = 5 

bCompileAll = False
skipHistory = False
compute_steady_state = False
compute_steady_state &= bCompileAll
reviseProjections = False
ds.bOneVarEquation = True # Solve one variable equations
ds.default_value = 1.e0 # Default value of missing variables or parameters

output_variables = ["ENDA_CAEM","FPOLM_CAEM","NCP_R_CAEM","NX_R","NX_R_CAEM",
                    "PCPI_PCH_CAEM","D","ENDA","EDNA","NGDP","FPOLM_US",
                    "PCPI_PCH_CAEM","L_ENDA","PCPI_TAR_PCH","PCPI_US_TAR_PCH",
                    "IAR_BP6_GDP","L_NFIP_R","L_REXPP","NGDP_R","NX_R","NCP_R",
                    "CG_R","NCP_R","NFIG_R","NFIP_R","NM_R_CAEM","NX_R","NGDP_R"]
                    #"NCG","NCP","NFI","NINV","NM"]

if __name__ == '__main__':
    """The main test program."""
    fpe_file = "GUY.fpe"
    #fpe_file = "GUY_WEO.fpe"
    #fpe_file = "Guyana.fpe"
    #fpe_file = "ALB.fpe"
    #fpe_file = "Phil.fpe"
    #fpe_file = "Fin.fpe"
        
    cprint(f'\nRunning {fpe_file[:fpe_file.index(".")]}:\n','blue',attrs=['bold','underline'])
        
    test(fpe_file=fpe_file,save=True,debug=False)
    
