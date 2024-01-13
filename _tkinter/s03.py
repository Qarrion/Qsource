

import tkinter as tk
from tkinterweb import HtmlFrame   # tkinterweb 모듈에서 HtmlFrame을 임포트

# 메인 윈도우 생성
root = tk.Tk()
root.title("Tkinter 내장 웹 브라우저 예제")
root.geometry("800x600")

# HtmlFrame 생성
frame = HtmlFrame(root, horizontal_scrollbar="auto")
frame.pack(fill="both", expand=True)

# 웹 페이지 로드
# 여기서 'https://www.example.com'는 JavaScript를 실행하는 웹 페이지 주소로 대체해야 합니다.
frame.load_website("https://www.naver.com")

# 메인 루프
root.mainloop()