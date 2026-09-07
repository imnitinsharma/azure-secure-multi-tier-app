# Secure Multi-Tier Cloud Application & DevSecOps Pipeline

An enterprise-aligned, secure-by-design multi-tier cloud application built with **FastAPI**, containerized via **Docker**, provisioned using **Infrastructure as Code (Terraform)**, and protected via zero-trust cloud security principles and automated DevSecOps pipelines. 

This project demonstrates practical competency in modern secure software development lifecycle (SSDLC) standards, cloud architecture, and security automation:
* **Least Privilege (PoLP)**: Restricting runtime access boundaries so application identities only hold explicit required permissions (`get`, `list`) via Microsoft Entra ID.
* **Defense-in-Depth**: Multi-layered security covering container vulnerability scanning, infrastructure-as-code automation, and cloud-native secret isolation.
* **Identity Federation**: Completely eliminating hardcoded credentials using token-based authentication (`DefaultAzureCredential`).

---

## Tech Stack & Core Libraries

| Domain | Technology / Tool | Purpose in Project |
| :--- | :--- | :--- |
| **Backend Framework** | Python, FastAPI, Uvicorn | High-performance asynchronous API engine |
| **Azure Python SDKs** | `azure-identity`, `azure-keyvault-secrets` | Programmatic secure token management and Key Vault integration |
| **Infrastructure (IaC)** | Terraform, Azure CLI | Automated, version-controlled cloud resource lifecycle management |
| **Containerization** | Docker | Immutable application packaging and runtime isolation |
| **Security Scanning** | Trivy (Open Source) | Automated static vulnerability and dependency scanning for container images |
| **Cloud & IAM** | Microsoft Azure, Entra ID | Enterprise hosting, system-assigned managed identities, and Key Vault |
| **CI/CD Automation** | GitHub Actions (`.yml`) | Automated build, security scan, and deploy pipelines |

---

## Architecture & Security Workflow

```text
[ Git / Developer ] 
       │
       ▼ (CI/CD Pipeline via GitHub Actions .yml)
[ Trivy Scanner ] ──(Scans Docker image for CVEs & vulnerabilities)
       │
       ▼
[ Docker Hub / ACR ] ──(Immutable Container Image)
       │
       ▼
[ Azure App Service ] ──(Authenticates via Microsoft Entra ID Managed Identity)
       │
       ▼
[ Azure Key Vault ] ──(Enforces Least-Privilege Access Policy -> Returns Secret)


'''text

markdown_content = """# Project Structure & Component Breakdown

* **`app.py`**: The core FastAPI backend. It utilizes Python's `azure-identity` and `azure-keyvault-secrets` libraries to authenticate securely via Managed Identity and fetch runtime secrets, featuring a robust fallback error-handling pattern for high availability.
* **`Dockerfile`**: Defines the immutable container runtime environment, packaging FastAPI and its dependencies securely for cloud execution.
* **`main.tf` (Terraform)**: Infrastructure as Code declarations that provision and configure the cloud stack (Resource Groups, App Service Plans, Key Vaults) reproducibly without manual portal configurations.
* **`.github/workflows/*.yml` (CI/CD Pipeline)**: Automates the build and deployment pipeline. It triggers on code pushes, invokes Trivy to scan the container image for vulnerabilities, and deploys the verified build to Azure.

---

# Security Implementation Summary

* **Supply Chain Security**: Every code push triggers a CI/CD pipeline where Trivy inspects the Docker container image for security vulnerabilities before deployment.
* **Passwordless Authentication**: The application avoids storing static database strings by requesting dynamic tokens through Microsoft Entra ID and `DefaultAzureCredential`.
* **Strict Access Control**: Cloud-level Key Vault policies restrict the application's runtime Object ID strictly to get and list operations, ensuring complete isolation of sensitive data.

---

# Proof of Work & Implementation Screenshots

### 1. Infrastructure Provisioning (Terraform & Azure CLI)
Successful execution of Terraform state application and verification of deployed Azure cloud resources within the isolated resource group.

### 2. CI/CD Pipeline Automation (GitHub Actions & Secrets)
Configured secure pipeline credentials and verified successful workflow execution stages (build, scan, deploy).

### 3. Live Application & Secure Secret Verification
FastAPI documentation endpoint deployed live on Azure App Service, returning a successful passwordless vault verification response.
"""

with open("project_summary.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)

print("Markdown file created successfully.")
