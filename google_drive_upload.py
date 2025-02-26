import argparse
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Read environment variables
CREDENTIALS_FILE = os.getenv("GDRIVE_CREDENTIALS_FILE", "creds.json")

def get_mime_type(filename):
    mime_types = {
        ".txt": "text/plain",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".html": "text/html",
        ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    }
    for ext, mime in mime_types.items():
        if filename.endswith(ext):
            return mime
    return "application/octet-stream"  # Default for unknown file types

def upload_to_drive(source_file, destination_name, folder_id):
    # Authenticate
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=["https://www.googleapis.com/auth/drive"]
    )
    service = build("drive", "v3", credentials=creds)

    # Get MIME type
    mime_type = get_mime_type(source_file)

    # Upload file
    file_metadata = {
        "name": destination_name,
        "parents": [folder_id]
    }
    media = MediaFileUpload(source_file, mimetype=mime_type)
    file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()

    print(f"Uploaded file ID: {file.get('id')}")

def main():
    parser = argparse.ArgumentParser(description="Upload a file to Google Drive")
    parser.add_argument("source_file", help="Path to the local file to upload")
    parser.add_argument("destination_path", help="Destination path in the format dest_folder_id:dest_file_name")
    args = parser.parse_args()

    # Parse destination path
    if ":" not in args.destination_path:
        raise ValueError("Destination path must be in the format dest_folder_id:dest_file_name")
    folder_id, destination_name = args.destination_path.split(":", 1)
    
    upload_to_drive(args.source_file, destination_name, folder_id)

if __name__ == "__main__":
    main()

