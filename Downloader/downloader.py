import requests


def main():
    url = input("Enter the URL of the file you want to download: ")
    download_file(url)


def download_file(url):
    try:
        response = requests.get(url)
        # Raise an HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()
        
        # Extract the filename from the URL
        filename = url.split("/")[-1]

        with open(filename, "wb") as file:
            file.write(response.content)

        print(f"File downloaded successfully: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")


if __name__ == "__main__":
    main()
   
