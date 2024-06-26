# Click Tracker

Click Tracker is a Django application designed to track user clicks on a link. It records user data such as IP address,
browser, and the time of the click in a database. This project allows you to implement a server backend that processes
GET requests, redirects users to another page, and stores their data.

## Getting Started

To get started with Click Tracker, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Accult/click_tracker.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd click_tracker
   ```

3. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment:**
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

5. **Install Django and other dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Create and Configure .env File**
    - Create a `.env` file based on the `.env-example` template.
    - Fill in the required environment variables such as database credentials and encryption keys.


7. **Migrate the database:**
   ```bash
   python manage.py migrate
   ```

8. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

9. . **Run the development server:**
   ```bash
   python manage.py runserver
   ```

You can view user data by accessing the admin panel at `/admin`.
Also, on the /admin page, in the RedirectData section, you can specify the url for redirection, the one that was saved
last will be relevant

Enjoy! 🚀
