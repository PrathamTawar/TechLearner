# TechLearners - Online Course Platform

TechLearners is an online course platform where users can browse through various tech courses, view detailed course information, and enroll in them. It is built using Django and showcases essential features such as media handling (images and videos), dynamic content rendering, and a user-friendly interface.

---

## Features

- **Course Listing**: Browse all available courses with details like name, description, tutor name, price, and duration.
- **Course Details Page**: View in-depth details of each course with images and video support.
- **Media Handling**: Supports both URL-based and locally uploaded images/videos for courses.
- **Dynamic Content**: Courses are fetched and displayed dynamically using Django's templating system.

---

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, basic JavaScript
- **Database**: SQLite (default, configurable)
- **Media Management**: Django's `ImageField` and `FileField`

---

## Installation

### Prerequisites

- Python 3.6 or later
- Django 4.x or later

### Steps to Install and Run Locally

1. **Clone the Repository**:
   ```
   git clone https://github.com/PrathamTawar/TechLearner.git
   cd techlearners
   ```
2. **Create a Virtual Environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```
3. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```
4. **Apply Migrations:**
   ```
   python manage.py migrate
   ```
5. **Create a Superuser (optional):**
   ```
   python manage.py createsuperuser
   ```
6. **Run the Development Server:**
   ```
   python manage.py runserver
   ```
7. Access the App: Open your browser and go to http://127.0.0.1:8000/ or follow the link in terminal

---

## Directory Structure
```
  techlearners/
  ├── courses/               # App for handling courses
  │   ├── migrations/        # Database migrations
  │   ├── models.py          # Course model
  │   ├── views.py           # Course views
  │   ├── templates/         # HTML templates
  │   ├── urls.py            # App-specific URL patterns
  ├── techlearners/          # Main project folder
  │   ├── settings.py        # Project settings
  │   ├── urls.py            # Project-wide URL patterns
  ├── manage.py              # Django management script
  ├── requirements.txt       # Python dependencies
  ├── README.md              # Project documentation
```

---

## Usage
1.**Home Page:** Displays featured courses with their posters, descriptions, and prices.

2.**Courses Page:** Lists all available courses in a grid layout with detailed information.

3.**Course Details Page:** Provides course-specific details, including duration, price, tutor name, and a promotional video.

---

## Media Configuration
1. Ensure proper configuration of `MEDIA_URL` and `MEDIA_ROOT` in your `settings.py`:
```
  # settings.py
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
```
2. In development, serve media files by adding this to your `urls.py`:
```
  from django.conf import settings
  from django.conf.urls.static import static

  if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### Contributing
1. Fork the Repository.
 
2. Create a Feature Branch:
```
  git checkout -b feature/your-feature
```
3. Commit Changes:
```
  git commit -m "Add your message here"
```
4. Push to GitHub:
```
  git push origin feature/your-feature
```
5.Submit a Pull Request.

---

### Bug Reports & Feature Requests
## If you encounter any issues or have suggestions for improvement, please open an issue on GitHub.
