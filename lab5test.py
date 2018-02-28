
# Author: zixuan zhang
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


print('start testing now! ')
# Main program loop.
while True:
    #blink for 5 times with interval of 500ms
    for i in range(5):
        #turn LED one
        print('turn LED On')
        time.sleep(0.5)
        #turn LED off
        print('LED off')
        time.sleep(0.5)
    for i in range(50):
        #read light sensor
        print('read light sensor')
        time.sleep(0.1)
    for i in range(4):
        #turn LED one
        print('turn LED On')
        time.sleep(0.2)
        #turn LED off
        print('LED off')
        time.sleep(0.2)
    for i in range(50):
        #read light sensor
        print('read sound sensor')
        time.sleep(0.1)
    for i in range(4):
        #turn LED one
        print('turn LED On')
        time.sleep(0.2)
        #turn LED off
        print('LED off')
        time.sleep(0.2)
    
    
        
    # Read all the ADC channel values in a list.
    #values = [0]*8
    #for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
    #    values[i] = mcp.read_adc(i)
    # Print the ADC values.
    #print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    # Pause for half a second.
    #time.sleep(0.5)
