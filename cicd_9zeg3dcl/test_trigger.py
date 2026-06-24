import subprocess

def run_command(user_input):
    result = subprocess.check_output(["ls", user_input], capture_output=True)
    return result.decode().rstrip('\n')