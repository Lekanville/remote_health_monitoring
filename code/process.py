import argparse
#import numpy as np
#import pandas as pd
#import scipy.stats as st
#import seaborn as sns
#import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker
#import os
#path = "/Users/ev22335/Documents/Remote_Health_Monitoring/code"
#os.chdir(path)
import tools.remote_process as remote
import tools.spygh_process as sphyg
import tools.cond_bpm as cond_bpm
import tools.cond_syst as cond_syst
import tools.cond_diast as cond_diast
import tools.no_cond_bpm as no_cond_bpm
import tools.no_cond_syst as no_cond_syst 
import tools.no_cond_diast as no_cond_diast
import tools.cond_t_stat as cond_t_stat
import tools.no_cond_t_stat as no_cond_t_stat

parser = argparse.ArgumentParser(description="Preprocessing the data")
parser.add_argument("-i", "--remote_dataset", type=str, required=True, help="The dataset taken remotely from the FIT API")
parser.add_argument("-j", "--sphyg_dataset", type=str, required=True, help="The dataset obatained from the sphygmomanometer")

def process_all(REMOTE_DATASET, SPHYG_DATASET):

    #Data reading and values extraction
    df_CI_remote_cond, df_CI_remote_no_cond = remote.remote_features(REMOTE_DATASET)
    df_CI_sphyg_cond, df_CI_sphyg_no_cond = sphyg.sphyg_features(SPHYG_DATASET)

    print(df_CI_remote_cond.head())
    print("\n")
    print(df_CI_remote_no_cond.head())
    print("\n")
    print(df_CI_sphyg_cond.head())
    print("\n")
    print(df_CI_sphyg_no_cond.head())

    #Plotting the values
    cond_bpm.cond_bpm_plot(df_CI_remote_cond, df_CI_sphyg_cond)
    no_cond_bpm.no_cond_bpm_plot(df_CI_remote_no_cond, df_CI_sphyg_no_cond)

    cond_syst.cond_syst_plot(df_CI_remote_cond, df_CI_sphyg_cond)
    no_cond_syst.no_cond_syst_plot(df_CI_remote_no_cond, df_CI_sphyg_no_cond)

    cond_diast.cond_diast_plot(df_CI_remote_cond, df_CI_sphyg_cond)
    no_cond_diast.no_cond_diast_plot(df_CI_remote_no_cond, df_CI_sphyg_no_cond)

    #The t-test analysis
    cond_t_stat.cond_t_stat_analysis(df_CI_remote_cond, df_CI_sphyg_cond)
    cond_t_stat.cond_t_stat_analysis(df_CI_remote_no_cond, df_CI_sphyg_no_cond)

if __name__ == "__main__":
    args = parser.parse_args()
    process_all(args.remote_dataset, args.sphyg_dataset)