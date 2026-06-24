import subprocess
import shutil
def run_command(user_input):
    if shutil.which(user_input):
        result = subprocess.check_output(user_input, shell=False)
        return result.decode()
    else:
        return "Command not found: " + user_input