"""
Program for testing Troll models.

Created in November 2022
@author: A.Goumilevski
"""
import os
import sys
import numpy as np
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))
working_dir = os.path.abspath(path + "/../../..")
sys.path.append(working_dir)
os.chdir(working_dir)

bReports = True      # Generate pdf reports
bForecast = True    # Run forecasts
bSynchrounous = True # Flag to run reports synchroniously. If this flag is not raised, 
                     # reports will run in a background and forecast will exit upon completion.
report_types = "all" # "standard" "tables" "vartables" "reportss" "all"

if __name__ == '__main__':
    """
    The main test program.
    """
    from snowdrop.src.driver import run,findSteadyStateSolution
    from snowdrop.src.utils.getTrollData import getTrollModel
    from snowdrop.src.utils.util import saveToExcel
    
    use_cache = False
    #Solver = "ABLR"; bSparse = True
    Solver = "LBJ"; bSparse = False
    model_folder="FSGM";  model_class = "FSGM3"
    
    ### Path to model file
    fname = 'ISRMOD.inp' # Three regions Flexible System of Global Models
    # fname = 'FORMOD.inp' # Six regions Flexible System of Global Models

    # Path to shock file
    shock_name = 'Permanent_1_percent_increase_of_GDP_using_Total_Factor_Productivity.csv'
    shocks_file_path = os.path.abspath(os.path.join(working_dir,'snowdrop/data/Troll/',model_class,'files', shock_name))
    fout = os.path.abspath(os.path.join(working_dir,'snowdrop/data/Troll/' + model_class + '/results_shock_' + shock_name))   # Results are saved in this file
    fss  = os.path.abspath(os.path.join(working_dir,'snowdrop/data/Troll',model_class,'results_shock_NoShock.csv')) # Steady state file
          
    output_variables = None #['USA_GDP_R','ISR_GDP_R','WRL_GDP_R','RC0_GDP_R']  # List of variables that will be plotted
    decomp_variables = None #['USA_GDP_R','WRL_GDP_R']  # List of variables for which decomposition plots are produced
   
    calib = 'snowdrop/data/Troll/' + model_class + '/calibration_dict.csv' 
    
    file_path = os.path.abspath(os.path.join(working_dir, 'snowdrop/models/Troll',model_class,fname))
    calib_path = os.path.abspath(os.path.join(working_dir, calib))
    
    df = pd.read_csv(calib_path)
    calibration = dict(zip(df["var"],df["value"]))
    #calibration = {}
        
    # Please use parameter 'use_cache' with a caution...
    # If set to True it will deserialize model from a file neglecting calibrations and conditions settings.
    # If set to False it will save (aka serialize) this model in a file with the new set of conditions and calibration parameters.
    model = getTrollModel(file_path,Solver=Solver,calibration=calibration,use_cache=use_cache,check=False,debug=False)
    model.bSparse = bSparse
    #print(model)
    
    variables = model.symbols["variables"]
    var_values = model.calibration["variables"]
    var_labels = model.symbols.get("variables_labels",None)
    param_names = model.symbols["parameters"]
    param_values = model.calibration["parameters"]
    params = dict(zip(param_names,param_values))
    m = dict(zip(variables,var_values))
  
    model.options["frequency"] = 0 # Annual
    model.options["range"] = ["2024-1-1","2124-1-1"]
    # If periods is not set in model.options block, then shock is treated as permanent.
    # Otherwise set time periods of this shock occurances.
    #model.options["periods"] = ["2025-1-1"]
    if "periods" in model.options: del model.options["periods"]
    # Steady state is computed as the numerical solution at the end of this time interval
    model.options["ss_interval"] = 100
    
    dates = pd.date_range(start=model.options["range"][0],end= model.options["range"][1],freq="YS")
        
    if False:
        # Compute steady state
        ss_values, ss_growth = findSteadyStateSolution(model=model)
        ss = dict(zip(variables,ss_values))
        ss_gr = dict(zip(variables,ss_growth))
        
        # print("Steady state:")
        # print("-"*13)
        # i = 0
        # for x in sorted(variables):
        #     if not "_plus_" in x and not "_minus_" in x:
        #         i += 1
        #         lbl = var_labels[x] if x in var_labels else ""
        #         if bool(lbl):
        #             print(f"{i}: {lbl} -  {x} = ({ss[x]:.3f}, {ss_gr[x]:.3f})")
        #         else:
        #             print(f"{i}: {x} = ({ss[x]:.3f}, {ss_gr[x]:.3f})")
        # print()
        
        # model.steady_state = ss
    
        saveToExcel(fname=fss,data=[[[ss_values]]],
                    variable_names=[x for x in variables if not ("__p" in x or "__m" in x)],
                    par_values=param_values,par_names=param_names,rng=dates)
    
    if bForecast:
        # Temporary shock of TFP at period 1
        list_shocks = ['E_USA_TFP_FE_R']
        shock_names = model.symbols["shocks"]
        n_shocks = len(shock_names)
        
        shocks = [0.0102/1.3]
        num_shocks = len(list_shocks)
        for i in range(num_shocks):
            # Set shocks
            shock_name = list_shocks[i]
            
            if shock_name in shock_names:
                ind = [i for i,x in enumerate(shock_names) if x==shock_name][0]
                shock_values = np.zeros(n_shocks)
                shock_values[ind] = shocks[i]
                model.options["shock_values"] = shock_values
                
                run(model=model,output_variables=output_variables,Solver=Solver,
                    shocks_file_path=shocks_file_path,fout=fout,Output=True,Plot=False)

    
    if bReports:    
        
        print("\nRunning reports...\n\n")
        
        ### Run reports
        report_dir = os.path.abspath(path + "/../../../../Reports")
        sys.path.append(report_dir)
        os.chdir(report_dir)
        import run
        import subprocess
        
        results_dir = os.path.abspath(os.path.join(working_dir,"snowdrop/data/Troll",model_class))
        file_name = os.path.basename(fout)
        base_dir = os.path.abspath(os.path.join(report_dir,"reports",model_folder,model_class))
        cmd = f"python run.py -model_folder {model_folder} -model_name {model_class} -results_dir {results_dir} -file_name {file_name} -report_types {report_types}"
        print("\n\n"+cmd+"\n")
        if bSynchrounous:
            returned_value = run.main(model_folder=model_folder,model_name=model_class,results_dir=results_dir,base_dir=base_dir,file_name=file_name,report_types=report_types)
            if not returned_value == 0:
                flog = file_name.replace(".csv",".txt").replace(".xlsx",".txt")
                if "shock" in flog:
                    ind = flog.index("shock")
                    flog = flog[ind+5:]
                flog = "log_" + report_types + flog
                flog = os.path.abspath(os.path.join(base_dir,"log",flog))
                print(f"Report was not generated. Please see: {flog}")
            else:
                if "shock" in file_name:
                    ind = file_name.index("shock")
                    file_name = file_name[ind+5:]
                freports = os.path.abspath(os.path.join(base_dir,file_name))
                freports = freports.replace(".csv","").replace(".xlsx","").replace("_","")
                print(f"\nGenerated report in the folder:\n {freports}")
        else:
            process = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            output = None
            #output, _ = process.communicate()  
            if "shock" in file_name:
                ind = file_name.index("shock")
                file_name = file_name[ind+5:]
            freports = os.path.abspath(os.path.join(base_dir,file_name))
            freports = freports.replace(".csv","").replace(".xlsx","").replace("_","")
            print(output)
            print(f"\nReport will be generated in the folder:\n {freports}")
            
    print("\nDone!")
