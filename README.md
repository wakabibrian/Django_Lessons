# Django_Lessons

## What is Django?

- Django is a Python web framework
- It is a backend framework (Server side framework)
- It has packages and modules for the designs
- It is a heavy weight framework (Bateries included) unlike light weight frameworks like Flask
- It uses the MVT Design pattern (Model-View-Template)

## What is a Web Framework?

It is collection of modules, packages, and libraries designed to speed up web development

- No need to start building code from scratch

## What can you build with Django?

- Ecommerce websites
- Social App
- API for a mobile App
- Etc

Building APIs with django is easy. It has the Django REST framework.

- Rest framework help build Dajango rest APIs

## Other Python Frameworks

- Flask (More light weight)
- Cherry Pie
- Web2py
- Pyramid

## MVT Design Pattern

<img src="Resources/Mvt.png" alt= "MVT Design Pattern" width="600" />

**Model** - Data Access Layer (How we model data with the data base). Data base tables built out with classes
**Templates** - Presentation Layer. This is what the user sees (Web page)
**sView** - Business logic.
MVT design pattern is very similar to MVC

## Django Installation and Setup

- Install python (From python.org)
- Select part on a computer (folder) where you want to install
- Install Django. First create a **virtual environment** and download Django into the virtual environment
- Virtual environment is a way of creating different environments for all of our downloads and installs so that we do not have any conflicts with our projects
- _pip list_ shows all the python packages available grobally or in a chosen virtual environment
- Virtual environments helps in projects management (Being updated with the latest versions of django) keeping the projects which worked with the other versions. To avoid conflicts when installed globally

- **To install virtual environment:** _pip install virtualenv_ Package for installing virtual environments

- **To Create a Virtual Environment:** _virtualenv < virtual_environment_name >_
- Start/activate the virtual environment (bash terminal): _source < virtual_environment_name >/scripts/activate_
- To deactivate the virtual environment: _deactivate_
- _pip list_ - shows all the list of packages installed in that environment

- **To install Django** (pip install django) (while in the virtual environment)
- **To check django list of command:** _django-admin_
