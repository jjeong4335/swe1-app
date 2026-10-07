# swe1-app

Django polls app (official tutorial, parts 1-4) deployed to AWS Elastic Beanstalk.

## Run locally

    python -m venv venv && source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Then open http://127.0.0.1:8000/polls/
