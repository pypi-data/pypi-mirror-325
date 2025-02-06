import yaml

def generate_commands(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    # Logic to generate commands from the configuration
    commands = []
    for test in config['tests']:
        command = f"run_test --name {test['name']} --params {test['params']}"
        commands.append(command)
    
    return commands
