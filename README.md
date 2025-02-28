# it-lessons-materials

The repository contains materials for informatics lessons of the "New Ukrainian School" program.
Presentations are added in the Marp (Markdown flavor) format, and the CI/CD pipeline is responsible for creating PDF and HTML versions and pushing them to the GDrive.

## Setup

1. Create a new GCloud Project.
2. Enable Google Drive API.
3. Create a new service account and grant it the Editor role.
4. Download the service account key in JSON format and add it to the GitHub Secrets as `GDRIVE_CREDENTIALS`
5. Add the following env variables `GRADE_5_FOLDER_ID`  `GRADE_6_FOLDER_ID` `GRADE_5_FOLDER_ID` with respective folder IDs (can be determined by looking at the folder URL in the browser).
6. Generate personal access token (classic) with read access to the repo. Set repository secret `PAT_TOKEN` so the pipeline can download artifacts.
7. Grant edit access to all folders for various grades to the service account email address.
8. Commit merge and enjoy.

## Adding new presentation

1. Install [Marp](https://marp.app/)
2. Choose the folder according to the grade (5, 6 or 7).
3. Create a new markdown file in the folder following naming convention `<lesson-number>-<lesson-topic>.md`.
4. Once your file is merged to the `main` branch both html and pdf versions of it should appear on your GDrive.
