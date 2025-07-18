#!/bin/bash

# Add local bin to PATH
export PATH=$PATH:/home/ubuntu/.local/bin

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "Streamlit not found. Installing..."
    pip3 install --break-system-packages streamlit
fi

# Create data2 directory if it doesn't exist
mkdir -p data2

# Run the Streamlit application
echo "Starting Talk2PDF application..."
echo "Open your browser and go to http://localhost:8501"
streamlit run main.py