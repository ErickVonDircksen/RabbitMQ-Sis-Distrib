import pika
from pika.exchange_type import ExchangeType

def on_message_received1(ch, method, properties, body):
    print(f'Fly By Wire Computer - received new message: {body} and send it to Elevator\n')

def on_message_received2(ch, method, properties, body):
    print(f'Fly By Wire Computer - received new message: {body}and send it to Rudder\n')

def on_message_received3(ch, method, properties, body):
    print(f'Fly By Wire Computer - received new message: {body}and send it to Aileron\n')


def elevator(b,a): # consumes upORdown inputs
    
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',heartbeat=5))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic1', exchange_type=ExchangeType.topic)

    queue = channel.queue_declare(queue='', exclusive=True)

    channel.queue_bind(exchange='topic1', queue=queue.method.queue, 
                       routing_key='up')
    
    channel.basic_consume(queue=queue.method.queue, auto_ack=True,
        on_message_callback=on_message_received1)

    print('Elevator Starting Consuming')

    channel.start_consuming()

def rudder(b,a): # consumes upORdown inputs
    
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',heartbeat=5))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic1', exchange_type=ExchangeType.topic)

    queue = channel.queue_declare(queue='', exclusive=True)

    channel.queue_bind(exchange='topic1', queue=queue.method.queue,
                        routing_key='#.yaw.#')

    channel.basic_consume(queue=queue.method.queue, auto_ack=True,
        on_message_callback=on_message_received2)

    print('Rudder Starting Consuming')

    channel.start_consuming()

def aileron(b,a): # consumes upORdown inputs
    
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',heartbeat=5))
    channel = connection.channel()
    
    channel.exchange_declare(exchange='topic1', exchange_type=ExchangeType.topic)

    queue = channel.queue_declare(queue='', exclusive=True)

    channel.queue_bind(exchange='topic1', queue=queue.method.queue, 
                       routing_key='#.bank.#')

    channel.basic_consume(queue=queue.method.queue, auto_ack=True,
        on_message_callback=on_message_received3)

    print('Aileron Starting Consuming')

    channel.start_consuming()