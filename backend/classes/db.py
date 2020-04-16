import boto3

import json

def WriteToDatabase(table: str, data: dict) -> None:

    print(f"Writing to table: {str}")
    print(dict)

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)

    table.put_item(
        Item = data
    )

def GetAllInTable(table: str) -> dict:

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)

    data = table.scan()

    return data['Items']