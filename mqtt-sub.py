import paho.mqtt.client as mqtt
import time

cliente = mqtt.Client(client_id='devpy')

cliente.connect('localhost', port=1883)
cliente.subscribe('casa/sala/lampada/1')

print('Subscriber connected')

def on_message(cliente, userdata, message):
    print(message.payload.decode('uft.8'))
    
cliente.on_message = on_message_callback 

cliente.loop_forever()
# cliente.loop_star()
# time.sleep(100)
# cliente.loop_stop()

