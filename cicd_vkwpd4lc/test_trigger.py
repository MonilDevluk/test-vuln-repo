import subprocess
def run_command(user_input):
    args = ['ls']
    try:
        result = subprocess.check_output(args + [user_input])
        return result.decode()
    except subprocess.CalledProcessError as e:
        return str(e)