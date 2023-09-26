import boto3

aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name='YOUR_REGION_NAME'
)

ec2 = session.resource('ec2')

instance = ec2.create_instances(
    ImageId='AMI_ID',
    InstanceType='INSTANCE_TYPE',
    KeyName='KEY_PAIR_NAME',
    SecurityGroups=['SECURITY_GROUP_NAME'],
    MinCount=1,
    MaxCount=1
)[0]

print(instance.id)
