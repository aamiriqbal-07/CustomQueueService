import requests
import json
import time


def main():
    queue_name = input("Enter the queue name to consume from:\n")
    api_url = 'http://localhost:5000/consume'

    while True:
        try:
            response = requests.get(api_url, params={'topic': queue_name})

            if response.status_code == 200:
                message_data = response.json()
                print("Received Message:")
                print(json.loads(message_data["message"]))
            elif response.status_code == 204:
                # No new messages available, just wait
                pass
            else:
                print(response.json().get("error", "An error occurred."))
        except requests.RequestException as e:
            print(f"Request failed: {e}")

        time.sleep(1)  # Poll every second to avoid excessive CPU usage


if __name__ == "__main__":
    main()
