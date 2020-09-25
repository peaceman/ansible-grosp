Ansible Role: node_exporter
===========================

Installs and configures the prometheus node exporter

Role Variables
--------------

```yaml
# if defined the peaceman.pki wont be used for certificate file copying
node_exporter_ca_file:
node_exporter_cert_file:
node_exporter_cert_key_file:
```

Dependencies
------------
Roles
* peaceman.pki
  * Required if no paths to the certificate files are defined via variables
* cloudalchemy.node-exporter
* weareinteractive.ufw
