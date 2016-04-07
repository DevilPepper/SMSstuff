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

#190d85cd36b6a949a8828cc12e3892f5

#CID U8xslalJaqxYb9NtS7NeWAvbmM2UfNOOIVQDsfHB
#CSec mgDB5GnYAp7qjNtWMD1GMFjVAusk0-O_iS3fAa0g

#access AtDBvC9A6iYdXiYrNRdCgp3zBmdHpr
