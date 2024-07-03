# CTFd-docker
One-click configuration of CTFd using Docker


## Quick installation

You need to modify CTFD_URL, DIRECT_URL, DYNAMIC_URL in docker-compose.yml and resolve it on the DNS server



The script will automatically initialize the configuration when it is executed for the first time, and it cannot be automatically modified after initialization

```
sudo apt install git -y
git clone https://github.com/expiol/CTF_Integration.git CTFd
vi CTFd/docker-compose.yml
#Modify CTFD_URL, DIRECT_URL, DYNAMIC_URL, and resolve on the DNS server
sudo sh CTFd/install.sh
```

