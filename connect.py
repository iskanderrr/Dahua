import socket
import struct
import time
try:
    login = ""
    passw = ""
    ip = ""
    con = socket.create_connection((ip, 37777))
    con.send(b'\xa0\x00\x00\x60%b\x00\x00\x00%b%b%b%b\x04\x01\x00\x00\x00\x00\xa1\xaa%b&&%b\x00Random:%b\r\n\r\n' % (struct.pack('b', 24 + len(login) + len(passw)),
                                    login.encode('ascii'),
                                    (8-len(login)) * b'\x00', passw.encode('ascii'),
                                    (8-len(passw)) * b'\x00', login.encode('ascii'),
                                    passw.encode('ascii'), str(int(time.time())).encode('ascii')))
    data = con.recv(128)
    if data[8]==0:
        print("success")
    else:
        print("login failed")
except:
    print("error")
