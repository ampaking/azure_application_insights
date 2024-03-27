import os
import logging

from fastapi import FastAPI, HTTPException
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from dotenv import load_dotenv

# Load environment variable
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn")

app = FastAPI()

APPLICATIONINSIGHTS_CONNECTION_STRING = os.getenv(
    "APPLICATIONINSIGHTS_CONNECTION_STRING"
)

# Simple validation
assert (
    APPLICATIONINSIGHTS_CONNECTION_STRING
), "APPLICATIONINSIGHTS_CONNECTION_STRING is not set."


try:
    configure_azure_monitor(
        connection_string=APPLICATIONINSIGHTS_CONNECTION_STRING,
    )
    FastAPIInstrumentor.instrument_app(app)
except Exception as e:
    raise HTTPException(
        status_code=500,
        detail=f"Application Insights was not set up properly. {(str(e))}",
    ) from e


@app.get("/health_check")
async def health_check():
    """
    The `health_check` function in Python implements custom logic for performing a health check and
    returns a dictionary with a status message.
    :return: The `health_check` function is returning a dictionary with a key "status" and the value "I
    am ok!!!".
    """

    logger.info("Health check endpoint was called")

    return {"status": "I am ok!!!"}
