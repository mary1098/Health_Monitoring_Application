**Step-by-Step Guide**

1.Clone the Repository:
Open your terminal or command prompt.
Run the command to clone the repository from GitHub: **git clone https://github.com/mary1098/Health_Monitoring_Application.git**.

2.Create a Virtual Environment:
In the project directory, create a virtual environment by running: **python3 -m venv venv**.
Activate the virtual environment:
On macOS and Linux: **source venv/bin/activate**.
On Windows: **venv\Scripts\activate**.

3.Install Dependencies:
With the virtual environment activated, install the required dependencies by running: **pip install -r requirement.txt**.

4.Apply Migrations:
Run the database migrations to set up your database schema:**python manage.py makemigrations** then **python manage.py migrate**.

5.Run the Development Server:
Start the Django development server to run the application locally: **python manage.py runserver**.
