import pika
import json
import sqlite3

connection = sqlite3.connect("messages.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   content TEXT)''')
connection.commit()

def callback(ch, method, properties, body):
    message = body.decode()
    cursor.execute("INSERT INTO messages (content) VALUES (?)", (message,))
    connection.commit()
    print("Message saved to database:", message)

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection_rabbit = pika.BlockingConnection(parameters)
channel = connection_rabbit.channel()

channel.queue_declare(queue='fila')

channel.basic_consume(
    queue='fila',
    on_message_callback=callback,
    auto_ack=True
)

print('Waiting for messages... To exit press CTRL+C')
channel.start_consuming()