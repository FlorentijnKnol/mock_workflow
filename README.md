### Setup

To setup up using pip simply run

```
pip install git+https://github.com/FlorentijnKnol/mock_workflow.git
```


### Using process()

```python
from mock_workflow import run_process

def process(msg):
    return msg

#Two example messages
topic_in = [{"a":1, "b":2}, {"a":3, "b":4}]

run_process(process_fn=process, topic_in=topic_in)
```

### Explicitly defining producer / consumer

```python
from mock_workflow import Consumer, Producer, setup_mock_workflow

#Two example messages
topic_in = [{"a":1, "b":2}, {"a":3, "b":4}]
setup_mock_workflow(topic_in)

consumer = Consumer.connect()
producer = Producer.connect()

while True:
    msg = consumer.consume()
    producer.produce(msg)
    consumer.ack(msg)
```

### Using the store
```python
from mock_workflow import store

store.insert('a', 'b')
print(store.get('a'))
#prints 'b'
```

### Using the reader
```python
from mock_workflow import Reader, setup_mock_workflow

#One hundred example messages
topic_in = [{"a": i} for i in range(100)]

setup_mock_workflow(topic_in)

reader = Reader.connect()

#Gets the first 50 messages
reader.batch_get(50, 0)
```