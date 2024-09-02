# Invoice Management System 📊

This Django-based web application provides a system for managing invoices. Built using Django and various Python libraries, it offers an interface for users to upload, process, and analyze invoice data. The application can be run within a Docker container for easy deployment and consistency across environments.

## Features

- Upload and process multiple XML invoice files.
- Extract and display key information from invoices.
- Generate comprehensive reports and analytics.
- Export data to CSV and Excel formats.
- User authentication and authorization system.
- Responsive design for desktop and mobile use.

## How To Use It

### Prerequisites

1. Install [Docker](https://docs.docker.com/get-docker/).
2. Ensure you have [Docker Compose](https://docs.docker.com/compose/install/) installed.
3. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/villoslado/ledgerworks24.git
   cd ledgerworks24
   ```

### Running the App with Docker

This project includes a `Dockerfile` and a `docker-compose.yml` file to make it easy to build and run the app in a container.

#### Build and Run the Docker Container:

Build and start the Docker container by running the following command:

```bash
docker-compose up --build
```

This command will build the Docker image and start the container. The first time you run this, it may take a few minutes to download and install all the necessary dependencies.

#### Access the Application

Once the container is running, the application will be accessible at:

`http://localhost:8000`

You can now use the application to upload, process, and analyze invoice data.

## Technologies Used

- Django 5.0.6
- Python 3.10
- Docker
- pandas for data processing
- crispy-forms for enhanced form rendering
