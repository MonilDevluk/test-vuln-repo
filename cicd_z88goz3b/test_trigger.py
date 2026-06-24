import subprocess
import shlex

def run_command(user_input):
    arguments = shlex.split("ls " + user_input)
    result = subprocess.check_output(arguments)
    return result.decode()