# File: m (Python 2.2)

import ui
import chr
import chat
import player
import math
import app
import dbg

class MetinFinder(ui.ScriptWindow):
    Gui = []
    MetinList = []
    
    def __init__(self):
        self.Gui = []
        ui.ScriptWindow.__init__(self)
        self.AddGui()
        dbg.LogBox('Metin2Bot Scanner 0.1', 'Bilgiler')

    
    def __del__(self):
        self.Gui[0].Hide()
        ui.ScriptWindow.__del__(self)

    
    def AddGui(self):
        Gui = [
            [
                [
                    ui.ThinBoard,
                    ''],
                [
                    275,
                    320],
                [
                    0,
                    0],
                [
                    [
                        'SetCenterPosition',
                        [
                            '']]],
                [
                    'movable',
                    'float']],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    243,
                    18],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/close_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/close_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/close_button_03.sub']],
                    [
                        'SetToolTipText',
                        [
                            'Close',
                            0,
                            -23]],
                    [
                        'SetEvent',
                        [
                            lambda : self.__del__()]]],
                []],
            [
                [
                    ui.SlotBar,
                    0],
                [
                    250,
                    225],
                [
                    10,
                    35 + 20],
                [],
                []],
            [
                [
                    ui.ListBoxEx,
                    0],
                [
                    0,
                    0],
                [
                    17,
                    50 + 20],
                [
                    [
                        'SetViewItemCount',
                        [
                            10]]],
                []],
            [
                [
                    ui.ScrollBar,
                    0],
                [
                    0,
                    0],
                [
                    240,
                    40 + 20],
                [
                    [
                        'SetScrollBarSize',
                        [
                            220]]],
                []],
            [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    70,
                    20],
                [
                    [
                        'SetDefaultFontName',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            'Metin Bulucu 0.1']],
                    [
                        'SetFontColor',
                        [
                            0.40000000000000002,
                            0.90000000000000002,
                            1.0]]],
                []],
            [
                [
                    ui.TextLine,
                    0],
                [
                    0,
                    0],
                [
                    17,
                    57],
                [
                    [
                        'SetDefaultFontName',
                        [
                            '']],
                    [
                        'SetText',
                        [
                            'VID:\t\t\t\tAdlar:\t\t\t\tKoordinatlar:']],
                    [
                        'SetFontColor',
                        [
                            0.20000000000000001,
                            0.80000000000000004,
                            1.0]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    40,
                    290],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Yuru']],
                    [
                        'SetEvent',
                        [
                            lambda : self.YouwantaMetinHuh(0)]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    135,
                    290],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/public/Large_button_03.sub']],
                    [
                        'SetText',
                        [
                            'Teleport']],
                    [
                        'SetEvent',
                        [
                            lambda : self.YouwantaMetinHuh(1)]]],
                []],
            [
                [
                    ui.Button,
                    0],
                [
                    0,
                    0],
                [
                    218,
                    16],
                [
                    [
                        'SetUpVisual',
                        [
                            'd:/ymir work/ui/game/guild/refresh_button_01.sub']],
                    [
                        'SetOverVisual',
                        [
                            'd:/ymir work/ui/game/guild/refresh_button_02.sub']],
                    [
                        'SetDownVisual',
                        [
                            'd:/ymir work/ui/game/guild/refresh_button_03.sub']],
                    [
                        'SetToolTipText',
                        [
                            'Yenile',
                            0,
                            -23]],
                    [
                        'SetEvent',
                        [
                            lambda : self.UpdateFileList()]]],
                []]]
        GuiParser(Gui, self.Gui)
        self.Gui[3].SetScrollBar(self.Gui[4])
        self.UpdateFileList()

    
    def UpdateFileList(self):
        
        try:
            aa = len(self.MetinList)
            for x in xrange(aa):
                del self.MetinList[0]
        except:
            pass

        self.Gui[3].RemoveAllItems()
        continue
        metinlist = []
        for i in metinlist:
            (x, y, z) = chr.GetPixelPosition(i)
            name = chr.GetNameByVID(i)
            self.Gui[3].AppendItem(Item('%s\t\t %s\t\t(%s, %s)' % (i, name, int(x) / 100, int(y) / 100)))
            metin_dict = {
                'VID': i,
                'NAME': name,
                'COORDX': x,
                'COORDY': y }
            self.MetinList.append(metin_dict)
        

    
    def YouwantaMetinHuh(self, type):
        ItemIndex = self.Gui[3].GetSelectedItem()
        if ItemIndex:
            pass
        1
        chat.AppendChat(chat.CHAT_TYPE_INFO, "Hicbir sey secmedin!")
        return None
        SelectedItem = ItemIndex.GetText().split('\t\t ')
        for i in self.MetinList:
            vid = i['VID']
            if vid == int(SelectedItem[0]):
                if type == 0:
                    self.Walk(i['COORDX'], i['COORDY'])
                elif type == 1:
                    self.Teleport(i['COORDX'], i['COORDY'])
                
            
        

    
    def Walk(self, x, y):
        myVid = player.GetMainCharacterIndex()
        (myx, myy, myz) = player.GetMainCharacterPosition()
        distance = 135
        if myx < x:
            self.aimx = int(x) - distance
        else:
            self.aimx = int(x) + distance
        if myy < y:
            self.aimy = int(y) - distance
        else:
            self.aimy = int(y) + distance
        chr.MoveToDestPosition(int(myVid), int(self.aimx), int(self.aimy))

    
    def Teleport(self, aimx, aimy):
        (TmpX, TmpY, Count) = GetTmpTeleport(aimx, aimy)
        TmpCount = 0
        while TmpCount < Count:
            (TmpX, TmpY, Crap) = GetTmpTeleport(aimx, aimy)
            chr.SetPixelPosition(int(TmpX), int(TmpY))
            TmpCount += 1
            self.Debug()
        chr.SetPixelPosition(int(aimx), int(aimy))
        self.Debug()

    
    def Debug(self):
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)



