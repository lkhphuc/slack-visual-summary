import os
import json
from urllib.parse import parse_qs
import boto3

# Token use to verify the request really came from our Slash command
expected_token = os.environ['expected_token']

# Function to create a respond for the Slash command, it's must contain a statusCode, body and header
def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

# The actual function that handle the HTTP request
def lambda_handler(event, context):
    params = parse_qs(event['body'])
    token = params['token'][0]
    if token != expected_token:
        return respond(Exception('Invalid request token'))

    user = params['user_name'][0]
    channel = params['channel_name'][0]
    # text = params['text'][0].split(' ')
    # try:
    #     minute = int(text[1])
    #     output = user + ", we are preparing a summary for channel " + channel
    #     sns_publish(json.dumps(params))
    #     return respond(None, output)
    # except (IndexError, ValueError):
    #     return respond(None, "Sorry, please use the form \"/summarize last ... min\" ")
    output = user + ", a summary is being prepared for channel " + channel
    sns_publish(json.dumps(params))
    return respond(None, output)

# Function to publish message to SNS event, this event will inturn trigger our second lambda function
def sns_publish(message):
    client = boto3.client(
                'sns', 
                aws_access_key_id=os.environ['aws_access'],
                aws_secret_access_key=os.environ['aws_secret'],
                region_name='ap-southeast-1'
            )
    client.publish(TopicArn='arn:aws:sns:ap-southeast-1:xxxxxxxxx:summarizer', Message=message)