# Custom Messaging Queue Service

This project implements a simple custom messaging queue service using Python. It includes a publisher that sends messages to a queue, a consumer that retrieves messages from the queue, and a queue service hosted on `localhost` using Flask. The system provides one-way persistent communication, ensuring that messages are delivered and consumed reliably.

## Components

1. **Queue Service**: A REST API hosted using Flask to manage and serve messages in queues.
2. **Publisher**: A command-line interface (CLI) tool to send messages to the queue service.
3. **Consumer**: A CLI tool that polls the queue service to retrieve and display messages.

## How It Works

### 1. Queue Service

The queue service provides endpoints to publish and consume messages. It uses JSON files to persist messages in different queues. 

- **POST /publish**: Adds a message to a specified queue.
  - **Request Body**:
    ```json
    {
      "topic": "queue_name",
      "content": {
        "message": "Your message here"
      }
    }
    ```
  - **Response**:
    - `200 OK`: Message successfully added.
    - `400 Bad Request`: Invalid request format.
    - `404 Not Found`: Queue does not exist.

- **GET /consume**: Retrieves the next message from a specified queue.
  - **Query Parameter**:
    - `topic`: The name of the queue to consume from.
  - **Response**:
    - `200 OK`: Message retrieved successfully.
    - `204 No Content`: No messages available in the queue.
    - `400 Bad Request`: Invalid request format.
    - `404 Not Found`: Queue does not exist.

### 2. Publisher

The publisher is a CLI tool that sends messages to the queue service using the `/publish` API endpoint.

- **Usage**:
  - Run the publisher script: `python publisher.py`
  - Enter messages in JSON format to publish:
    ```json
    {
      "topic": "queue_name",
      "content": {
        "message": "Your message here"
      }
    }
    ```
  - Type `exit` to quit the publisher.

### 3. Consumer

The consumer is a CLI tool that polls the queue service for new messages from a specified queue.

- **Usage**:
  - Run the consumer script: `python consumer.py`
  - Enter the queue name when prompted to start consuming messages.
  - The consumer will continuously poll the queue service and print messages as they arrive.

## Setup and Running

1. **Install Dependencies**:
   - Ensure you have Python 3.x installed.
   - Install Flask for the queue service:
     ```sh
     pip install Flask
     ```
   - Install `requests` for HTTP requests:
     ```sh
     pip install requests
     ```

2. **Start the Queue Service**:
   - Run `queue_service.py` to start the Flask server:
     ```sh
     python queue_service.py
     ```

3. **Run the Publisher**:
   - Open a new terminal and run the publisher script:
     ```sh
     python publisher.py
     ```

4. **Run the Consumer**:
   - Open one or more new terminals and run the consumer script:
     ```sh
     python consumer.py
     ```

## Example Workflow

1. **Start the Queue Service**:
   ```sh
   python queue_service.py
   ```

2. **Publish Messages**:
   - In a new terminal, start the publisher:
     ```sh
     python publisher.py
     ```
   - Enter a message:
     ```json
     {
       "topic": "example_queue",
       "content": {
         "message": "Hello, World!"
       }
     }
     ```

3. **Consume Messages**:
   - In a new terminal, start the consumer and specify the queue name:
     ```sh
     python consumer.py
     ```
   - The consumer will display any new messages published to the specified queue.

## Notes

- The queue service stores messages in JSON files named after the queue names. These files are created and updated automatically.
- The consumer uses a polling mechanism to check for new messages, which may introduce a slight delay.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the content based on any specific requirements or additional details you may have.
