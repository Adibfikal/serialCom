import serial_com

ser = serial_com.Serial(
    port='/dev/ttyUSB0',  # Adjust this to your serial port 
    baudrate=9600,        # Set the baud rate
    timeout=1,             # Set a timeout for read operations
    bytesize=serial_com.EIGHTBITS,  # Set the number of data bits
    parity=serial_com.PARITY_NONE,   # Set parity checking
    stopbits=serial_com.STOPBITS_ONE  # Set the number of stop bits
)
try:
    ser.open()  # Open the serial port  
    print("Serial port opened successfully.")
except serial_com.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit(1) 
