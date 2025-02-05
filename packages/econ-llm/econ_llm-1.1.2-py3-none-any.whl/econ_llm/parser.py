# Parse the logs from experiment runs

# System imports
import os
# Parsing imports
import json
import io
import pandas as pd

# Log directory
LOGS = f"{os.path.expanduser('~')}/econ-llm-data"

def parse(experiment_id: str = "", user_id: str = "", timestamp: str = ""):
    """
    Parse the logs from experiment runs.

    Parameters
    ----------
    experiment_id : str, optional
        The experiment ID.
    user_id : str, optional
        The user ID.
    timestamp : str, optional
        The timestamp (yyyy-mm-dd-hh), 24 hours hour format.
    
    Notes
    -----
    - For all parameters, the default value means match any value.
    """
    # Validate timestamp
    if timestamp:
        if len(timestamp) != 13:
            raise ValueError("Invalid timestamp format. Use yyyy-mm-dd-hh.")
    
    # Get the relevant logs
    logs = []
    for log in os.listdir(LOGS):
        # Check if the log matches requirements
        if not log.endswith(".json"):
            continue
        if experiment_id and experiment_id not in log:
            continue
        if user_id and user_id not in log:
            continue
        if timestamp and timestamp not in log:
            continue
        logs.append(log)
    
    # Parse the logs
    data = []
    for log in logs:
        with open(os.path.join(LOGS, log), "r") as f:
            data.append(json.load(f))

if __name__ == '__main__':
    parse(user_id="agent_two")
