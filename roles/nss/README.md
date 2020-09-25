Ansible Role: nss
=================

Requirements
------------

The main task list requires a running docker and the python packages
docker and docker-compose

```yaml
- import_role:
    name: peaceman.docker
```

Role Variables
--------------

Defines

```yaml
# will be used to determine the necessary client certificates for nss
nss_client_certs_group_name: nss_clients

# used during setup of the docker compose project on the edge node
nss_cert_file:
# used during setup of the docker compose project on the edge node
nss_cert_key_file:

nss_docker_compose_project_folder: /opt/docker/nss
nss_docker_image: peaceman/grosp-nss:master
```

Dependencies
------------

Roles
* peaceman.pki
