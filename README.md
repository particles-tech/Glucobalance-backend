### Introduction

Welcome to the project called Glucometer built using **Flutter** for the frontend, **Django** for the backend, and **SQlite** for the database.
This project is part of our major project.

**This repo only contain backend code.**


## Table of Content
- [Table of Content](#table-of-content)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites \[For Backend\]](#prerequisites-for-backend)
- [Cloning the Project](#cloning-the-project)
- [Setting up the Backend](#setting-up-the-backend)
    - [1. Navigate to Backend folder:](#1-navigate-to-backend-folder)
    - [2. Create Virtual Environment and activate:](#2-create-virtual-environment-and-activate)
    - [3. Install dependencies:](#3-install-dependencies)
    - [5. Apply migrations:](#5-apply-migrations)
    - [6. Create a superuser (for admin panel access):](#6-create-a-superuser-for-admin-panel-access)
    - [7. Run the Django development server:](#7-run-the-django-development-server)
- [Running the Project](#running-the-project)
- [Contributing](#contributing)

## Features

- User authentication (login, signup)
- Product listing, search, and filters
- Shopping cart and checkout functionality
- Admin panel for product and order management

## Technologies Used

- **Frontend**:Flutter
- **Backend**: Django, Django REST Framework
- **Database**: SQlite

## Prerequisites [For Backend]

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)

## Cloning the Project

To clone this repository, run the following command in your terminal:

```bash
git clone https://github.com/Mandakini-S/Glucobalance.git


```

## Setting up the Backend

#### 1. Navigate to Backend folder:
```bash
cd Glucobalance/major_project/
```
#### 2. Create Virtual Environment and activate:

```bash

python3 -m venv .venv
# for Linux/macOS
source .venv/bin/activate 
 # for Windows
.\.venv\Scripts\Activate.ps1

```


#### 3. Install dependencies:
```bash
pip install -r requirements.txt
```
#### 4. Install django
```bash
python3 -m  pip install django  
```

#### 5. Apply migrations:
```bash
python3 manage.py migrate
```

#### 6. Create a superuser (for admin panel access):
```bash
python3 manage.py createsuperuser

```

#### 7. Run the Django development server:
```bash
python3 manage.py runserver

```

## Running the Project
To run the project, ensure the **Django** backend servers is running.

Visit http://localhost:8000/admin for the Django admin panel.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit and push your changes (`git commit -m "Add new feature"`).
5. Submit a pull request.

<div align = 'center'><b>Happy coding !</b></div>

