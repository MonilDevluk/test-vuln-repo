import subprocess
import shlex

def run_command(user_input):
    command_parts = shlex.split("ls " + user_input)
    result = subprocess.check_output(command_parts)
    return result.decode()