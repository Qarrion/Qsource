import tkinter as tk
from tkinterweb import HtmlFrame

# Tkinter 창 생성
root = tk.Tk()
root.title("Bokeh Chart in Tkinter")

# tkinterweb HtmlFrame 위젯 생성 및 설정
frame = HtmlFrame(root, horizontal_scrollbar="auto")
frame.load_website("http://localhost:5000/")
frame.pack(fill="both", expand=True)

# Tkinter 이벤트 루프 실행
root.mainloop()