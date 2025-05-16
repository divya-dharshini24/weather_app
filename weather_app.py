import tkinter as tk
import requests  
root = tk.Tk()
root.title("Weather App")
label = tk.Label(root, text="City Name")
label.pack()
cityentry = tk.Entry(root)
cityentry.pack()
def getweather():
    city = cityentry.get().strip()
    if city == "":
        resultlabel.config(text="Please enter the city name")
        return
    api_key = "7c8ebfac7b48697758dda4e589f44e32" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("cod") == 200: 
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            resultlabel.config(text=f"Temperature: {temp}°C\nDescription: {description}\nHumidity: {humidity}%")
        else:
            resultlabel.config(text="City not found. Please try again.")
    
    except requests.exceptions.RequestException:
        resultlabel.config(text="Error: Unable to fetch weather data.")
button = tk.Button(root, text="Get Weather", command=getweather)
button.pack()
resultlabel = tk.Label(root, text="")
resultlabel.pack()
root.geometry("400x250")
root.config(bg="#4c8bf5")
label.config(font=("Arial", 15), bg="#4c8bf5", fg="white")
cityentry.pack(pady=6)
button.config(font=("Arial", 13), bg="#0073e6", fg="white")
resultlabel.config(font=("Arial", 12), bg="#4c8bf5", fg="white")
root.mainloop()
