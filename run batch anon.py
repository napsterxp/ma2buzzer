import telnetlib
import requests
host = "192.168.0.105"
port = "30000"
from time import sleep


import ftplib
def reset():
    session = ftplib.FTP('217.199.187.250','USERNAME','PASSWORD')
    file = open('helloworld.txt','rb')                  # file to send
    session.storbinary('STOR /public_html/wordpress/GLP/hits.txt', file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()

def Full():
    telnet_client = telnetlib.Telnet(host, port)
    print('Connection established')
    telnet_client.write(b'login MAUSER MAPWD')
    telnet_client.write(b'\r')
    telnet_client.write(b'Executor 1 at 100')
    telnet_client.write(b'\r')
    print('<END/>')





while True:
    url = "http://domain.com/wordpress/GLP/hits.txt"
    r = requests.get(url).text
    if r == "BMFL":
        Full()
        sleep(2)
        reset()
    else:
        sleep(1)

