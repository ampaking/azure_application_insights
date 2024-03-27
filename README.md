# FastAPI Application with Azure Application Insights Integration

This repository contains a FastAPI application that is integrated with Azure Application Insights for enhanced observability and monitoring. It showcases how to set up basic telemetry, including custom logging, within a Python web application.

## Prerequisites

- Python 3.7+
- An Azure account
- Azure Application Insights resource

## Setting Up

1. **Clone the Repository**

   ```bash
   git clone `project`
   cd `<repository-name>`
   ```

2. **Install Dependencies**

   Create a virtual environment and activate it:

   ```bash
   python -m venv .venv

   Mac or Linux:
   source .venv/bin/activate

   Windows:
   .\.venv\Scripts\activate
   ```

   Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**

   Copy the `.env.example` file to a new file named `.env`, and fill in the `APPLICATIONINSIGHTS_CONNECTION_STRING` with your Azure Application Insights connection string.

   ```plaintext
   APPLICATIONINSIGHTS_CONNECTION_STRING=<your_connection_string>
   ```

## Running the Application

To run the application locally, use the following command:

```bash
uvicorn main:app --reload
```
