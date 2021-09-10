from tkinter import *
from time import sleep
from os.path import abspath
import speedtest

cor = {
    'transparent': '#f0f0f0',
    'gray-20': '#202020',
    'white': '#ffffff',
    'green': '#61FFBD',
}


class Actions:

    def close(self, event) -> None:
        app.destroy()
    
    def effects(self, event, button: str, effect: bool) -> None:
        if button == 'bt_result':
            if effect:
                sleep(0.1)
                bt_result.place(x=200, y=213)
            else:
                bt_result.place(x=200, y=215)
    
    def result(self, event) -> None:
        test = speedtest.Speedtest()
        test.download()
        test.upload()
        test_result = test.results
        upload.delete(0, END)
        ping.delete(0, END)
        download.delete(0, END)
        upload.insert(0, str(int(test_result.upload / 1000000)))
        ping.insert(0, str(int(test_result.ping)))
        download.insert(0, str(int(test_result.download / 1000000)))


def _get_pos(event):
    xwin = app.winfo_x()
    ywin = app.winfo_y()
    startx = event.x_root
    starty = event.y_root

    xwin -= startx
    ywin -= starty

    def move_window(event):
        app.configure(cursor="fleur")
        app.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

    def release_window(event):
        app.config(cursor="arrow")

    title_frame.bind('<B1-Motion>', move_window)
    title_frame.bind('<ButtonRelease-1>', release_window)


def search(*files: str) -> str:
    path = []
    for file in files:
        path.append(file)
    return str(abspath('/'.join(path)))


def window(root: Tk, size: tuple[int, int, int]) -> None:
    width, height, expand = size[0], size[1], size[2]
    x = root.winfo_screenwidth() // 2 - width // 2
    y = root.winfo_screenheight() // 2 - height // 2
    root.geometry(f'{width}x{height}+{x}+{y}')
    root.resizable(expand, expand)
    root.mainloop()


# -----> Create object
app = Tk()
action = Actions()
app.overrideredirect(True)
app.wm_attributes('-topmost', True)
app.configure(background=cor['transparent'])
app.wm_attributes('-transparentcolor', cor['transparent'])

# Create window
img0 = PhotoImage(file=search('img', 'background.png'))
background = Label(app, image=img0, border=0)
background.place(x=0, y=0)

# Frame-title
img1 = PhotoImage(file=search('img', 'title.png'))
title_frame = Label(app, image=img1, border=0)
title_frame.bind('<1>', _get_pos)
title_frame.place(x=0, y=0)

# Button close-window
img2 = PhotoImage(file=search('img', 'close.png'))
bt_close = Label(app, image=img2, border=0, background=cor['gray-20'])
bt_close.bind('<1>', lambda event: action.close(event))
bt_close.place(x=12, y=4)


# -----> Widgets

# Upload
img3 = PhotoImage(file=search('img', 'upload.png'))
upload_img = Label(app, image=img3, border=0, background=cor['white'])
upload_img.place(x=10, y=50)

upload = Entry(app, background=cor['white'], foreground=cor['green'], font='Arial 32 bold', relief='flat', justify='center')
upload.place(x=45, y=105, width=80)
upload.insert(0, '0')

# Ping
img4 = PhotoImage(file=search('img', 'ping.png'))
ping_img = Label(app, image=img4, border=0, background=cor['white'])
ping_img.place(x=175, y=50)

ping = Entry(app, background=cor['white'], foreground=cor['green'], font='Arial 32 bold', relief='flat', justify='center')
ping.place(x=210, y=105, width=80)
ping.insert(0, '0')

# Download
img5 = PhotoImage(file=search('img', 'download.png'))
download_img = Label(app, image=img5, border=0, background=cor['white'])
download_img.place(x=340, y=50)

download = Entry(app, background=cor['white'], foreground=cor['green'], font='Arial 32 bold', relief='flat', justify='center')
download.place(x=375, y=105, width=80)
download.insert(0, '0')

# Button-result
img6 = PhotoImage(file=search('img', 'result_deactive.png'))
bt_result = Label(app, image=img6, border=0, background=cor['white'])
bt_result.bind('<1>', lambda event: action.result(event))
bt_result.bind('<Enter>', lambda event, button='bt_result', effect=True: action.effects(event, button, effect))
bt_result.bind('<Leave>', lambda event, button='bt_result', effect=False: action.effects(event, button, effect))
bt_result.place(x=200, y=215)


# -----> Size window
window(app, (500, 250, 0))
