import yaml

with open('../config.yaml', 'r') as file:
    config = yaml.safe_load(file)

if config['run_localhost']:
    print("Error: Cannot run on localhost.")
