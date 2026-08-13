# 📷 Infrastructure & Verification Screenshots

This directory contains visual proof of deployment, configuration, and end-to-end testing for the multi-tier Azure infrastructure lab.

---

## 🗺️ Architecture Overview

![Azure Multi-Tier Architecture](01-azure-architecture.png)

---

## 🌐 1. Network & Subnet Setup

### Virtual Network & Subnets
Configuration showing the VNet address space (`10.0.0.0/16`) divided into public, backend-private, and database subnets.
![VNet Subnets](02-vnet-subnets.png.png)

---

## 🖥️ 2. Compute Resources & Resource Group Inventory

### Public Web VM (`vm-web-01`)
Overview blade showing running status, public IP assignment, and subnet association.
![Web VM Overview](03-web-vm.png.png)

### Resource Group Inventory (`rg-cloud-security-lab`)
Complete resource group view displaying all provisioned Azure assets (NAT Gateway, Disks, NICs, and VMs).
![Resource Group Inventory](04-resource-group-overview.png.png)

---

## 🛡️ 3. Network Security Groups (NSG)

### All Security Groups Summary
List of all Network Security Groups controlling tier isolation (`nsg-web-public`, `nsg-backend-private`, `nsg-db-private`).
![NSG Overview List](09-nsg-overview-list.png.png)

### Web Tier Inbound Rules
Inbound security rules enforcing SSH restricted to administrative IP and allowing public HTTPS traffic.
![NSG Web Rules](05-nsg-web-rules.png.png)

---

## 🧪 4. Testing & Verification

### Backend API Local Test
Verification using Azure Run Command showing Gunicorn active and Flask API responding locally on port 5000 (`200 OK`).
![Backend API Test](06-backend-api-test.png.png)

### Inter-Tier Network Connectivity Test
PowerShell `Test-NetConnection` verifying successful TCP reachability between tiers over private networking.
![Connectivity Test](07-web-backend-private-test.png.png)

### Final Live Application UI
Frontend web application rendering live data queried from the private backend tier and database.
![Final Web Application](08-final-application.png.png)
