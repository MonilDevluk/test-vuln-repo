import subprocess
import shlex
def run_command(user_input):
    command = shlex.split("ls " + user_input)
    result = subprocess.check_output(command)
    return result.decode()