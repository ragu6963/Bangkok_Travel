# url = "https://www.google.com/maps/@27.1739164,78.0432149,3a,75y,264.8h,97.86t/data=!3m7!1e1!3m5!1sBKlPm5OH6iuzNr2HoNQxjA!2e0!3e5!7i13312!8i6656?hl=ko"
# lst = url.split(",")
# lat = lst[0].split("@")[1]
# lng = lst[1]
# pitch = lst[4].replace("h", "")
# heading = lst[5].split("t")[0]
# print(lst)
# print(lat, lng, pitch, heading)
import requests

MAPS_API_KEY = "AIzaSyDs_7L7DY1NhNiII1fe29gZ4Ap4-ZKyw4Y"
static_image = requests.get(
    f"https://maps.googleapis.com/maps/api/streetview?size=400x400&location=11.0,11.0&fov=80&key=AIzaSyDs_7L7DY1NhNiII1fe29gZ4Ap4-ZKyw4Y"
)
static_image = requests.get(
    f"https://maps.googleapis.com/maps/api/streetview?size=400x400&location=27.1739164,78.0432149&fov=80&pitch=7.859999999999999&heading=264.8&key=AIzaSyDs_7L7DY1NhNiII1fe29gZ4Ap4-ZKyw4Y"
)
print(static_image)
with open("hyderabad.png", "wb") as file:
    file.write(static_image.content)