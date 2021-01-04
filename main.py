import wx

app = wx.App()

frame = wx.Frame(None, -1, title='main.py', pos=(300, 400), size=(200, 150))

frame.Show()

app.MainLoop()