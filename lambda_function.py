import json
import boto3

sns = boto3.client('sns')

SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:107851813880:S3-Notification-System"

def lambda_handler(event, context):
    if 'Records' not in event:
        print("Event does not contain Records. Not an S3 trigger.")
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid event source')
        }

    for record in event['Records']:
        if record.get('eventSource') != 'aws:s3':
            continue

        bucket = record['s3']['bucket']['name']
        file_name = record['s3']['object']['key']

        message = (
            "New file uploaded to S3.\n"
            f"Bucket Name: {bucket}\n"
            f"File Name: {file_name}"
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="S3 File Upload Notification"
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully')
    }