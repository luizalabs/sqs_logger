import os

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

QUEUE_NAME = os.getenv('QUEUE_NAME', 'sqs-logger')
REGION_NAME = os.getenv('REGION_NAME', 'us-east-1')
