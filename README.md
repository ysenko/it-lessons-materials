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

### Prerequisites

- Install [Marp](https://marp.app/)

### Creating presentation

1. Copy the template file from the `templates` folder into the `content` folder.
   Make sure you replaced `<GRADE>` with the correct grade (i.e. 5, 6 or 7), `<LESSON-NUMBER>` with a correct lesson number, and `<LESSON-TITLE>` with a short and readable lesson title:

   ```sh
   cp templates/gaia_template.md content/<GRADE>/<LESSON-NUMBER>-<LESSON-TITLE>.md
   ```

2. Any assets (e.g. images) must be placed inside the `content/<GRADE>/assets/<LESSON-NUMBER>` folder.

3. Please do not commit any artifacts (i.e. pdf, html, pptx files). The CI pipeline will build PDF and PPTX (non-editable) versions of all changed presentations and will upload them to your Google Drive. **Existing files with same names will be DELETED! from your Google Drive folder.**

4. Once your file is merged to the `main` branch both html and pdf versions of it should appear on your GDrive.

### Building presentation locally

The repository provides a Makefile that automates building process.

#### Build html, pdf and pptx versions simultaneously

```sh
make SRC=<path-to-your-presentaion-md-file>
```

#### Build specify type of output

You can build **html** using the following command

```sh
make html SRC=<path-to-your-presentaion-md-file>
```

You can build **pdf** using the following command

```sh
make pdf SRC=<path-to-your-presentaion-md-file>
```

And you can build pptx using the following command

```sh
make pptx SRC=<path-to-your-presentaion-md-file>
```

Make sure you replace path with the actual path you your presentation md file.
By default the resulting files will apper alongside of your presentation in the `content` directory. You can change this by specifying the `OUTPUT_DIR=<path>` option.

#### Removing local artifacts

**The command below is highly destructive**. Please make sure you know what you are doing.

Run the following command to remove **all** pdf, html and pptx files inside the project dir:

```sh
make clean
```
