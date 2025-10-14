import paramiko

def ssh_to_wsl2(host, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    print("Output:")
    print(stdout.read().decode())
    print("Error:")
    print(stderr.read().decode())
    ssh.close()

if __name__ == "__main__":
    wsl2_ip = "<WSL2_IP>"
    user = "<ubuntu_username>"
    pwd = "<your_password>"
    cmd = "ls -l ~"

    ssh_to_wsl2(wsl2_ip, user, pwd, cmd)