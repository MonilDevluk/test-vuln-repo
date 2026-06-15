import subprocess
from pathlib import Path

def run_command(user_input):
    path = Path("/path/to/allowed/directory")
    result = subprocess.check_output([str(path / user_input)], env={"PATH": "/path/to/allowed/executables"})
    return result.decode()