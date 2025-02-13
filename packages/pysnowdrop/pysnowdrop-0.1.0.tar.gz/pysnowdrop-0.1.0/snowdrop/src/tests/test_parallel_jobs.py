""" 
Program for running Troll models in parallel. 
 
@author: A.Goumilevski 
""" 
import os
import sys
from time import time 
import glob 
# import cProfile
# import pstats
import subprocess
import multiprocessing as mp 
from concurrent.futures import as_completed 
     
path = os.path.dirname(os.path.abspath(__file__))
working_dir = os.path.abspath(path + "/../../..")
sys.path.append(working_dir)
os.chdir(working_dir)

from snowdrop.src.driver import run

### Run reports
report_dir = os.path.abspath(path + "/../../../../Reports")
sys.path.append(report_dir)
os.chdir(report_dir)

model_folder="FSGM"; model_class = "FSGM3"

results_dir = os.path.abspath(os.path.join(working_dir,"snowdrop/data/Troll",model_class))
base_dir = os.path.abspath(os.path.join(report_dir,"reports",model_folder,model_class))
        
use_thread_pool = False  # It set True will run simulations by using thread pool, otherwise - by processes pool
bForecast = True        # Run forecast
bReports = True          # Generate pdf reports
bSynchrounous = False    # Flag to run reports synchroniously. If this flag is not raised, 
                         # reports will run in a background and forecast will exit upon completion.
report_types = "all"     # standard tables vartables reportss all

use_cache = True
#Solver = "ABLR"; bSparse = True
Solver = "LBJ"; bSparse = False
 
def forecast(x): 
    """Run one scenario""" 
    fname,fout,shock_file,calibration_file = x
    if bForecast:
        y,dates = \
        run(fname=fname,fout=fout,Output=True,Plot=False,shocks_file_path=shock_file,
            calibration_file_path=calibration_file,use_cache=use_cache) 
    
    if bReports:
        file_name = os.path.basename(fout)  
        cmd = f"python run.py -model_folder {model_folder} -model_name {model_class} -results_dir {results_dir} -file_name {file_name} -report_types {report_types}"
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
            print(f"\nReport will be generated in folder:\n {freports}")
             
def parallel_run(fname,fout,output_variables=None,decomp_variables=None,shock_files=[],calibration_files=[],use_thread_pool=False): 
    """Asynchronous run""" 
    n_files = max(1,len(shock_files),len(calibration_files))
    if len(shock_files) < n_files:
        shock_files += [None]*(n_files-len(shock_files))
    if len(calibration_files) < n_files:
        calibration_files += [None]*(n_files-len(calibration_files))
        
    if use_thread_pool: 
        max_workers = n_files 
        from concurrent.futures import ThreadPoolExecutor as PoolExecutor  
    else: 
        max_workers = min(mp.cpu_count(),n_files) 
        from concurrent.futures import ProcessPoolExecutor as PoolExecutor  
        
    # Set upper limit on number of workers.  Otherwise, this program will eat all computer resources.
    max_workers = min(3,max_workers)
 
    t0 = time() 
    lst = [(fname,results_file,shock_file,calib_file) for results_file,shock_file,calib_file in zip(results_files,shock_files,calibration_files)] 
 
    # Run parallel jobs 
    with PoolExecutor(max_workers=max_workers) as executor: 
        futures = {executor.submit(forecast,x): x for x in lst} 
        for future in as_completed(futures): 
            data = futures[future] 
            try: 
                future.result() 
            except Exception as exc: 
                print('\n%r \nGenerated an exception: %s' % (data, exc)) 
 
    elapsed = time() - t0 
    print("Elapsed time: %.2f (seconds)" % elapsed) 
     
    return 
 
if __name__ == '__main__': 
    """ 
    The main program. 
    """ 
    fname = 'ISRMOD.inp' # Three regions Flexible System of Global Models 
    fdir = os.path.abspath(os.path.join(working_dir,'snowdrop/models/Troll',model_class))
    fdata = os.path.abspath(os.path.join(working_dir,'snowdrop/data/Troll',model_class))
                           
    # Path to model file 
    file_path = os.path.abspath(os.path.join(fdir,fname)) 
     
    # Path to files (all shocks and parameters files)
    files = glob.glob(fdata+"/files/*.csv")
    shock_files = []; calib = []; results_files = []
    for f in files:
        name = os.path.basename(f)
        results_files.append(os.path.abspath(fdata+"/results_shock_"+name.replace("par_","")))
        # Parameters files start with prefix "par_"
        if name.startswith("par_"):
            calib.append(f)
            shk_file = os.path.abspath(os.path.join(fdata,name.replace("par_","")))
            if os.path.exists(shk_file):
                shock_files.append(shk_file)
            else:
                shock_files.append(None)
            results_files.append(shk_file)
        else:
            shock_files.append(f)
            par_file = os.path.abspath(os.path.join(fdata,"par_"+name))
            if os.path.exists(par_file):
                calib.append(par_file)
            else:
                calib.append(None)
            results_files.append(f)
           
    # # All calibration files 
    # calib = glob.glob(fdata+"/calibration*") 
    # calib *= len(shock_files)
 
    parallel_run(fname=file_path,fout=results_files,shock_files=shock_files,calibration_files=calib,use_thread_pool=use_thread_pool)

    # ### Profiler
    # with cProfile.Profile() as pr:
    #     parallel_run(fname=file_path,fout=fout,shock_files=shock_files,calibration_files=calibration_files,use_thread_pool=True)

    # # Path to profiler results
    # file_path = os.path.abspath(
    #     os.path.join(working_dir, '../results/profiler', 'profiler_test.log')
    #     )
    # with open(file_path, 'w') as stream:  # for writing to file
    #     stats = pstats.Stats(
    #         pr, stream=stream
    #         ).sort_stats('tottime')  # for sorting based on a certain column
    #     stats.print_stats()
  
     
 
 
