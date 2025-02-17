import socket

def check_github_connection():
    github_host = "github.com"
    port = 443  # HTTPS port
    
    try:
        # Get the IP address of GitHub
        ip_address = socket.gethostbyname(github_host)
        print(f"GitHub IP Address: {ip_address}")
        
        # Attempt to connect to GitHub
        with socket.create_connection((github_host, port), timeout=5):
            print("Successfully connected to GitHub!")
    
    except socket.gaierror:
        print("Failed to resolve GitHub domain name.")
    except socket.timeout:
        print("Connection to GitHub timed out.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_github_connection()