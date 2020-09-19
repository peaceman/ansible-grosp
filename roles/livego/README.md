Ansible Role: livego
====================

Installs livego

Requirements
------------

Requires an already available systemd service for livego that is available
under the name {{ livego_server_name }}

Role Variables
--------------

```yaml
livego_binary_url: https://github.com/gwuhaolin/livego/releases/download/0.0.11/livego_0.0.11_linux_amd64.tar.gz
livego_binary_checksum: sha256:772fc895b1daab37e3346758606c6d977e534a86d73d27dfb2456303f0f782cb
livego_service_name: livego

# livego configuration
livego_logging_level: debug
livego_rtmp_addr: ":1935"
livego_rtmp_read_timeout: 10
livego_rtmp_write_timeout: 10
livego_hls_addr: "127.0.0.1:7002"
livego_api_addr: "127.0.0.1:8090"
livego_servers: []
```
