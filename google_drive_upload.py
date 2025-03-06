import argparse
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Read environment variables
CREDENTIALS_FILE = os.getenv("GDRIVE_CREDENTIALS_FILE", "creds.json")


def get_mime_type(filename):
    """
    Get the MIME type based on the file extension.

    Args:
        filename (str): The name of the file.

    Returns:
        str: The MIME type of the file.
    """
    mime_types = {
        ".txt": "text/plain",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".html": "text/html",
        ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    }
    for ext, mime in mime_types.items():
        if filename.endswith(ext):
            return mime
    return "application/octet-stream"  # Default for unknown file types


def upload_to_drive(service, source_file, destination_name, folder_id):
    """
    Upload a file to Google Drive.

    Args:
        service: The authenticated Google Drive service instance.
        source_file (str): The path to the local file to upload.
        destination_name (str): The name of the file in Google Drive.
        folder_id (str): The ID of the destination folder in Google Drive.
    """
    # Get MIME type
    mime_type = get_mime_type(source_file)

    # Upload file
    file_metadata = {"name": destination_name, "parents": [folder_id]}
    media = MediaFileUpload(source_file, mimetype=mime_type)
    file = (
        service.files()
        .create(body=file_metadata, media_body=media, fields="id")
        .execute()
    )

    print(f"Uploaded file ID: {file.get('id')}")


def get_destination_file_name(destination_path):
    """
    Parse the destination path to get the folder ID and destination file name.

    Args:
        destination_path (str): The destination path in the format dest_folder_id:dest_file_name.

    Returns:
        tuple: A tuple containing the folder ID and destination file name.

    Raises:
        ValueError: If the destination path is not in the correct format.
    """
    if ":" not in destination_path:
        raise ValueError(
            "Destination path must be in the format dest_folder_id:dest_file_name"
        )
    return destination_path.split(":", 1)


def remove_existing_file(service, folder_id, destination_name):
    """
    Remove an existing file with the same name in the specified folder.

    Args:
        service: The authenticated Google Drive service instance.
        folder_id (str): The ID of the folder in Google Drive.
        destination_name (str): The name of the file to remove.
    """
    # Search for existing file with the same name in the folder
    query = (
        f"'{folder_id}' in parents and name = '{destination_name}' and trashed = false"
    )
    results = service.files().list(q=query, fields="files(id, name)").execute()
    items = results.get("files", [])

    if items:
        # Delete existing file
        for item in items:
            print(f"Will remove: {item}")
            service.files().delete(fileId=item["id"]).execute()


def main():
    """
    Main function to parse arguments and upload a file to Google Drive.
    """
    parser = argparse.ArgumentParser(description="Upload a file to Google Drive")
    parser.add_argument("source_file", help="Path to the local file to upload")
    parser.add_argument(
        "destination_path",
        help="Destination path in the format dest_folder_id:dest_file_name",
    )
    parser.add_argument(
        "--override",
        action="store_true",
        default=False,
        help="Override existing file with the same name",
    )
    args = parser.parse_args()

    # Parse destination path
    folder_id, destination_name = get_destination_file_name(args.destination_path)

    # Authenticate
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=["https://www.googleapis.com/auth/drive"]
    )
    service = build("drive", "v3", credentials=creds)

    if args.override:
        remove_existing_file(service, folder_id, destination_name)

    upload_to_drive(service, args.source_file, destination_name, folder_id)


if __name__ == "__main__":
    main()
