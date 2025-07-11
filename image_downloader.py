# -*- coding: utf-8 -*-
"""image_downloader_colab.py
# Image Downloader from CSV 
This code downloads images from URLs listed in a CSV file. It saves the images back to Drive and appends the local paths to a new column in the CSV.
"""

# Install tqdm if not available
# Python script to download images and update CSV
import os
import csv
import requests
from tqdm import tqdm

def download_images_and_update_csv(csv_path, url_column_name='url', id_column_name='message_id',
                                    output_folder='/tweets/images', output_csv_path=None, git_path=None):
    os.makedirs(output_folder, exist_ok=True)
    updated_rows = []

    with open(csv_path, 'r', newline='', encoding='utf-8') as infile:
        reader = list(csv.DictReader(infile))
        fieldnames = reader[0].keys() if reader else []
        fieldnames = list(fieldnames) + ['local_image_path']

        for row in tqdm(reader, desc="Downloading images", unit="img"):
            image_url = row.get(url_column_name)
            message_id = row.get(id_column_name)

            if not image_url or not message_id:
                row['local_image_path'] = ''
                updated_rows.append(row)
                continue

            try:
                response = requests.get(image_url, timeout=10)
                response.raise_for_status()

                ext = os.path.splitext(image_url)[-1]
                if not ext or len(ext) > 5:
                    ext = ".jpg"

                image_name = f"{message_id}{ext}"
                image_path = os.path.join(output_folder, image_name)

                with open(image_path, 'wb') as f:
                    f.write(response.content)

                row['local_image_path'] = os.path.join(git_path, image_name)

            except Exception as e:
                row['local_image_path'] = ''

            updated_rows.append(row)

    if not output_csv_path:
        output_csv_path = os.path.splitext(csv_path)[0] + '_with_images.csv'

    with open(output_csv_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

    print(f"\n Updated CSV saved to: {output_csv_path}")

# Replace with your actual file paths 
csv_path = 'twitter_data.csv'
output_csv_path = 'twitter_data_with_images.csv'
output_folder = 'image/'
git_path='https://github.com/Itugeosocial/images/blob/main/image/'

download_images_and_update_csv(
    csv_path=csv_path,
    url_column_name='photo_url',
    id_column_name='message_id',
    output_folder=output_folder,
    output_csv_path=output_csv_path,
    git_path=git_path)