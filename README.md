# it-lessons-materials

Репозиторій містить матеріали для уроків інформатики за програмою НУШ

# Setup

1. Create a new GCloud Project.
2. Enable Google Drive API.
3. Create a new service account and grant it the Editor role.
4. Download the service account key in JSON format and add it to the GitHub Secrets as `GDRIVE_CREDENTIALS`
5. Add the following env variables `GRADE_5_FOLDER_ID`  `GRADE_6_FOLDER_ID` `GRADE_5_FOLDER_ID` with respective folder ids (can be determined by looking at the folder URL in the browser).
6. Grant edit access to all folders for various grades to the service account email address.
7. Commit merge and enjoy.
