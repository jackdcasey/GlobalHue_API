from flask import Flask
app = Flask(__name__)

import json, boto3, os

from boto3.dynamodb.conditions import Key




@app.route("/")
def hello():
    return "Hello Folks!"


# def lambda_handler(event, context):

#     data = ScanTable(
#         DB_TABLE_HISTORY,
#         'city',
#         'Vancouver',
#         ['city', 'color', 'success', 'capturetime']
#     )

#     return {
#         'statusCode': 200,
#         'body': json.dumps(data)
#     }


def ScanTable(table: str, filter_key: str, filter_value: str, attributes: list) -> dict:

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)

    filtering_exp = Key(filter_key).eq(filter_value)

    response = table.scan(
        FilterExpression=filtering_exp,
        ProjectionExpression=', '.join(attributes)
        )

    items = response['Items']

    while True:

        if response.get('LastEvaluatedKey'):
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items += response['Items']
        else:
            break

    return items