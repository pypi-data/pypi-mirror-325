# 5X Google BigQuery Client Authentication Library

This Python library provides a simple way to create a **Google BigQuery client** using either an **access token** or a **service account JSON file**. It handles authentication seamlessly, allowing developers to focus on querying BigQuery.

- **Preferred Authentication:** Access Token (`FIVEX_BIGQUERY_ACCESS_TOKEN`)
- **Fallback Authentication:** Service Account JSON (`FIVEX_BIGQUERY_SERVICE_ACCOUNT_KEY`)

---

## Installation

Install the package from PyPI using:

```bash
pip install 5x-google-bigquery-auth-manager
```

---

## **Environment Variables**

This function relies on **environment variables** for authentication.

| Variable                             | Description                               | Example                         |
| ------------------------------------ | ----------------------------------------- | ------------------------------- |
| `FIVEX_BIGQUERY_ACCESS_TOKEN`        | Access token for authentication           | `ya29.a0AfH6SMA...`             |
| `FIVEX_BIGQUERY_DEFAULT_PROJECT_ID`  | Your BigQuery project ID                  | `your-project-id`               |
| `FIVEX_BIGQUERY_SERVICE_ACCOUNT_KEY` | Path to the service account JSON key file | `/path/to/service_account.json` |

### **Example: Setting Environment Variables**

```bash
export FIVEX_BIGQUERY_ACCESS_TOKEN="your-access-token"
export FIVEX_BIGQUERY_DEFAULT_PROJECT_ID="your-project-id"
export FIVEX_BIGQUERY_SERVICE_ACCOUNT_KEY="/path/to/service_account.json"
```

---

## **Usage**

### **Import and Use in Python**

```python
from bigquery_auth import create_bigquery_client

try:
    client = create_bigquery_client()
    print("✅ BigQuery Client Created Successfully!")
except Exception as e:
    print(f"❌ Error: {e}")
```

---

## **Function Overview**

### **`create_bigquery_client()`**

Creates a **BigQuery client** using either:

1. **Access Token (Preferred)**
2. **Service Account JSON File (Fallback)**

### **How It Works**

✔ **First, tries to authenticate using the access token (`FIVEX_BIGQUERY_ACCESS_TOKEN`).**  
✔ **If the access token is expired or invalid, it raises an exception.**  
✔ **If no access token is available, it attempts authentication via service account JSON.**  
✔ **Implements logging and error handling for seamless debugging.**

---

## **Error Handling**

This function will **raise exceptions** in case of failure:

| Exception            | Cause                                       |
| -------------------- | ------------------------------------------- |
| `ValueError`         | No authentication method found              |
| `RefreshError`       | Access token is expired or invalid          |
| `GoogleAPICallError` | BigQuery API request failure                |
| `BadRequest`         | Insufficient permissions to access BigQuery |

### **Example Handling in Python**

```python
try:
    client = create_bigquery_client()
except RefreshError as e:
    print(f"❌ Token Error: {e}")
except ValueError as e:
    print(f"❌ Configuration Error: {e}")
except GoogleAPICallError as e:
    print(f"❌ BigQuery API Error: {e}")
except BadRequest as e:
    print(f"❌ Permission Error: {e}")
```

---

## **Logging**

This function uses Python’s built-in **`logging`** module to track:

- **Which authentication method is used** (Access Token or Service Account)
- **Errors and exceptions** for easier debugging

---

## **Why Use This Library?**

✔ **Simplifies Google BigQuery authentication** – No need to manage authentication manually.  
✔ **Supports both Access Tokens & Service Account authentication** – Provides flexibility.  
✔ **Ensures proper error handling** – Avoids silent failures with meaningful error messages.  
✔ **Easy to integrate into any project** – Just install and use.

---
