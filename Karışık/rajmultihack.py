import dbg
dbg.LogBox('mh zaladowany')
import chr
try:
    import playerm2g2 as player
    chr.GetPixelPosition = player.GetMainCharacterPosition #na globalu zastapic funkcje - chr.MoveToDestPosition(myvid, x, y) - ruch do pozycji myvid do z i y pozycja moba
                                                            #na globalu zastapic x, y, z = chr.GetPixelPosition(vid)- x,y,z to pozycja dowolnego vid
except:
    import player
try:
    import chatm2g as chat
except:
    import chat
try:
    import m2netm2g as net
except:
    import net    
import app
import time
import ui
bosy=(192,193,191,194,394,591,534,533,691,2191,1901,791,1304,2307,2206,2091)
cipa=0
kukloma=0
dokoftowaniewida=0

class ciulskoodkacki(ui.ThinBoard):
    def __init__(self):
        ui.ThinBoard.__init__(self)
        self.pozycjax = 5
        self.pozycjay = 15
        self.odstepy = 22
        self.odstepx = 44
        self.__pierdola_dupa()
    def __del__(self):
        ui.ThinBoard.__del__(self)
    def Destroy(self):
        self.Hide()
        return TRUE
    def Show(self):
        ui.ThinBoard.Show(self)
    def Close(self):
        self.Hide()
        return TRUE
    def _ciulskoodkacki__pierdola_dupa(self):
        self.SetPosition(100, 200)
        self.SetSize(210, 490)
        self.Close()
        self.AddFlag('float')
        self.AddFlag('movable')
        self.przyciski()
        self.teksty()
    def przyciski(self):
        self.ukryjokno = ui.Button()
        self.ukryjokno.SetParent(self)
        self.ukryjokno.SetPosition(0, 0)
        self.ukryjokno.SetUpVisual('d:/ymir work/ui/public/close_button_01.sub')
        self.ukryjokno.SetOverVisual('d:/ymir work/ui/public/close_button_02.sub')
        self.ukryjokno.SetDownVisual('d:/ymir work/ui/public/close_button_03.sub')
        self.ukryjokno.SetEvent(ui.__mem_func__(self.Hide))
        self.ukryjokno.Show()
        
        self.autopotystart = ui.ToggleButton()
        self.autopotystart.SetParent(self)
        self.autopotystart.SetPosition(self.pozycjax, self.pozycjay)
        self.autopotystart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.autopotystart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.autopotystart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.autopotystart.SetToggleUpEvent(ui.__mem_func__(self.autopotystopfunkcja))
        self.autopotystart.SetToggleDownEvent(ui.__mem_func__(self.autopotystartfunkacja))
        self.autopotystart.SetText('start')
        self.autopotystart.SetToolTipText('wlacza skrypt')
        self.autopotystart.Show()

        self.autopotystop = ui.Button()
        self.autopotystop.SetParent(self)
        self.autopotystop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay)
        self.autopotystop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.autopotystop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.autopotystop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.autopotystop.SetEvent(ui.__mem_func__(self.autopotystopfunkcja))
        self.autopotystop.SetText('stop')
        self.autopotystop.SetToolTipText('wylacza skrypt')
        self.autopotystop.Show()

        self.kon = ui.Button()
        self.kon.SetParent(self)
        self.kon.SetPosition(self.pozycjax, self.pozycjay+self.odstepy)
        self.kon.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        self.kon.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        self.kon.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        self.kon.SetEvent(ui.__mem_func__(self.konfunkcja))
        self.kon.SetText('wlaz i zlaz')
        self.kon.SetToolTipText('wlacza skrypt')
        self.kon.Show()

        self.wykrywaczgmstart = ui.ToggleButton()
        self.wykrywaczgmstart.SetParent(self)
        self.wykrywaczgmstart.SetPosition(self.pozycjax, self.pozycjay+(2*self.odstepy))
        self.wykrywaczgmstart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.wykrywaczgmstart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.wykrywaczgmstart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.wykrywaczgmstart.SetToggleUpEvent(ui.__mem_func__(self.wykrywaczgmstopfunkcja))
        self.wykrywaczgmstart.SetToggleDownEvent(ui.__mem_func__(self.wykrywaczgmstartfunkcja))
        self.wykrywaczgmstart.SetText('start')
        self.wykrywaczgmstart.SetToolTipText('wlacza skrypt')
        self.wykrywaczgmstart.Show()

        self.wykrywaczgmstop = ui.Button()
        self.wykrywaczgmstop.SetParent(self)
        self.wykrywaczgmstop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(2*self.odstepy))
        self.wykrywaczgmstop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.wykrywaczgmstop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.wykrywaczgmstop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.wykrywaczgmstop.SetEvent(ui.__mem_func__(self.wykrywaczgmstopfunkcja))
        self.wykrywaczgmstop.SetText('stop')
        self.wykrywaczgmstop.SetToolTipText('wylacza skrypt')
        self.wykrywaczgmstop.Show()

        self.wykrywaczgraczystart = ui.ToggleButton()
        self.wykrywaczgraczystart.SetParent(self)
        self.wykrywaczgraczystart.SetPosition(self.pozycjax, self.pozycjay+(3*self.odstepy))
        self.wykrywaczgraczystart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.wykrywaczgraczystart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.wykrywaczgraczystart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.wykrywaczgraczystart.SetToggleUpEvent(ui.__mem_func__(self.wykrywaczgraczystopfunkcja))
        self.wykrywaczgraczystart.SetToggleDownEvent(ui.__mem_func__(self.wykrywaczgraczystartfunkcja))
        self.wykrywaczgraczystart.SetText('start')
        self.wykrywaczgraczystart.SetToolTipText('wlacza skrypt')
        self.wykrywaczgraczystart.Show()

        self.wykrywaczgraczystop = ui.Button()
        self.wykrywaczgraczystop.SetParent(self)
        self.wykrywaczgraczystop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(3*self.odstepy))
        self.wykrywaczgraczystop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.wykrywaczgraczystop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.wykrywaczgraczystop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.wykrywaczgraczystop.SetEvent(ui.__mem_func__(self.wykrywaczgraczystopfunkcja))
        self.wykrywaczgraczystop.SetText('stop')
        self.wykrywaczgraczystop.SetToolTipText('wylacza skrypt')
        self.wykrywaczgraczystop.Show()

        self.wykrywaczmetkowstart = ui.ToggleButton()
        self.wykrywaczmetkowstart.SetParent(self)
        self.wykrywaczmetkowstart.SetPosition(self.pozycjax, self.pozycjay+(4*self.odstepy))
        self.wykrywaczmetkowstart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.wykrywaczmetkowstart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.wykrywaczmetkowstart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.wykrywaczmetkowstart.SetToggleUpEvent(ui.__mem_func__(self.wykrywaczmetkowstopfunkcja))
        self.wykrywaczmetkowstart.SetToggleDownEvent(ui.__mem_func__(self.wykrywaczmetkowstartfunkcja))
        self.wykrywaczmetkowstart.SetText('start')
        self.wykrywaczmetkowstart.SetToolTipText('wlacza skrypt')
        self.wykrywaczmetkowstart.Show()

        self.wykrywaczmetkowstop = ui.Button()
        self.wykrywaczmetkowstop.SetParent(self)
        self.wykrywaczmetkowstop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(4*self.odstepy))
        self.wykrywaczmetkowstop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.wykrywaczmetkowstop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.wykrywaczmetkowstop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.wykrywaczmetkowstop.SetEvent(ui.__mem_func__(self.wykrywaczmetkowstopfunkcja))
        self.wykrywaczmetkowstop.SetText('stop')
        self.wykrywaczmetkowstop.SetToolTipText('wylacza skrypt')
        self.wykrywaczmetkowstop.Show()

        self.autopickupstart = ui.ToggleButton()
        self.autopickupstart.SetParent(self)
        self.autopickupstart.SetPosition(self.pozycjax, self.pozycjay+(5*self.odstepy))
        self.autopickupstart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.autopickupstart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.autopickupstart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.autopickupstart.SetToggleUpEvent(ui.__mem_func__(self.autopickupstopfunkcja))
        self.autopickupstart.SetToggleDownEvent(ui.__mem_func__(self.autopickupstartfunkcja))
        self.autopickupstart.SetText('start')
        self.autopickupstart.SetToolTipText('wlacza skrypt')
        self.autopickupstart.Show()

        self.autopickupstop = ui.Button()
        self.autopickupstop.SetParent(self)
        self.autopickupstop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(5*self.odstepy))
        self.autopickupstop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.autopickupstop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.autopickupstop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.autopickupstop.SetEvent(ui.__mem_func__(self.autopickupstopfunkcja))
        self.autopickupstop.SetText('stop')
        self.autopickupstop.SetToolTipText('wylacza skrypt')
        self.autopickupstop.Show()

        self.slot1234start = ui.ToggleButton()
        self.slot1234start.SetParent(self)
        self.slot1234start.SetPosition(self.pozycjax, self.pozycjay+(6*self.odstepy))
        self.slot1234start.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.slot1234start.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.slot1234start.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.slot1234start.SetToggleUpEvent(ui.__mem_func__(self.slot1234stopfunkcja))
        self.slot1234start.SetToggleDownEvent(ui.__mem_func__(self.slot1234startfunkcja))
        self.slot1234start.SetText('start')
        self.slot1234start.SetToolTipText('wlacza skrypt')
        self.slot1234start.Show()

        self.slot1234stop = ui.Button()
        self.slot1234stop.SetParent(self)
        self.slot1234stop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(6*self.odstepy))
        self.slot1234stop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.slot1234stop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.slot1234stop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.slot1234stop.SetEvent(ui.__mem_func__(self.slot1234stopfunkcja))
        self.slot1234stop.SetText('stop')
        self.slot1234stop.SetToolTipText('wylacza skrypt')
        self.slot1234stop.Show()

        self.slotweq12345start = ui.ToggleButton()
        self.slotweq12345start.SetParent(self)
        self.slotweq12345start.SetPosition(self.pozycjax, self.pozycjay+(7*self.odstepy))
        self.slotweq12345start.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.slotweq12345start.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.slotweq12345start.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.slotweq12345start.SetToggleUpEvent(ui.__mem_func__(self.slotweq12345stopfunkcja))
        self.slotweq12345start.SetToggleDownEvent(ui.__mem_func__(self.slotweq12345startfunkcja))
        self.slotweq12345start.SetText('start')
        self.slotweq12345start.SetToolTipText('wlacza skrypt')
        self.slotweq12345start.Show()

        self.slotweq12345stop = ui.Button()
        self.slotweq12345stop.SetParent(self)
        self.slotweq12345stop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(7*self.odstepy))
        self.slotweq12345stop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.slotweq12345stop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.slotweq12345stop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.slotweq12345stop.SetEvent(ui.__mem_func__(self.slotweq12345stopfunkcja))
        self.slotweq12345stop.SetText('stop')
        self.slotweq12345stop.SetToolTipText('wylacza skrypt')
        self.slotweq12345stop.Show()

        self.autopelestart = ui.ToggleButton()
        self.autopelestart.SetParent(self)
        self.autopelestart.SetPosition(self.pozycjax, self.pozycjay+(8*self.odstepy))
        self.autopelestart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.autopelestart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.autopelestart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.autopelestart.SetToggleUpEvent(ui.__mem_func__(self.autopelestopfunkcja))
        self.autopelestart.SetToggleDownEvent(ui.__mem_func__(self.autopelestartfunkcja))
        self.autopelestart.SetText('start')
        self.autopelestart.SetToolTipText('wlacza skrypt')
        self.autopelestart.Show()

        self.autopelestop = ui.Button()
        self.autopelestop.SetParent(self)
        self.autopelestop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(8*self.odstepy))
        self.autopelestop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.autopelestop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.autopelestop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.autopelestop.SetEvent(ui.__mem_func__(self.autopelestopfunkcja))
        self.autopelestop.SetText('stop')
        self.autopelestop.SetToolTipText('wylacza skrypt')
        self.autopelestop.Show()

        self.megapelestart = ui.ToggleButton()
        self.megapelestart.SetParent(self)
        self.megapelestart.SetPosition(self.pozycjax, self.pozycjay+(9*self.odstepy))
        self.megapelestart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.megapelestart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.megapelestart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.megapelestart.SetToggleUpEvent(ui.__mem_func__(self.megapelestopfunkcja))
        self.megapelestart.SetToggleDownEvent(ui.__mem_func__(self.megapelestartfunkcja))
        self.megapelestart.SetText('start')
        self.megapelestart.SetToolTipText('wlacza skrypt')
        self.megapelestart.Show()

        self.megapelestop = ui.Button()
        self.megapelestop.SetParent(self)
        self.megapelestop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(9*self.odstepy))
        self.megapelestop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.megapelestop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.megapelestop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.megapelestop.SetEvent(ui.__mem_func__(self.megapelestopfunkcja))
        self.megapelestop.SetText('stop')
        self.megapelestop.SetToolTipText('wylacza skrypt')
        self.megapelestop.Show()

        self.moblockstart = ui.ToggleButton()
        self.moblockstart.SetParent(self)
        self.moblockstart.SetPosition(self.pozycjax, self.pozycjay+(10*self.odstepy))
        self.moblockstart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.moblockstart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.moblockstart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.moblockstart.SetToggleUpEvent(ui.__mem_func__(self.moblockstopfunkcja))
        self.moblockstart.SetToggleDownEvent(ui.__mem_func__(self.moblockstartfunkcja))
        self.moblockstart.SetText('start')
        self.moblockstart.SetToolTipText('wlacza skrypt')
        self.moblockstart.Show()

        self.moblockstop = ui.Button()
        self.moblockstop.SetParent(self)
        self.moblockstop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(10*self.odstepy))
        self.moblockstop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.moblockstop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.moblockstop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.moblockstop.SetEvent(ui.__mem_func__(self.moblockstopfunkcja))
        self.moblockstop.SetText('stop')
        self.moblockstop.SetToolTipText('wylacza skrypt')
        self.moblockstop.Show()

        self.dopalaczestart = ui.ToggleButton()
        self.dopalaczestart.SetParent(self)
        self.dopalaczestart.SetPosition(self.pozycjax, self.pozycjay+(11*self.odstepy))
        self.dopalaczestart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.dopalaczestart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.dopalaczestart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.dopalaczestart.SetToggleUpEvent(ui.__mem_func__(self.dopalaczestopfunkcja))
        self.dopalaczestart.SetToggleDownEvent(ui.__mem_func__(self.dopalaczestartfunkcja))
        self.dopalaczestart.SetText('start')
        self.dopalaczestart.SetToolTipText('wlacza skrypt')
        self.dopalaczestart.Show()

        self.dopalaczestop = ui.Button()
        self.dopalaczestop.SetParent(self)
        self.dopalaczestop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(11*self.odstepy))
        self.dopalaczestop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.dopalaczestop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.dopalaczestop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.dopalaczestop.SetEvent(ui.__mem_func__(self.dopalaczestopfunkcja))
        self.dopalaczestop.SetText('stop')
        self.dopalaczestop.SetToolTipText('wylacza skrypt')
        self.dopalaczestop.Show()

        self.playerlockstart = ui.ToggleButton()
        self.playerlockstart.SetParent(self)
        self.playerlockstart.SetPosition(self.pozycjax, self.pozycjay+(12*self.odstepy))
        self.playerlockstart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.playerlockstart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.playerlockstart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.playerlockstart.SetToggleUpEvent(ui.__mem_func__(self.playerlockstopfunkcja))
        self.playerlockstart.SetToggleDownEvent(ui.__mem_func__(self.playerlockstartfunkcja))
        self.playerlockstart.SetText('start')
        self.playerlockstart.SetToolTipText('wlacza skrypt')
        self.playerlockstart.Show()

        self.playerlockstop = ui.Button()
        self.playerlockstop.SetParent(self)
        self.playerlockstop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(12*self.odstepy))
        self.playerlockstop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.playerlockstop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.playerlockstop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.playerlockstop.SetEvent(ui.__mem_func__(self.playerlockstopfunkcja))
        self.playerlockstop.SetText('stop')
        self.playerlockstop.SetToolTipText('wylacza skrypt')
        self.playerlockstop.Show()

        self.targetlockstart = ui.ToggleButton()
        self.targetlockstart.SetParent(self)
        self.targetlockstart.SetPosition(self.pozycjax, self.pozycjay+(13*self.odstepy))
        self.targetlockstart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.targetlockstart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.targetlockstart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.targetlockstart.SetToggleUpEvent(ui.__mem_func__(self.targetlockstopfunkcja))
        self.targetlockstart.SetToggleDownEvent(ui.__mem_func__(self.targetlockstartfunkcja))
        self.targetlockstart.SetText('start')
        self.targetlockstart.SetToolTipText('wlacza skrypt')
        self.targetlockstart.Show()

        self.targetlockstop = ui.Button()
        self.targetlockstop.SetParent(self)
        self.targetlockstop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(13*self.odstepy))
        self.targetlockstop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.targetlockstop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.targetlockstop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.targetlockstop.SetEvent(ui.__mem_func__(self.targetlockstopfunkcja))
        self.targetlockstop.SetText('stop')
        self.targetlockstop.SetToolTipText('wylacza skrypt')
        self.targetlockstop.Show()

        self.targetinfo = ui.Button()
        self.targetinfo.SetParent(self)
        self.targetinfo.SetPosition(self.pozycjax, self.pozycjay+(14*self.odstepy))
        self.targetinfo.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        self.targetinfo.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        self.targetinfo.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        self.targetinfo.SetEvent(ui.__mem_func__(self.targetinfofunkcja))
        self.targetinfo.SetText('start')
        self.targetinfo.SetToolTipText('wlacza skrypt')
        self.targetinfo.Show()

        self.teleport = ui.Button()
        self.teleport.SetParent(self)
        self.teleport.SetPosition(self.pozycjax, self.pozycjay+(15*self.odstepy))
        self.teleport.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        self.teleport.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        self.teleport.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        self.teleport.SetEvent(ui.__mem_func__(self.teleportfunkcja))
        self.teleport.SetText('start')
        self.teleport.SetToolTipText('wlacza skrypt')
        self.teleport.Show()

        self.zoomnofog = ui.Button()
        self.zoomnofog.SetParent(self)
        self.zoomnofog.SetPosition(self.pozycjax, self.pozycjay+(16*self.odstepy))
        self.zoomnofog.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        self.zoomnofog.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        self.zoomnofog.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        self.zoomnofog.SetEvent(ui.__mem_func__(self.zoomnofogfunkcja))
        self.zoomnofog.SetText('start')
        self.zoomnofog.SetToolTipText('wlacza skrypt')
        self.zoomnofog.Show()

        self.lvlbotstart = ui.ToggleButton()
        self.lvlbotstart.SetParent(self)
        self.lvlbotstart.SetPosition(self.pozycjax, self.pozycjay+(17*self.odstepy))
        self.lvlbotstart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.lvlbotstart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.lvlbotstart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.lvlbotstart.SetToggleUpEvent(ui.__mem_func__(self.lvlbotstopfunkcja))
        self.lvlbotstart.SetToggleDownEvent(ui.__mem_func__(self.lvlbotstartfunkcja))
        self.lvlbotstart.SetText('start')
        self.lvlbotstart.SetToolTipText('wlacza skrypt')
        self.lvlbotstart.Show()

        self.lvlbotstop = ui.Button()
        self.lvlbotstop.SetParent(self)
        self.lvlbotstop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(17*self.odstepy))
        self.lvlbotstop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.lvlbotstop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.lvlbotstop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.lvlbotstop.SetEvent(ui.__mem_func__(self.lvlbotstopfunkcja))
        self.lvlbotstop.SetText('stop')
        self.lvlbotstop.SetToolTipText('wylacza skrypt')
        self.lvlbotstop.Show()

        self.autoatakstart = ui.ToggleButton()
        self.autoatakstart.SetParent(self)
        self.autoatakstart.SetPosition(self.pozycjax, self.pozycjay+(18*self.odstepy))
        self.autoatakstart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.autoatakstart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.autoatakstart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.autoatakstart.SetToggleUpEvent(ui.__mem_func__(self.autoatakstopfunkcja))
        self.autoatakstart.SetToggleDownEvent(ui.__mem_func__(self.autoatakstartfunkcja))
        self.autoatakstart.SetText('start')
        self.autoatakstart.SetToolTipText('wlacza skrypt')
        self.autoatakstart.Show()

        self.autoatakstop = ui.Button()
        self.autoatakstop.SetParent(self)
        self.autoatakstop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(18*self.odstepy))
        self.autoatakstop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.autoatakstop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.autoatakstop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.autoatakstop.SetEvent(ui.__mem_func__(self.autoatakstopfunkcja))
        self.autoatakstop.SetText('stop')
        self.autoatakstop.SetToolTipText('wylacza skrypt')
        self.autoatakstop.Show()

        self.autorestartstart = ui.ToggleButton()
        self.autorestartstart.SetParent(self)
        self.autorestartstart.SetPosition(self.pozycjax, self.pozycjay+(19*self.odstepy))
        self.autorestartstart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.autorestartstart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.autorestartstart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.autorestartstart.SetToggleUpEvent(ui.__mem_func__(self.autorestartstopfunkcja))
        self.autorestartstart.SetToggleDownEvent(ui.__mem_func__(self.autorestartstartfunkcja))
        self.autorestartstart.SetText('start')
        self.autorestartstart.SetToolTipText('wlacza skrypt')
        self.autorestartstart.Show()

        self.autorestartstop = ui.Button()
        self.autorestartstop.SetParent(self)
        self.autorestartstop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(19*self.odstepy))
        self.autorestartstop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.autorestartstop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.autorestartstop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.autorestartstop.SetEvent(ui.__mem_func__(self.autorestartstopfunkcja))
        self.autorestartstop.SetText('stop')
        self.autorestartstop.SetToolTipText('wylacza skrypt')
        self.autorestartstop.Show()

        self.horsestart = ui.ToggleButton()
        self.horsestart.SetParent(self)
        self.horsestart.SetPosition(self.pozycjax, self.pozycjay+(20*self.odstepy))
        self.horsestart.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.horsestart.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.horsestart.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.horsestart.SetToggleUpEvent(ui.__mem_func__(self.horsestopfunkcja))
        self.horsestart.SetToggleDownEvent(ui.__mem_func__(self.horsestartfunkcja))
        self.horsestart.SetText('start')
        self.horsestart.SetToolTipText('wlacza skrypt')
        self.horsestart.Show()

        self.horsestop = ui.Button()
        self.horsestop.SetParent(self)
        self.horsestop.SetPosition(self.pozycjax+self.odstepx, self.pozycjay+(20*self.odstepy))
        self.horsestop.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
        self.horsestop.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
        self.horsestop.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
        self.horsestop.SetEvent(ui.__mem_func__(self.horsestopfunkcja))
        self.horsestop.SetText('stop')
        self.horsestop.SetToolTipText('wylacza skrypt')
        self.horsestop.Show()

        

    def teksty(self):
        self.tekst1 = ui.TextLine()
        self.tekst1.SetParent(self)
        self.tekst1.SetDefaultFontName()
        self.tekst1.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2)
        self.tekst1.SetFeather()
        self.tekst1.SetText('auto poty')
        self.tekst1.SetOutline()
        self.tekst1.Show()

        self.tekst2 = ui.TextLine()
        self.tekst2.SetParent(self)
        self.tekst2.SetDefaultFontName()
        self.tekst2.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+self.odstepy)
        self.tekst2.SetFeather()
        self.tekst2.SetText('curik kon zwierz')
        self.tekst2.SetOutline()
        self.tekst2.Show()

        self.tekst3 = ui.TextLine()
        self.tekst3.SetParent(self)
        self.tekst3.SetDefaultFontName()
        self.tekst3.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(2*self.odstepy))
        self.tekst3.SetFeather()
        self.tekst3.SetText('wykrywacz gm')
        self.tekst3.SetOutline()
        self.tekst3.Show()

        self.tekst4 = ui.TextLine()
        self.tekst4.SetParent(self)
        self.tekst4.SetDefaultFontName()
        self.tekst4.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(3*self.odstepy))
        self.tekst4.SetFeather()
        self.tekst4.SetText('wykrywacz graczy')
        self.tekst4.SetOutline()
        self.tekst4.Show()

        self.tekst5 = ui.TextLine()
        self.tekst5.SetParent(self)
        self.tekst5.SetDefaultFontName()
        self.tekst5.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(4*self.odstepy))
        self.tekst5.SetFeather()
        self.tekst5.SetText('wykrywacz metkow')
        self.tekst5.SetOutline()
        self.tekst5.Show()

        self.tekst6 = ui.TextLine()
        self.tekst6.SetParent(self)
        self.tekst6.SetDefaultFontName()
        self.tekst6.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(5*self.odstepy))
        self.tekst6.SetFeather()
        self.tekst6.SetText('auto pickup')
        self.tekst6.SetOutline()
        self.tekst6.Show()

        self.tekst7 = ui.TextLine()
        self.tekst7.SetParent(self)
        self.tekst7.SetDefaultFontName()
        self.tekst7.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(6*self.odstepy))
        self.tekst7.SetFeather()
        self.tekst7.SetText('slot 1,2,3,4')
        self.tekst7.SetOutline()
        self.tekst7.Show()

        self.tekst8 = ui.TextLine()
        self.tekst8.SetParent(self)
        self.tekst8.SetDefaultFontName()
        self.tekst8.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(7*self.odstepy))
        self.tekst8.SetFeather()
        self.tekst8.SetText('slot w eq 1,2,3,4,5')
        self.tekst8.SetOutline()
        self.tekst8.Show()

        self.tekst9 = ui.TextLine()
        self.tekst9.SetParent(self)
        self.tekst9.SetDefaultFontName()
        self.tekst9.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(8*self.odstepy))
        self.tekst9.SetFeather()
        self.tekst9.SetText('auto pele')
        self.tekst9.SetOutline()
        self.tekst9.Show()

        self.tekst10 = ui.TextLine()
        self.tekst10.SetParent(self)
        self.tekst10.SetDefaultFontName()
        self.tekst10.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(9*self.odstepy))
        self.tekst10.SetFeather()
        self.tekst10.SetText('mega pele')
        self.tekst10.SetOutline()
        self.tekst10.Show()

        self.tekst11 = ui.TextLine()
        self.tekst11.SetParent(self)
        self.tekst11.SetDefaultFontName()
        self.tekst11.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(10*self.odstepy))
        self.tekst11.SetFeather()
        self.tekst11.SetText('mob lock')
        self.tekst11.SetOutline()
        self.tekst11.Show()

        self.tekst12 = ui.TextLine()
        self.tekst12.SetParent(self)
        self.tekst12.SetDefaultFontName()
        self.tekst12.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(11*self.odstepy))
        self.tekst12.SetFeather()
        self.tekst12.SetText('dopalacze')
        self.tekst12.SetOutline()
        self.tekst12.Show()

        self.tekst13 = ui.TextLine()
        self.tekst13.SetParent(self)
        self.tekst13.SetDefaultFontName()
        self.tekst13.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(12*self.odstepy))
        self.tekst13.SetFeather()
        self.tekst13.SetText('player lock')
        self.tekst13.SetOutline()
        self.tekst13.Show()

        self.tekst14 = ui.TextLine()
        self.tekst14.SetParent(self)
        self.tekst14.SetDefaultFontName()
        self.tekst14.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(13*self.odstepy))
        self.tekst14.SetFeather()
        self.tekst14.SetText('target lock')
        self.tekst14.SetOutline()
        self.tekst14.Show()

        self.tekst15 = ui.TextLine()
        self.tekst15.SetParent(self)
        self.tekst15.SetDefaultFontName()
        self.tekst15.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(14*self.odstepy))
        self.tekst15.SetFeather()
        self.tekst15.SetText('target info')
        self.tekst15.SetOutline()
        self.tekst15.Show()

        self.tekst16 = ui.TextLine()
        self.tekst16.SetParent(self)
        self.tekst16.SetDefaultFontName()
        self.tekst16.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(15*self.odstepy))
        self.tekst16.SetFeather()
        self.tekst16.SetText('teleport')
        self.tekst16.SetOutline()
        self.tekst16.Show()

        self.tekst17 = ui.TextLine()
        self.tekst17.SetParent(self)
        self.tekst17.SetDefaultFontName()
        self.tekst17.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(16*self.odstepy))
        self.tekst17.SetFeather()
        self.tekst17.SetText('zoom i nofog')
        self.tekst17.SetOutline()
        self.tekst17.Show()

        self.tekst18 = ui.TextLine()
        self.tekst18.SetParent(self)
        self.tekst18.SetDefaultFontName()
        self.tekst18.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(17*self.odstepy))
        self.tekst18.SetFeather()
        self.tekst18.SetText('lvl bot')
        self.tekst18.SetOutline()
        self.tekst18.Show()

        self.tekst19 = ui.TextLine()
        self.tekst19.SetParent(self)
        self.tekst19.SetDefaultFontName()
        self.tekst19.SetPosition(20, 2)
        self.tekst19.SetFeather()
        self.tekst19.SetText('multihack by kag321 v1.1')
        self.tekst19.SetOutline()
        self.tekst19.Show()

        self.tekst20 = ui.TextLine()
        self.tekst20.SetParent(self)
        self.tekst20.SetDefaultFontName()
        self.tekst20.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(18*self.odstepy))
        self.tekst20.SetFeather()
        self.tekst20.SetText('auto atak z rotacja')
        self.tekst20.SetOutline()
        self.tekst20.Show()

        self.tekst21 = ui.TextLine()
        self.tekst21.SetParent(self)
        self.tekst21.SetDefaultFontName()
        self.tekst21.SetPosition(self.pozycjax+2+(2*self.odstepx), self.pozycjay+2+(19*self.odstepy))
        self.tekst21.SetFeather()
        self.tekst21.SetText('autorestart')
        self.tekst21.SetOutline()
        self.tekst21.Show()
        
    def teleportfunkcja(self):
        kurwiszonka.Show()
    def autopotystartfunkacja(self):
        self.autopotystartfunkacjaczas=czas()
        self.autopotystartfunkacjaczas.otwoz(0.5)
        self.autopotystartfunkacjaczas.czas1(self.autopotystartfunkacja)
        maxhp = player.GetStatus(player.MAX_HP)
        aktualnehp = player.GetStatus(player.HP)
        if (float(aktualnehp) / float(maxhp)) * 100 < int(90):
            for i in xrange(90):
                a = player.GetItemIndex(i)
                if a == 27001 or a == 1940 or a == 27003:
                    net.SendItemUsePacket(i)
                    break
        maxmp = player.GetStatus(player.MAX_SP)
        aktualnemp = player.GetStatus(player.SP)
        if (float(aktualnemp) / float(maxmp)) * 100 < int(90):
            for i in xrange(90):
                a = player.GetItemIndex(i)
                if a==27004 or a==1941 or a==27006:
                    net.SendItemUsePacket(i)
                    break
    def autopotystopfunkcja(self):
        self.autopotystartfunkacjaczas=czas()
        self.autopotystartfunkacjaczas.otwoz(100000000.0)
        self.autopotystartfunkacjaczas.czas1(self.autopotystartfunkacja)
    def konfunkcja(self):
        net.SendChatPacket('/ride')
    def wykrywaczgmstartfunkcja(self):
        self.wykrywaczgmstartfunkcjaczas=czas()
        self.wykrywaczgmstartfunkcjaczas.otwoz(20.0)
        self.wykrywaczgmstartfunkcjaczas.czas1(self.wykrywaczgmstartfunkcja)
        o=player.GetMainCharacterIndex()
        for i in xrange(o-50000, o+100000):
            if chr.IsGameMaster(i):
                dystans = player.GetCharacterDistance(i)
                imie=chr.GetNameByVID(i)
                dbg.LogBox(str(imie)+'  '+str(int(dystans)))
    def wykrywaczgmstopfunkcja(self):
        self.wykrywaczgmstartfunkcjaczas=czas()
        self.wykrywaczgmstartfunkcjaczas.otwoz(100000000.0)
        self.wykrywaczgmstartfunkcjaczas.czas1(self.wykrywaczgmstartfunkcja)
    def wykrywaczgraczystartfunkcja(self):
        self.wykrywaczgraczystartfunkcjaczas=czas()
        self.wykrywaczgraczystartfunkcjaczas.otwoz(20.0)
        self.wykrywaczgraczystartfunkcjaczas.czas1(self.wykrywaczgraczystartfunkcja)
        o=player.GetMainCharacterIndex()
        for i in xrange(o-50000, o+100000):
            dystans = player.GetCharacterDistance(i) 
            if dystans > 0 and dystans < 3000:
                a = chr.GetInstanceType(i)
                if a==6:
                    imie=chr.GetNameByVID(i)
                    dbg.LogBox(str(imie)+'  '+str(int(dystans)))
                    
    def wykrywaczgraczystopfunkcja(self):
        self.wykrywaczgraczystartfunkcjaczas=czas()
        self.wykrywaczgraczystartfunkcjaczas.otwoz(100000000.0)
        self.wykrywaczgraczystartfunkcjaczas.czas1(self.wykrywaczgraczystartfunkcja)
    def wykrywaczmetkowstartfunkcja(self):
        b = 0
        self.wykrywaczmetkowstartfunkcjaczas=czas()
        self.wykrywaczmetkowstartfunkcjaczas.otwoz(10.0)
        self.wykrywaczmetkowstartfunkcjaczas.czas1(self.wykrywaczmetkowstartfunkcja)
        o=player.GetMainCharacterIndex()
        for i in xrange(o-500000, o+50000):
            dystans = player.GetCharacterDistance(i) 
            if dystans > 0:
                a = chr.GetInstanceType(i)
                if a==2:
                    imie=chr.GetNameByVID(i)
                    chr.SelectInstance(i)
                    x, y, z = chr.GetPixelPosition(i)
                    if b == 0:
                        dupek.eeee(x,y,z,imie)
                        dupek.Show()
                    if b == 1:
                        dupek1.eeee(x,y,z,imie)
                        dupek1.Show()
                    if b == 2:
                        dupek2.eeee(x,y,z,imie)
                        dupek2.Show()
                    b=b+1
                if a==0:
                    chr.SelectInstance(i)
                    g=chr.GetRace(i)
                    for k in bosy:
                        if g==k:
                            imie=chr.GetNameByVID(i)
                            chr.SelectInstance(i)
                            x, y, z = chr.GetPixelPosition(i)
                            if b == 0:
                                dupek.eeee(x,y,z,imie)
                                dupek.Show()
                            if b == 1:
                                dupek1.eeee(x,y,z,imie)
                                dupek1.Show()
                            if b == 2:
                                dupek2.eeee(x,y,z,imie)
                                dupek2.Show()
                            b=b+1
                            
                        
    def wykrywaczmetkowstopfunkcja(self):
        self.wykrywaczmetkowstartfunkcjaczas=czas()
        self.wykrywaczmetkowstartfunkcjaczas.otwoz(100000000.0)
        self.wykrywaczmetkowstartfunkcjaczas.czas1(self.wykrywaczmetkowstartfunkcja)
    def autopickupstartfunkcja(self):
        self.autopickupstartfunkcjaczas=czas()
        self.autopickupstartfunkcjaczas.otwoz(0.5)
        self.autopickupstartfunkcjaczas.czas1(self.autopickupstartfunkcja)
        player.PickCloseItem()
    def autopickupstopfunkcja(self):
        self.autopickupstartfunkcjaczas=czas()
        self.autopickupstartfunkcjaczas.otwoz(100000000.0)
        self.autopickupstartfunkcjaczas.czas1(self.autopickupstartfunkcja)
    def slot1234startfunkcja(self):
        self.slot1234startfunkcjaczas=czas()
        self.slot1234startfunkcjaczas.otwoz(5.0)
        self.slot1234startfunkcjaczas.czas1(self.slot1234startfunkcja)
        player.RequestUseLocalQuickSlot(0)
        player.RequestUseLocalQuickSlot(0)
        player.RequestUseLocalQuickSlot(1)
        player.RequestUseLocalQuickSlot(1)
        player.RequestUseLocalQuickSlot(2)
        player.RequestUseLocalQuickSlot(2)
        player.RequestUseLocalQuickSlot(3)
        player.RequestUseLocalQuickSlot(3)
    def slot1234stopfunkcja(self):
        self.slot1234startfunkcjaczas=czas()
        self.slot1234startfunkcjaczas.otwoz(100000000.0)
        self.slot1234startfunkcjaczas.czas1(self.slot1234startfunkcja)
    def slotweq12345startfunkcja(self):
        self.slotweq12345startfunkcjaczas=czas()
        self.slotweq12345startfunkcjaczas.otwoz(180.0)
        self.slotweq12345startfunkcjaczas.czas1(self.slotweq12345startfunkcja)
        for i in xrange(10):
            net.SendItemUsePacket(i)
    def slotweq12345stopfunkcja(self):
        self.slotweq12345startfunkcjaczas=czas()
        self.slotweq12345startfunkcjaczas.otwoz(100000000.0)
        self.slotweq12345startfunkcjaczas.czas1(self.slotweq12345startfunkcja)
    def autopelestartfunkcja(self):
        self.autopelestartfunkcjaczas=czas()
        self.autopelestartfunkcjaczas.otwoz(10.0)
        self.autopelestartfunkcjaczas.czas1(self.autopelestartfunkcja)
        for i in xrange(90):
            a = player.GetItemIndex(i)
            if a==70038:
                net.SendItemUsePacket(i)
                break
    def autopelestopfunkcja(self):
        self.autopelestartfunkcjaczas=czas()
        self.autopelestartfunkcjaczas.otwoz(100000000.0)
        self.autopelestartfunkcjaczas.czas1(self.autopelestartfunkcja)
    def megapelestartfunkcja(self):
        global cipa
        self.megapelestartfunkcjaczas=czas()
        self.megapelestartfunkcjaczas.otwoz(0.2)
        self.megapelestartfunkcjaczas.czas1(self.megapelestartfunkcja)
        myVid = player.GetMainCharacterIndex()
        ciulsko = -1
        for i in xrange(90):
            b=player.GetItemIndex(i)
            if b==70038:
                ciulsko=i
        a=1
        while a:
            x, y, z = player.GetMainCharacterPosition()
            if cipa == 0:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x) - 2000, int(y), int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 1:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x) - 2000, int(y), int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                net.SendItemUsePacket(ciulsko)
                net.SendItemUsePacket(ciulsko)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 2:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x) + 2000, int(y), int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 3:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x) + 2000, int(y), int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 4:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x), int(y) - 2000, int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 5:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x), int(y) - 2000, int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                net.SendItemUsePacket(ciulsko)
                net.SendItemUsePacket(ciulsko)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 6:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x), int(y) + 2000, int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 7:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x), int(y) + 2000, int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 8:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x) + 2000, int(y), int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 9:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x) + 2000, int(y), int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                net.SendItemUsePacket(ciulsko)
                net.SendItemUsePacket(ciulsko)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 10:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x) - 2000, int(y), int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 11:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x) - 2000, int(y), int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 12:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x), int(y) + 2000, int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 13:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x), int(y) + 2000, int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                net.SendItemUsePacket(ciulsko)
                net.SendItemUsePacket(ciulsko)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 14:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x), int(y) - 2000, int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                a = 0
                cipa = cipa + 1
                continue
            if cipa == 15:
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(x), int(y) - 2000, int(z))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                net.SendItemUsePacket(ciulsko)
                net.SendItemUsePacket(ciulsko)
                a = 0
                cipa = 0
                self.megapelestartfunkcjaczas=czas()
                self.megapelestartfunkcjaczas.otwoz(20.0)
                self.megapelestartfunkcjaczas.czas1(self.megapelestartfunkcja)
                continue
    def megapelestopfunkcja(self):
        self.megapelestartfunkcjaczas=czas()
        self.megapelestartfunkcjaczas.otwoz(100000000.0)
        self.megapelestartfunkcjaczas.czas1(self.megapelestartfunkcja)
    def moblockstartfunkcja(self):
        self.moblockstartfunkcjaczas=czas()
        self.moblockstartfunkcjaczas.otwoz(20.0)
        self.moblockstartfunkcjaczas.czas1(self.moblockstartfunkcja)
        o=player.GetMainCharacterIndex()
        x, y, z = player.GetMainCharacterPosition()
        for i in xrange(o-200000, o+100000, 2):
            dystans = player.GetCharacterDistance(i) 
            if dystans > 0 and dystans < 3400:
                if chr.IsEnemy(i):
                    chr.SelectInstance(i)
                    chr.SetPixelPosition(int(x), int(y), int(z))
    def moblockstopfunkcja(self):
        self.moblockstartfunkcjaczas=czas()
        self.moblockstartfunkcjaczas.otwoz(100000000.0)
        self.moblockstartfunkcjaczas.czas1(self.moblockstartfunkcja)
    def dopalaczestartfunkcja(self):
        self.dopalaczestartfunkcjaczas=czas()
        self.dopalaczestartfunkcjaczas.otwoz(180.0)
        self.dopalaczestartfunkcjaczas.czas1(self.dopalaczestartfunkcja)
        for i in xrange(90):
            a = player.GetItemIndex(i)
            if a == 50823 or a == 50824 or a == 50821 or a == 50825 or a== 50822:
                net.SendItemUsePacket(i)
    def dopalaczestopfunkcja(self):
        self.dopalaczestartfunkcjaczas=czas()
        self.dopalaczestartfunkcjaczas.otwoz(100000000.0)
        self.dopalaczestartfunkcjaczas.czas1(self.dopalaczestartfunkcja)
    def playerlockstartfunkcja(self):
        self.playerlockstartfunkcjaczas=czas()
        self.playerlockstartfunkcjaczas.otwoz(20.0)
        self.playerlockstartfunkcjaczas.czas1(self.playerlockstartfunkcja)
        o=player.GetMainCharacterIndex()
        x, y, z = player.GetMainCharacterPosition()
        for i in xrange(o-50000, o+100000):
            dystans = player.GetCharacterDistance(i) 
            if dystans > 0:
                a = chr.GetInstanceType(i)
                if a==6:
                    chr.SelectInstance(i)
                    chr.SetPixelPosition(int(x), int(y), int(z))
    def playerlockstopfunkcja(self):
        self.playerlockstartfunkcjaczas=czas()
        self.playerlockstartfunkcjaczas.otwoz(100000000.0)
        self.playerlockstartfunkcjaczas.czas1(self.playerlockstartfunkcja)
    def targetlockstartfunkcja(self):
        self.targetlockstartfunkcjaczas=czas()
        self.targetlockstartfunkcjaczas.otwoz(0.5)
        self.targetlockstartfunkcjaczas.czas1(self.targetlockstartfunkcja)
        x, y, z = player.GetMainCharacterPosition()
        i = player.GetTargetVID()
        chr.SelectInstance(i)
        chr.SetPixelPosition(int(x), int(y), int(z))
    def targetlockstopfunkcja(self):
        self.targetlockstartfunkcjaczas=czas()
        self.targetlockstartfunkcjaczas.otwoz(100000000.0)
        self.targetlockstartfunkcjaczas.czas1(self.targetlockstartfunkcja)
    def targetinfofunkcja(self):
        i = player.GetTargetVID()
        a = chr.GetInstanceType(i)
        imie=chr.GetNameByVID(i)
        chr.SelectInstance(i)
        rr=chr.GetRace(i)
        x, y, z = chr.GetPixelPosition(i)
        r = player.GetCharacterDistance(i)
        bleble=str(imie)+' pozycja- '+str(int(x))+' '+str(int(y))+' '+str(int(z))+' vid- '+str(int(i))+' dystans- '+str(int(r))+' typ- '+str(int(a))+' race- '+str(int(rr))
        dupek2.eeee(x,y,z,bleble)
        dupek2.Show()
    def zoomnofogfunkcja(self):
        app.SetCameraMaxDistance(12000)
        app.SetMinFog(90000)
    def lvlbotstartfunkcja(self):
        global dokoftowaniewida
        self.lvlbotstartfunkcjaczas=czas()
        self.lvlbotstartfunkcjaczas.otwoz(2.0)
        self.lvlbotstartfunkcjaczas.czas1(self.lvlbotstartfunkcja)
        player.SetAttackKeyState(FALSE)
        o=player.GetMainCharacterIndex()
        dokoftowaniewida=dokoftowaniewida+5
        c=0
        for i in xrange(o-50000+dokoftowaniewida, o+300000+dokoftowaniewida):
            if chr.IsEnemy(i):
                dystans = player.GetCharacterDistance(i) 
                if dystans > 0 and dystans < 5000:
                    if c==0:
                        dystans2=dystans
                        c=1
                        a=i
                        player.SetTarget(a)
                        x, y, z = chr.GetPixelPosition(a)
                        chr.MoveToDestPosition(o, int(x), int(y))
                    if dystans2 > dystans:
                        a=i
                        dystans2=dystans
                        player.SetTarget(a)
                        x, y, z = chr.GetPixelPosition(a)
                        chr.MoveToDestPosition(o, int(x), int(y))
                    if dystans < 200:
                        player.SetTarget(i)
                        chr.SelectInstance(o)
                        player.SetAttackKeyState(TRUE)
                        rnd = app.GetRandom(0, 7)
                        chr.SetDirection(rnd)
                        break
    def lvlbotstopfunkcja(self):
        global dokoftowaniewida
        dokoftowaniewida=0
        self.lvlbotstartfunkcjaczas=czas()
        self.lvlbotstartfunkcjaczas.otwoz(100000000.0)
        self.lvlbotstartfunkcjaczas.czas1(self.lvlbotstartfunkcja)
        player.SetAttackKeyState(FALSE)
    def autoatakstartfunkcja(self):
        self.autoatakstartfunkcjaczas=czas()
        self.autoatakstartfunkcjaczas.otwoz(1.0)
        self.autoatakstartfunkcjaczas.czas1(self.autoatakstartfunkcja)
        player.SetAttackKeyState(TRUE)
        rnd = app.GetRandom(0, 7)
        o = player.GetMainCharacterIndex()
        chr.SelectInstance(o)
        chr.SetDirection(rnd)
    def autoatakstopfunkcja(self):
        self.autoatakstartfunkcjaczas=czas()
        self.autoatakstartfunkcjaczas.otwoz(100000000.0)
        self.autoatakstartfunkcjaczas.czas1(self.autoatakstartfunkcja)
        player.SetAttackKeyState(FALSE)
    def autorestartstartfunkcja(self):
        self.autorestartstartfunkcjaczas=czas()
        self.autorestartstartfunkcjaczas.otwoz(3.0)
        self.autorestartstartfunkcjaczas.czas1(self.autorestartstartfunkcja)
        maxhp=player.GetStatus(player.MAX_HP)
        aktualnehp=player.GetStatus(player.HP)
        if float(aktualnehp) / float(maxhp) * 100 < int(0):
            player.SetAttackKeyState(FALSE)
            net.SendChatPacket('/restart_here')
        
    def autorestartstopfunkcja(self):
        self.autorestartstartfunkcjaczas=czas()
        self.autorestartstartfunkcjaczas.otwoz(100000000.0)
        self.autorestartstartfunkcjaczas.czas1(self.autorestartstartfunkcja)
    def horsestartfunkcja(self):
        global kukloma
        if kukloma==0:
            self.horsestartfunkcjaczas=czas()
            self.horsestartfunkcjaczas.otwoz(30.0)
            self.horsestartfunkcjaczas.czas1(self.horsestartfunkcja)
            kukloma=kukloma+1
            net.SendChatPacket('/ride')
        else:
            self.horsestartfunkcjaczas=czas()
            self.horsestartfunkcjaczas.otwoz(5.0)
            self.horsestartfunkcjaczas.czas1(self.horsestartfunkcja)
            kukloma=0
            net.SendChatPacket('/ride')
            
            
    def horsestopfunkcja(self):
        self.horsestartfunkcjaczas=czas()
        self.horsestartfunkcjaczas.otwoz(100000000.0)
        self.horsestartfunkcjaczas.czas1(self.horsestartfunkcja)
        
    class tele(ui.ThinBoard):
        def __init__(self):
            ui.ThinBoard.__init__(self)
            self.kutafono()
        def __del__(self):
            ui.ThinBoard.__del__(self)
        def Close(self):
            self.Hide()
            return TRUE
        def Show(self):
            ui.ThinBoard.Show(self)
        def kutafono(self):
            self.SetPosition(400, 300)
            self.SetSize(97, 92)
            self.Close()
            self.AddFlag('float')
            self.AddFlag('movable')
            self.przyciski()
        def przyciski(self):
            self.ukryjokno = ui.Button()
            self.ukryjokno.SetParent(self)
            self.ukryjokno.SetPosition(0, 0)
            self.ukryjokno.SetUpVisual('d:/ymir work/ui/public/close_button_01.sub')
            self.ukryjokno.SetOverVisual('d:/ymir work/ui/public/close_button_02.sub')
            self.ukryjokno.SetDownVisual('d:/ymir work/ui/public/close_button_03.sub')
            self.ukryjokno.SetEvent(ui.__mem_func__(self.Hide))
            self.ukryjokno.Show()
            
            self.gora = ui.Button()
            self.gora.SetParent(self)
            self.gora.SetPosition(jebac.pozycjax+(jebac.odstepx/2), jebac.pozycjay)
            self.gora.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
            self.gora.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
            self.gora.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
            self.gora.SetEvent(ui.__mem_func__(self.gorafunkcja))
            self.gora.SetText('gora')
            self.gora.Show()

            self.dul = ui.Button()
            self.dul.SetParent(self)
            self.dul.SetPosition(jebac.pozycjax+(jebac.odstepx/2), jebac.pozycjay+(2*jebac.odstepy))
            self.dul.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
            self.dul.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
            self.dul.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
            self.dul.SetEvent(ui.__mem_func__(self.dulfunkcja))
            self.dul.SetText('dul')
            self.dul.Show()

            self.lewo = ui.Button()
            self.lewo.SetParent(self)
            self.lewo.SetPosition(jebac.pozycjax, jebac.pozycjay+jebac.odstepy)
            self.lewo.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
            self.lewo.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
            self.lewo.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
            self.lewo.SetEvent(ui.__mem_func__(self.lewofunkcja))
            self.lewo.SetText('lewo')
            self.lewo.Show()

            self.prawo = ui.Button()
            self.prawo.SetParent(self)
            self.prawo.SetPosition(jebac.pozycjax+(jebac.odstepx), jebac.pozycjay+jebac.odstepy)
            self.prawo.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
            self.prawo.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
            self.prawo.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
            self.prawo.SetEvent(ui.__mem_func__(self.prawofunkcja))
            self.prawo.SetText('prawo')
            self.prawo.Show()
        def gorafunkcja(self):
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            x, y, z = player.GetMainCharacterPosition()
            chr.SetPixelPosition(int(x), int(y) - 2000, int(z))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        def dulfunkcja(self):
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            x, y, z = player.GetMainCharacterPosition()
            chr.SetPixelPosition(int(x), int(y) + 2000, int(z))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        def lewofunkcja(self):
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            x, y, z = player.GetMainCharacterPosition()
            chr.SetPixelPosition(int(x) - 2000, int(y), int(z))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        def prawofunkcja(self):
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            x, y, z = player.GetMainCharacterPosition()
            chr.SetPixelPosition(int(x) + 2000, int(y), int(z))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
    class metki(ui.ThinBoard):
        def __init__(self):
            ui.ThinBoard.__init__(self)
            self.zmienne=[0,0,0]
            self.kutafonoo()
        def __del__(self):
            ui.ThinBoard.__del__(self)
        def Close(self):
            self.Hide()
            return TRUE
        def Show(self):
            ui.ThinBoard.Show(self)
        def kutafonoo(self):
            self.SetPosition(500, 200)
            self.SetSize(150, 50)
            self.Close()
            self.AddFlag('float')
            self.AddFlag('movable')
            self.przyciskiii()
            self.tekstyiii()
        def przyciskiii(self):
            self.ukryjoknooo = ui.Button()
            self.ukryjoknooo.SetParent(self)
            self.ukryjoknooo.SetPosition(0, 0)
            self.ukryjoknooo.SetUpVisual('d:/ymir work/ui/public/close_button_01.sub')
            self.ukryjoknooo.SetOverVisual('d:/ymir work/ui/public/close_button_02.sub')
            self.ukryjoknooo.SetDownVisual('d:/ymir work/ui/public/close_button_03.sub')
            self.ukryjoknooo.SetEvent(ui.__mem_func__(self.Hide))
            self.ukryjoknooo.Show()

            self.go = ui.Button()
            self.go.SetParent(self)
            self.go.SetPosition(100, 15)
            self.go.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
            self.go.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
            self.go.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
            self.go.SetEvent(ui.__mem_func__(self.idzfunkcja))
            self.go.SetText('idz')
            self.go.SetToolTipText('wlacza skrypt')
            self.go.Show()
        def tekstyiii(self):
            self.tekst1metin = ui.TextLine()
            self.tekst1metin.SetParent(self)
            self.tekst1metin.SetDefaultFontName()
            self.tekst1metin.SetPosition(5, 15)
            self.tekst1metin.SetFeather()
            self.tekst1metin.SetText('target lock')
            self.tekst1metin.SetOutline()
            self.tekst1metin.Show()
        def idzfunkcja(self):
            k = player.GetMainCharacterIndex()
            chr.MoveToDestPosition(k, int(self.zmienne[0]), int(self.zmienne[1]))
        def eeee(self,x,y,z,tekst):
            self.tekst1metin.SetText(str(tekst))
            self.zmienne=[x,y,z]
            
            
        
        

