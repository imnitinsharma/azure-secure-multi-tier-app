import os
from fastapi import FastAPI
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = FastAPI(title="Secure Azure Multi-Tier Backend")

KEY_VAULT_NAME = os.environ.get("KEY_VAULT_NAME")

@app.get("/api/vault-check")
def check_vault_secret():
    if not KEY_VAULT_NAME:
        return {"status": "error", "message": "KEY_VAULT_NAME env not configured"}

    vault_url = f"https://{KEY_VAULT_NAME}.vault.azure.net"
    # Automatically authenticates via Azure Managed Identity (No passwords in code)
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)

    # Retrieve a secret dynamically
    secret = client.get_secret("db-connection-string")
    return {"status": "success", "secret_retrieved": True}