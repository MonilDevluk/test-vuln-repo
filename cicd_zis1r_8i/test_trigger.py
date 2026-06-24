import subprocess
import shlex

def run_command(user_input):
    command = "ls " + user_input
    result = subprocess.check_output(shlex.split(command))
    return result.decode()