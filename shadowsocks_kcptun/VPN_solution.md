
# Shadowsocks and Kcptun, a VPN solution


## [Shadowsocks](https://shadowsocks.org/en/index.html)

A secure socks5 proxy. 

 - Setup
> pip install shadowsocks

- Startup server
> ssserver -p PORT -k password -m aes-256-cfb

- Startup client
> sslocal -s serverIP -p serverPORT -b 0.0.0.0 -l 8880 -m aes-256-cfb -k password

Set your socks proxy to localhost:8880, then you can use Shadowsocks to Browse foreign domains.

- Used in command line

> apt-get install proxychains

Make a config file at ~/.proxychains/proxychains.conf with content:

    strict_chain
    proxy_dns 
    remote_dns_subnet 224
    tcp_read_time_out 15000
    tcp_connect_time_out 8000
    localnet 127.0.0.0/255.0.0.0
    quiet_mode
    
    [ProxyList]
    socks5  127.0.0.1 8880
 
 Then run command with proxychains. Examples:

> proxychains curl https://www.twitter.com/

- Configure Multiple Users

Currently Python and Go servers support multiple users.
You can use different passwords on different ports like this:

    {
            "server": "0.0.0.0",
            "port_password": {
                "8381": "foobar1",
                "8382": "foobar2",
                "8383": "foobar3",
                "8384": "foobar4"
            },
            "timeout": 300,
            "method": "aes-256-cfb"
    }

Each user will occupy a port

## [Kcptun](https://github.com/xtaci/kcptun)

A Secure Tunnel Based On [KCP](https://github.com/skywind3000/kcp/wiki/EN_Home) with N:M Multiplexing.

    Application -> KCP Client(8388/tcp) -> KCP Server(4000/udp) -> Server(8388/tcp)

![kcptun_connect](https://raw.githubusercontent.com/xtaci/kcptun/master/kcptun.png)

-  [Download Precompiled Released Page](https://github.com/xtaci/kcptun/releases)

- Startup server
> ./server_linux_amd64 -t "TARGET_IP:8388" -l ":4000" -mode fast2

- Startup client
> ./client_darwin_amd64 -r "KCP_SERVER_IP:4000" -l ":8388" -mode fast2


## Connect Shadowsocks and Kcptun

![Shadowsocks_and_Kcptun](http://upload-images.jianshu.io/upload_images/957246-707c314e6015b72b.png)


    Network Proxy(10.0.0.105:8880)
    <-> Shadowsocks Client(from localhost:7880 to 0.0.0.0:8880)
    <-> KCP Client(from serverIP:PORT2 to localhost:7880)
    <->
    <-> KCP Server(from localhost:PORT1 to 0.0.0.0:PORT2)
    <-> Shadowsocks Server(localhost:PORT1)


## [Flora_Pac](https://github.com/usufu/Flora_Pac)

Proxy auto-config,  will not use proxy server to link baidu but google.
Use Flora_Pac to generate PAC file, and used in Automatic Proxy Configuration.
