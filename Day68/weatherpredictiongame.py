import random

def weather():
    weather_options = ["Sunny", "Rainy", "Cloudy", "Windy"]

    prediction = input("Predict the weather: ").capitalize()

    actual = random.choice(weather_options)

    print("Actual Weather:", actual)

    if prediction == actual:
        print("Correct Prediction!")

    else:
        print("Better Luck Next Time!")

weather()