import os
import requests
from duckduckgo_search import DDGS

def download_images(search_term, num_images=5, output_folder="4k_images"):
    os.makedirs(output_folder, exist_ok=True)
    with DDGS() as ddgs:
        results = list(ddgs.images(search_term, max_results=num_images))
    
    count = 0
    for result in results:
        image_url = result["image"]
        try:
            response = requests.get(image_url, stream=True, timeout=10)
            response.raise_for_status()
            
            ext = image_url.split(".")[-1].split("?")[0]
            file_path = os.path.join(output_folder, f"{search_term.replace(' ', '_')}_{count}.{ext}")
            
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            
            print(f"✅ Downloaded: {file_path}")
            count += 1
        except Exception as e:
            print(f"⚠ Error downloading image: {e}")

if __name__ == "__main__":
    search_query = input("Enter search term for 4K images: ")
    num_images = int(input("How many images do you want to download? "))
    download_images(search_query, num_images)
