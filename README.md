# Click Tracker

Click Tracker is a Django application designed to track user clicks on a link. It records user data such as IP address, browser, and the time of the click in a database. This project allows you to implement a server backend that processes GET requests, redirects users to another page, and stores their data.

## Getting Started

To get started with Click Tracker, follow these steps:

1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd click_tracker`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
   - On macOS/Linux: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`
5. Install Django and other dependencies: `pip install -r requirements.txt`
6. Create a `.env` file in the project directory.
7. Customize the .env file using the template from .env-example
8. Migrate the database: `python manage.py migrate`
9. Run the development server: `python manage.py runserver`


Enjoy your usage 🙃
