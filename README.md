* Steps to run this app
1) Install mysql database to a machine and add db host and port in settings.py
2) Create the database splitwise using `create database splitwise`
3) make a virtualenv using `python3 -m venv ~/venv`
4) activate venv using `source ~/venv/bin/activate`
5) Install requirements using `pip3 install -r requirements.txt`
6) Run migrations using `python manage.py migrate`
7) Run the application using `python manage.py runserver`
8) Using the postman collection `splitwise_postman_collection` 
   * Create a user
   * create group
   * create more users and register users to group
   * Add bills
   * Check the group balances and user balances