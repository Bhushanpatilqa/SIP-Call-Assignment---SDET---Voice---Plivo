import paramiko
from time import sleep


class remote_CallerA:
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
        print ('Logging in to SIPP caller Machine')
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
                output=remote_connect.recv(999999)
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
a=remote_CallerA('10.1.1.22','controller','admin')
""" Use below SIPP commands: in below method for CallerA:
For TCP Transport: 
/sipp-3.3/sipp -t t1 -sf uacplivo_tcp.xml -inf uacplivo.csv -m 1 -l 1 trace_err uacplivo_tcp.log phone.plivo.com
for UDP Transport:
/sipp-3.3/sipp -sf registerA.xml -inf registerA.csv -m 1 -l 1 trace_err uacplivoReg.log phone.plivo.com
/sipp-3.3/sipp -sf uacplivo.xml -inf uacplivo.csv -m 1 -l 1 trace_err uacplivo_udp.log phone.plivo.com
"""
a.execute_commands('cd /home/yoursystem/sipp-3.3','pwd','su','password','./sipp -t t1  -sn uac -sf uacplivo.xml -inf basiccall.csv  -m 1 -l 1 -trace_msg Registration.log phone.plivo.com')  

