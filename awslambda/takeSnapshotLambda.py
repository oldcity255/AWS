import boto3, json
session = boto3.Session(profile_name='development')
east = 'us-east-1'
ec2East = session.client('ec2', region_name = east)
ec2Resource = session.resource('ec2', region_name=east)