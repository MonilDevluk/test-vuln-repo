import subprocess
import shlex

def run_command(user_input):
    if user_input is not None and user_input != "":
        command = f"ls {user_input}"
        result = subprocess.check_output(shlex.split(command))
        return result.decode()
    else:
        return "Invalid input"