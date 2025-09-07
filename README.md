# 🌤️ Django Weather App

A simple Django web app to search for current weather data using the
OpenWeather API.\
Supports search history, dynamic backgrounds, and Celsius temperature
units.

------------------------------------------------------------------------

## 🚀 Features

-   Search weather by city name
-   Display temperature, feels-like, humidity, pressure, wind,
    sunrise/sunset
-   City search history (last 10 searches)
-   Dynamic weather icons and descriptions
-   Secure API key management with `.env`

------------------------------------------------------------------------

## 🛠️ Installation & Setup

### 1. Clone the repository

``` bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

### 2. Create a virtual environment

``` bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Create `.env` file

Create a `.env` file in the project root (next to `manage.py`):

    OPENWEATHER_API_KEY=your_api_key_here

👉 You can get a free API key from
[OpenWeather](https://home.openweathermap.org/api_keys).

### 5. Apply migrations

``` bash
python manage.py migrate
```

### 6. Run the server

``` bash
python manage.py runserver
```

Now open your browser at `http://127.0.0.1:8000/` 🎉

------------------------------------------------------------------------

## ⚙️ Project Structure

    weather-app/
    ├── weather/               # Django app with views/templates
    │   ├── views.py
    │   └── templates/weather/
    │       └── index.html
    ├── project_name/          # Django project folder (settings, urls)
    ├── manage.py
    ├── .env.example           # Example environment file
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## 🔐 Security Notes

-   **Never commit your real `.env` file.** It contains secrets.
-   The `.env.example` file is provided as a template.
-   If an API key is ever exposed, rotate it immediately (delete old
    one, create new).

------------------------------------------------------------------------

## 👤 Author

Maintained by [OmAr1dev](https://github.com/OmAr1dev/django-weather-app)

------------------------------------------------------------------------

## 📝 License

This project is open-source and available under the [MIT
License](LICENSE).
