import time
import warnings

class Consumer:
    def __init__(self):
        self.i = 0
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called', exc_value, exc_traceback)

    def connect(topic=None):
        return Consumer()

    def consume(self):
        try:
            TOPIC_IN
        except NameError:
            raise ValueError("TOPIC_IN not set. Please run mock_workflow.setup_mock_workflow.")

        try:
            out_msg = Message(payload=TOPIC_IN[self.i])
            self.i += 1
            return out_msg
        except IndexError:
            warnings.warn("No messages left in topic_in. Going to sleep")
            while True:
                time.sleep(60)

    def ack(self, msg):
        pass


class Producer:
    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called', exc_value, exc_traceback)

    def connect(topic=None):
        return Producer()

    def produce(self, msg):
        assert type(msg) == Message
        print(msg.payload)
        return None


class Message:
    def __init__(self, payload):
        self.payload = payload

class Store:
    def __init__(self):
        self.s = {}

    def get(self, k):
        return self.s.get(k, None)

    def insert(self, k, v):
        self.s[k] = v

store = Store()

class Reader:
    def __init__(self):
        pass

    def connect(timeout=None, topic=None):
        return Reader()

    def batch_get(self, batch_size, offset):
        multiplier = 1
        add = 0
        if batch_size < 0:
            multiplier = -1
            add = 1
        batch = [Message(TOPIC_IN[(i+add)*multiplier]) for i in range(offset, offset+(batch_size*multiplier))]
        if len(batch) < batch_size:
            warnings.warn("Couldn't fill entire batch")

        return batch


def setup_mock_workflow(topic_in):
    global TOPIC_IN
    TOPIC_IN = topic_in

def run_process(process_fn, topic_in):
    setup_mock_workflow(topic_in)

    consumer = Consumer.connect()
    producer= Producer.connect()

    while True:
        msg_in = consumer.consume()
        msg_out = process_fn(msg_in)
        producer.produce(msg_out)
        consumer.ack(msg_in)