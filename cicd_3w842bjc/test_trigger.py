import subprocess
def run_command(user_input):
    result = subprocess.check_output(["ls", user_input], universal_newlines=True)
    return result