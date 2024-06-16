import boto3

session = boto3.Session()
ec2_client = session.client('ec2')

def get_ec2_instances():
    ec2_client = boto3.client('ec2')
    region = ec2_client.meta.region_name
    response = ec2_client.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                "InstanceId": instance['InstanceId'],
                "InstanceType": instance['InstanceType'],
                "State": instance['State']['Name'],
                "LaunchTime": instance['LaunchTime'],
                "Region": region
            })
    return instances

print(get_ec2_instances())
