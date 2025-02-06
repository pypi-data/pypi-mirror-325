import os
import subprocess
import logging
from datetime import datetime
from celery import Celery
import yaml
from .database import log_run
from regression_testing_framework.command_generator import generate_commands

app = Celery("regression_framework")
app.config_from_object("celeryconfig")

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

@app.task
def run_test(config_path: str):
    """
    Runs test cases defined in a YAML configuration file and logs the output.
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    base_command = config['base_command']
    
    for run_name, run_config in config.items():
        if run_name == 'base_command':
            continue
        
        log_file = os.path.join(LOG_DIR, f"{run_name}.log")
        logging.basicConfig(filename=log_file, level=logging.INFO)
        
        start_time = datetime.utcnow()
        try:
            command = [base_command]
            for param in run_config['params']:
                for key, value in param.items():
                    if value is None:
                        command.append(f"-{key}")
                    else:
                        command.append(f"--{key}={value}")
            
            result = subprocess.run(command, capture_output=True, text=True)
            
            with open(log_file, "w") as log:
                log.write(result.stdout)
                log.write("\n" + result.stderr)
            
            success = result.returncode == 0
            error_trace = result.stderr.split("\n")[-3:] if not success else None
        
        except Exception as e:
            success = False
            error_trace = str(e).split("\n")[-3:]
        
        end_time = datetime.utcnow()
        log_run(run_name, success, start_time, end_time, log_file, error_trace)

        return {"config": run_name, "success": success, "log_file": log_file, "error_trace": error_trace}

@app.task
def publish_to_pypi():
    """
    Publishes the package to PyPI.
    """
    try:
        result = subprocess.run(["python3", "setup.py", "sdist", "bdist_wheel"], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Error creating distribution: {result.stderr}")
        
        result = subprocess.run(["twine", "upload", "dist/*"], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Error uploading to PyPI: {result.stderr}")
        
        logging.info("Successfully published to PyPI")
    except Exception as e:
        logging.error(f"Failed to publish to PyPI: {str(e)}")
        raise

def run_test_from_cli(config_path, output_path):
    commands = generate_commands(config_path)
    # Logic to execute the commands and generate the report
    for command in commands:
        # Ensure command is a list of strings
        command_list = command.split()
        result = subprocess.run(command_list, capture_output=True, text=True)
        # Handle the result as needed
        pass
    # Save the report to output_path

