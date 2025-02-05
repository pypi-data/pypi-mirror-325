# econ-llm
A python package that uses LLM agents to automate experiments using the VEcon Lab Website.

## ToDo 
- [ ] add parser to package

## Installation
To install the package, run the following command:
```bash
pip install econ-llm
```

## Dependencies
### Experiment Execution
```bash
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
```
`secrets.txt` needs to contain the following two lines:
OpenAI_API_KEY
Github_Username Github_Access_Token
And also be in the same directory as execution.

### Upload
Assumes git credentials are set
```bash
git config --global user.email "YOUR_EMAIL"
git config --global user.name "YOUR_NAME"
```

## Commands
### Run
To run an experiment (multi-round ultimatum game), use the following command:
```bash
econ-llm run [experiment_id] [user_id]
```
The agent automatically detects if it is a proposer or responder.

### Upload
Upload output to `econ-llm-data` using the following command:
```bash
econ-llm upload
```

### Visualize
Visualize the output using the following command:
```bash
econ-llm visualize
```

### Upgrade
To update the package, use the following command:
```bash
econ-llm upgrade
```

## Output
The output will be saved in the `~/econ-llm-data` directory. File names contains experiment_id, user_id, and timestamp. Metadata includes the previous and the role of the agent.

## Specification
The package is currently using `gpt-4o-2024-08-06` as the model from OpenAI.

## Change Log
### Version 1.X.X
#### Version 1.1.X
- 1.1.3:
    - Add visualizer command
- 1.1.2: 
    - Update logging structure
    - Add log parsing
    - Auality of life improvements 
        - Use aboslute import paths
        - Better argument parsing
- 1.1.1: 
    - Initial stable release
    - Contains working versions of proposer/responder for multi-round ultimatum game.
