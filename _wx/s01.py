import wx
import wx.html2

class MyBrowser(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.browser = wx.html2.WebView.New(self)
        self.browser.LoadURL("http://localhost:5000/")

if __name__ == '__main__':
    app = wx.App()
    frame = MyBrowser(None, wx.ID_ANY, "wxPython WebView Example")
    frame.Show()
    app.MainLoop()