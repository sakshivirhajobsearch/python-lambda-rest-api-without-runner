import json


def lambda_handler(event, context):
    path = event.get('rawPath')
    method = event.get('requestContext', {}).get('http', {}).get('method')

    if path == "/hello" and method == "GET":
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'message': 'Hello World from Lambda!'})
        }

    elif path == "/data" and method == "POST":
        body = json.loads(event.get('body', '{}'))
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'received_data': body})
        }

    else:
        return {
            'statusCode': 404,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'Not Found'})
        }
