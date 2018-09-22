## Ansible

The goal of this exercise is to start an EC2 instance using `ansible`.

* Install Ansible following the [documentation](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

This `ec2` role will be used moving forward as we provision new resources in the infrastructure.

Fork the following Github repository [ansible-role-ec2](https://github.com/Lowess/ansible-role-ec2) which contains an ansible
role skeleton.

> :point_up: In order to make the `ec2` module working with AWS Educate you need to make sure to export the `AWS_SESSION_TOKEN` env variables otherwise the module will fail provisioning.
