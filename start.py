import os
import subprocess

# Install dependencies
subprocess.run(["pip", "install", "-r", "requirements.txt"])

# Run Streamlit
subprocess.run(["streamlit", "run", "app.py", "--server.port", os.getenv("PORT", 8501)])
