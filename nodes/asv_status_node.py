!#/usr/bin/env

import socket
import rospy
from std_msgs.msg import String

def status_listener():
    sock =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('',11000))
    


