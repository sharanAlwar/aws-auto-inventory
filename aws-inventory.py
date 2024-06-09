import boto3
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("")
db = client[""]

# Boto3 clients
session = boto3.Session()
ec2_client = session.client('ec2')
rds_client = session.client('rds')
s3_client = session.client('s3')
elb_client = session.client('elbv2')
eks_client = session.client('eks')
lambda_client = session.client('lambda')
workspaces_client = session.client('workspaces')
ecr_client = session.client('ecr')
beanstalk_client = session.client('elasticbeanstalk')
route53_client = session.client('route53')
apigw_client = session.client('apigateway')
acm_client = session.client('acm')
iam_client = session.client('iam')
dms_client = session.client('dms')
cloudwatch_client = session.client('cloudwatch')
ecs_client = session.client('ecs')
kms_client = session.client('kms')
secretsmanager_client = session.client('secretsmanager')

def upload_to_mongodb(collection_name, documents):
    collection = db[collection_name]
    if documents:
        collection.insert_many(documents)

def get_aws_workspace():
    response = workspaces_client.describe_workspaces()
    return [{"WorkspaceId": ws['WorkspaceId'], "DirectoryId": ws['DirectoryId'], "State": ws['State'], "UserName": ws['UserName']} for ws in response['Workspaces']]

def get_ec2_instances():
    response = ec2_client.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({"InstanceId": instance['InstanceId'], "InstanceType": instance['InstanceType'], "State": instance['State']['Name'], "LaunchTime": instance['LaunchTime']})
    return instances

def get_ebs_volumes():
    response = ec2_client.describe_volumes()
    return [{"VolumeId": vol['VolumeId'], "Size": vol['Size'], "State": vol['State'], "CreateTime": vol['CreateTime']} for vol in response['Volumes']]

def get_elastic_ips():
    response = ec2_client.describe_addresses()
    return [{"PublicIp": eip['PublicIp'], "AllocationId": eip['AllocationId'], "Domain": eip['Domain'], "InstanceId": eip.get('InstanceId', 'N/A')} for eip in response['Addresses']]

def get_security_groups():
    response = ec2_client.describe_security_groups()
    return [{"GroupId": sg['GroupId'], "GroupName": sg['GroupName'], "Description": sg['Description'], "VpcId": sg.get('VpcId', 'N/A')} for sg in response['SecurityGroups']]

def get_eks_clusters():
    response = eks_client.list_clusters()
    clusters = []
    for name in response['clusters']:
        cluster_info = eks_client.describe_cluster(name=name)['cluster']
        clusters.append({"ClusterName": name, "Status": cluster_info['status'], "RoleArn": cluster_info['roleArn'], "Version": cluster_info['version']})
    return clusters

def get_lambdas():
    response = lambda_client.list_functions()
    return [{"FunctionName": fn['FunctionName'], "Runtime": fn['Runtime'], "Role": fn['Role'], "Handler": fn['Handler']} for fn in response['Functions']]

def get_rds_instances():
    response = rds_client.describe_db_instances()
    return [{"DBInstanceIdentifier": db['DBInstanceIdentifier'], "DBInstanceClass": db['DBInstanceClass'], "Engine": db['Engine'], "DBInstanceStatus": db['DBInstanceStatus']} for db in response['DBInstances']]

def get_rds_subnet_groups():
    response = rds_client.describe_db_subnet_groups()
    return [{"DBSubnetGroupName": sg['DBSubnetGroupName'], "DBSubnetGroupDescription": sg['DBSubnetGroupDescription'], "VpcId": sg['VpcId'], "SubnetGroupStatus": sg['SubnetGroupStatus']} for sg in response['DBSubnetGroups']]

def get_rds_reserved_instances():
    response = rds_client.describe_reserved_db_instances()
    return [{"ReservedDBInstanceId": ri['ReservedDBInstanceId'], "DBInstanceClass": ri['DBInstanceClass'], "Duration": ri['Duration'], "State": ri['State']} for ri in response['ReservedDBInstances']]

def get_vpcs():
    response = ec2_client.describe_vpcs()
    return [{"VpcId": vpc['VpcId'], "State": vpc['State'], "CidrBlock": vpc['CidrBlock'], "IsDefault": vpc['IsDefault']} for vpc in response['Vpcs']]

def get_subnets():
    response = ec2_client.describe_subnets()
    return [{"SubnetId": subnet['SubnetId'], "VpcId": subnet['VpcId'], "CidrBlock": subnet['CidrBlock'], "AvailabilityZone": subnet['AvailabilityZone']} for subnet in response['Subnets']]

def get_s3_buckets():
    response = s3_client.list_buckets()
    return [{"Name": bucket['Name'], "CreationDate": bucket['CreationDate']} for bucket in response['Buckets']]

def get_load_balancers():
    response = elb_client.describe_load_balancers()
    return [{"LoadBalancerArn": lb['LoadBalancerArn'], "DNSName": lb['DNSName'], "Scheme": lb['Scheme'], "VpcId": lb['VpcId']} for lb in response['LoadBalancers']]

def get_ecr_repositories():
    response = ecr_client.describe_repositories()
    return [{"RepositoryName": repo['repositoryName'], "RepositoryArn": repo['repositoryArn'], "CreatedAt": repo['createdAt'], "RegistryId": repo['registryId']} for repo in response['repositories']]

def get_beanstalk_applications():
    response = beanstalk_client.describe_applications()
    return [{"ApplicationName": app['ApplicationName'], "Description": app.get('Description', 'N/A'), "DateCreated": app['DateCreated'], "DateUpdated": app['DateUpdated']} for app in response['Applications']]

