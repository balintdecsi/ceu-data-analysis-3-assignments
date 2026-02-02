#!/usr/bin/env python3
"""
Fetch Airbnb listings data from Inside Airbnb.
Downloads gzipped CSV files and extracts them to data/raw/
"""

import gzip
import os
import shutil
import urllib.request
from pathlib import Path

# Data sources from Inside Airbnb
DATA_SOURCES = {
    "copenhagen_listings_2025_03_train.csv": "https://data.insideairbnb.com/denmark/hovedstaden/copenhagen/2025-03-23/data/listings.csv.gz",
    "copenhagen_listings_2025_09_test.csv": "https://data.insideairbnb.com/denmark/hovedstaden/copenhagen/2025-09-29/data/listings.csv.gz",
    "oslo_listings_2025_09_test.csv": "https://data.insideairbnb.com/norway/oslo/oslo/2025-09-29/data/listings.csv.gz",
}

def fetch_and_extract(url: str, output_path: Path) -> None:
    """Download a gzipped file and extract it."""
    gz_path = output_path.with_suffix(".csv.gz")
    
    print(f"Downloading {url}...")
    urllib.request.urlretrieve(url, gz_path)
    
    print(f"Extracting to {output_path}...")
    with gzip.open(gz_path, "rb") as f_in:
        with open(output_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    # Clean up the .gz file
    gz_path.unlink()
    print(f"Done: {output_path}")


def main():
    # Determine project root (script is in scripts/, data is in data/raw/)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    data_dir = project_root / "data" / "raw"
    
    # Create data directory if it doesn't exist
    data_dir.mkdir(parents=True, exist_ok=True)
    
    for filename, url in DATA_SOURCES.items():
        output_path = data_dir / filename
        
        if output_path.exists():
            print(f"Skipping {filename} (already exists)")
            continue
        
        fetch_and_extract(url, output_path)
    
    print("\nAll data downloaded successfully!")


if __name__ == "__main__":
    main()
