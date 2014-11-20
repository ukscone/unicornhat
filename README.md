

Silly little pimoroni UnicornHAT stuff

unimess
=======
utility to send the stdin and dump it on to the unicorn HAT a char at a time.

ls -al | sudo ./unimess.py 

 /sbin/ifconfig | sed -n '/inet [Aa]d\{1,2\}r\{0,1\}:/ { s# *inet [Aa]d\{1,2\}r\{0,1\}:##; s# .*##p }' | sudo ./unimess.py

uni-2048
========

Borrowed ( http://www.thetaranights.com/make-a-2048-game-in-python/ )& modded python version of 2048 that uses unicornHAT as the display.
