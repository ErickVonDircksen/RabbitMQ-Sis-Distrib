
import pika

def pitchInput(connection):
    # Connect to RabbitMQ server
    
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue="elevator")

    channel.exchange_declare(exchange='pitchInput', exchange_type='topic')

    channel.basic_publish(exchange='pitchInput', routing_key='up.down', body='action')

    print(" [x] Sent 'Hello, RabbitMQ!'")

    # Close the connection
    connection.close()





def rollInput(connection):
    # Connect to RabbitMQ server
    
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue="aileron")

    channel.exchange_declare(exchange='rollInput', exchange_type='topic')

    channel.basic_publish(exchange='rollInput', routing_key="roll", body='action')

    print(" [x] Sent 'Hello, RabbitMQ!'")

    # Close the connection
    connection.close()
    




def yawInput(connection):
    # Connect to RabbitMQ server
    
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue="rudder")

    channel.exchange_declare(exchange='yawInput', exchange_type='topic')

    channel.basic_publish(exchange='yawInput', routing_key='yaw', body='action')

    print(" [x] Sent 'Hello, RabbitMQ!'")

    # Close the connection
    connection.close()
    