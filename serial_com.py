import serial
import time

ser = serial.Serial(
    port='/dev/ttyUSB0',  # Adjust this to your serial port 
    baudrate=9600,        # Set the baud rate
    timeout=1,             # Set a timeout for read operations
    bytesize=serial.EIGHTBITS,  # Set the number of data bits
    parity=serial.PARITY_NONE,   # Set parity checking
    stopbits=serial.STOPBITS_ONE  # Set the number of stop bits
)

try:
    ser.open()  # Open the serial port  
    print("Serial port opened successfully.")
    
    # Send data periodically every 1 second
    while True:
        try:
            message = "hello world\n"  # Adding newline for better readability
            ser.write(message.encode('utf-8'))  # Encode string to bytes
            print(f"Sent: {message.strip()}")
            time.sleep(1)  # Wait for 1 second
            
        except KeyboardInterrupt:
            print("\nStopping data transmission...")
            break
        except serial.SerialException as e:
            print(f"Error writing to serial port: {e}")
            break
            
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit(1)
    
finally:
    # Clean up and close the serial port
    if ser.is_open:
        ser.close()
        print("Serial port closed.") 
