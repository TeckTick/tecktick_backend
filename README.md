

## Tecktick Backend

This is the backend for the Tecktick project. It is a RESTful API built with django and django rest framework.

## Folder Structure

    ├──techtick-backend (root folder)

            ├── base (base of our project. Contains     settings, urls, wsgi, etc)
            |
            ├── home (contains the logic for landing page data such as testimonials, team, etc)
            |
            ├── blog (contains the logic for blog)
            |
            (...) (other apps)

## Endpoints
    /resources/ - GET, POST 

    /resources/<int:pk>/ - GET, PUT, DELETE

## Installation

1. Clone the repository

      ```bash
    git clone ' our repo link'

    cd techtick-backend
    ```
2. Create a virtual environment

    ```bash
    python3 -m venv venv (for linux)  (or whatever version of python you have installed)

    python -m venv venv (for windows)

    source venv/bin/activate (for linux)

    venv\Scripts\activate (for windows)
    ```

3. Install the requirements

    ```bash
    pip install -r requirements.txt
    ```

4. Run the server
    
    ```bash
    python manage.py runserver
    ```

## Pushing to the repository

1. Create a new branch
2. Make your changes
3. Add and commit your changes
4. Push your changes to the branch
5. Create a pull request


## After installing any new package

```bash
pip freeze > requirements.txt
```

This will update the requirements.txt file with the new package you installed so that others can install it as well.

