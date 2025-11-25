
import requests
def fetch_data(url):
    try:
        print(f"\nFetching: {url}")
        response = requests.get(url, timeout=5)
        response.raise_for_status()     # checks for 404, 500 etc.

        return response.json()          # convert to JSON

    except requests.exceptions.Timeout:
        print("Timeout: Server took too long to respond.")

    except requests.exceptions.ConnectionError:
        print("Connection Error: Host unreachable.")

    except requests.exceptions.HTTPError:
        print(f"HTTP Error: Status code {response.status_code}")

    except ValueError:
        print("Invalid JSON received.")

    except Exception as e:
        print("Unexpected error:", e)
print(fetch_data("https://jsonplaceholder.typicode.com/posts"))  # Good URL

print(fetch_data("https://wrongurl12345.com"))                   # Invalid host

print(fetch_data("https://httpstat.us/200?sleep=6000"))          # Timeout URL