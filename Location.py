import requests
from tabulate import tabulate  # Import the tabulate library

def get_ip_location(ip_address):
    try:
        # Send a GET request to the ipinfo.io API
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            country = data.get("country", "N/A")
            region = data.get("region", "N/A")
            city = data.get("city", "N/A")
            postal = data.get("postal", "N/A")
            org = data.get("org", "N/A")

            # Create a list of lists for tabulate
            table_data = [
                ["IP Address", ip_address],
                ["Country", country],
                ["Region", region],
                ["City", city],
                ["Postal Code", postal],
                ["Organization", org]
            ]

            # Use tabulate to format and print the data as a table
            table = tabulate(table_data, tablefmt="grid")
            print(table)
        else:
            print(f"Failed to retrieve information for IP address: {ip_address}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    ip_address = input("Enter an IP address: ")
    get_ip_location(ip_address)
