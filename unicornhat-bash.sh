#!/bin/bash

randint() {
  rand=$RANDOM
  let "rand %= $1"
  echo $rand
}

hexify() {
  result=$(printf %02x $1)
  echo $result
}

if [ ! -S /var/run/unicornd.socket ]; then
  echo "Please start the unicornd daemon/service & rerun the script\n"
  exit
fi

clear_unicornhat() {
  string="\x02"
  for i in `seq 0 63`;
  do
    string+="\x00\x00\x00"
  done
  echo -e $string | socat - UNIX-CONNECT:/var/run/unicornd.socket
}


$(clear_unicornhat)

while true
do
  x=$(randint 8)
  y=$(randint 8)
  r=$(randint 256)
  g=$(randint 256)
  b=$(randint 256)

  echo -e "\x01\x"$(hexify $x)"\x"$(hexify $y)"\x"$(hexify $r)"\x"$(hexify $g)"\x"$(hexify $b) | socat - UNIX-CONNECT:/var/run/unicornd.socket
  echo -e '\x03' | socat - UNIX-CONNECT:/var/run/unicornd.socket
done
