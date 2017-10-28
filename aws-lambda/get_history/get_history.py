import os
import json
from urllib.parse import parse_qs
from slackclient import SlackClient
import boto3

oauth_token = os.environ['oauth_token']

sc = SlackClient(oauth_token)

def getHistory(channel_id):
    conlist = sc.api_call("conversations.history", channel=channel_id, count=20)
    tmpfile = open('/tmp/tmp.csv', 'w')
    messages = conlist['messages']
    for i in range(len(messages)):
        if 'user' in messages[i]:
            tmpfile.write(messages[i]['user'] + ":::" + messages[i]['text'] + '\n')
    tmpfile.close()

    # S3 Connect
    s3 = boto3.resource('s3',
                        aws_access_key_id=os.environ['aws_access'],
                        aws_secret_access_key=os.environ['aws_secret'])
    s3.Bucket('lkhphuc-summ').upload_file('/tmp/tmp.csv', 'request1.csv')

def lambda_handler(event, context):
    params = json.loads(event)

    channel_id = params['channel_id'][0]

    getHistory(channel_id)