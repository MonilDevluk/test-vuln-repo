import subprocess
import shlex

def run_command(user_input):
    command_args = shlex.split("ls " + user_input)
    result = subprocess.check_output(command_args)
    return result.decode()