def GetTmpTeleport(DestX, DestY):
    (PlayerX, PlayerY, PlayerZ) = player.GetMainCharacterPosition()
    DifX = DestX - PlayerX
    DifY = DestY - PlayerY
    Vektor = DivideToFloat(2000, math.sqrt(DifX ** 2 + DifY ** 2))
    TempX = PlayerX + Vektor * DifX
    TempY = PlayerY + Vektor * DifY
    Count = DivideToFloat(DestX - PlayerX, Vektor * DifX)
    return (TempX, TempY, Count)


def DivideToFloat(x, y):
    
    try:
        return x * y ** -1
    except:
        return 0



def GuiParser(guiobjects, list):
    for object in guiobjects:
        Object = object[0][0]()
        if object[0][1] != '':
            Object.SetParent(list[object[0][1]])
        
        if object[1][0] + object[1][1] != 0:
            Object.SetSize(object[1][0], object[1][1])
        
        if object[2][0] + object[2][1] != 0:
            Object.SetPosition(object[2][0], object[2][1])
        
        for command in object[3]:
            cmd = command[0]
            attr = getattr(Object, cmd)
            if callable(attr):
                argument = command[1]
                lenght = len(argument)
                if lenght == 1:
                    if argument[0] == '':
                        attr()
                    else:
                        attr(argument[0])
                elif lenght == 2:
                    attr(argument[0], argument[1])
                elif lenght == 3:
                    attr(argument[0], argument[1], argument[2])
                elif lenght == 4:
                    attr(argument[0], argument[1], argument[2], argument[3])
                
            
        
        for flag in object[4]:
            Object.AddFlag(str(flag))
        
        Object.Show()
        list.append(Object)
    


class Item(ui.ListBoxEx.Item):
    
    def __init__(self, fileName):
        ui.ListBoxEx.Item.__init__(self)
        self.canLoad = 0
        self.text = fileName
        self.textLine = self._Item__CreateTextLine(fileName)

    
    def __del__(self):
        ui.ListBoxEx.Item.__del__(self)

    
    def GetText(self):
        return self.text

    
    def SetSize(self, width, height):
        ui.ListBoxEx.Item.SetSize(self, 6 * len(self.textLine.GetText()) + 4, height)

    
    def _Item__CreateTextLine(self, fileName):
        textLine = ui.TextLine()
        textLine.SetParent(self)
        textLine.SetPosition(0, 0)
        textLine.SetText(fileName)
        textLine.Show()
        return textLine


MetinFinder().Show()
