from datetime import datetime

import requests
from django.conf import settings
from django.shortcuts import redirect, render


def weather_view(request):
    """
    Weather view with search history and dynamic backgrounds (Celsius only).
    """
    weather_data = None
    history = request.session.get("history", [])

    # Handle delete request
    if request.method == "POST" and request.POST.get("delete_index") is not None:
        index = int(request.POST.get("delete_index"))
        if 0 <= index < len(history):
            history.pop(len(history) - 1 - index)  # reverse order
            request.session["history"] = history
        return redirect("weather_view")

    if request.method == "POST" and request.POST.get("city"):
        city = request.POST.get("city")

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "name": data["name"],
                "temp": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "description": data["weather"][0]["description"],
                "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
                "wind_speed": data["wind"]["speed"],
                "wind_deg": data["wind"].get("deg", 0),
                "clouds": data["clouds"]["all"],
                "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime(
                    "%H:%M"
                ),
                "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime(
                    "%H:%M"
                ),
                "coord": data["coord"],
            }

            # Save to history
            history.append(
                {"city": city, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            )
            request.session["history"] = history[-10:]  # keep last 10

        else:
            weather_data = {"error": response.json().get("message", "City not found")}

    context = {
        "weather_data": weather_data,
        "history": history[::-1],  # most recent first
    }
    return render(request, "weather/index.html", context)
