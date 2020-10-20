import tkinter as tk
from io import BytesIO
from logging import exception

from PIL import ImageTk, Image
import requests as r


class MemeGUI():

    def __init__(self):
        self.window = tk.Tk()
        self.window['background'] = '#606060'
        self.window.resizable(0,0)
        self.window.geometry("800x600")
        self.window.title('Memes')
        self.download_status = "Download Succesfuly"
        self.label = tk.Label(self.window, text=self.download_status)
        tk.Button(self.window, text="Save", width=13, height=2, command=self.save, bg='green').place(x=0, y=300)
        tk.Button(self.window, text="Next >>", width=13, height=2, command=self.next, bg='green').place(x=700, y=300)
        tk.Button(self.window, text="Close", width=15, height=2, command=self.window.quit, bg='red').place(x=350, y=520)
        self.next()

    def mainloop(self):
        self.window.mainloop()

    def save(self):
        try:
            self.imgForSave.save("".join(filter(str.isalnum,self.jsonResponse['title']))+".jpg" )
        except Exception as e:
            self.download_status = 'Cant download'
        self.label.place(x=350, y=570)

    def next(self):
        self.label.place(x=1000, y=1000)
        try:
            self.jsonResponse =  r.get('https://meme-api.herokuapp.com/gimme').json()
            url = self.jsonResponse['url']
            response = r.get(url)
            self.imgForSave = Image.open(BytesIO(response.content)).resize((600,500), Image. ANTIALIAS)
            img = ImageTk.PhotoImage(self.imgForSave)
            panel = tk.Label(self.window, image=img)
            panel.image = img
            panel.place(y=10, x=97.5)
        except Exception as e:
            tk.Label(self.window,text='wifi not connected' ).place(x=350,y=300)

if __name__ == '__main__':
    MemeGUI().mainloop()
