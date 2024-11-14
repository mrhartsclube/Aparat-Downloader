import requests  # Import the requests library to make HTTP requests
import sys  # Import sys to access command-line arguments
import os  # Import os to create directories and handle file paths
from tqdm import tqdm  # Import tqdm for a progress bar

def download_video(url, title, quality, dest_folder):
    # Make an HTTP GET request to the video URL, stream the response to download it in chunks
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        print(f"Failed to download {title}")
        return
    
    # Create the destination folder if it doesn't exist
    os.makedirs(dest_folder, exist_ok=True)
    # Get the file size from the response headers
    file_size = int(response.headers.get("Content-Length", 0))
    # Rename the file based on the title pattern
    filename = os.path.join(dest_folder, f"{title}.mp4")
    
    # Open the file to write binary data
    with open(filename, "wb") as file:
        # Create a tqdm progress bar for the download
        with tqdm(total=file_size, unit='B', unit_scale=True, desc=f"{title} ({quality})") as pbar:
            # Iterate over the response content in chunks
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    # Write each chunk to the file
                    file.write(chunk)
                    # Update the progress bar with the size of the chunk
                    pbar.update(len(chunk))

def main(video_hashes):
    for video_hash in video_hashes:
        # Construct the API URL for each video hash
        api_url = f"https://www.aparat.com/api/fa/v1/video/video/show/videohash/{video_hash}"
        # Make an HTTP GET request to the API URL
        video_response = requests.get(api_url)
        # Parse the JSON response
        video_data = video_response.json()
        
        # Get the video title from the JSON data
        title = video_data['data']['attributes']['title']
        # Rename based on the title is [فصل S سریال ویچر قسمت E | The Witcher دوبله فارسی]
        # title = f"S0{title[4]}E0{title[22]}"
        # Get all file links from the JSON data
        file_links = video_data['data']['attributes']['file_link_all']
        
        # Find the best quality by comparing profile numbers
        best_quality = max(file_links, key=lambda x: int(x['profile'].replace('p', '')))
        # Get the download URL for the best quality video
        video_url = best_quality['urls'][0]
        
        # Download the video into a folder names downloads
        download_video(video_url, title, best_quality['profile'], 'downloads')

if __name__ == "__main__":
    # Check if the script has received enough command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <video_hashes:comma_separated>")
    else:
        # Split the command-line argument into individual video hashes
        video_hashes = sys.argv[1].split(',')
        # Call the main function with the list of video hashes
        main(video_hashes)