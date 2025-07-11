# Image Downloader from CSV

This script downloads images from URLs listed in a CSV file and saves them locally. It also appends the corresponding local image paths to a new column in the output CSV file, making it ideal for organizing datasets with linked media like tweets.

## Features

- Reads image URLs from a CSV file.
- Downloads images and saves them to a specified folder.
- Appends local image paths to the original CSV.
- Automatically handles errors (e.g., missing URLs or failed downloads).
- Compatible with GitHub-hosted paths for web-based access.

## Requirements

Install dependencies via pip (if not already installed):

```bash
pip install tqdm requests
```

## How to Use

1. Place your input CSV file (e.g., `twitter_data.csv`) in the same directory.
2. Make sure your CSV has:
   - A column containing image URLs (e.g., `photo_url`)
   - A unique ID column for naming images (e.g., `message_id`)
3. Run the script:

```bash
python image_downloader.py
```

By default, it will:

- Read from `twitter_data.csv`
- Save images in the `image/` folder
- Output a new CSV called `twitter_data_with_images.csv` with a `local_image_path` column

## Customization

You can modify the script parameters:

```python
download_images_and_update_csv(
    csv_path='your_file.csv',
    url_column_name='photo_url',
    id_column_name='message_id',
    output_folder='your_output_folder/',
    output_csv_path='your_output_file.csv',
    git_path='https://github.com/your_repo/path/to/image/folder/'
)
```

## Output

- **Images**: Downloaded to the `output_folder` you specify.
- **CSV**: A new CSV file with the added `local_image_path` column.

## Example

Input CSV:

| message_id | photo_url               |
|------------|-------------------------|
| 12345      | http://example.com/1.jpg|

Output CSV:

| message_id | photo_url               | local_image_path                                 |
|------------|-------------------------|--------------------------------------------------|
| 12345      | http://example.com/1.jpg | https://github.com/your_repo/image/12345.jpg    |

## License

MIT License

---

*Created by [Ehsaneddin jalilian : ehsaneddin.jalilian@it-u.at ]*
