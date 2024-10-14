# TCP Client for Server Communication

### Overview
This Python script functions as a TCP/IP client to communicate with a server. It establishes a connection, sends an introductory message, and processes expressions sent by the server. The client evaluates mathematical expressions and responds with results, while also handling success or failure messages from the server.

### Key Features
1. **TCP/IP Communication:** The script uses the `socket` module to establish and maintain communication with a server over TCP.
2. **Expression Evaluation:** It receives mathematical expressions from the server, evaluates them using Python's `eval()` function, and returns the result.
3. **Custom Protocol:** The communication follows a specific message format (`EECE7374` protocol) for sending and receiving commands, expressions, and results.

### Components

1. **`evaluate_expression(expression):`**
   - Evaluates a mathematical expression received from the server.
   - Returns the result as a string or an error message in case of an exception.

2. **`main()`**
   - Establishes a TCP connection to a server using the provided host (`localhost`) and port (`5206`).
   - Sends an introductory message (`EECE7374 INTR 002642073`) to initiate the communication.
   - Continuously listens for messages from the server, processes the message, and takes appropriate actions:
     - **EXPR:** Evaluates expressions sent by the server and returns results.
     - **FAIL:** Handles failure messages from the server, indicating an issue.
     - **SUCC:** Indicates successful communication and extracts a secret flag from the message.

3. **Server Connection:**
   - The client connects to a server at the `localhost` address on port `5206`.
   - Communication uses UTF-8 encoding for sending and receiving messages.

### How to Use
1. **Run the Script:**
   - The script initiates a TCP connection to the server and sends an introductory message.
   - The client enters a loop, waiting for messages from the server. Depending on the message type, it evaluates mathematical expressions or processes success/failure messages.

2. **Message Handling:**
   - The client expects messages starting with the prefix `EECE7374`, followed by a message type:
     - **EXPR:** Followed by a mathematical expression, which is evaluated, and the result is sent back to the server.
     - **FAIL:** Signals an issue, prompting the client to terminate.
     - **SUCC:** Signals success and delivers a secret flag.

3. **Closing the Connection:**
   - The connection is closed after the secret flag is received or upon encountering an error.

### Example Workflow
- The client sends an introductory message: `"EECE7374 INTR 002642073"`.
- The server responds with a message of type `EXPR`, such as: `"EECE7374 EXPR 2 + 2"`.
- The client evaluates the expression (`2 + 2 = 4`) and sends back the result in the format: `"EECE7374 RSLT 4"`.
- The process continues until a success or failure message is received.

### Requirements
- Python 3.x
- No external libraries required (uses Python’s built-in `socket` module)

### How to Run
1. Clone the repository or download the script.
2. Ensure that a compatible server is running on `localhost:5206`.
3. Run the script using Python:
   ```bash
   python client.py
   ```
4. The client will automatically handle communication with the server and display results or secret flags in the console.
