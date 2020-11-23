Ansible Role: eas
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
eas_docker_compose_project_folder: /opt/docker/eas
eas_docker_image: peaceman/grosp-eas:master

# will be passed as RUST_LOG env to eas
eas_log_level: debug
```
