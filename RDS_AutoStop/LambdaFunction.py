import boto3
import os

#環境変数 
client = boto3.client('rds')
TAGKEY = os.environ['TAGKEY']
TAGVALUE = os.environ['TAGVALUE']

def lambda_handler(event, context):
    #クラスターを停止
    clusters = client.describe_db_clusters()
    for cluster in clusters['DBClusters']:
        if cluster['Status'] == "available":
            tags = client.list_tags_for_resource(ResourceName=cluster['DBClusterArn'])
            for tag in tags['TagList']:
                if tag['Key'] == TAGKEY and tag['Value'] == TAGVALUE:
                    client.stop_db_cluster(DBClusterIdentifier=cluster['DBClusterIdentifier'])

    #インスタンスを停止
    instances = client.describe_db_instances()
    for instance in instances['DBInstances']:
        if instance['DBInstanceStatus'] == "available":
            tags = client.list_tags_for_resource(ResourceName=instance['DBInstanceArn'])
            for tag in tags['TagList']:
                if tag['Key'] == TAGKEY and tag['Value'] == TAGVALUE:
                    client.stop_db_instance(DBInstanceIdentifier=instance['DBInstanceIdentifier'])