### Phishing Detection Project
## Overview
This project aims to detect phishing websites by analyzing key features that distinguish phishing websites from legitimate ones. It utilizes a modular coding approach and incorporates the full lifecycle of a machine learning pipeline, including data ingestion, validation, transformation, model training, evaluation, and deployment.

The project was deployed to Azure Cloud using Azure Container Registry and Azure Web App. The deployment process was automated using GitHub Actions for a seamless CI/CD workflow. A Flask application serves as the frontend for interacting with the model.

## Features
Phishing Data
The dataset includes 30 features that help classify websites as phishing (-1) or legitimate (1). Key features include:

having_IP_Address: Whether the URL contains an IP address.
URL_Length: Length of the URL.
Shortining_Service: Checks for shortened URLs.
SSLfinal_State: SSL certificate status.
Request_URL: If resources (e.g., images) are loaded from another domain.
Submitting_to_email: Forms submitting directly to email addresses.
Iframe: Hidden iframes present in the webpage.
(Full list of features can be found in the dataset description.)

## Project Workflow
This project follows a modular coding style to ensure clear separation of responsibilities and maintainability.

## Data Ingestion

Collect and load the phishing dataset.
Ensure data is in a format suitable for processing.
## Data Validation

Validate data for completeness and correctness.
Handle missing values and anomalies.
## Data Transformation

Feature engineering (e.g., scaling, encoding categorical features).
Prepare data for machine learning models.
## Model Training

Train classification models to predict whether a website is phishing or legitimate.
Evaluate multiple algorithms like Decision Trees, Random Forests, and Neural Networks.
## Model Evaluation

Evaluate model performance using metrics like accuracy, precision, recall, and F1-score.
## Deployment

## Azure Cloud:
Containerize the application using Docker.
Push the Docker image to Azure Container Registry.
Deploy the containerized application to Azure Web App.
Flask Application:
Build a user-friendly interface to interact with the model and test URLs.
GitHub Actions Workflow:
Automate CI/CD pipeline for testing and deployment.
Installation
Follow these steps to set up the project locally:

## Prerequisites
Python 3.8+
Azure CLI installed
Docker installed
GitHub account for CI/CD
Setup
Clone the repository:
git clone [https://github.com/pratham009/network_security](https://github.com/pratham009/network_security.git)
-- cd phishing-detection
## Create a virtual environment and install dependencies:

pip install -r req.txt
## After installing dependencies use 
python app.py in command prompt (run in your virtual environment)
Deployment
Azure Deployment
Build the Docker image:
docker build -t phishing-detection:latest .

Push the image to Azure Container Registry:

az acr login --name your-container-registry
docker tag phishing-detection:latest your-container-registry.azurecr.io/phishing-detection:latest

docker push your-container-registry.azurecr.io/phishing-detection:latest
Deploy to Azure Web App:

az webapp create --resource-group your-resource-group --plan your-app-service-plan --name your-webapp-name --deployment-container-image-name your-container-registry.azurecr.io/phishing-detection:latest

## GitHub Actions Workflow
Configure a .github/workflows/deploy.yml file for CI/CD.
Automate:
Build and test the project.
Push changes to Azure upon successful builds.
Learnings

## During this project, I gained knowledge and experience in:

## Modular Coding Style

Breaking the project into reusable, independent modules.
Data Engineering

Basics concepts of data ingestion, validation, and transformation.

## Model Development

Training and evaluating machine learning models with real-world data.

## Cloud Deployment

Deploying a containerized application on Azure using the Azure Container Registry and Azure Web App.
Flask Development

Building and deploying a web application with Flask.
DevOps Automation

Automating workflows using GitHub Actions.
Usage
Run the Flask application.
Use the web interface to input website URLs.
Get predictions on whether the website is phishing or legitimate.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
If you have any questions or feedback, feel free to reach out:
Email: prathamvichare645@gmail.com
GitHub: pratham009
