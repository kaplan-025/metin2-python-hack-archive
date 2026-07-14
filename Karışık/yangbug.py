# Metin2Bot [Dreamfancy]
import ui
import dbg
import chat
import net
import time
BugYangV = 0

class Dialog1(ui.BoardWithTitleBar):
    
    def __init__(self):
        ui.BoardWithTitleBar.__init__(self)
        self.BuildWindow()

    
    def __del__(self):
        ui.BoardWithTitleBar.__del__(self)

    
    def BuildWindow(self):
        self.SetSize(162, 100)
        self.SetCenterPosition()
        self.AddFlag('movable')
        self.AddFlag('float')
        self.SetTitleName('Bug yang bot')
        self.SetCloseEvent(self.Close)
        self.comp = Component()
        self.btnbugyang = self.comp.Button(self, 'Aktiflestir', '', 83, 37, self.btnbugyang_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        (self.slotbar_editlugar, self.editlugar) = self.comp.EditLine(self, '', 54, 39, 20, 15, 2)
        self.txtlugar = self.comp.TextLine(self, 'Slot:', 18, 39, self.comp.RGB(255, 255, 255))
        self.txtcredit = self.comp.TextLine(self, 'Yapimci: Metin2Bot', 55, 73, self.comp.RGB(255, 255, 255))

    
    def btnbugyang_func(self):
        global BugYangV
        if BugYangV == 0:
            LugarBugYang = self.editlugar.GetText()
            if LugarBugYang == '':
                chat.AppendChat(chat.CHAT_TYPE_INFO, 'Bu alani bos birakmayin.')
            else:
                BugYangV = 1
                self.btnbugyang.SetText('Kapat')
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Envanterin tamamini ve ilk slotlarini bos birakiniz.')
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Envanterin tamamini ve ilk slotlarini bos birakiniz.')
                self.BugYangActivado()
        else:
            BugYangV = 0
            self.btnbugyang.SetText('Aktiflestir')
            self.BugYangDesactivado()

    
    def BugYangActivado(self):
        LugarBugYang = self.editlugar.GetText()
        net.SendShopBuyPacket(int(LugarBugYang))
        net.SendShopBuyPacket(int(LugarBugYang))
        net.SendShopSellPacket(0)
        net.SendShopSellPacket(1)
        self.BugYangSegundos = WaitingDialog()
        self.BugYangSegundos.Open(float(1e-070))
        self.BugYangSegundos.SAFE_SetTimeOverEvent(self.BugYangActivado)

    
    def BugYangDesactivado(self):
        self.BugYangSegundos = WaitingDialog()
        self.BugYangSegundos.Open(int(0x47BF19673DF52E37F2410011D0FFFFFFFFFFFL))
        self.BugYangSegundos.SAFE_SetTimeOverEvent(self.BugYangDesactivado)

    
    def Close(self):
        self.Hide()



class Component:
    
    def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
        button = ui.Button()
        button.SetParent(parent)
        button.SetPosition(x, y)
        button.SetUpVisual(UpVisual)
        button.SetOverVisual(OverVisual)
        button.SetDownVisual(DownVisual)
        button.SetText(buttonName)
        button.SetToolTipText(tooltipText)
        button.Show()
        button.SetEvent(func)
        return button

    
    def ToggleButton(self, parent, buttonName, tooltipText, x, y, funcUp, funcDown, UpVisual, OverVisual, DownVisual):
        button = ui.ToggleButton()
        button.SetParent(parent)
        button.SetPosition(x, y)
        button.SetUpVisual(UpVisual)
        button.SetOverVisual(OverVisual)
        button.SetDownVisual(DownVisual)
        button.SetText(buttonName)
        button.SetToolTipText(tooltipText)
        button.Show()
        button.SetToggleUpEvent(funcUp)
        button.SetToggleDownEvent(funcDown)
        return button

    
    def EditLine(self, parent, editlineText, x, y, width, heigh, max):
        SlotBar = ui.SlotBar()
        SlotBar.SetParent(parent)
        SlotBar.SetSize(width, heigh)
        SlotBar.SetPosition(x, y)
        SlotBar.Show()
        Value = ui.EditLine()
        Value.SetParent(SlotBar)
        Value.SetSize(width, heigh)
        Value.SetPosition(5, 1)
        Value.SetMax(max)
        Value.SetText(editlineText)
        Value.Show()
        return (SlotBar, Value)

    
    def TextLine(self, parent, textlineText, x, y, color):
        textline = ui.TextLine()
        textline.SetParent(parent)
        textline.SetPosition(x, y)
        if color != None:
            textline.SetFontColor(color[0], color[1], color[2])
        
        textline.SetText(textlineText)
        textline.Show()
        return textline

    
    def RGB(self, r, g, b):
        return (r * 255, g * 255, b * 255)

    
    def SliderBar(self, parent, sliderPos, func, x, y):
        Slider = ui.SliderBar()
        Slider.SetParent(parent)
        Slider.SetPosition(x, y)
        Slider.SetSliderPos(sliderPos / 100)
        Slider.Show()
        Slider.SetEvent(func)
        return Slider

    
    def ExpandedImage(self, parent, x, y, img):
        image = ui.ExpandedImageBox()
        image.SetParent(parent)
        image.SetPosition(x, y)
        image.LoadImage(img)
        image.Show()
        return image

    
    def ComboBox(self, parent, text, x, y, width):
        combo = ui.ComboBox()
        combo.SetParent(parent)
        combo.SetPosition(x, y)
        combo.SetSize(width, 15)
        combo.SetCurrentItem(text)
        combo.Show()
        return combo

    
    def ThinBoard(self, parent, moveable, x, y, width, heigh, center):
        thin = ui.ThinBoard()
        if parent != None:
            thin.SetParent(parent)
        
        if moveable == TRUE:
            thin.AddFlag('movable')
            thin.AddFlag('float')
        
        thin.SetSize(width, heigh)
        thin.SetPosition(x, y)
        if center == TRUE:
            thin.SetCenterPosition()
        
        thin.Show()
        return thin



class WaitingDialog(ui.ScriptWindow):
    
    def __init__(self):
        ui.ScriptWindow.__init__(self)
        
        self.eventTimeOver = lambda *arg: None
        
        self.eventExit = lambda *arg: None

    
    def __del__(self):
        ui.ScriptWindow.__del__(self)

    
    def Open(self, waitTime):
        curTime = time.clock()
        self.endTime = curTime + waitTime
        self.Show()

    
    def Close(self):
        self.Hide()

    
    def Destroy(self):
        self.Hide()

    
    def SAFE_SetTimeOverEvent(self, event):
        self.eventTimeOver = ui.__mem_func__(event)

    
    def SAFE_SetExitEvent(self, event):
        self.eventExit = ui.__mem_func__(event)

    
    def OnUpdate(self):
        lastTime = max(0, self.endTime - time.clock())
        if 0 == lastTime:
            self.Close()
            self.eventTimeOver()
        else:
            return None


Dialog1().Show()
