from tkinter import *
from tkinter import messagebox
import requests
window =Tk()
window.title("Python text downloader")
# .....Enter URL..............
message1 = Label(window, text="Enter URL :")
message1.grid(column=1, row=1)
# ..............................

# ......URL text box.........
url_txt = Entry(window,width=12)
url_txt.grid(column=1,row=2)
# ...........................

# .....Download Path...........
message2 =Label(window,text="Download Path")
message2.grid(column=1,row=3)
# .............................
window.geometry('135x150')



# ......Download Path box.........
path_txt = Entry(window,width=12)
path_txt.grid(column=1,row=4)
# ...........................

def get_url():
    url = url_txt.get()
    download_path = path_txt.get()
    download_path+="/file_wrote.txt"
    pages = requests.get(url).text
    reader = open(download_path,"w")
    reader.write(pages)

    reader.close()
    messagebox.showinfo("Alert","Download Done!")

# ...........DOWNLOAD BTN..........
url_btn = Button(window , text="Download" , command =get_url)
url_btn.grid(column=1,row =6)
# .................................



window.mainloop()
