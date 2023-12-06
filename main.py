def weather_predictor(T, H, w):
    W = (0.5 * (T**2)) - (0.2 * H) + (0.1 * w) - 15
    print(W)
    if W > 300:
        return "Sunny"
    elif 200 < W <= 300:
        return "Cloudy"
    elif 100 < W <= 200:
        return "Rainy"
    else:
        return "Stormy"


t = float(input("Enter temperature(in celsius) : "))
h = float(input("Enter humidity (in %): "))
ws = float(input("Enter wind speed (in kmph): "))

print(weather_predictor(t, h, ws))


