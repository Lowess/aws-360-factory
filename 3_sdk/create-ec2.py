import boto3
import datetime


client = boto3.client('ec2')


def get_latest_ami_id(ami_name="ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server*"):
    amis = client.describe_images(
      Filters=[
          {
              'Name': 'name',
              'Values': [
                  ami_name
              ]
          }
      ]
    )
    latest_ami = None
    for ami in amis['Images']:
        if latest_ami is None or latest_ami <= ami['CreationDate']:
            latest_ami = ami

    return latest_ami['ImageId']


def get_vpc_id():
    pass


def get_subnet_id(vpc_id):
    pass


def get_security_group_id(group_names=[]):
    pass


def create_ec2(ami_id, subnet_id, group_ids):
    pass


if __name__ == "__main__":
    print(get_latest_ami_id())
