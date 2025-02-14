import numpy as np
import pandas as pd
import scipy.stats as st

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



def sphyg_features(SPHYG_DATASET):
    sns.set_style("whitegrid")

    df = pd.read_excel(SPHYG_DATASET)

    df_sphyg_cond = df[df["Condition"] != "None"]
    df_sphyg_no_cond = df[df["Condition"] == "None"]


    #for those with conditions
    x = []
    for i in set(df_sphyg_cond["ID"]):
        user_data = df_sphyg_cond[df_sphyg_cond["ID"] == i]
        len_user_data = len(user_data)
        
        data_bpm = user_data["BPM"].to_list()
        mean_bpm = np.mean(data_bpm)
        
        data_systolic = user_data["SYS"].to_list()
        mean_systolic = np.mean(data_systolic)
        
        
        data_diastolic = user_data["DIA"].to_list()
        mean_diastolic = np.mean(data_diastolic)
        
        
        bpm_CI = st.t.interval(confidence=0.95, df=len_user_data-1, loc=mean_bpm, scale=st.sem(data_bpm))
        systolic_CI = st.t.interval(confidence=0.95, df=len_user_data-1, loc=mean_systolic, scale=st.sem(data_systolic))
        diastolic_CI = st.t.interval(confidence=0.95, df=len_user_data-1, loc=mean_diastolic, scale=st.sem(data_diastolic))
        
        bpm_CI_value = mean_bpm - bpm_CI[0]
        systolic_CI_value = mean_systolic - systolic_CI[0]
        diastolic_CI_value = mean_diastolic - diastolic_CI[0]
        
        if (str(bpm_CI_value) == "nan"):
            bpm_CI_value  = 0.00

        if (str(systolic_CI_value) == "nan"):
            systolic_CI_value  = 0.00
            
        if (str(diastolic_CI_value) == "nan"):
            diastolic_CI_value  = 0.00
            
        
        computed = {
                    "User":i,
                    "mean_bpm (Sypgmomanometer)":float("%.2f" % mean_bpm),
                    "bpm_CI_value (Sypgmomanometer)":float("%.2f" % bpm_CI_value),
                    "mean_systolic (Sypgmomanometer)":float("%.2f" % mean_systolic),
                    "systolic_CI_value (Sypgmomanometer)":float("%.2f" % systolic_CI_value),
                    "mean_diastolic (Sypgmomanometer)":float("%.2f" % mean_diastolic),
                    "diastolic_CI_value (Sypgmomanometer)":float("%.2f" % diastolic_CI_value)
                }
        x.append(computed)

    #for those without conditions
    y = []
    for i in set(df_sphyg_no_cond["ID"]):
        user_data = df_sphyg_no_cond[df_sphyg_no_cond["ID"] == i]
        len_user_data = len(user_data)
        
        data_bpm = user_data["BPM"].to_list()
        mean_bpm = np.mean(data_bpm)
        
        data_systolic = user_data["SYS"].to_list()
        mean_systolic = np.mean(data_systolic)
        
        
        data_diastolic = user_data["DIA"].to_list()
        mean_diastolic = np.mean(data_diastolic)
        
        
        bpm_CI = st.t.interval(confidence=0.95, df=len_user_data-1, loc=mean_bpm, scale=st.sem(data_bpm))
        systolic_CI = st.t.interval(confidence=0.95, df=len_user_data-1, loc=mean_systolic, scale=st.sem(data_systolic))
        diastolic_CI = st.t.interval(confidence=0.95, df=len_user_data-1, loc=mean_diastolic, scale=st.sem(data_diastolic))
        
        bpm_CI_value = mean_bpm - bpm_CI[0]
        systolic_CI_value = mean_systolic - systolic_CI[0]
        diastolic_CI_value = mean_diastolic - diastolic_CI[0]
        
        if (str(bpm_CI_value) == "nan"):
            bpm_CI_value  = 0.00

        if (str(systolic_CI_value) == "nan"):
            systolic_CI_value  = 0.00
            
        if (str(diastolic_CI_value) == "nan"):
            diastolic_CI_value  = 0.00
            
        
        computed = {
                    "User":i,
                    "mean_bpm (Sypgmomanometer)":float("%.2f" % mean_bpm),
                    "bpm_CI_value (Sypgmomanometer)":float("%.2f" % bpm_CI_value),
                    "mean_systolic (Sypgmomanometer)":float("%.2f" % mean_systolic),
                    "systolic_CI_value (Sypgmomanometer)":float("%.2f" % systolic_CI_value),
                    "mean_diastolic (Sypgmomanometer)":float("%.2f" % mean_diastolic),
                    "diastolic_CI_value (Sypgmomanometer)":float("%.2f" % diastolic_CI_value)
                }
        y.append(computed)
    
    df_CI_sphyg_cond = pd.DataFrame(x).sort_values(by = "User", ignore_index = True)
    df_CI_sphyg_no_cond = pd.DataFrame(y).sort_values(by = "User", ignore_index = True)

    return (df_CI_sphyg_cond, df_CI_sphyg_no_cond)