import subprocess
def run_command(user_input):
    result = subprocess.check_output(["ls"] + [user_input], stderr=subprocess.STDOUT)
    return result.decode()