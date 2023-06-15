import boto3
import json

def get_data():
    s3 = boto3.client('s3')
    data = []
    keys = []

    # We have to identify the Contents dict key during the S3 call. 
    # Won't work otherwise if not mentioned. 
    objects = s3.list_objects_v2(Bucket='random-users-data-410743714069', MaxKeys=5)['Contents']
    
    for k in objects:
        obj = s3.get_object(
            Bucket = 'random-users-data-410743714069',
            Key = k['Key']
            )
        data += json.loads(obj['Body'].read())
         
    print(len(data))
    return data

def handler(event, context):
    # Call the "get_data" function and return appropriately formatted results.

    # print(objKeys)
    return {'isBase64Encoded': False,'statusCode': 200,'body': json.dumps(get_data()), 'headers': {"Access-Control-Allow-Origin": "*"}}