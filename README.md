# Secure Multi-Tier Web Application on Azure

A hands-on cloud security project demonstrating how to deploy a three-tier web application on Microsoft Azure using network segmentation, private communication, Network Security Groups (NSGs), least privilege and defense-in-depth principles.

The project consists of a public Web tier, a private Backend/Application tier and a private Database tier.

---

## Project Overview

The objective of this project was not simply to deploy a web application to Azure.

The main goal was to understand how cloud networking and security controls can be used to:

- Reduce the application's attack surface
- Separate Internet-facing and internal resources
- Restrict inbound network access
- Apply least-privilege principles
- Keep backend and database resources private
- Control communication between application tiers
- Understand how network architecture affects potential attack paths

This project was built as my first hands-on Cloud Security project.

---

# Architecture

```text
                         INTERNET
                            │
                            │
                       HTTPS / 443
                            │
                            ▼
                 ┌────────────────────┐
                 │      WEB TIER      │
                 │                    │
                 │   Azure Linux VM   │
                 │      Nginx         │
                 │                    │
                 │    10.0.1.x        │
                 │                    │
                 │  Public Subnet     │
                 └─────────┬──────────┘
                           │
                           │ TCP / 5000
                           │ Private Network
                           ▼
                 ┌────────────────────┐
                 │  BACKEND TIER      │
                 │                    │
                 │   Azure Linux VM   │
                 │ Flask + Gunicorn   │
                 │                    │
                 │    10.0.2.x        │
                 │                    │
                 │  Private Subnet     │
                 └─────────┬──────────┘
                           │
                           │ TCP / 3306
                           │ Private Network
                           ▼
                 ┌────────────────────┐
                 │   DATABASE TIER    │
                 │                    │
                 │       MySQL        │
                 │                    │
                 │    10.0.3.x        │
                 │                    │
                 │  Private Subnet    │
                 └────────────────────┘
