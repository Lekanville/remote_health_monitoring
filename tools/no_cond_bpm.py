import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


#For BPM
def no_cond_bpm_plot(df_CI_remote_no_cond, df_CI_sphyg_no_cond):
    fig = plt.figure()
    ax = fig.add_axes([0,0, 1, 1])
    j = 1

    for i in range(len(df_CI_remote_no_cond)):
        value_sphyg = df_CI_sphyg_no_cond.iloc[i, 1]
        ci_sphyg =  df_CI_sphyg_no_cond.iloc[i, 2]
        value_remote = df_CI_remote_no_cond.iloc[i, 1]
        ci_remote =  df_CI_remote_no_cond.iloc[i, 2]
        
        ax.errorbar(value_sphyg, j, 0, ci_sphyg, linestyle='None', marker='o', color = "b", label = "Spyhg")
        j+=1
        ax.errorbar(value_remote, j, 0, ci_remote, linestyle='None', marker='o', color = "magenta", label = "Remote")
        j+=10

    ax.set_xlabel('Mean Beats Per Minute')
    #ax.set_ylabel('mmHg')
    ax.set_title('Comparison of Sphygmomanometer and Smart Watch\'s Mean BPM in Users without Health Conditions')
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.legend(['Sphymomanometer', 'Smartwatch'])

    output_file = "output/bpm_with_no_health_conditions.png"
    plt.savefig(output_file, bbox_inches='tight', dpi=150)