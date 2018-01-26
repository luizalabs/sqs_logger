import pytest

from sqs_logger.aws.exceptions import QueueError
from sqs_logger.aws.sqs import SQSManager


@pytest.mark.integration
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
