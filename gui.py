from tkinter import *
window =Tk()
window.title("Python text downloader")

message1 = Label(window, text="Enter URL :")
message1.grid(column=1, row=4)
message2 =Label(window,text="Download Path")
message2.grid(column=1,row=6)
window.geometry('300x100')

def get_url():
    url = url_txt.get()

url_btn = Button(window , text="Download" , command =get_url)
url_btn.grid(column=1,row =0)
url_txt = Entry(window,width=10)
url_txt.grid(column=2,row=0)





window.mainloop()
