import os
import boto3

region = os.environ['REGION']

def lambda_handler(event, context):
    
    # EventBridgeからパラメータを渡し、変数"action"に格納する
    action = event['Action']
    client = boto3.client('ec2', region_name=region)
    
    # タグ「LambdaStartStop」が「enable」であるインスタンス情報を取得
    response = client.describe_instances(Filters=[{'Name': 'tag:LambdaStartStop', "Values": ['enable']}])
    
    # "Reservations" → "Instance" → "InstanceId"の順番で取り出し、変数target_instance_idsに格納する
    target_instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
             target_instance_ids.append(instance['InstanceId'])
    
    # 格納されたインスタンスIDを出力
    print(target_instance_ids)
    
    # EventBridgeに渡されたパラメータ"start"/"stop"により処理を分岐させる
    if not target_instance_ids:
        print('There are no instances subject to automatic start / stop.')
    else:
        if action == 'start':
            client.start_instances(InstanceIds=target_instance_ids)
            print('started instances.')
        elif action == 'stop':
            client.stop_instances(InstanceIds=target_instance_ids)
            print('stopped instances.')
        else:
            print('Invalid action.')