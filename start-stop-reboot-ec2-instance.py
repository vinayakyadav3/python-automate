import boto3


ec2 = boto3.client('ec2',region_name='ap-south-1') 
#Add your region


instances = ["<instance-id>"] 
# or ["<instance-id-1>","<instance-id-2>",...,"<instance-id-n>"]

#start the instance
ec2.start_instances(InstanceIds=instances)

#stop the instance
ec2.stop_instances(InstanceIds=instances)

#reboot the instance
ec2.reboot_instances(InstanceIds=instances)
