import requests

def check_api():
    while True:
        # GET the API url from the user
        url = input("Enter the API URL you want to check: ").strip()

        # A header section for any necessary headers
        headers = {
            "Authorization": "Bearer your_api_key", # A token or key (will be needed in the expansion of the program once a bearer token is aquired)
            "Content-Type": "application/json"
        }
 
        # Make the GET request
        try:
            response = requests.get(url, headers=headers)

            # Check the status of the the API
            if response.status_code == 200:
                print("API is nominal!")
                print("Response:", response.json())
            else:
                print(f"API health check failed with status code: {response.status_code}")
                print("Response:", response.text)

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

        # Allows the user to check another API
        another = input("Would you like to check another API? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Goodbye!")
            break

# Runs the function again if condition is met
check_api()
