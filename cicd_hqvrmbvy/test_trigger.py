import subprocess
import shlex

def run_command(user_input):
    user_input = shlex.quote(user_input)
    result = subprocess.check_output(["ls", user_input])
    return result.decode()