from Tkinter import *
from PIL import Image, ImageTk    #pillow package
import W
import requests


class MyWeather:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("350x400+350+100")
        self.root.config(bg="white")
        # icons
        self.search_icon = Image.open("images/Search.png")
        self.search_icon = self.search_icon.resize((30, 30), Image.ANTIALIAS)
        self.search_icon = ImageTk.PhotoImage(self.search_icon)

        self.var_search = StringVar()
        title = Label(self.root, text="Weather App", font=("goudy old style", 30, "bold"), bg="#262626",
                      fg="white").place(x=0, y=0, relwidth=1, height=60)
        lbl_city = Label(self.root, text="City Name", font=("goudy old style", 15, "bold"), bg="#033958", fg="white",
                         anchor="w", padx=5).place(x=0, y=60, relwidth=1, height=50)
        txt_city = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"),
                         bg="lightyellow",
                         fg="#262626").place(x=100, y=75, width=200, height=25)
        btn_Search = Button(self.root, cursor="hand2", image=self.search_icon, bg="#033958",
                            activebackground="#033958", bd=0, command=self.get_weather).place(x=310, y=73, width=30,
                                                                                              height=30)

        # Result

        self.lbl_city = Label(self.root, font=("goudy old style", 15, "bold"), bg="white",fg="blue")
        self.lbl_city.place(x=0, y=130, relwidth=1, height=20)
        self.lbl_icon = Label(self.root, font=("goudy old style", 15, "bold"), bg="white")
        self.lbl_icon.place(x=0, y=155,relwidth=1, height=100)
        self.lbl_temp = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", fg="orange")
        self.lbl_temp .place( x=0, y=250, relwidth=1, height=20)
        self.lbl_wind = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", fg="#262626")
        self.lbl_wind.place(x=0, y=285, relwidth=1, height=20)
        self.lbl_error = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", fg="red")
        self.lbl_error.place(x=0, y=325, relwidth=1, height=20)

        # ==footer===
        lbl_footer = Label(self.root, text="Develope by Shrutee", font=("gaudy old style", 10, "bold"), bg="#033958",
                           fg="white", pady=5).pack(side=BOTTOM, fill=X)

    def get_weather(self):
        api_key = W.api_key
        city="{}".format(self.var_search.get())
        complete_url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}".format(**locals())
        if city=="":
            self.lbl_error.config(text="City Name Required")
        else:
            result = requests.get(complete_url)
            if result:
                json = result.json()
                city_name = json["name"]
                country = json["sys"]["country"]
                icons = json["weather"][0]["icon"]
                temp_c = json["main"]["temp"] - 273.15
                temp_f = (json["main"]["temp"] - 273.15) * 9 / 5 + 32
                wind = json["weather"][0]["main"]

                self.lbl_city.config(text=city_name + "," + country)
                # ==new icons
                self.search_icon2 = Image.open("images/{icons}.png".format(**locals()))
                self.search_icon2 = self.search_icon2.resize((100, 100), Image.ANTIALIAS)
                self.search_icon2 = ImageTk.PhotoImage(self.search_icon2)
                self.lbl_icon.config(image=self.search_icon2)

                deg = u"\N{DEGREE SIGN}"
                self.lbl_temp.config(text=str(round(temp_c, 2)) + "C | " + str(round(temp_f, 2)) + deg + " f")
                self.lbl_wind.config()
                self.lbl_wind.config(text=wind)
                self.lbl_error.config(text="")
            else:
                self.lbl_city.config(text="")
                self.lbl_icon.config(image="")
                self.lbl_temp.config(text="")
                self.lbl_wind.config(text="")
                self.lbl_error.config(text="Invalid City Name")






root = Tk()
obj = MyWeather(root)
root.mainloop()
