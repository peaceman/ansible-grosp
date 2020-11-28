Ansible Role: nginx_rtmp_hls
============================

Installs nginx via docker-compose as rtmp ingest service

Requirements
------------

Requires a running docker and the python packages docker and docker-compose

Role Variables
--------------

```yaml
nginx_rtmp_hls_docker_compose_project_folder: /opt/docker/nginx-rtmp-hls
nginx_rtmp_hls_git_repo_url: https://github.com/peaceman/nginx-rtmp-hls.git
nginx_rtmp_hls_git_version: master

# secret key that is used to verify the signature of the jwt that is used as stream key
nginx_rtmp_hls_jwt_signing_key:

nginx_rtmp_hls_rtmp_port: 1935
nginx_rtmp_hls_http_port: "127.0.0.1:4202"

```
