# This code acts as a client to communicate with a server over TCP/IP.
# Importing the 'socket' module provides low-level interface for network communication.
# The 'evaluate_expression' function takes an expression as input, evaluates it by returning the result or an error.
# The 'main' function of the script contains the details the server will connect to.
# The 'main' function establishes TCP  connection with the server using 'socket.socket()' and 'connect()' methods.
# It then sends an introductory message (intro_message) to the server after encoding it into bytes using UTF-8 encoding.
# It also enters into an infinite loop to continuously receive and process messages from the server using 'recv()' method, decoding them from bytes to strings using UTF-8 encoding.
import socket

def evaluate_expression(expression):
    # logic to evaluate the expression and return the result
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error: " + str(e)

def main():
    # Server's host and port details
    host = 'localhost'
    port = 5206

    # Establish TCP connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        # Send introductory message
        intro_message = "EECE7374 INTR 002642073"
        client_socket.sendall(intro_message.encode('utf-8'))

        while True:
            # Receive and process messages
            message = client_socket.recv(1024).decode('utf-8')

            # Tokenize the message
            tokens = message.split()
            if len(tokens) >= 2 and tokens[0] == 'EECE7374':
                message_type = tokens[1]

                if message_type == 'EXPR':  # Expression message
                    expression = ' '.join(tokens[2:])  # Join tokens after EECE7374 EXPR
                    result = evaluate_expression(expression)
                    result_message = "EECE7374 RSLT " + result
                    client_socket.sendall(result_message.encode('utf-8'))

                elif message_type == 'FAIL':  # Failure message
                    print("Server indicated failure. Check your implementation.")
                    break

                elif message_type == 'SUCC':  # Success message
                    secret_flag = tokens[2]
                    print("Received secret flag:", secret_flag)
                    break

                else:
                    print("Unexpected message type:", message_type)
                    break

        # Close connection
        client_socket.close()

if __name__ == "__main__":
    main()

