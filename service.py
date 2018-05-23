import cv2
import socket
import threading
import time
import sys
from tuscen import *
config={}
def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('10.164.33.222', 6666))
        s.listen(1)
        #cv2.VideoCapture(0)
    except socket.error as msg:
        print msg
        #camera.close()
        sys.exit(1)
    print 'Waiting connection...'
        
    while 1:
        conn, addr = s.accept()
        deal_data(conn,addr)
    #    conn, addr = s.accept()
    #    t = threading.Thread(target=deal_data, args=(conn, addr,camera))
    #    t.start()

def deal_data(conn, addr,camera=None):
    print 'Accept new connection from {0}'.format(addr)
    #conn.send('Hi, Welcome to the server!')
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    camera = ccd()
    while 1:
        data = conn.recv(1024).decode()
        #print '{0} client send data is {1}'.format(addr, data)
        #time.sleep(1)
        if data == 'exit' or not data:
            print '{0} connection close'.format(addr)
            conn.send('Connection closed!'.encode())
            break
        elif data[0:7] == 'acquire':
            #print('##############')
            img = camera.read()
            img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
            data_tobe_send=cv2.imencode('.jpg',img,encode_param)[1].tostring()
            #print('len',len(data_tobe_send)) 
            conn.send(str(len(data_tobe_send)).ljust(16))
            conn.send(data_tobe_send);
            #conn.send(data_tobe_send.encode('utf-8'))
            #time.sleep(1)
    conn.close()
    camera.stop()

if __name__ == '__main__':
    socket_service()