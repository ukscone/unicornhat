unimess
=======

Silly little pimoroni UnicornHAT utility

messing around with my unicorn HAT and made a silly little utility to send the stdin and dump it on to the unicorn HAT a char at a time.

it's rubbish coz i don't python & what python i do do i suck at

ls -al | sudo ./unimess.py 
 /sbin/ifconfig | sed -n '/inet [Aa]d\{1,2\}r\{0,1\}:/ { s# *inet [Aa]d\{1,2\}r\{0,1\}:##; s# .*##p }' | sudo ./unimess.py
