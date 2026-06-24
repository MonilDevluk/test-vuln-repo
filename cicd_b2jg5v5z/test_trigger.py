import subprocess

def run_command(user_input):
    allowed_commands = ['ls', 'echo', 'cat']
    command = ' '.join(["ls", user_input])
    result = subprocess.check_output(command, shell=False, universal_newlines=True)
    for allowed_command in allowed_commands:
        if command.startswith(allowed_command):
            return result
    return f"Command {command} is not allowed"