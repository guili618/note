## docker的安装

### 官方安装脚本

```sh
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```

```sh
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
# Executing docker install script, commit: 36b78b2
+ sudo -E sh -c 'apt-get update -qq >/dev/null'
+ sudo -E sh -c 'apt-get install -y -qq apt-transport-https ca-certificates curl >/dev/null'
+ sudo -E sh -c 'curl -fsSL "https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg" | apt-key add -qq - >/dev/null'
+ sudo -E sh -c 'echo "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu xenial edge" > /etc/apt/sources.list.d/docker.list'
+ '[' ubuntu = debian ']'
+ sudo -E sh -c 'apt-get update -qq >/dev/null'
+ sudo -E sh -c 'apt-get install -y -qq --no-install-recommends docker-ce >/dev/null'
+ sudo -E sh -c 'docker version'
Client:
 Version:      18.05.0-ce
 API version:  1.37
 Go version:   go1.9.5
 Git commit:   f150324
 Built:        Wed May  9 22:16:25 2018
 OS/Arch:      linux/amd64
 Experimental: false
 Orchestrator: swarm

Server:
 Engine:
  Version:      18.05.0-ce
  API version:  1.37 (minimum version 1.12)
  Go version:   go1.9.5
  Git commit:   f150324
  Built:        Wed May  9 22:14:32 2018
  OS/Arch:      linux/amd64
  Experimental: false
If you would like to use Docker as a non-root user, you should now consider
adding your user to the "docker" group with something like:

  sudo usermod -aG docker guiax

Remember that you will have to log out and back in for this to take effect!

WARNING: Adding a user to the "docker" group will grant the ability to run
         containers which can be used to obtain root privileges on the
         docker host.
         Refer to https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface
         for more information.
```