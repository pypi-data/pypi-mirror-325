import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_accs(eps_list, cert_accs, adv_accs):
    x = np.arange(len(eps_list))  # the label locations
    width = 0.4  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(constrained_layout=True)
    
    data = {
        "Certified Accuracy": cert_accs,
        "Adversarial Accuracy": adv_accs
    }

    for attribute, measurement in data.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        
        labels = [f"{measure:.2f}" for measure in measurement]
        ax.bar_label(rects, labels=labels, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Accuracy')
    ax.set_title('Adv. and Certified Robustness')
    ax.set_xticks(x + width, eps_list)
    ax.legend(loc='upper right', ncols=1,)
    # ax.set_ylim(0, 1)
    
    fig.tight_layout(pad=2)
    
    plt.savefig("./bar_plot_accs.png")


def plot_results_boxplot(stats_path, boxplot_path):
    with open(stats_path, 'r') as f:
        stats = json.load(f)
    
    df = pd.DataFrame.from_dict({(i,j): stats[i][j] 
                           for i in stats.keys() 
                           for j in stats[i].keys()},
                       orient='index')
    df['network_eps'] = df.index.get_level_values(0)

    df_melted = df.melt(id_vars='network_eps', var_name='Evaluation Method', value_name='Accuracy')
    plt.figure(figsize=(20, 10))
    sns.boxplot(x='network_eps', y='Accuracy', data=df_melted, hue='Evaluation Method')
    plt.title("Distribution of Accuracies over 10 Training Runs")
    plt.savefig(boxplot_path)
    
    
if __name__ == "__main__":
    plot_results_boxplot('./results/gowal/mnist/stats.json', 'results/gowal/mnist/stats_boxplot.png')