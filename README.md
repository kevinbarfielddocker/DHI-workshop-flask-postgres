## Docker DHI Python and Postgres workshop

## Sample application

### Run the sample application

    git clone https://github.com/kevinbarfielddocker/dhi-python-postgres

Review the `Dockerfile` file.

Review the `docker-compose.yml` file.

Start the application:

    docker compose up -d --build

Go to the application in the browser:

    http://localhost:5000

Enter a reservation using the application.

### Scan the base python image using Trivy:

    docker run -it -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image --scanners vuln docker.io/python:3.13-slim

Review vulnerabilities in the base image.

## Docker Hardended Images

Go to the Analog Docker Hub organization

    https://hub.docker.com/orgs/analog/repositories

Click Hardened Images and Catalog.

Type python in the search bar to find the python hardended image.

Select the python image.

Review the Guide for implementing the image.

Go to images/tags.

Search by `3.13`.

Select Python 3.13.x (dev) - the tag is `3.13-alpine3.22-dev`.

Review packages, specifications, vulnerabilities, and attestations for the hardened image.

Mirror the python repository to your organziation with the name dhi-python(already done).

Select the `dhi-python` repository in your organization.

Select the `customize image` button.

Select `Python 3.13.x (dev) alpine 3.22`.

Select to add the `curl` package.

Review other customizations available.

Start customization build with tag `curl` (already done).

Mirror the postgres DHI image to dhi-postgres (already done).

### Scan the DHI images using Trivy with Vex statements

#### Python

Part 1: Collect Vex statements:

    docker scout vex get registry://docker.io/analog/dhi-python:3.13-alpine3.22-dev_curl -o vex-python.json

Part 2: Use Vex statements to scan DHI image:

    docker run -it -v /var/run/docker.sock:/var/run/docker.sock -v .:/opt aquasec/trivy image --scanners vuln --vex /opt/vex-python.json docker.io/analog/dhi-python:3.13-alpine3.22-dev_curl

Review Trivy output

#### Postgres

Part 1: Collect Vex statements:

    docker scout vex get registry://docker.io/analog/dhi-postgres:17.7 -o vex-postgres.json

Part 2: Use Vex statements to scan DHI image:

    docker run -it -v /var/run/docker.sock:/var/run/docker.sock -v .:/opt aquasec/trivy image --scanners vuln --vex /opt/vex-postgres.json docker.io/analog/dhi-postgres:17.7

Review Trivy output for the hardened images.

### Modify application to use DHI Images

#### Modify Dockerfile

Change the image in the FROM statement to `FROM analog/dhi-python:3.13-alpine3.22-dev_curl` and save.

#### Modify Docker Compose file

Change the db image tag to `    image: analog/dhi-postgres:17.7` and save the file.

Run `docker compose up --build`.

Confirm the application is running in the browser:

     http://localhost:5000

Discuss the volume directory change for postgres.

#### Exec curl from the python image using the Docker Desktop GUI

Open the Docker Desktop GUI.

Select the `web-1` container.

Select Exec.

Enter `curl https://www.docker.com` and see the resulting HTML.