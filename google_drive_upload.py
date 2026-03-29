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


def _escape_drive_query_value(value: str) -> str:
    """Escape a string value for use inside a Google Drive API query."""
    return value.replace("'", "\\'")


def get_or_create_folder(service, parent_folder_id, folder_name):
    """
    Find or create a subfolder by name inside the given parent folder.

    Args:
        service: The authenticated Google Drive service instance.
        parent_folder_id (str): The ID of the parent folder.
        folder_name (str): The name of the subfolder to find or create.

    Returns:
        str: The ID of the found or created subfolder.
    """
    safe_name = _escape_drive_query_value(folder_name)
    query = (
        f"'{parent_folder_id}' in parents and name = '{safe_name}' "
        f"and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    )
    results = service.files().list(q=query, fields="files(id, name)").execute()
    items = results.get("files", [])
    if items:
        return items[0]["id"]

    file_metadata = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [parent_folder_id],
    }
    folder = service.files().create(body=file_metadata, fields="id").execute()
    print(f"Created subfolder '{folder_name}' with ID: {folder.get('id')}")
    return folder.get("id")


def resolve_folder_path(service, root_folder_id, relative_path):
    """
    Resolve a slash-separated subfolder path, creating missing folders as needed.

    Args:
        service: The authenticated Google Drive service instance.
        root_folder_id (str): The ID of the root folder.
        relative_path (str): Slash-separated path of subfolders (e.g. "plans").

    Returns:
        str: The ID of the deepest resolved folder.
    """
    folder_id = root_folder_id
    for part in relative_path.split("/"):
        part = part.strip()
        if not part:
            continue
        if part in {".", ".."}:
            raise ValueError(
                f"Invalid path segment '{part}' in subfolder path '{relative_path}'"
            )
        folder_id = get_or_create_folder(service, folder_id, part)
    return folder_id


def get_destination_file_name(destination_path):
    """
    Parse the destination path to get the folder ID and destination file name.

    The path format is ``dest_folder_id:dest_file_name`` or
    ``dest_folder_id:subfolder/dest_file_name`` for nested uploads.

    Args:
        destination_path (str): The destination path.

    Returns:
        tuple: A tuple of (folder_id, subfolder_path, file_name) where
            ``subfolder_path`` is an empty string when there is no subfolder.

    Raises:
        ValueError: If the destination path is not in the correct format.
    """
    if ":" not in destination_path:
        raise ValueError(
            "Destination path must be in the format dest_folder_id:dest_file_name"
        )
    folder_id, rest = destination_path.split(":", 1)
    parts = rest.rsplit("/", 1)
    if len(parts) == 2:
        subfolder_path, file_name = parts
    else:
        subfolder_path, file_name = "", parts[0]
    return folder_id, subfolder_path, file_name


def remove_existing_file(service, folder_id, destination_name):
    """
    Remove an existing file with the same name in the specified folder.

    Args:
        service: The authenticated Google Drive service instance.
        folder_id (str): The ID of the folder in Google Drive.
        destination_name (str): The name of the file to remove.
    """
    # Search for existing file with the same name in the folder
    safe_name = _escape_drive_query_value(destination_name)
    query = (
        f"'{folder_id}' in parents and name = '{safe_name}' and trashed = false"
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
    root_folder_id, subfolder_path, destination_name = get_destination_file_name(
        args.destination_path
    )

    # Authenticate
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=["https://www.googleapis.com/auth/drive"]
    )
    service = build("drive", "v3", credentials=creds)

    # Resolve (or create) any subfolders
    folder_id = (
        resolve_folder_path(service, root_folder_id, subfolder_path)
        if subfolder_path
        else root_folder_id
    )

    if args.override:
        remove_existing_file(service, folder_id, destination_name)

    upload_to_drive(service, args.source_file, destination_name, folder_id)


if __name__ == "__main__":
    main()
