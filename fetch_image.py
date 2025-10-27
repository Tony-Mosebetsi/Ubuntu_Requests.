import requests
import os
from urllib.parse import urlparse
from datetime import datetime

def fetch_and_save_image():
    # Principle: Community - Connect to the global web
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web")
    print()

    try:
        # Prompt user for a URL
        url = input("Please enter the image URL: ").strip()

        # Validate URL (basic check for image file extensions)
        valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
        if not url.lower().endswith(valid_extensions):
            print("Warning: URL may not point to a valid image file (jpg, jpeg, png, gif, bmp). Proceeding anyway...")

        # Principle: Respect - Handle errors gracefully
        # Send HTTP GET request to fetch the image
        response = requests.get(url, stream=True)
        
        # Check for HTTP errors
        response.raise_for_status()

        # Principle: Sharing - Create directory for organized storage
        output_dir = "Fetched_Images"
        os.makedirs(output_dir, exist_ok=True)

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        # If no filename or invalid, generate one with timestamp
        if not filename or not filename.lower().endswith(valid_extensions):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"image_{timestamp}.jpg"  # Default to .jpg if unknown

        # Construct full path for saving
        output_path = os.path.join(output_dir, filename)

        # Principle: Practicality - Save the image in binary mode
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # Filter out keep-alive chunks
                    file.write(chunk)

        # Match the exact output format
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {output_path}")
        print()
        print("Connection strengthened. Community enriched.")

    except requests.exceptions.HTTPError as http_err:
        print(f"Error: HTTP issue occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the server. Please check your internet connection.")
    except requests.exceptions.InvalidURL:
        print("Error: Invalid URL provided.")
    except requests.exceptions.RequestException as req_err:
        print(f"Error: Network issue occurred: {req_err}")
    except OSError as os_err:
        print(f"Error: File system issue occurred: {os_err}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    fetch_and_save_image()

if __name__ == "__main__":
    main()
