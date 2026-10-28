# swe1-app

[![Build Status](https://app.travis-ci.com/jjeong4335/swe1-app.svg?branch=main)](https://app.travis-ci.com/jjeong4335/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/jjeong4335/swe1-app/badge.svg?branch=main)](https://coveralls.io/github/jjeong4335/swe1-app?branch=main)

Django polls app (official tutorial, parts 1-4) deployed to AWS Elastic Beanstalk.

## Run locally

    python -m venv venv && source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Then open http://127.0.0.1:8000/polls/
