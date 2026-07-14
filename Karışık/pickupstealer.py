import textTail
import ui
import dbg
import app
import net
import chr # 
import time # sleep and clock
import player # hp
import thread # start_new_thread ( bad performance )
import item # Get VID of the PickUpBot
import chat # AppendChat
import background
from dbg import LogBox as debug
offical_server = TRUE
Y_RANGE = xrange(125, 600, 18)
X_RANGE = xrange(300, 825, 31)

class PickUpBot(ui.ScriptWindow):
    MODE_YANG = 2
    MODE_ALL = 1

    def __init__(self, parentUI, mode = 0):
        ui.ScriptWindow.__init__(self)
        self.Run = 1
        self.C = 0
        self.Ghostmode = 0
        self.NYList = []
        self.mode = mode
        self.parentUI = parentUI
        self.Movespeed = 100
        self.x, self.y = (0, 0)

    def SetMode(self, mode):
        if mode == PickUpBot.MODE_ALL:
            self.GetVIDs = self.GetItems
        elif mode == PickUpBot.MODE_YANG:
            self.NYList[:] = []
            self.GetVIDs = self.GetYang
        self.mode = mode

    def SetGhostmode(self, flag = TRUE):
        self.Ghostmode = flag

    def __del__(self):
        self.Cancel()
        ui.ScriptWindow.__del__(self)

    def Cancel(self):
        self.Run = 0

    def Revive(self):
        net.SendChatPacket('/restart')
        chat.AppendChat(1, '[PickUpBot]You will now auto-Restart !')
        chat.AppendChat(1, '[PickUpBot]Because if you be longer than 2 minutes in Ghostmode')
        chat.AppendChat(1, '[PickUpBot]you will restart in Town.')
        self.isAlive = 1

    def GetItems(self, y_range = Y_RANGE, x_range = X_RANGE):
        List = []
        Picker = Pick
        for y in y_range:
            for x in x_range:
                iVID = Picker(x, y)
                if iVID != -1 and iVID not in List:
                    List.append(iVID)

        return List

    def GetVIDs(self):
        pass

    def GetYang(self, y_range = Y_RANGE, x_range = X_RANGE):
        List = []
        NYList = self.NYList
        Picker = Pick
        for y in y_range:
            for x in x_range:
                FirstCoord = None
                LastCoord = None
                iVID = Picker(x, y)
                if iVID != -1:
                    if iVID not in List:
                        _range = xrange(1, 29)
                        for i in _range:
                            if Picker(x - i, y) != iVID:
                                FirstCoord = x - i + 1
                                break

                        if FirstCoord == None:
                            continue
                        for i in _range:
                            if Picker(FirstCoord + i, y) != iVID:
                                LastCoord = FirstCoord + i - 1
                                break

                        if LastCoord == None:
                            continue
                        List.append(iVID)

        return List

    def CountEvents(self, count):
        self.parentUI.GhostLeftTimer(count)
        chr.Revive()

    def OnUpdate(self):
        if self.Run:
            if self.C >= 5:
                sendPickUp = net.SendItemPickUpPacket
                for iVID in self.GetVIDs():
                    sendPickUp(iVID)

                self.C = 0
            self.C += 1
        if not offical_server:
            pStatus = player.GetStatus
            chr.SetMoveSpeed(self.Movespeed)
            x, y = player.GetMainCharacterPosition()[:2]
            DifX = self.x - x
            DifY = self.y - y
            if DifX < 0:
                DifX *= -1
            if DifY < 0:
                DifY *= -1
            if DifX + DifY > 2200:
                chr.PushOnceMotion(chr.MOTION_WAIT)
                self.x, self.y = player.GetMainCharacterPosition()[:2]
            if self.Ghostmode:
                hp = pStatus(player.HP)
                if self.isAlive and hp < 1:
                    chr.Revive()
                    self.TimeOutWaiter = CountDown()
                    self.TimeOutWaiter.SAFE_SetTimeOverEvent(self.Revive)
                    self.TimeOutWaiter.eventCountEvent = self.CountEvents
                    self.TimeOutWaiter.Open(119)
                    self.isAlive = 0
                if self.isAlive == 0 and hp > 0:
                    self.TimeOutWaiter.Close()
                    self.CountEvents(120)
                    self.isAlive = 1

    def Start(self):
        self.Run = 1
        if self.mode == 0:
            self.parentUI.UseDefaultModus()
        self.isAlive = 1
        self.Show()

    def FlagRun(self):
        self.Run = 1

    def Stop(self):
        self.Run = 0
        self.Hide()


