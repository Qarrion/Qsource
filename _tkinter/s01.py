# from tkinter import *
# import webview

# # Create an instance of tkinter frame or window
# win = Tk()

# # Set the size of the window
# win.geometry("700x350")

# # Create a GUI window to view the HTML content
# webview.create_window('tutorialspoint', 'https://www.tutorialspoint.com')
# webview.start()

from cefpython3 import cefpython as cef
import tkinter as tk

# Tkinter 창 생성
root = tk.Tk()
root.title("Frame Ratio 1:3")

# 윈도우 크기 설정
root.geometry("800x600")
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

# 메인 컨테이너 프레임 생성
main_frame = tk.Frame(root, bg='red')
main_frame.grid(row=0, column=0, sticky='nsew')

# main_frame.pack(expand=True, fill="both")

# 메인 컨테이너를 그리드로 분할
main_frame.grid_columnconfigure(0,weight=1)
main_frame.grid_rowconfigure(0, weight=1)  # 위쪽 프레임 가중치
main_frame.grid_rowconfigure(1, weight=3)  # 아래쪽 프레임 가중치


# 위쪽 프레임 생성 및 빨간색 배경 설정
frame_top = tk.Frame(main_frame, bg="yellow",height=100)
frame_top.grid(row=0,column=0, sticky="nsew")


# 아래쪽 프레임 생성 및 파란색 배경 설정
frame_bottom = tk.Frame(main_frame, bg="blue")
frame_bottom.grid(row=1, sticky="nsew")

frame_bottom.grid_columnconfigure(0,weight=1)
frame_bottom.grid_rowconfigure(0,weight=1)

frame = cef.CreateBrowserSync(window_info=cef.WindowInfo(root.winfo_id()),
                                url="https://www.example.com")
frame.SetAsChild(root.winfo_id(), [0, 0, 800, 600])


import tkinter as tk
from tkinterweb import HtmlFrame
web_frame = HtmlFrame(frame_bottom)
web_frame.pack(fill="both", expand=True)
web_frame.load_website("https://localhost:5000/")
# Tkinter 이벤트 루프 시작
root.mainloop()