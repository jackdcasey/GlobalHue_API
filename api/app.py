import boto3
from boto3.dynamodb.conditions import Key

from flask import Flask
app = Flask(__name__)

DB_TABLE_CURRENT = 'GlobalHue_Current'
DB_TABLE_HISTORY = 'GlobalHue_History'

@app.route("/")
def hello():
    return {"Status": "OK"}

@app.route("/cities/")
def cities():
    data = GetFullTable(DB_TABLE_CURRENT)

    return {"Items": data}

@app.route("/cities/<cityname>")
def specific_city(cityname: str):
    cityname = cityname.lower().capitalize()

    data = ScanTable(
        DB_TABLE_HISTORY,
        'city',
        cityname,
        ['color', 'success', 'capturetime']
    )

    return {"Items": data}



def GetFullTable(table: str) -> dict:

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)

    response = table.scan()

    return response['Items']



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