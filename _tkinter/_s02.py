import tkinter as tk
from cefpython3 import cefpython as cef
import sys

def main():
    # CEF 초기화
    cef.Initialize()

    # Tkinter 윈도우 생성
    root = tk.Tk()
    root.geometry("800x600")

    # CEF 브라우저 프레임 생성
    frame = tk.Frame(root, width=800, height=600)
    frame.pack(fill=tk.BOTH, expand=True)
    window_info = cef.WindowInfo(frame.winfo_id())
    window_info.SetAsChild(frame.winfo_id(), [0, 0, 800, 600])

    # CEF 브라우저 내에서 웹 페이지 로드
    browser = cef.CreateBrowserSync(window_info, url="https://www.example.com/")

    # Tkinter 메인 루프 실행
    root.mainloop()

    # CEF 종료 처리
    cef.Shutdown()

if __name__ == '__main__':
    main()