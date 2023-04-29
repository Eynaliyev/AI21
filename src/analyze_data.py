import os
from pathlib import Path

def analyze_data(data):
    data['Response Length'] = data['Response'].apply(len)
    data['Task Length'] = data['Task'].apply(len)
    current_file_path = Path(__file__).resolve()
    parent_folder_path = current_file_path.parent.parent
    results_folder = os.path.join(parent_folder_path, 'results')
    output_file_path = os.path.join(results_folder, 'analysis_results.txt')

    with open(output_file_path, 'w') as output_file:
        # Mean performance score
        mean_performance = data[['Helpfulness', 'Honesty', 'Harmlessness', 'Factuality', 'Effectiveness']].mean()
        print("Mean performance scores:\n", mean_performance, file=output_file)
        print("\n", file=output_file)

        # Different context lengths - e.g. 50th, 75th percentile
        context_lengths = data['Task Length'].quantile([0.5, 0.75])
        print("Task length percentiles:\n", context_lengths, file=output_file)
        print("\n", file=output_file)

        # Deeper analysis of prompts that are too short - e.g. bottom 10th percentile length
        short_prompts = data[data['Task Length'] <= data['Task Length'].quantile(0.1)]
        high_scoring_short_prompts = short_prompts[short_prompts['Helpfulness'] >= 8]
        print("High scoring short prompts:\n", high_scoring_short_prompts, file=output_file)
        print("\n", file=output_file)

        # Sum of total tokens used for all steps of the task - to estimate cost
        task_tokens = data['Task Length'].sum()
        response_tokens = data['Task Length'].sum()
        total_tokens = task_tokens + response_tokens
        print("Total tokens used for all steps of the task:", total_tokens, file=output_file)
        print("\n", file=output_file)

        # Aggregate scores by LLM
        agg_scores_by_llm = data.groupby('Model')[['Helpfulness', 'Honesty', 'Harmlessness', 'Factuality', 'Effectiveness']].agg(['mean', 'median', 'count', 'std'])
        print("Aggregate scores by LLM:\n", agg_scores_by_llm, file=output_file)
        print("\n", file=output_file)

        # Aggregate scores by Evaluator
        agg_scores_by_evaluator = data.groupby('Evaluator')[['Helpfulness', 'Honesty', 'Harmlessness', 'Factuality', 'Effectiveness']].agg(['mean', 'median', 'count', 'std'])
        print("Aggregate scores by Evaluator:\n", agg_scores_by_evaluator, file=output_file)
        print("\n", file=output_file)

        
