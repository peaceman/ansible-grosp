Ansible Role: bps
=================

Requirements
------------

The main task list requires a running docker and the python packages
docker and docker-compose

```yaml
- import_role:
    name: peaceman.docker

- import_role:
    name: geerlingguy.pip
    vars:
    pip_install_packages:
        - name: docker
        - name: docker-compose
```


Role Variables
--------------

```yaml
bps_docker_compose_project_folder: /opt/docker/bps
bps_docker_image: peaceman/grosp-bps:master

# will be passed as RUST_LOG env to bps
bps_log_level: debug
bps_host_port: 2350
bps_segment_signing_key: ""
```
