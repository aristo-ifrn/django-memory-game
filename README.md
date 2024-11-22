<p id="title" align="center">
  <a href="#title">
    <img width="80" height="80" src="./.github/logo.png">
    <h1 align="center">Django Memory Game</h1>
  </a>
</p>

<p align="center">
  <a aria-label="Made By Aristofany Herderson" href="https://github.com/aristofany-herderson/">
    <img src="https://img.shields.io/badge/MADE%20BY%20Aristofany%20Herderson-000000.svg?style=for-the-badge&labelColor=000&logo=starship&logoColor=fff&logoWidth=20">
  </a>
  <a aria-label="Project version" href="https://github.com/aristofany-herderson/django-memory-game">
    <img alt="Version" src="https://img.shields.io/badge/VERSION-1.0.0-000000.svg?style=for-the-badge&labelColor=000">
  </a>
  <a aria-label="License" href="./license.md">
    <img alt="License" src="https://img.shields.io/badge/LICENSE-MIT-000000.svg?style=for-the-badge&labelColor=000">
  </a>
  <a aria-label="Built with Django" href="https://www.djangoproject.com/">
    <img alt="Django" src="https://img.shields.io/badge/BUILT%20WITH%20DJANGO-000000.svg?style=for-the-badge&labelColor=000&logo=django&logoColor=fff&logoWidth=20">
  </a>
</p>

<p align="center">🧠 A memory game integrated with Django to track and save player results in a database.</p>

<br>

## 🧪 Technologies

This project was developed using the following technologies:

- [Python 3.8+](https://www.python.org/)
- [Django 4.0+](https://www.djangoproject.com/)
- [SQLite](https://www.sqlite.org/index.html) 

<br>

## 🧑🏻‍💻 Getting Started

#### Clone the project and access the root folder:

```bash
$ git clone https://github.com/aristo-ifrn/django-memory-game
$ cd django-memory-game
```

#### Setting up the environment:

1. Install the dependencies:

```bash
$ pip install -r requirements.txt
```

2. Run the migrations to set up the database:
```bash
$ python manage.py migrate
```

3. Start the server:

```bash
$ python manage.py runserver
```

Access the application in your browser at http://127.0.0.1:8000/.

<br>

## 💻&nbsp; Project

**Resume:** 🧠 A Django-powered memory game application where players' results, including flips, time, and completion status, are saved and displayed in a ranking system.

#### 🎨&nbsp; Project Structure
- ```templates/:``` HTML templates for the frontend (index.html, game.html, ranking.html).
- ```views.py:``` Defines the logic for handling game, ranking, and API endpoints.
- ```models.py:``` Contains the Player model to store player data in the database.
- ```urls.py:``` Maps application routes to views.
- ```static/:``` Contains CSS, JavaScript, and other static assets.

#### 🚀&nbsp; Features

- [x] Play the memory game and track player performance.
- [x] Save game results (username, flips, time, and completion status) to a database.
- [x] View a ranking of players based on game performance.
- [x] Expose API endpoints for fetching and adding player data.

<br />

## 📚 API Endpoints

- GET ```/get/```

Returns a JSON response with all player results, ordered by completion status, flips, and time.

- POST ```/add/```

Accepts JSON data to create a new player result.

```json
{
  "username": "JohnDoe",
  "flips_quantity": 15,
  "used_time": 120,
  "date": "2024-11-22T12:34:56",
  "has_completed": true
}
```

<br>

## 🧑🏻&nbsp; Author

<p align="center">
  <img width="140px" src="https://images.weserv.nl/?url=github.com/aristofany-herderson.png?v=4&h=300&w=300&fit=cover&mask=circle&maxage=7d" alt="aristofany-herderson">
  <p align="center">
    Aristofany Herderson
  </p>
  <p align="center">
    <a  href="https://www.linkedin.com/in/aristofany-herderson/" target="_blank">
    <img align="center" src="https://img.shields.io/badge/LINKEDIN-000000.svg?style=for-the-badge&labelColor=0a66c2&logo=linkedin&logoColor=fff&logoWidth=20" alt="linkedin"/>
    </a>
    <a href="https://twitter.com/aristofanyherde" target="_blank">
      <img align="center" src="https://img.shields.io/badge/TWITTER-000000.svg?style=for-the-badge&labelColor=1d9bf0&logo=x&logoColor=fff&logoWidth=20" alt="linkedin"/>
    </a>
    <a href="https://www.instagram.com/aristofany_herderson/" target="_blank">
      <img align="center" src="https://img.shields.io/badge/INSTAGRAM-000000.svg?style=for-the-badge&labelColor=dd326f&logo=instagram&logoColor=fff&logoWidth=20" alt="linkedin"/>
    </a>
  </p>
</p>

<br>
