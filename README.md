# Management Information System for Church Operations

This project is a comprehensive web-based system designed to streamline and manage various aspects of church operations. It provides tailored functionalities for administrators, members, and the public through role-based access. The system facilitates efficient event management, document handling, financial tracking, and community engagement while ensuring a secure and user-friendly experience.

### Technology Stack

Backend: Django (Python)

Database: SQLite

Frontend: HTML5, CSS3, Bootstrap, JavaScript, jQuery

Libraries: FullCalendar (for event scheduling)


## Installation Setup 

1. Clone the repository
2. Navigate to the project directory
3. Create and activate a virtual environment
   
    <sub>python -m venv venv <sub>
   
    <sub>venv\Scripts\activate   _(Window)_<sub>
   
    <sub>source venv/bin/activate<sub>

4. Install the required dependecies

   <sub>pip install -r requirements.txt<sub>

5. Apply database migrations

   <sub>python manage.py migrate<sub>

6. Run the development server

   <sub>python manage.py runserver<sub>

7. Access the system via your browser at _http://127.0.0.1:8000/_ .



