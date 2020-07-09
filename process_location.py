#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:08:26 2020

@author: arsi
"""

# standard library imports
from pathlib import Path

# third party imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Local application import


from vector_encoding import ordinal_encoding, one_hot_encoding, decode_string, decode_string_3, custom_resampler, normalize_values
from calculate_RQA import Calculate_RQA
from plot_recurrence import Show_recurrence_plot
from save_results import dump_to_json
from plot_timeseries import show_timeseries_scatter, show_timeseries_line, show_features
from save2mat import save2mat
from calculate_similarity import calculate_similarity
from calculate_novelty import compute_novelty_SSM
from json_load import load_one_subject
from Plot_similarity import Plot_similarity
from interpolate_missing import interpolate_missing

def process_location(df):
    
    #%% calculate receursion plot and metrics

    # Recursion plot settings
    ED = 2 # embedding dimensions
    TD = 2 # time delay
    RA = 0.25 # neigborhood radius
    
    timeseries = df['totdist'].values.reshape(-1,1)
    
    # Calculate recursion plot and metrix
    res, mat = Calculate_RQA(timeseries,ED,TD,RA)
    sim = calculate_similarity(timeseries,'euclidean')
    nov = compute_novelty_SSM(sim)
    Plot_similarity(sim,nov)
    
    #%% show recursion plot and save figure
    
    # set correct names and plot title
    FIGPATH = Path(r'/home/arsi/Documents/SpecialAssignment/Results/Plots/')
    FIGNAME = "recplot_3"
    TITLE = "Location / daily Recurrence Plot \n dim = {}, td = {}, r = {}".format(ED,TD,RA)  
    Show_recurrence_plot(mat,TITLE,FIGPATH,FIGNAME)
    
    # set correct names and save metrics as json 
    RESPATH = Path(r'/home/arsi/Documents/SpecialAssignment/Results/Metrics/')
    RESNAME = "metrics_3.json"
    dump_to_json(res,RESPATH,RESNAME)   
    
    # save the timeseries
    TSPATH = Path(r'/home/arsi/Documents/SpecialAssignment/Results/Timeseries/')
    TSNAME = "timeseries_3.mat"
    save2mat(timeseries,TSPATH,TSNAME)       
    
    #%% Plot timeseries and save figure
    FIGPATH = Path(r'/home/arsi/Documents/SpecialAssignment/Results/Plots/')
    FIGNAME = "timeseries_3"
    show_timeseries_scatter(df.totdist,"Total distance travelled / daily binned","time","Level",FIGPATH,FIGNAME)
    
    
    return df

if __name__ == "__main__":
    pass