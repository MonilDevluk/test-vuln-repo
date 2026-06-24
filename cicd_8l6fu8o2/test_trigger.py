import subprocess
def run_command(user_input):
    result = subprocess.check_output(["/bin/ls", user_input])
    return result.decode()