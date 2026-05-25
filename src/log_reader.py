import subprocess

def get_security_logs():
    command = 'wevtutil qe Security /c:500 /f:text'
    logs = subprocess.check_output(command, shell=True, text=True)
    return logs


if __name__ == "__main__":
    logs = get_security_logs()
    print(logs)