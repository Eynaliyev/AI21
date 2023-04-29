import os
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

def visualize(data):
    # Here, we'll simply plot the length of the responses
    data['Response Length'] = data['Response'].apply(len)
    current_file_path = Path(__file__).resolve()
    parent_folder_path = current_file_path.parent.parent
    folder_path = os.path.join(parent_folder_path, 'results', 'plots')
    
    # Bar plot - per model
    plt.figure()
    sns.countplot(data=data, x='Model', hue='Helpfulness')
    plt.title('Helpfulness ranking per model')
    plt.savefig(f"""{folder_path}/helpfulness_per_model.png""", dpi=300)

    # Scatter plot - LLM name vs performance
    plt.figure()
    sns.scatterplot(data=data, x='Model', y='Helpfulness')
    plt.title('Performance scatter plot')
    plt.savefig(f"""{folder_path}/performance_scatter_plot.png""", dpi=300)

    # Scatter plot - context length tokens used vs score
    data['Task Length'] = data['Task'].apply(len)
    plt.figure()
    sns.scatterplot(data=data, x='Task Length', y='Helpfulness')
    plt.title('Context length tokens used vs score scatter plot')
    plt.savefig(f"""{folder_path}/context_length_vs_score_scatter_plot.png""", dpi=300)

    # Scatter plot - response length
    plt.figure()
    sns.scatterplot(data=data, x='Response Length', y='Helpfulness')
    plt.title('Response length scatter plot')
    plt.savefig(f"""{folder_path}/response_length_scatter_plot.png""", dpi=300)
