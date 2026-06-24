import subprocess

def run_command(user_input):
    result = subprocess.check_output(f"ls {user_input}", shell=False)
    return result.decode()