import wx
from math import *


class CalcFrame(wx.Frame):

    def __init__(self, title):
        super(CalcFrame, self).__init__(None, title=title, size=(300, 250))
        self.InitUI()

        self.Centre()
        self.Show()

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.textprint = wx.TextCtrl(self, -1, '', style=wx.TE_RIGHT|wx.TE_READONLY)
        self.equation=""
        vbox.Add(self.textprint, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        gridBox = wx.GridSizer(5, 4, 5, 5)
        labels = ['AC', 'DEL', 'pi', 'CLOSE', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=',
                  '+']
        for label in labels:
            btnItem = wx.Button(self, label=label)
            self.createHandler(btnItem, label)
            gridBox.Add(btnItem, 1, wx.EXPAND)
        vbox.Add(gridBox, proportion=7, flag=wx.EXPAND)
        self.SetSizer(vbox)

    def createHandler(self, button, labels):
        item = "DEL AC = CLOSE"
        if labels not in item:
            self.Bind(wx.EVT_BUTTON, self.OnAppend, button)
        elif labels == 'DEL':
            self.Bind(wx.EVT_BUTTON, self.OnDel, button)
        elif labels == 'AC':
            self.Bind(wx.EVT_BUTTON, self.OnAc, button)
        elif labels == '=':
            self.Bind(wx.EVT_BUTTON, self.OnTarget, button)
        elif labels == 'CLOSE':
            self.Bind(wx.EVT_BUTTON, self.OnClose, button)

    def OnAppend(self, event):
        eventbtn = event.GetEventObject()
        label = eventbtn.GetLabel()
        self.equation += label
        self.textprint.SetValue(self.equation)

    def OnDel(self, event):
        self.equation = self.equation[:-1]
        self.textprint.SetValue(self.equation)

    def OnAc(self, event):
        self.textprint.Clear()
        self.equation = ""


    def OnTarget(self, event):
        string = self.equation
        try:
            target = eval(string)
            self.equation = str(target)
            self.textprint.SetValue(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self, u'wrong syntax', u'watch out', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def OnClose(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    CalcFrame(title='Calculator')
    app.MainLoop()
