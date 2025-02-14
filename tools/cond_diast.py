import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


#For Diastolic
def cond_diast_plot(df_CI_remote_cond, df_CI_sphyg_cond):
    fig = plt.figure()
    ax = fig.add_axes([0,0, 1, 1])
    j = 1

    for i in range(len(df_CI_remote_cond)):
        value_sphyg = df_CI_sphyg_cond.iloc[i, 5]
        ci_sphyg =  df_CI_sphyg_cond.iloc[i, 6]
        value_remote = df_CI_remote_cond.iloc[i, 5]
        ci_remote =  df_CI_remote_cond.iloc[i, 6]
        
        ax.errorbar(value_sphyg, j, 0, ci_sphyg, linestyle='None', marker='o', color = "b", label = "Spyhg")
        j+=1
        ax.errorbar(value_remote, j, 0, ci_remote, linestyle='None', marker='o', color = "magenta", label = "Remote")
        j+=10

    ax.set_xlabel('Mean Diastolic Blood Pressure')
    #ax.set_ylabel('mmHg')
    ax.set_title('Comparison of Sphygmomanometer and Smart Watch\'s Mean Diastolic BP in Users with Health Conditions')
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.legend(['Sphymomanometer', 'Smartwatch'])

    output_file = "output/diastolic_with_health_conditions.png"
    plt.savefig(output_file, bbox_inches='tight', dpi=150)