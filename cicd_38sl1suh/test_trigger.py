import subprocess
def run_command(user_input):
    arguments = ["ls", user_input]
    result = subprocess.check_output(arguments)
    return result.decode()