Ansible Role: nss
=================

Role Variables
--------------

Uses

```
# folder on the host that executes ansible
# will be used to store the certificate authority and more
local_data_dir: data
```

Defines

```
# will be used as dirname to store ca related files below $local_data_dir/nss
nss_ca_dirname: ca

# will be used as dirname to store certificates
nss_certs_dirname: certs

# will be used to determine the necessary client certificates for nss
nss_client_certs_group_name: nss_clients
```