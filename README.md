# Script Executor

A Python package to manage command/script execution with support for sequential and immediate modes.

## Installation
```bash
pip install .
```

## Usage

### Run Bash Script
```bash
script-executor --mode immediate --on_fail continue bash x.sh --arg1 value1
```

### Run Python Script
```bash
script-executor --mode sequential python a.py --arg1 value1
```

### Execute Make Command
```bash
script-executor --mode immediate make
```

### Change Directory
```bash
script-executor --mode sequential cd /path/to/directory
```

### Run Custom Shell Command
```bash
script-executor --mode immediate --on_fail stop echo "Hello, World!"
```

### Multiple Commands Sequentially
```bash
script-executor --mode sequential --on_fail continue bash setup.sh && python train.py && make install
```

### View Output Logs
All command outputs are saved in the `script_outputs` directory with timestamped filenames:
```bash
cat script_outputs/20250116_153045_command.log
```

### MANIFEST.in
include README.md
