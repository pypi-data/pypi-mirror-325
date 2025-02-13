#!/usr/bin/env python3

import os
import glob 
from pathlib import Path
import pandas as pd



def get_pool_dicts(exp_design):
    
    """
    Get file2pool_dict indicating which input file belongs to which pool and
    pool2dim dict indicating which  pool belongs to which dimension
        


    Parameters
    ----------
    exp_design : str
       Name of file encoding experimental design. The experimental design file 
       should have columns, Filename, Poolname and Pooldimension.

    Returns
    -------
    file2pool_dict: dict
        indicating which input file belongs to which pool
    pool2dim_dict: dict
        indicating which  pool belongs to which dimension

    """
    
    exp_design_ = pd.read_csv(exp_design, index_col=0)

    file2pool_dict = {Path(i).stem.split(".")[0]:exp_design_.loc[i,"Poolname"] for i in exp_design_.index.unique()}
    
    exp_design_ = pd.read_csv(exp_design, index_col=2)

    pool2dim_dict = {i:exp_design_.loc[i,"Poolname"].unique().tolist() for i in exp_design_.index.unique()}

    return file2pool_dict, pool2dim_dict
    
def get_input_files(experiment):
    """
    
    
    Parameters
    ----------
    experiment : LibraryExperiment
        Object holding input parameters.

    Returns
    -------
    paths : list of strings
        paths of input files
    names : list of strings
        names of input files

    """    

    exp_design = pd.read_csv(experiment.exp_design)
    assert all(exp_design.columns == ["Filename", "Poolname", "Pooldimension"]), \
        "Please provide an experimental design file with columns: Filename, Poolname, Pooldimension"
    names = [Path(i).stem.split(".")[0] for i in exp_design["Filename"]]
    paths = [os.path.join(experiment.input_dir, i) for i in exp_design["Filename"]]
    #assert len(paths) != 0, "No input files found in " + str(experiment.input_dir)

    return paths, names




def set_up_tmpdir():
    """´
    Set up temp directory and clean up previous results.

    
    Returns
    -------
    None.

    """
    
    
    if not os.path.exists("temp"):
        os.makedirs("temp")
    

