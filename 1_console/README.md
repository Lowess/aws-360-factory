## AWS Console

The goal of this exercise is to start an EC2 from the console.

* First go to the `EC2` service:

![Console 1](../docs/console-1.png)

* Then click on `Launch Instance`

![Console 2](../docs/console-2.png)

* **Choose AMI** Find and select the latest `AMI` built for `Ubuntu 16.04` using an `EBS` root device and running on `HVM`

![Console 3](../docs/console-3.png)

* **Choose Instance Type** Let's use a `t2.micro` for this example

![Console 4](../docs/console-4.png)

* **Configure Instance** Start the instance in the `default VPC`. Make sure it's placed in a `public subnet` in AZ `us-east-1b`

![Console 5](../docs/console-5.png)

* **Add Storage** Ensure the EBS `root` volume is `20G`

![Console 6](../docs/console-6.png)

* **Add Tags** Add meaningful tags to your instance to clearly identify it's purpose, environment, etc...

![Console 7](../docs/console-7.png)

* **Configure Security Group** Create a new security group named `ops` that will allow us to connect to the server using SSH

![Console 8](../docs/console-8.png)

* **Review** Review your instace details and launch the instance !

![Console 9](../docs/console-9.png)

* Create an SSH Keypair in order to be able to connect to your server

![Console 10](../docs/console-10.png)

* Visit the EC2 main page and connect to your server

![Console 11](../docs/console-11.png)
![Console 12](../docs/console-12.png)