def get_route53_hosted_zones():
    response = route53_client.list_hosted_zones()
    return [{"Id": zone['Id'], "Name": zone['Name'], "CallerReference": zone['CallerReference'], "ResourceRecordSetCount": zone['ResourceRecordSetCount']} for zone in response['HostedZones']]

def get_api_gateways():
    response = apigw_client.get_rest_apis()
    return [{"Id": api['id'], "Name": api['name'], "Description": api.get('description', 'N/A'), "CreatedDate": api['createdDate']} for api in response['items']]

def get_certificates():
    response = acm_client.list_certificates()
    return [{"CertificateArn": cert['CertificateArn'], "DomainName": cert['DomainName'], "Status": cert['Status'], "Type": cert['Type']} for cert in response['CertificateSummaryList']]

def get_iam_users():
    response = iam_client.list_users()
    return [{"UserName": user['UserName'], "UserId": user['UserId'], "Arn": user['Arn'], "CreateDate": user['CreateDate']} for user in response['Users']]

def get_iam_groups():
    response = iam_client.list_groups()
    return [{"GroupName": group['GroupName'], "GroupId": group['GroupId'], "Arn": group['Arn'], "CreateDate": group['CreateDate']} for group in response['Groups']]

def get_nat_gateways():
    response = ec2_client.describe_nat_gateways()
    return [{"NatGatewayId": nat['NatGatewayId'], "VpcId": nat['VpcId'], "SubnetId": nat['SubnetId'], "State": nat['State']} for nat in response['NatGateways']]

def get_s2s_connections():
    response = ec2_client.describe_vpn_connections()
    return [{"VpnConnectionId": conn['VpnConnectionId'], "State": conn['State'], "CustomerGatewayId": conn['CustomerGatewayId'], "VpnGatewayId": conn['VpnGatewayId']} for conn in response['VpnConnections']]

def get_dms_tasks():
    response = dms_client.describe_replication_tasks()
    return [{"ReplicationTaskIdentifier": task['ReplicationTaskIdentifier'], "Status": task['Status'], "MigrationType": task['MigrationType'], "ReplicationInstanceArn": task['ReplicationInstanceArn']} for task in response['ReplicationTasks']]

def get_cloudwatch_alarms():
    response = cloudwatch_client.describe_alarms()
    return [{"AlarmName": alarm['AlarmName'], "StateValue": alarm['StateValue'], "MetricName": alarm['MetricName'], "Namespace": alarm['Namespace']} for alarm in response['MetricAlarms']]

def get_ecs_clusters():
    response = ecs_client.list_clusters()
    clusters = []
    for arn in response['clusterArns']:
        cluster_info = ecs_client.describe_clusters(clusters=[arn])['clusters'][0]
        clusters.append({"ClusterArn": cluster_info['clusterArn'], "ClusterName": cluster_info['clusterName'], "Status": cluster_info['status'], "RunningTasksCount": cluster_info['runningTasksCount'], "PendingTasksCount": cluster_info['pendingTasksCount']})
    return clusters

def get_kms_keys():
    response = kms_client.list_keys()
    keys = []
    for key in response['Keys']:
        key_info = kms_client.describe_key(KeyId=key['KeyId'])['KeyMetadata']
        keys.append({"KeyId": key_info['KeyId'], "Arn": key_info['Arn'], "Description": key_info.get('Description', 'N/A'), "Enabled": key_info['Enabled']})
    return keys

def get_secrets():
    response = secretsmanager_client.list_secrets()
    return [{"Name": secret['Name'], "ARN": secret['ARN'], "Description": secret.get('Description', 'N/A'), "SecretType": secret['SecretType']} for secret in response['SecretList']]

# Collecting and uploading data
upload_to_mongodb('AWS_Workspaces', get_aws_workspace())
upload_to_mongodb('EC2_Instances', get_ec2_instances())
upload_to_mongodb('Elastic_Blockstore', get_ebs_volumes())
upload_to_mongodb('Elastic_IPs', get_elastic_ips())
upload_to_mongodb('Security_Groups', get_security_groups())
upload_to_mongodb('EKS_Clusters', get_eks_clusters())
upload_to_mongodb('Lambda_Functions', get_lambdas())
upload_to_mongodb('RDS_Instances', get_rds_instances())
upload_to_mongodb('RDS_Subnet_Groups', get_rds_subnet_groups())
upload_to_mongodb('RDS_Reserved_Instances', get_rds_reserved_instances())
upload_to_mongodb('VPCs', get_vpcs())
upload_to_mongodb('Subnets', get_subnets())
upload_to_mongodb('S3_Buckets', get_s3_buckets())
upload_to_mongodb('Load_Balancers', get_load_balancers())
upload_to_mongodb('ECR_Repositories', get_ecr_repositories())
upload_to_mongodb('Beanstalk_Applications', get_beanstalk_applications())
upload_to_mongodb('Route53_Hosted_Zones', get_route53_hosted_zones())
upload_to_mongodb('API_Gateways', get_api_gateways())
upload_to_mongodb('Certificates', get_certificates())
upload_to_mongodb('IAM_Users', get_iam_users())
upload_to_mongodb('IAM_Groups', get_iam_groups())
upload_to_mongodb('NAT_Gateways', get_nat_gateways())
upload_to_mongodb('S2S_Connections', get_s2s_connections())
upload_to_mongodb('DMS_Tasks', get_dms_tasks())
upload_to_mongodb('CloudWatch_Alarms', get_cloudwatch_alarms())
upload_to_mongodb('ECS_Clusters', get_ecs_clusters())
upload_to_mongodb('KMS_Keys', get_kms_keys())
upload_to_mongodb('Secrets', get_secrets())
