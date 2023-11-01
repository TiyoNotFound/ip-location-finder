import requests

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
            
            print(f"IP Address: {ip_address}")
            print(f"Country: {country}")
            print(f"Region: {region}")
            print(f"City: {city}")
            print(f"Postal Code: {postal}")
            print(f"Organization: {org}")
        else:
            print(f"Failed to retrieve information for IP address: {ip_address}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    ip_address = input("Enter an IP address: ")
    get_ip_location(ip_address)
