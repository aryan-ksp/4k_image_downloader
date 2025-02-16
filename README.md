# 4K Image Downloader

## Overview
4K Image Downloader is a lightweight and efficient tool that allows users to download high-resolution 4K images from various websites. This tool automates the process of fetching, processing, and storing images, making it ideal for photographers, designers, and content creators who need high-quality visuals.

## Features
- Download 4K resolution images from supported sources
- Batch downloading support
- Multi-threaded downloading for faster performance
- Automatic file naming and organization
- Supports popular image formats (JPEG, PNG, WebP, etc.)
- Proxy support for anonymous downloading
- User-friendly interface with CLI support

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- `pip` (Python package manager)
- `requests` and `beautifulsoup4` (for web scraping)
- `tqdm` (for progress visualization)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/aryan-ksp/4k_image_downloader
   cd 4k_image_downloader
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Command
To download a single image, run:
```bash
python downloader.py --url "IMAGE_URL" --output "path/to/save"
```

### Batch Download
To download multiple images from a text file containing URLs:
```bash
python downloader.py --file urls.txt --output "path/to/save"
```

```

### Additional Options
- `--threads` : Number of simultaneous downloads (default: 4)
- `--format` : Specify output format (jpeg, png, etc.)

## Example
```bash
python downloader.py --url "https://example.com/sample-image.jpg" --output "./downloads"
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For any inquiries or issues, feel free to contact the project maintainer at `aryn.ksp@gmail.com`.

