from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests  
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try: 
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude) 
        print(result)
        lng=str(location.longitude)
        lat=str(location.latitude)
    
    
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text = current_time)
        name.config(text = "CURRENT WEATHER")
    
        #weather
        api = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lng+"&appid=2ed6ebed26ad8ffd1aa24fd6e7804dcd"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
    
        t.config(text = str(temp) + "°C")
        c.config(text = (condition, "|", "FEELS", "LIKE", temp, "°C"))
    
        w.config(text = str(wind) + "m/s")
        h.config(text = str(humidity) + "%")
        d.config(text = str(description))
        p.config(text = str(pressure) + "hPa")
    
    except Exception as e:
        messagebox.showerror("Error", "Invalid City Name")
        
    
    
    
    
    
    
    
    



#search bar
search_bar  = PhotoImage(file = "search_bar.png")
image_bar= Label(image = search_bar)
image_bar.place(x=20,y=20)

textfield = tk.Entry(root, justify = "center", width = 17, font = ("poppins" ,25, "bold"), bg= "#404040",border =0, fg = "white")
textfield.place(x=50,y=40)
textfield.focus()


search_icon = PhotoImage(file = "search_icon.png")
image_icon= Button(image = search_icon, borderwidth = 0, cursor = "hand2", bg = "#404040", command = getWeather)
image_icon.place(x=400,y=34)

#logo
logo = PhotoImage(file = "logo.png")
image_logo = Label(image = logo)
image_logo.place(x= 150, y= 100)

#Frame(blue)
frame = PhotoImage(file = "frame.png")
image_frame = Label(image = frame)
image_frame.pack(padx = 5, pady =5, side = BOTTOM)

#time
name = Label ( root, font=("arial", 15, "bold"))
name.place(x= 30, y = 100)
clock = Label ( root, font=("Helvetica", 20))
clock.place(x= 30, y = 130)


#LABELS
label1 = Label(root, text="WIND" , font =(" Helvetica", 15, "bold"), bg = "#1ab5ef", fg = "white")
label1.place(x= 120, y= 400)

label2 = Label(root, text="HUMIDITY" , font =(" Helvetica", 15, "bold"), bg = "#1ab5ef", fg = "white")
label2.place(x= 250, y= 400)

label3 = Label(root, text=" DESCRIPTION" , font =(" Helvetica", 15, "bold"), bg = "#1ab5ef", fg = "white")
label3.place(x= 430, y= 400)

label4 = Label(root, text=" PRESSURE" , font =(" Helvetica", 15, "bold"), bg = "#1ab5ef", fg = "white")
label4.place(x= 650, y= 400)

t= Label(font=("arial", 70,"bold"), fg = "#ee666d")
t.place( x=400, y = 150)
c = Label(font=("arial", 15,"bold"))
c.place( x= 400, y = 250)

w= Label(text = "..." , font=("arial",20 ,"bold"), bg = "#1ab5ef")
w.place(x= 120, y = 430)
h= Label(text = "..." , font=("arial",20 ,"bold"), bg = "#1ab5ef")
h.place(x= 280, y = 430)
d= Label(text = "..." , font=("arial",20 ,"bold"), bg = "#1ab5ef")
d.place(x= 450, y = 430)
p= Label(text = "..." , font=("arial",20 ,"bold"), bg = "#1ab5ef")
p.place(x= 670, y = 430)






root.mainloop()