class CountDown(ui.ScriptWindow):

    def __init__(self):
        ui.ScriptWindow.__init__(self)
        self.eventTimeOver = lambda *arg: None
        self.eventExit = lambda *arg: None
        self.eventCountEvent = lambda *arg: None

    def __del__(self):
        ui.ScriptWindow.__del__(self)

    def Open(self, waitTime):
        curTime = time.clock()
        self.endTime = curTime + 1
        self.Counter = waitTime + 1
        self.Show()

    def Close(self):
        self.Hide()

    def Destroy(self):
        self.Hide()

    def SAFE_SetTimeOverEvent(self, event):
        self.eventTimeOver = ui.__mem_func__(event)

    def SAFE_SetCountEvent(self, event):
        self.eventCountEvent = ui.__mem_func__(event)

    def SAFE_SetExitEvent(self, event):
        self.eventExit = ui.__mem_func__(event)

    def OnUpdate(self):
        lastTime = max(0, self.endTime - time.clock())
        if 0 == lastTime:
            self.endTime = time.clock() + 1
            self.Counter -= 1
            self.eventCountEvent(self.Counter)
            if self.Counter < 1:
                self.Close()
                self.eventTimeOver()


class Dialog1(ui.Window):

    def __init__(self):
        ui.Window.__init__(self)
        self.PickUpBot = PickUpBot(self)
        self.BuildWindow()
        self.x = net.SendItemDropPacketNew
        net.SendItemDropPacketNew = self.DropPacketNew

    def DropPacketNew(self, *args):
        self.PickUpBot.Run = 0
        self.XX = CountDown()
        self.XX.eventTimeOver = lambda SLF = self.PickUpBot: SLF.FlagRun()
        self.XX.Open(3)
        return self.x(*args)

    def __del__(self):
        ui.Window.__del__(self)

    def BuildWindow(self):
        self.Ghostmode = 0
        self.Board = ui.ThinBoard()
        self.Board.SetSize(299, 136)
        self.Board.SetCenterPosition()
        self.Board.AddFlag('movable')
        self.Board.AddFlag('float')
        self.Board.Show()
        self.comp = Component()
        self.btnActiv = self.comp.Button(self.Board, 'Aktivieren', '', 204, 12, self.ActivFunc, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.btnDeactiv = self.comp.Button(self.Board, 'Deaktivieren', '', 204, 34, self.DeactivFunc, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.btnDeactiv.Hide()
        self.btnYang = self.comp.Button(self.Board, 'Yang Only', '', 30, 83, self.btnYang_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.btnEvery = self.comp.Button(self.Board, 'Everything', '', 90, 83, self.btnEvery_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.btnCredits = self.comp.Button(self.Board, 'CrashMap', '', 204, 83, self.btnCredits_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.btnGhost = self.comp.Button(self.Board, 'Ghostmode', '', 204, 56, self.btnGhostFunc, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.btnKick = self.comp.Button(self.Board, '', '', 31, 106, self.onClickKick, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
        self.lblModus = self.comp.TextLine(self.Board, 'Verfugbare Modus:', 30, 68, self.comp.RGB(0, 229, 650))
        self.title = self.comp.TextLine(self.Board, 'PickUpBot by !Beni!@e*pvp', 30, 11, self.comp.RGB(255, 255, 0))
        self.lblGhostLeftText = self.comp.TextLine(self.Board, 'Left Ghosttime:      s', 98, 29, self.comp.RGB(0, 229, 650))
        self.lblGhostLeft = self.comp.TextLine(self.Board, '120', 168, 29, self.comp.RGB(0, 229, 650))
        self.lblKick = self.comp.TextLine(self.Board, 'Instant Kick', 49, 105, self.comp.RGB(255, 0, 255))
        if not offical_server:
            self.lblSpeedText = self.comp.TextLine(self.Board, 'Speed:', 30, 29, self.comp.RGB(0, 255, 255))
            self.lblSpeed = self.comp.TextLine(self.Board, '100', 66, 29, self.comp.RGB(0, 0, 255))
            self.Speed = self.comp.SliderBar(self.Board, 0.0, self.SetPickSpeed, 30, 51)
        else:
            self.lblOfficalServer = self.comp.TextLine(self.Board, 'Offical Server', 30, 29, self.comp.RGB(0, 255, 255))

    def ActivFunc(self):
        self.btnActiv.Hide()
        self.btnDeactiv.Show()
        self.PickUpBot.Start()

    def DeactivFunc(self):
        self.btnDeactiv.Hide()
        self.btnActiv.Show()
        self.PickUpBot.Stop()

    def GhostLeftTimer(self, count):
        self.lblGhostLeft.SetText(str(count))

    def btnYang_func(self):
        self.PickUpBot.SetMode(PickUpBot.MODE_YANG)
        self.btnYang.ButtonText.SetFontColor(*self.comp.RGB(255, 255, 255))
        self.btnEvery.ButtonText.SetFontColor(*self.comp.RGB(200, 200, 200))

    def btnEvery_func(self):
        self.PickUpBot.SetMode(PickUpBot.MODE_ALL)
        self.btnYang.ButtonText.SetFontColor(*self.comp.RGB(200, 200, 200))
        self.btnEvery.ButtonText.SetFontColor(*self.comp.RGB(255, 255, 255))

    def UseDefaultModus(self):
        self.PickUpBot.SetMode(PickUpBot.MODE_YANG)
        self.btnYang.ButtonText.SetFontColor(*self.comp.RGB(255, 255, 255))
        self.btnEvery.ButtonText.SetFontColor(*self.comp.RGB(200, 200, 200))

    def btnCredits_func(self):
        x, y = player.GetMainCharacterPosition()[:2]
        background.LoadMap(background.GetCurrentMapName(), x, y, 0)

    def btnGhostFunc(self):
        if self.Ghostmode:
            self.Ghostmode = 0
            self.PickUpBot.SetGhostmode(FALSE)
            self.btnGhost.ButtonText.SetFontColor(*self.comp.RGB(200, 200, 200))
        else:
            self.Ghostmode = 1
            self.PickUpBot.SetGhostmode(TRUE)
            self.btnGhost.ButtonText.SetFontColor(*self.comp.RGB(255, 255, 255))

    def onClickKick(self):
        start_new_thread(lambda : (player.SetSingleDIKKeyState(app.DIK_UP, TRUE),
         [ net.LogOutGame() for i in xrange(251) ],
         time.sleep(1.0),
         player.SetSingleDIKKeyState(app.DIK_UP, FALSE)), ())

    def SetPickSpeed(self):
        speed = int(self.Speed.GetSliderPos() * 1000)
        if speed < 100:
            speed = 100
        self.lblSpeed.SetText(str(speed))
        self.PickUpBot.Movespeed = speed

    def OnKeyDown(self, key):
        try:
            self.onPressKeyDict[key]()
        except KeyError:
            pass
        except:
            raise

        return TRUE

    def OpenWindow(self):
        if self.Board.IsShow():
            self.Board.Hide()
        else:
            self.Board.Show()

    def Close(self):
        self.Board.Hide()


class Component:

    def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
        button = ui.Button()
        if parent != None:
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
        if parent != None:
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
        if parent != None:
            SlotBar.SetParent(parent)
        SlotBar.SetSize(width, heigh)
        SlotBar.SetPosition(x, y)
        SlotBar.Show()
        Value = ui.EditLine()
        Value.SetParent(SlotBar)
        Value.SetSize(width, heigh)
        Value.SetPosition(1, 1)
        Value.SetMax(max)
        Value.SetLimitWidth(width)
        Value.SetMultiLine()
        Value.SetText(editlineText)
        Value.Show()
        return (SlotBar, Value)

    def TextLine(self, parent, textlineText, x, y, color):
        textline = ui.TextLine()
        if parent != None:
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
        if parent != None:
            Slider.SetParent(parent)
        Slider.SetPosition(x, y)
        Slider.SetSliderPos(sliderPos / 100)
        Slider.Show()
        Slider.SetEvent(func)
        return Slider

    def ExpandedImage(self, parent, x, y, img):
        image = ui.ExpandedImageBox()
        if parent != None:
            image.SetParent(parent)
        image.SetPosition(x, y)
        image.LoadImage(img)
        image.Show()
        return image

    def ComboBox(self, parent, text, x, y, width):
        combo = ui.ComboBox()
        if parent != None:
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

    def Gauge(self, parent, width, color, x, y):
        gauge = ui.Gauge()
        if parent != None:
            gauge.SetParent(parent)
        gauge.SetPosition(x, y)
        gauge.MakeGauge(width, color)
        gauge.Show()
        return gauge

    def ListBoxEx(self, parent, x, y, width, heigh):
        bar = ui.Bar()
        if parent != None:
            bar.SetParent(parent)
        bar.SetPosition(x, y)
        bar.SetSize(width, heigh)
        bar.SetColor(1996488704)
        bar.Show()
        ListBox = ui.ListBoxEx()
        ListBox.SetParent(bar)
        ListBox.SetPosition(0, 0)
        ListBox.SetSize(width, heigh)
        ListBox.Show()
        scroll = ui.ScrollBar()
        scroll.SetParent(ListBox)
        scroll.SetPosition(width - 15, 0)
        scroll.SetScrollBarSize(heigh)
        scroll.Show()
        ListBox.SetScrollBar(scroll)
        return (bar, ListBox)


Dialog1().Show()