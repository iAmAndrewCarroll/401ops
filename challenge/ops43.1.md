
### Part 3: Create a Port Scanner

```markdown
# Ops Challenge: Create a Port Scanner

## Using Python's Socket Module

```python
#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5  # Set a timeout of 5 seconds
sockmod.settimeout(timeout)

hostip = input("Enter the host IP: ")  # Collect a host IP from the user
portno = int(input("Enter the port number: "))  # Collect a port number from the user, then convert it to an integer

def portScanner(portno):
    try:
        result = sockmod.connect_ex((hostip, portno))
        if result == 0:
            print("Port open")
        else:
            print("Port closed")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sockmod.close()

portScanner(portno)
