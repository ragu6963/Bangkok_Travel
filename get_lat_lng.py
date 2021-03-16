url = "https://www.google.com/maps/@27.1739164,78.0432149,3a,75y,264.8h,97.86t/data=!3m7!1e1!3m5!1sBKlPm5OH6iuzNr2HoNQxjA!2e0!3e5!7i13312!8i6656?hl=ko"
lst = url.split(",")
lat = lst[0].split("@")[1]
lng = lst[1]
print(lat, lng)
