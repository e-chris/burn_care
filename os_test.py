#!/usr/bin/env python3

import os
command = 'sudo iptables -A INPUT -p tcp -s any --sport 22 -d any --dport 22 -j ACCEPT'
print(command)
os.system(command)

