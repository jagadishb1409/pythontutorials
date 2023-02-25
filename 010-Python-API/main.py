
import paramiko

# create an SSH client
ssh = paramiko.SSHClient()

# automatically add the server's key
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to the server
ssh.connect('example.com', username='username', password='password')

# execute a command
stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.readlines())

# close the connection
ssh.close()


# second method

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

key = paramiko.RSAKey.from_private_key_file('/path/to/your/key.pem')

ssh.connect(hostname='<your-instance-ip-address>', username='<your-username>', pkey=key)

stdin, stdout, stderr = ssh.exec_command('ls')

print(stdout.readlines())

ssh.close()
