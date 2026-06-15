import subprocess
def run_command(user_input):
    result = subprocess.run(["ls", user_input], capture_output=True, text=True)
    return result.stdout