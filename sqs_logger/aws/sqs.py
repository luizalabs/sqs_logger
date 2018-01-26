import logging
import os

from boto import sqs
from boto.sqs.message import RawMessage as SQSMessage

from .exceptions import QueueError

logger = logging.getLogger(__name__)


class SQSManager:

    def __init__(
        self,
        queue_name=os.getenv('QUEUE_NAME'),
        region_name=os.getenv('REGION_NAME'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    ):
        self._queue = None
        self.queue_name = queue_name
        self.client = sqs.connect_to_region(
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    @property
    def queue(self):
        if not self._queue:
            try:
                self._queue = self.client.create_queue(self.queue_name)
            except Exception as e:
                logger.error(
                    'Fail to get SQS queue:{}'.format(self.queue_name)
                )
                raise QueueError(e.message)

        return self._queue

    def put(self, message):
        if not message:
            raise QueueError('Message cannot be empty')

        logger.debug('Sending message {} to queue:{}'.format(
            message,
            self.queue_name
        ))

        sqs_message = SQSMessage()
        sqs_message.set_body(message)

        return self.queue.write(sqs_message)
