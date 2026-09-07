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
