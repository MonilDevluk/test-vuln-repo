import subprocess
import shlex
def run_command(user_input):
    try:
        result = subprocess.check_output("ls " + shlex.quote(user_input), shell=False)
    except subprocess.CalledProcessError as e:
        return str(e)
    return result.decode()