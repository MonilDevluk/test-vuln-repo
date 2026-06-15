import subprocess
def run_command(user_input):
    result = subprocess.check_output("ls " + user_input, shell=False)
    result = subprocess.check_output(["ls", user_input]).decode()
    return result