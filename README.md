####Setup

To setup up using pip simply run

```
pip install -r https://github.com/FlorentijnKnol/mock_workflow
```


####Using process()

```python
from mock_workflow import run_process

def process(msg):
    return msg

run_process(process_fn=process, topic_in=[{"a":1, "b":2}])
```

####Explicitly defining producer / consumer

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

####Using the store
```python
from mock_workflow import store

store.insert('a', 'b')
print(store.get('a'))
#prints 'b'
```