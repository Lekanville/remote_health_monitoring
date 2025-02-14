import numpy as np
import scipy.stats as st


def cond_t_stat_analysis(df_CI_remote_no_cond, df_CI_sphyg_no_cond):
    #The remote and sphyg bpms
    bpms_remote_no_cond = df_CI_remote_no_cond["mean_bpm (remote)"].to_list()
    bpms_sphyg_no_cond = df_CI_sphyg_no_cond["mean_bpm (Sypgmomanometer)"].to_list()

    #The remote and sphyg systolic bps
    sys_remote_no_cond = df_CI_remote_no_cond["mean_systolic (remote)"].to_list()
    sys_sphyg_no_cond = df_CI_sphyg_no_cond["mean_systolic (Sypgmomanometer)"].to_list()

    #The remote and sphyg diastolic bps
    dia_remote_no_cond = df_CI_remote_no_cond["mean_diastolic (remote)"].to_list()
    dia_sphyg_no_cond = df_CI_sphyg_no_cond["mean_diastolic (Sypgmomanometer)"].to_list()

    #The mean and ttest of remote and sphyg bpm
    bpm_mean_sphyg = np.mean(bpms_sphyg_no_cond)
    bpm_mean_remote = np.mean(bpms_remote_no_cond)
    bpm_ttest = st.ttest_rel(bpms_sphyg_no_cond, bpms_remote_no_cond)
    print("Mean sphygmomanometer BPM reading of users without health conditions: ", bpm_mean_sphyg)
    print("Mean smart watch BPM reading of users without health conditions: ", bpm_mean_remote)
    print(bpm_ttest)
    print("\n")

    #The mean and ttest of remote and sphyg systolic bp
    syst_mean_sphyg = np.mean(sys_sphyg_no_cond)
    syst_mean_remote = np.mean(sys_remote_no_cond)
    syst_ttest = st.ttest_rel(sys_sphyg_no_cond, sys_remote_no_cond)
    print("Mean sphygmomanometer systolic BP reading of users without health conditions: ", syst_mean_sphyg)
    print("Mean smart watch systolic BP reading of users without health conditions: ", syst_mean_remote)
    print(syst_ttest)
    print("\n")

    #The mean and ttest of remote and sphyg diastolic bp
    diast_mean_sphyg = np.mean(dia_sphyg_no_cond)
    diast_mean_remote = np.mean(dia_remote_no_cond)
    diast_ttest = st.ttest_rel(dia_sphyg_no_cond, dia_remote_no_cond)
    print("Mean sphygmomanometer diastolic BP reading of users without health conditions: ", diast_mean_sphyg)
    print("Mean smart watch diastolic BP reading of users without health conditions: ", diast_mean_remote)
    print(diast_ttest)
    print("\n")
    print("\n")

    #extract, standardize, impute, finemap