import boto3

aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name='YOUR_REGION_NAME'
)

ec2 = session.resource('ec2')

instance_id = 'INSTANCE_ID'

instance = ec2.Instance(instance_id)
response = instance.stop()

print(response)
