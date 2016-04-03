import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('states')

# Print out some data about the table.
print(table.item_count)

table.put_item(
   Item={
        'phone': '+13476528022',
        'history': ''
    }
)
