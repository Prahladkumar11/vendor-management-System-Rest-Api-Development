# vendor-management-System-Rest-Api-Development-


Brief description or introduction of your project.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Overview

This web application help to manage the vendor and purchase record.And track the order and measure the performance of every vendor.

## Features

- List key features of your project.

## Requirements

List the requirements needed to run your project, including dependencies and versions.

- Python
- Django
- Django REST Framework

## Installation





https://github.com/Prahladkumar11/vendor-management-System-Rest-Api-Development/assets/96491878/865c19cb-8e1a-4226-9f0b-55503b60a580







Provide step-by-step instructions on how to install and set up your project locally.

```bash
# Clone the repository
git clone https://github.com/Prahladkumar11/vendor-management-System-Rest-Api-Development-.git

# Change to the project directory
cd vendor-management-System-Rest-Api-Development-

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```
## API Endpoints

### Vendors
```bash
- **GET /api/vendors/**
  - Retrieve all vendors.

- **GET /api/vendors/{vendor_id}/**
  - Retrieve a specific vendor.

- **PUT /api/vendors/{vendor_id}/**
  - Update a specific vendor.

- **DELETE /api/vendors/{vendor_id}/**
  - Delete a specific vendor.

- **GET /api/vendors/{vendor_id}/purchaseOrders/**
  - Retrieve all purchase orders for a specific vendor.
```
### Purchase Orders
```
- **GET /api/purchaseOrders/**
  - Retrieve all purchase orders.

- **GET /api/purchaseOrders/{purchaseOrder_id}/**
  - Retrieve a specific purchase order.

- **PUT /api/purchaseOrders/{purchaseOrder_id}/**
  - Update a specific purchase order.

- **DELETE /api/purchaseOrders/{purchaseOrder_id}/**
  - Delete a specific purchase order.
```
### Historical Performances
```
- **GET /api/performances/**
  - Retrieve all historical performances.

- **GET /api/performances/{performance_id}/**
  - Retrieve a specific historical performance.

- **PUT /api/performances/{performance_id}/**
  - Update a specific historical performance.

- **DELETE /api/performances/{performance_id}/**
  - Delete a specific historical performance.
```
### Vendor Historical Performance
```
- **POST /api/vendors/{vendor_id}/performance/**
  - Retrieve historical performance data for a specific vendor.



