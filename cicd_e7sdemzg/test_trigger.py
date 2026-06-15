import subprocess
import shlex

def run_command(user_input):
    args = shlex.split("ls " + user_input)
    result = subprocess.check_output(args)
    return result.decode()