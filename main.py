import random
import time
import threading
import pika
from producers import pitchInput, yawInput, rollInput
from consumers import elevator, rudder, aileron


def main():# Start the simulation
    
    a="0"
    b="0"
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',heartbeat=5))
    
    elevatorTread = threading.Thread(target=elevator, args=(b,a))     #consumer e producer recebem mesma coisa no type
    rudderTread = threading.Thread(target=rudder, args=(b,a))
    AileronTread = threading.Thread(target=aileron, args=(b,a))
   
    

    elevatorTread.start()
    rudderTread.start()
    AileronTread.start()
    
    
    while True: # simulate inputs from all 3 axisc
        time.sleep(4)
        pitchInput(connection) 

        time.sleep(4)
        yawInput(connection)

        time.sleep(4)
        rollInput(connection)

        
    
main()