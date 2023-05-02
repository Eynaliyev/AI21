# Project Name

A brief description of your project.

## Setup

### 1. Create a virtual environment

To store all dependencies, create a virtual environment:

```bash
python -m venv venv
```

### 2. Activate the virtual environment

```bash
source venv/bin/activate
```

### 3. Install dependencies

Navigate to the AI21 directory and run the setup script:

```bash
cd AI21
python setup.py
```

To deactivate the virtual environment, simply type:

```bash
deactivate
```

## Running the Script

Navigate to the src directory and run main.py:

```bash
cd src
python main.py
```

## Results

View the prompts, responses, and scores in the responses.csv file.
Visualizations can be found in the results/plots directory.
Analysis results can be viewed in the analysis_results.txt file.

Re-running the script should retrieve the results from the cache, not from the AI model.

API Keys
Set the API keys for the services in a .env file as shown below:

```bash
OPENAI_API_KEY=xyz
AI21_API_KEY=abc
```

Replace "Project Name" with the actual name of your project and provide a brief description. This improved version of the README provides clear instructions for setting up and running the project.
