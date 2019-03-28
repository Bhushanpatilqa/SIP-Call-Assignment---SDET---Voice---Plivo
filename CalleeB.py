import paramiko
from time import sleep


class remote_CallerB:
    def __init__(self,ip,username,password):
        self.ip=ip
        self.username=username
        self.password=password
        #self.n=n
        #print(n)
    def remote_connect(self):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.ip, port=22, username=self.username, password=self.password)
        print ('Logging in to SIPP Callee Machine')
        remote_connect=client.invoke_shell()
        return remote_connect, client
    def execute_commands(self, *n):
        self.n=n
        remote_connect, client=self.remote_connect()
        for commands in self.n:
            if commands.startswith('./sipp'):
                remote_connect.send(commands)
                remote_connect.send('\n')
                print("Wait your SIPP call is getting finished")
                sleep(60)
                output=remote_connect.recv(9999999)
                print (output.decode())
                remote_connect.send("\x03")
            else:
                remote_connect.send(commands)
                remote_connect.send('\n')
                sleep(1)
                output=remote_connect.recv(9999)
                print (output.decode())            
        remote_connect.close()
        client.close()
a=remote_CallerBremote_CallerA(IP ADDR,Username,Password)

""" Use below SIPP commands: in below method for CallerB:
./sipp -sf registerB.xml -inf registerB.csv -m 1 -l 1 trace_err uaBplivoReg.log phone.plivo.com
./sipp -sf uasplivo.xml -inf uasplivo.csv -m 1 -l 1 trace_err uaBplivo_udp.log phone.plivo.com
"""
""" Pass the Linux command to login as a root, changing the current DIR to SIPP """
a.execute_commands('cd /home/yoursystem/sipp-3.5.2','pwd','su','password','./sipp -t t1  -sf uasplivo.xml -inf uasplivo.csv -m 1 -l 1 -trace_err Caller.log phone.plivo.com')  


