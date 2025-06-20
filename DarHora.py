import datetime

def lambda_handler(event, context):
    now_utc = datetime.datetime.utcnow().isoformat() + 'Z'
    return {
        'statusCode': 200,
        'body': {'timestamp_utc': now_utc}
    }