class czas(ui.ScriptWindow):

    def __init__(self):
        ui.ScriptWindow.__init__(self)
        self.eventTimeOver = lambda *arg: None
        self.eventExit = lambda *arg: None

    def __del__(self):
        ui.ScriptWindow.__del__(self)

    def otwoz(self, waitTime):
        curTime = time.clock()
        self.endTime = curTime + waitTime
        self.Show()

    def Close(self):
        self.Hide()

    def Destroy(self):
        self.Hide()

    def czas1(self, event):
        self.eventTimeOver = ui.__mem_func__(event)

    def czas2(self, event):
        self.eventTimeOver = ui.__mem_func__(event)

    def czas3(self, event):
        self.eventExit = ui.__mem_func__(event)

    def OnUpdate(self):
        lastTime = max(0, self.endTime - time.clock())
        if 0 == lastTime:
            self.Close()
            self.eventTimeOver()
        else:
            return None
        return None

    def OnPressExitKey(self):
        self.Close()
        return TRUE

jebac = ciulskoodkacki()
kurwiszonka = jebac.tele()
dupek = jebac.metki()
dupek1 = jebac.metki()
dupek2 = jebac.metki()
hackprzycisk = ui.Button()
hackprzycisk.SetPosition(3, 100)
hackprzycisk.SetEvent(jebac.Show)
hackprzycisk.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
hackprzycisk.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
hackprzycisk.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
hackprzycisk.SetText('start')
hackprzycisk.Show()
        
    
