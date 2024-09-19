**sudo apt-get update
sudo apt-get install rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server

For test
pip install pika

producer.py - produce a queue (send 1 message)
consumer.py - consume a queue (get messages from RebbitMQ)

python producer.py
python consumer.py

In case of Exchanges

producer_exch.py
consumer_exch.py
