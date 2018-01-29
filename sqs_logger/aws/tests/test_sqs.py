import os

import pytest

from sqs_logger.aws.exceptions import QueueError
from sqs_logger.aws.sqs import SQSManager


class TestSQSManager:

    @pytest.fixture
    def sqs_manager(self):
        return SQSManager()

    def test_send_message_returns_queue_error(self, sqs_manager):
        with pytest.raises(QueueError) as e:
            sqs_manager.put(None)

        assert e.value.message == 'Message cannot be empty'

    def test_send_message_returns_success(self, sqs_manager):
        assert sqs_manager.put('Test')

    def test_send_message_missing_queue_name_returns_queue_error(self):
        with pytest.raises(QueueError) as e:
            sqs_manager = SQSManager(queue_name='')
            sqs_manager.put('Test')

        assert e.value.message == 'Queue name cannot be empty'

    def test_send_message_missing_credentials_returns_queue_error(self):
        os.environ['AWS_ACCESS_KEY_ID'] = ''
        os.environ['AWS_SECRET_ACCESS_KEY'] = ''

        with pytest.raises(QueueError) as e:
            sqs_manager = SQSManager()
            sqs_manager.put('Test')

        assert e.value.message == (
            'The security token included in the request is invalid.'
        )

    def test_send_message_with_big_payload_returns_queue_error(
        self,
        sqs_manager
    ):
        payload = ''
        for i in range(27000):
            payload += 'ABCABCABC1'

        with pytest.raises(QueueError) as e:
            sqs_manager.put(payload)

        assert e.value.message == 'Message size not allowed'
