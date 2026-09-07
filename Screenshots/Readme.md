# Project Visual Documentation & Proof of Work

This directory contains the sequential, step-by-step verification screenshots documenting the infrastructure provisioning, pipeline execution, and cloud validation for the **Azure Secure Multi-Tier Application & DevSecOps Pipeline**.

---

## Verification Screenshot Index

| Step | File Name | Description |
| :--- | :--- | :--- |
| **01** | `01-terraform-provisioning.png` | Successful execution of Terraform infrastructure-as-code deployment (`terraform apply`), creating the isolated cloud stack and verifying resources via Azure CLI. |
| **02** | `02-azure-portal-resources.png` | Azure Portal view of the resource group (`rg-devsecops-lab`), confirming the correct provisioning of the App Service Plan, App Service, and Virtual Network. |
| **03** | `03-github-actions-secrets.png` | Secure configuration of repository credentials (`AZURE_CREDENTIALS`) within GitHub Actions settings to enable passwordless pipeline access. |
| **04** | `04-github-actions-pipeline.png` | GitHub Actions workflow execution history demonstrating successful automated build, container security scanning (Trivy), and deployment stages. |
| **05** | `05-fastapi-docs.png` | Live FastAPI Swagger UI documentation endpoint (`/docs`) successfully deployed and accessible over Azure App Service. |
| **06** | `06-vault-check-success.png` | Live API verification response (`/api/vault-check`), confirming passwordless authentication via Managed Identity and successful dynamic retrieval of secrets from Azure Key Vault. |
