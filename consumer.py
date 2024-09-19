import pika

# RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# subscribe
channel.queue_declare(queue='hello')

# Callback for messages
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# RabbitMQ, what func is call in case of reciving a message
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
