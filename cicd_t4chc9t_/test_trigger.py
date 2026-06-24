import subprocess
def run_command(user_input):
    result = subprocess.check_output(["ls"] + [user_input], env={'LANG': 'en_US.UTF-8'})
    return result.decode()