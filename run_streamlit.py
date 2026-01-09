#!/usr/bin/env python
"""
Safe wrapper to run Streamlit app without signal handling errors
"""
import os
import sys
import subprocess

if __name__ == "__main__":
    # Run streamlit with Python's threading workaround
    os.environ['PYTHONUNBUFFERED'] = '1'
    
    # Run the streamlit app
    cmd = [sys.executable, "-m", "streamlit", "run", "streamlit_app.py"]
    subprocess.run(cmd)
