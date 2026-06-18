import boto3
from app.config import *

def get_ec2_instances():

    ec2 = boto3.client(
        'ec2',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )

    response = ec2.describe_instances()

    instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:

            instances.append({
                "id": instance['InstanceId'],
                "state": instance['State']['Name']
            })

    return instances