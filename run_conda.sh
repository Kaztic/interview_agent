#!/bin/bash

# First try to source conda from common locations
if [ -f "$HOME/anaconda3/etc/profile.d/conda.sh" ]; then
    . "$HOME/anaconda3/etc/profile.d/conda.sh"
elif [ -f "$HOME/miniconda3/etc/profile.d/conda.sh" ]; then
    . "$HOME/miniconda3/etc/profile.d/conda.sh"
else
    echo "Could not find conda.sh. Please ensure Conda is installed correctly."
    exit 1
fi

# Initialize conda in the shell
conda init bash
source ~/.bashrc

# Activate the environment
conda activate interview_agent

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "Failed to activate conda environment. Please ensure:"
    echo "1. The environment 'interview_agent' exists (run: conda env create -f environment.yml)"
    echo "2. Conda is properly initialized"
    exit 1
fi

# Start the FastAPI server
uvicorn server:app --reload --host 0.0.0.0 --port 8000 