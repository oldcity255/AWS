import boto3, json
session = boto3.Session(profile_name='development')
#global variables for region_name
east = 'us-east-1'
west = 'us-west-2'
# declaring ec2East variable to use ec2 session.client
ec2East = session.client('ec2', region_name = east)
ec2West = session.client('ec2', region_name = west)

ec2IDs = []

runningInstances = ec2East.describe_instances(
        Filters=[
            {
                'Name': 'tag:TechnicalTeam',
                'Values': [
                    'running',
                ]
            },
        ],
    )
a=runningInstances['Reservations']
for i in a:
    b=i['Instances']
    for j in b:
        ec2IDs.append(j['InstanceId'])

print('List of EC2 IDs: ',ec2IDs)

for instance in ec2IDs:
    response = ec2East.stop_instances(
        InstanceIds=[
            instance,
        ],
    )

# def helloWorld():
#     ec2IDs = []
#     ec2AMIs = []
#     hello = ec2East.describe_instances()
#     a = hello['Reservations']

# import boto3, json
# session = boto3.Session(profile_name='development')
# east = 'us-east-1'
# west = 'us-west-2'
# ec2East = session.client('ec2', region_name = east)

# def getEC2withTags():
#     ec2IDs = []
#     response = ec2East.describe_instances(
#         Filters=[
#             {
#                 'Name': 'tag:TechnicalTeam',
#                 'Values': [
#                     'DevOps',
#                 ]
#             },
#         ],
#     )
#     print(response)
# getEC2withTags()