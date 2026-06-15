import subprocess
def run_command(user_input):
    result = subprocess.run('ls', input=str(user_input).encode(), capture_output=True, text=True, shell=False).stdout
    return result