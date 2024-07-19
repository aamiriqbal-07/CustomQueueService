import json
import requests


def main():
    api_url = 'http://localhost:5000/publish'

    while True:
        input_data = input(
            "Enter message (in JSON format) to publish or 'exit' to quit:\n")
        if input_data.lower() == 'exit':
            break

        try:
            message = json.loads(input_data)
            response = requests.post(api_url, json=message)

            if response.status_code == 200:
                print(response.json()["message"])
            else:
                print(response.json()["error"])
        except json.JSONDecodeError:
            print("Invalid JSON format. Please try again.")
        except requests.RequestException as e:
            print(f"Request failed: {e}")


if __name__ == "__main__":
    main()
