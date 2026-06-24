import subprocess
def run_command(user_input):
    command = "ls " + user_input
    result = subprocess.check_output(command, shell=False)
    return result.decode()