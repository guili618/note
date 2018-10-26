## expect命令
---

###
```sh

#!/bin/bash

IP=(192.168.0.1 192.168.0.2 )
for ip_addr in "${IP[@]}"
    do
    /usr/bin/expect<<EOF
    send "ssh-copy-id -i .ssh/id_rsa.pub root@$ip_addr\r"
    expect -re {\? ?}
    send "yes\n"
    expect "root@$ip_addr's password:"
    send "password\n"
    expect eof
EOF
done
```