import boto3, json

session = boto3.Session(profile_name='development')

east = 'us-east-1'
ec2East = session.client('ec2', region_name = east)

response = ec2East.describe_security_groups(
    Filters=[ { 'Name': 'ip-permission.cidr', 'Values': [ '0.0.0.0/0' ] } ] )
sgs = response['SecurityGroups']
sgwithopenport = []
for i in sgs:
    sgwithopenport.append(i['GroupId'])
print(sgwithopenport)

for i in sgwithopenport:
    ports = [80, 22, 443]
    for j in ports:
        response = ec2East.revoke_security_group_ingress(
            CidrIp = '0.0.0.0/0',
            FromPort = j,
            GroupId = i,
            IpProtocol = 'TCP',
            ToPort = j,
        )
