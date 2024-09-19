channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Send to exchange, which routing it to all queues
channel.basic_publish(exchange='logs', routing_key='', body='Broadcast message')
