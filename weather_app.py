import tkinter as tk
import requests
root=tk.Tk()
root.title("Weather")
Height=700
Width=800
canvas=tk.Canvas(root, height=Height, width=Width)
canvas.pack()
#def test_fun(entry_box):
 #   print("the entry is:", entry_box)#a4aa5e3d83ffefaba8c00284de6ef7c3
def get_weather(city):
    weather_key='a4aa5e3d83ffefaba8c00284de6ef7c3'
    url='https://api.openweathermap.org/data/2.5/weather'#we can use here forcaste to get data instead of weather
    params={'APPID': weather_key, 'q':city,'units': 'imperial'}
    response=requests.get(url, params=params)
    weather=response.json()
    # print(weather['name'])
    # print(weather)
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])
    label['text']=format_response(weather)

def format_response(weather):
   try:
      name=weather['name']
      desc=weather['weather'][0]['description']
      temp=weather['main']['temp']
      t=round((temp-32)/1.8,2)
      final_data=f"city name : {name}\nTemp(celcius): {t}   \nDescription:{desc}"
      return final_data
   except:
       return "'May be,you entered wrong city details or there is a internet problem!'"
    #print(weather['weather'][0['description']])
    #print(weather['main']['temp'])
background_image=tk.PhotoImage(file="walll.png")
background_label=tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
frame=tk.Frame(root, bd=5,bg="blue")
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor="n")
entry_var=tk.StringVar()
entry_box=tk.Entry(frame,font=45)
entry_box.place(relwidth=0.65,relheight=1)
submit_btn=tk.Button(frame, text="Get Weather",bg="black", fg="red",font=40,command=lambda:get_weather(entry_box.get()))
submit_btn.place(relx=0.7, relheight=1,relwidth=0.3)
lower_frame=tk.Frame(root,bd=5,bg="blue")
lower_frame.place(relx=0.5, rely=0.25,relwidth=0.78,relheight=0.6,anchor="n")
label=tk.Label(lower_frame, font=56)
label.place(relheight=1, relwidth=1)

#API key:aec41187d645021771c406d1894c0ba7
#api call:api.openweathermap.org/data/2.5/forecast?id={city ID}&appid={your api key}
root.mainloop()