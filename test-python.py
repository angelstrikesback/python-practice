import json


def get_event_body(type, id):
    return json.dumps({
        "version": "0",
        "id": "46d64c18-6be9-f292-4b3e-67bee9d773c0",
        "detail-type": type,
        "source": "DuckCreek",
        "account": "448855094770",
        "time": "2020-08-21T22:08:15Z",
        "region": "us-east-1",
        "resources": [

        ],
        "detail": {
            "PartyID": id
        }
    })


event = {
    'Records': [
        {
            'messageId': 'b177c577-c661-4a74-9f87-f55b9c5cf3d2',
            'receiptHandle': '',
            'body': get_event_body("LMPartyAdded", "1"),
            'attributes': {
                'ApproximateReceiveCount': '1',
                'SentTimestamp': '1598047695997',
                'SenderId': 'AIDAJXNJGGKNS7OSV23OI',
                'ApproximateFirstReceiveTimestamp': '1598047696085'
            },
            'messageAttributes': {

            },
            'md5OfBody': 'b28f08c26d2b5cabc4325ef223e6db61',
            'eventSource': 'aws: sqs',
            'eventSourceARN': 'arn: aws: sqs: us-east-1: 448855094770: grs-wcclaims-ofac-integration-service-queue-sandbox',
            'awsRegion': 'us-east-1'
        },
        {
            'messageId': 'b177c577-c661-4a74-9f87-f55b9c5cf3d2',
            'receiptHandle': '',
            'body': get_event_body("LMPartyAdded", "2"),
            'attributes': {
                'ApproximateReceiveCount': '1',
                'SentTimestamp': '1598047695997',
                'SenderId': 'AIDAJXNJGGKNS7OSV23OI',
                'ApproximateFirstReceiveTimestamp': '1598047696085'
            },
            'messageAttributes': {

            },
            'md5OfBody': 'b28f08c26d2b5cabc4325ef223e6db61',
            'eventSource': 'aws: sqs',
            'eventSourceARN': 'arn: aws: sqs: us-east-1: 448855094770: grs-wcclaims-ofac-integration-service-queue-sandbox',
            'awsRegion': 'us-east-1'
        },
        {
            'messageId': 'b177c577-c661-4a74-9f87-f55b9c5cf3d2',
            'receiptHandle': '',
            'body': get_event_body("LMPartyUpdated", "3"),
            'attributes': {
                'ApproximateReceiveCount': '1',
                'SentTimestamp': '1598047695997',
                'SenderId': 'AIDAJXNJGGKNS7OSV23OI',
                'ApproximateFirstReceiveTimestamp': '1598047696085'
            },
            'messageAttributes': {

            },
            'md5OfBody': 'b28f08c26d2b5cabc4325ef223e6db61',
            'eventSource': 'aws: sqs',
            'eventSourceARN': 'arn: aws: sqs: us-east-1: 448855094770: grs-wcclaims-ofac-integration-service-queue-sandbox',
            'awsRegion': 'us-east-1'
        },
        {
            'messageId': 'b177c577-c661-4a74-9f87-f55b9c5cf3d2',
            'receiptHandle': '',
            'body': '',
            'attributes': {
                'ApproximateReceiveCount': '1',
                'SentTimestamp': '1598047695997',
                'SenderId': 'AIDAJXNJGGKNS7OSV23OI',
                'ApproximateFirstReceiveTimestamp': '1598047696085'
            },
            'messageAttributes': {

            },
            'md5OfBody': 'b28f08c26d2b5cabc4325ef223e6db61',
            'eventSource': 'aws: sqs',
            'eventSourceARN': 'arn: aws: sqs: us-east-1: 448855094770: grs-wcclaims-ofac-integration-service-queue-sandbox',
            'awsRegion': 'us-east-1'
        },

    ]
}
# print (str(list(map(lambda record: json.loads(record.get("body", "{}")), event.get('Records')))))
print ("Processed list:" + str([{'event-type': body.get('detail-type'), 'event-body': body.get('detail')} for body in [json.loads(message.get('body', '{}')) for message in event.get('Records') if message.get('body')]]))

# print("Messages:" + str(
#     [{'type':json.loads(message.get('body', '{}')).get('detail-type'), 'body': json.loads(message.get('body', '{}')).get('detail')}
#      for message in event.get('Records') if message.get('body')]))
