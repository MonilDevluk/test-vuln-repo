import subprocess
import shlex

def run_command(user_input):
    result = subprocess.check_output(shlex.split("ls " + user_input))
    return result.decode()