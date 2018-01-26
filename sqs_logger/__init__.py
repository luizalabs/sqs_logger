import logging
import multiprocessing
import sys
import threading
import traceback

from .aws.sqs import SQSManager

logger = logging.getLogger(__name__)


class SQSLoggerHandler(logging.Handler):
    def __init__(
        self,
        queue_name,
        region_name
    ):
        logging.Handler.__init__(self)

        self.sqs_manager = SQSManager(
            queue_name=queue_name,
            region_name=region_name
        )

        self.queue = multiprocessing.Queue(-1)

        t = threading.Thread(target=self.receive)
        t.daemon = True
        t.start()

    def receive(self):
        while True:
            try:
                record = self.queue.get()

                logger.debug('Message sent {} to the queue'.format(record))
                self.sqs_manager.put(record)
            except (KeyboardInterrupt, SystemExit):
                raise
            except EOFError:
                break
            except Exception:
                traceback.print_exc(file=sys.stderr)

    def send(self, record):
        self.queue.put_nowait(record)

    def emit(self, record):
        try:
            s = self._format_record(record)
            self.send(s.msg)
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception:
            self.handleError(record)

    def close(self):
        logging.Handler.close(self)

    def _format_record(self, record):
        if record.args:
            record.msg = record.msg % record.args
            record.args = None
        if record.exc_info:
            record.exc_info = None

        return record
