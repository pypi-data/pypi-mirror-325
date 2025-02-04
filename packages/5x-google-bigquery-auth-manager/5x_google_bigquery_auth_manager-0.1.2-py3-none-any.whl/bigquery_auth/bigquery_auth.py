import os
import logging
from google.cloud import bigquery
from google.oauth2 import credentials
from google.oauth2.service_account import Credentials
from google.api_core.exceptions import GoogleAPICallError, BadRequest
from google.auth.exceptions import RefreshError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_bigquery_client():
    """
    Creates a BigQuery client using either:
    1. An access token (preferred).
    2. A service account JSON file (fallback).

    Returns:
        bigquery.Client: A BigQuery client object if successful.

    Raises:
        ValueError: If no valid authentication method is found.
        RefreshError: If the access token is expired or invalid.
        GoogleAPICallError: If a general API error occurs.
        BadRequest: If access is denied due to permissions issues.
    """
    access_token = os.environ.get('FIVEX_BIGQUERY_ACCESS_TOKEN')
    project_id = os.environ.get('FIVEX_BIGQUERY_DEFAULT_PROJECT_ID')
    service_account_path = os.environ.get('FIVEX_BIGQUERY_SERVICE_ACCOUNT_KEY')

    if access_token and project_id:
        try:
            logger.info("Using Access Token for authentication.")
            creds = credentials.Credentials(access_token)
            client = bigquery.Client(credentials=creds, project=project_id)
            
            # Test the credentials to catch expired tokens
            client.query("SELECT 1").result()  # A simple test query to validate token
            
            return client
        
        except RefreshError as e:
            logger.error("Access Token has expired or is invalid.")
            raise RefreshError("The provided access token has expired or is invalid. Please refresh the token.")
        except GoogleAPICallError as e:
            logger.error(f"BigQuery API error (Access Token): {e.message}")
            raise GoogleAPICallError(f"BigQuery API error: {e.message}")
        except BadRequest as e:
            logger.error("Access Denied: Your account does not have access to this BigQuery project.")
            raise BadRequest("Access Denied: Your account does not have access to this BigQuery project.")

    elif service_account_path and os.path.exists(service_account_path):
        try:
            logger.info(f"Using Service Account JSON: {service_account_path}")
            creds = Credentials.from_service_account_file(service_account_path)
            client = bigquery.Client(credentials=creds, project=creds.project_id)
            return client
        except GoogleAPICallError as e:
            logger.error(f"BigQuery API error (Service Account): {e.message}")
            raise GoogleAPICallError(f"BigQuery API error: {e.message}")
        except BadRequest as e:
            logger.error("Access Denied: Service account does not have the required permissions.")
            raise BadRequest("Access Denied: Service account does not have the required permissions.")
        except Exception as e:
            logger.error(f"Unexpected error loading service account JSON: {str(e)}")
            raise ValueError(f"Unexpected error loading service account JSON: {str(e)}")

    else:
        logger.error("Neither Access Token nor Service Account credentials are available.")
        raise ValueError("No authentication method found. Please provide either an access token or a service account JSON file.")