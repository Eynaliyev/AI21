import openai
import os
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from tasks import prompts
from config import RESPONSES_CSV_PATH

from analyze_data import analyze_data
from quick_look import quick_look
from store_results import store_results
from call_agent import call_agent
from visualize import visualize
from process_combinations import process_combinations

# Step 1: Set up Python project
# Make sure to install necessary packages
# you can run the setup.py script

# Define the global variable for the 'responses.csv' file
_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    # Add the main logic of your script here

    process_combinations()
    
    # Step 4: Use pandas to analyze it
    # Load data from CSV
    data = pd.read_csv(RESPONSES_CSV_PATH)

    # Take a quick look at data
    # quick_look(data)

    # Step 5: Dig deeper analyze it
    # For simplicity, we'll analyze the average length of responses
    analyze_data(data)

    # Step 6: Visualize it
    # Here, we'll simply plot the length of the responses
    visualize(data)


    # Step 7: Clean the data
    # Removing any leading/trailing whitespace from responses
    data['Response'] = data['Response'].apply(lambda x: x.strip())

    # Step 8: Index it
    # Adding an index column to the DataFrame
    data['Index'] = range(1, len(data) + 1)

    # Step 9: Re-analyze again
    # Recalculate the average length of responses after cleaning
    average_length_cleaned = data['Response Length'].mean()
    # print(f"Average response length after cleaning: {average_length_cleaned}")

main()