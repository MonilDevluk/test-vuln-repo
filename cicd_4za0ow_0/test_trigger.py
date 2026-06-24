import subprocess
def run_command(user_input):
    result = subprocess.check_output("ls " + user_input, shell=False)
    result = result.decode().splitlines()
    return '\n'.join(result)