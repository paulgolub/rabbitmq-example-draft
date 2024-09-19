channel.exchange_declare(exchange='logs', exchange_type='fanout')

# declare temp queue
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# connect queue to exchange
channel.queue_bind(exchange='logs', queue=queue_name)

# get messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
