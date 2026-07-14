import ui
import dbg
import app
import wndMgr
import chat
import chr
import locale
import net
import player
import time
import interfacemodule
import background
import os
import chrmgr
import item
import textTail
import shop
import mouseModule
import grp
import uiToolTip
import nonplayer
import systemSetting
from uitooltip import ItemToolTip

# Import do Mobbera, biblioteka kamera
try:
    import kamer
except:
	pass

### Gui ###
Gui = 0
Language = 0
Save_Mode = 0
Info_Screen = 0

### Auto Attack ###
Auto_Attack_Status = 0
Auto_Attack_Mode = 0
Auto_Attack_Delay = 1
Auto_Attack_Mode_Combobox = ["Rotacyjny", "Zwyk³y"]

### Mobber ###
Mobber_Status = 0
Mobber_ID = 0
Mobber_Delay = 1
Mobber_HP = 0
Mobber_Mode = 0
Mobber_Mode_Combobox = ["Pelerynki", "Mobber"]

### Pick Up ###
Pick_Up_Status = 0
Pick_Up_Delay = 0.1

### Auto Pot ###
Auto_Pot_Status = 0
Auto_Pot_Red_ID = 0
Auto_Pot_Red_Value = 0
Auto_Pot_Blue_ID = 0
Auto_Pot_Blue_Value = 0

### Restart ###
Restart_Status = 0

### Use Item ###
Use_Item_Status = 0
Use_Item_Delay = 0
Use_Item_Delay_OK = 0
Use_Item_ID = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Use_Item_Delay_Mode_ComboBox = ["Minut", "Sekund"]

### GM Detector ###
GM_Detector_Status = 0
GM_Detector_Delay = 15
GM_Detector_Mode = 0
GM_Detector_PopUp_Time = 0
GM_Detector_Info = [0, 0, 0, 0]
GM_Detector_Mode_Combobox = ["Powiadom", "Wy³¹cz_Grê"] 

### Detector ###
Detector_Status = 0
Detector_Mode = 0
Detector_Delay = 15
Detector_List_Type = 0
Detector_Mode_Combobox = ["Metin", "Boss", "Ore", "Player", "Wszystko"] 

### Teleport ###
My_Coords_Info = [0, 0, 0] 

### Ghost Mod ###
Ghost_Mode = 0

### Other ###
### Item Clicker ###
Item_Clicker_Status = 0
Item_Clicker_ID = [0, 0, 0, 0, 0]

### Buff Bot ###
Buff_Bot_Status = 0
Buff_Bot_Type = 0
Buff_Bot_Target_VID = 0
Buff_Bot_Skill_1 = 0
Buff_Bot_Skill_2 = 0
Buff_Bot_Skill_3 = 0

### Yang Bug ###
Yang_Bug_Status = 0 
Yang_Bug_Item_ID = 0 
Yang_Bug_Check_Time = 0 
Yang_Bug_Past_Yang = 0 

### Book Reader ###
Book_Reader_Status = 0
Book_Reader_Book_ID = 0
Book_Reader_Egzo = 1 
Book_Reader_Rada = 1 
Book_Reader_Buy = 1 

### Exp Donator ###
Exp_Donator_Status = 0

### Inventory Menager ###
Inventory_Manager_Upgrade_Mode_ComboBox = ["Kowal", "Kowal DT", "Kowal Gildijny"]

### Environment ###
Environment_Snow = 0
Environment_Fog = 0
Environment_Crash_Map = 0
Environment_Shadow_Level = 0

### Feak Info ###
Fake_Info_GM = 0

### Another ###
AFFECT_DICT = ItemToolTip.AFFECT_DICT
BONUS_LIST_CUSTOM = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,21,22,23,27,28,29,30,31,32,33,34,37,39,41,44,45,48,53,71,72] 
BONUS_LIST_ALL = TRUE


### Info Screen ###
Info_Screen_Page = 0

### Options ###
Options_Gui_Position_Combobox = ["Lewo", "Dó³"]
Options_Save_Mode_Combobox = ["Ogólny", "Postaæ"]
Options_Language_Combobox = ["PL", "ENG"]

class ZAHON_MOD(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()
		self.GM_Detector_List_Refresh()	
		self.Detector_List_Create_All_List()
		self.Teleport_Coordinates_List_Refresh()		
		self.Load_ZAHON_MOD_func()
		self.Info_Screen_Load()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		
		self.Gui = ui.Board()
		self.Gui.SetSize(42, 450)
		self.Gui.SetPosition(-60, 120)
		#self.Gui.SetPosition((wndMgr.GetScreenWidth()-400), -120)
		self.Gui.AddFlag('movable')
		self.Gui.AddFlag('float')
		self.Gui.Show()

		self.Auto_Attack = ui.BoardWithTitleBar()
		self.Auto_Attack.SetSize(200, 90)
		self.Auto_Attack.SetPosition(50, 120)		
		self.Auto_Attack.AddFlag('movable')
		self.Auto_Attack.AddFlag('float')
		self.Auto_Attack.SetTitleName('Auto Attack')
		self.Auto_Attack.SetCloseEvent(self.Auto_Attack_Close)
		self.Auto_Attack.Hide()			
		
		self.Mobber = ui.BoardWithTitleBar()
		self.Mobber.SetSize(200, 185)
		self.Mobber.SetPosition(50, 120)
		self.Mobber.AddFlag('movable')
		self.Mobber.AddFlag('float')
		self.Mobber.SetTitleName('Mobber')
		self.Mobber.SetCloseEvent(self.Mobber_Close)
		self.Mobber.Hide()			
		
		self.Pick_Up = ui.BoardWithTitleBar()
		self.Pick_Up.SetSize(195, 65)
		self.Pick_Up.SetPosition(50, 120)
		self.Pick_Up.AddFlag('movable')
		self.Pick_Up.AddFlag('float')
		self.Pick_Up.SetTitleName('Pick Up')
		self.Pick_Up.SetCloseEvent(self.Pick_Up_Close)
		self.Pick_Up.Hide()			
		
		self.Auto_Pot = ui.BoardWithTitleBar()
		self.Auto_Pot.SetSize(200, 185)
		self.Auto_Pot.SetPosition(50, 120)
		self.Auto_Pot.AddFlag('movable')
		self.Auto_Pot.AddFlag('float')
		self.Auto_Pot.SetTitleName('Automatyczne Potowanie')
		self.Auto_Pot.SetCloseEvent(self.Auto_Pot_Close)
		self.Auto_Pot.Hide()			
		
		### Use Item ###
		self.Use_Item = ui.BoardWithTitleBar()
		self.Use_Item.SetSize(207, 245)
		self.Use_Item.SetPosition(50, 120)
		self.Use_Item.AddFlag('movable')
		self.Use_Item.AddFlag('float')
		self.Use_Item.SetTitleName('Use Item')
		self.Use_Item.SetCloseEvent(self.Use_Item_Close)
		self.Use_Item.Hide()
			
		self.Use_Item_Delete_All = ui.BoardWithTitleBar()
		self.Use_Item_Delete_All.SetSize(220, 80)
		self.Use_Item_Delete_All.SetCenterPosition()
		self.Use_Item_Delete_All.AddFlag('movable')
		self.Use_Item_Delete_All.AddFlag('float')
		self.Use_Item_Delete_All.SetTitleName('Usuñ wszystkie przedmioty?')
		self.Use_Item_Delete_All.SetCloseEvent(self.Use_Item_Delete_All_Close)
		self.Use_Item_Delete_All.Hide()			
		
		### GM Detector ###
		self.GM_Detector = ui.BoardWithTitleBar()
		self.GM_Detector.SetSize(175, 130)
		self.GM_Detector.SetPosition(50, 120)
		self.GM_Detector.AddFlag('movable')
		self.GM_Detector.AddFlag('float')
		self.GM_Detector.SetTitleName('GM Detector')
		self.GM_Detector.SetCloseEvent(self.GM_Detector_Close)
		self.GM_Detector.Hide()
		
		self.GM_Detector_List = ui.BoardWithTitleBar()
		self.GM_Detector_List.SetSize(220, 300)
		self.GM_Detector_List.SetCenterPosition()
		self.GM_Detector_List.AddFlag('movable')
		self.GM_Detector_List.AddFlag('float')
		self.GM_Detector_List.SetTitleName('GM Detector List')
		self.GM_Detector_List.SetCloseEvent(self.GM_Detector_List_Close)
		self.GM_Detector_List.Hide()			
		
		self.GM_Detector_Logs = ui.BoardWithTitleBar()
		self.GM_Detector_Logs.SetSize(340, 265)
		self.GM_Detector_Logs.SetCenterPosition()
		self.GM_Detector_Logs.AddFlag('movable')
		self.GM_Detector_Logs.AddFlag('float')
		self.GM_Detector_Logs.SetTitleName('GM Detector Logs')
		self.GM_Detector_Logs.SetCloseEvent(self.GM_Detector_Logs_Close)
		self.GM_Detector_Logs.Hide()			
		
		self.GM_Detector_PopUp = ui.BoardWithTitleBar()
		self.GM_Detector_PopUp.SetSize(220, 115)
		self.GM_Detector_PopUp.SetPosition(70, (wndMgr.GetScreenHeight()-150))
		self.GM_Detector_PopUp.AddFlag('movable')
		self.GM_Detector_PopUp.AddFlag('float')
		self.GM_Detector_PopUp.SetTitleName('Powiadomienie')
		self.GM_Detector_PopUp.SetCloseEvent(self.GM_Detector_PopUp_Close)
		self.GM_Detector_PopUp.Hide()			
		
		### Detector ###
		self.Detector_Bar = ui.Bar()
		self.Detector_Bar.SetSize(515, 265)
		self.Detector_Bar.SetCenterPosition()
		self.Detector_Bar.AddFlag('movable')
		self.Detector_Bar.AddFlag('float')			
		self.Detector_Bar.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.0))
		self.Detector_Bar.Hide()		
		
		self.Detector_Panel = ui.Board()
		self.Detector_Panel.SetParent(self.Detector_Bar)	
		self.Detector_Panel.SetSize(170, 205)
		self.Detector_Panel.SetPosition(345, 27)
		self.Detector_Panel.Show()		
	
		self.Detector = ui.BoardWithTitleBar()
		self.Detector.SetParent(self.Detector_Bar)			
		self.Detector.SetSize(360, 265)
		self.Detector.SetPosition(0, 0)		
		self.Detector.SetTitleName('Detector 1.1')
		self.Detector.SetCloseEvent(self.Detector_Close)
		self.Detector.Show()
		
		self.Detector_List = ui.BoardWithTitleBar()
		self.Detector_List.SetSize(220, 320)
		self.Detector_List.SetCenterPosition()
		self.Detector_List.AddFlag('movable')
		self.Detector_List.AddFlag('float')
		self.Detector_List.SetTitleName('Detector List')
		self.Detector_List.SetCloseEvent(self.Detector_List_Close)
		self.Detector_List.Hide()			
		
		self.Detector_Options = ui.BoardWithTitleBar()
		self.Detector_Options.SetSize(140, 210)
		self.Detector_Options.SetCenterPosition()
		self.Detector_Options.AddFlag('movable')
		self.Detector_Options.AddFlag('float')
		self.Detector_Options.SetTitleName('Ustawienia')
		self.Detector_Options.SetCloseEvent(self.Detector_Options_Close)
		self.Detector_Options.Hide()			
		
		### Teleport ###
		self.Teleport_Bar = ui.Bar()
		self.Teleport_Bar.SetSize(338, 318)
		self.Teleport_Bar.SetPosition(50, 120)
		self.Teleport_Bar.AddFlag('movable')
		self.Teleport_Bar.AddFlag('float')			
		self.Teleport_Bar.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.0))
		self.Teleport_Bar.Hide()	
	
		self.Teleport_Panel = ui.Board()
		self.Teleport_Panel.SetParent(self.Teleport_Bar)	
		self.Teleport_Panel.SetSize(150, 225)
		self.Teleport_Panel.SetPosition(185, 48)
		self.Teleport_Panel.Hide()	
	
		self.Teleport_Coordinates = ui.BoardWithTitleBar()
		self.Teleport_Coordinates.SetParent(self.Teleport_Bar)	
		self.Teleport_Coordinates.SetSize(200, 320)
		self.Teleport_Coordinates.SetPosition(0, 0)
		self.Teleport_Coordinates.SetTitleName('Teleport Hack 1.4')
		self.Teleport_Coordinates.SetCloseEvent(self.Teleport_Coordinates_Close)
		self.Teleport_Coordinates.Show()		
		
		self.Ghost_Mode = ui.ThinBoard()
		self.Ghost_Mode.SetSize(200, 60)
		self.Ghost_Mode.SetPosition(50, 140)
		self.Ghost_Mode.AddFlag('movable')
		self.Ghost_Mode.AddFlag('float')
		self.Ghost_Mode.Hide()			
		
		self.Options = ui.BoardWithTitleBar()
		self.Options.SetSize(243, 195)
		self.Options.SetPosition(50, 120)
		self.Options.AddFlag('movable')
		self.Options.AddFlag('float')
		self.Options.SetTitleName('Opcje')
		self.Options.SetCloseEvent(self.Options_Close)
		self.Options.Hide()		
			
		self.Restart_Options = ui.BoardWithTitleBar()
		self.Restart_Options.SetSize(240, 80)
		self.Restart_Options.SetCenterPosition()
		self.Restart_Options.AddFlag('movable')
		self.Restart_Options.AddFlag('float')
		self.Restart_Options.SetTitleName('Przywróciæ domyœlne ustawienia ?')
		self.Restart_Options.SetCloseEvent(self.Restart_Options_Close)
		self.Restart_Options.Hide()
			
		self.Other_Gui = ui.BoardWithTitleBar()
		self.Other_Gui.SetSize(295, 205)
		self.Other_Gui.SetPosition(50, 120)
		self.Other_Gui.AddFlag('movable')
		self.Other_Gui.AddFlag('float')
		self.Other_Gui.SetTitleName('Inne Funkcje')
		self.Other_Gui.SetCloseEvent(self.Other_Gui_Close)
		self.Other_Gui.Hide()			
		
		### Info Screen ###
		self.Info_Screen = ui.BoardWithTitleBar()
		self.Info_Screen.SetSize(370, 350)
		self.Info_Screen.SetCenterPosition()
		self.Info_Screen.SetTitleName('ZAHON_MOD Wprowadzenie')
		self.Info_Screen.SetCloseEvent(self.Info_Screen_Close)
		self.Info_Screen.Hide()			
	
		self.Info_Screen_Bar = ui.Bar()
		self.Info_Screen_Bar.SetParent(self)
		self.Info_Screen_Bar.SetSize(160,60)
		self.Info_Screen_Bar.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
		self.Info_Screen_Bar.SetPosition(0,0)	
		self.Info_Screen_Bar.Hide()				
			
		self.__BuildKeyDict()
		self.comp = Component()

	################################### Too lTip #######################################		
		
		self.txttooltip = uiToolTip.ToolTip()
		self.txttooltip.Hide()				
	
	###############################################################################################
	################################### Auto Attack Comp ##########################################		
	###############################################################################################	
		
		### Buttons ###
		self.Auto_Attack_Plus_Button = self.comp.Button(self.Auto_Attack, '', '', 120, 62, self.Auto_Attack_Plus_func, 'd:/ymir work/ui/game/windows/btn_plus_up.sub', 'd:/ymir work/ui/game/windows/btn_plus_over.sub', 'd:/ymir work/ui/game/windows/btn_plus_down.sub')
		self.Auto_Attack_Minus_Button = self.comp.Button(self.Auto_Attack, '', '', 136, 62, self.Auto_Attack_Minus_func, 'd:/ymir work/ui/game/windows/btn_minus_up.sub', 'd:/ymir work/ui/game/windows/btn_minus_over.sub', 'd:/ymir work/ui/game/windows/btn_minus_down.sub')
		
		### Text ###	
		self.Auto_Attack_Mode_Text = self.comp.TextLine(self.Auto_Attack, 'Rodzaj Auto Atacku: ', 15, 42, self.comp.RGB(255, 255, 255))		
		self.Auto_Attack_Delay_Text = self.comp.TextLine(self.Auto_Attack, 'Szybkoœæ rotacji x s', 15, 62, self.comp.RGB(255, 255, 255))		
					
		### ComboBox ###	
		self.Auto_Attack_Mode_ComboBox = self.comp.ComboBox(self.Auto_Attack, 'Rotacyjny', 120, 40, 60)	
		global Auto_Attack_Mode_Combobox
		for Auto_Attack_Mode_ComboBox in Auto_Attack_Mode_Combobox:
			self.Auto_Attack_Mode_ComboBox.InsertItem(1,str(Auto_Attack_Mode_ComboBox)) 			
	
	###############################################################################################
	################################### Mobber Comp ###############################################		
	###############################################################################################				

		### Thin Board ###
		self.Mobber_ThinBoard = self.comp.ThinBoard(self.Mobber, FALSE, 10, 35, 180, 60, FALSE)			
	
		### Buttons ###
		self.Mobber_Plus_Button = self.comp.Button(self.Mobber, '', '', 100, 101, self.Mobber_Plus_func, 'd:/ymir work/ui/game/windows/btn_plus_up.sub', 'd:/ymir work/ui/game/windows/btn_plus_over.sub', 'd:/ymir work/ui/game/windows/btn_plus_down.sub')
		self.Mobber_Minus_Button = self.comp.Button(self.Mobber, '', '', 116, 101, self.Mobber_Minus_func, 'd:/ymir work/ui/game/windows/btn_minus_up.sub', 'd:/ymir work/ui/game/windows/btn_minus_over.sub', 'd:/ymir work/ui/game/windows/btn_minus_down.sub')
				
		### Text ###	
		self.Mobber_Delay_Text = self.comp.TextLine(self.Mobber, 'Szybkoœæ x s', 15, 100, self.comp.RGB(255, 255, 255))		
		self.Mobber_Mode_Text = self.comp.TextLine(self.Mobber, 'Rodzaj Mobbera: ', 15, 120, self.comp.RGB(255, 255, 255))				
		self.Mobber_HP_Text = self.comp.TextLine(self.Mobber, 'Przestañ u¿ywaæ, jeœli HP < x%', 15, 140, self.comp.RGB(255, 255, 255))		

		### Slots ###
		self.Mobber_Item_Bar = ui.ExpandedImageBox()
		self.Mobber_Item_Bar.SetParent(self.Mobber_ThinBoard)	
		self.Mobber_Item_Bar.SetPosition(74, 14)
		self.Mobber_Item_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Mobber_Item_Bar.OnMouseLeftButtonUp = lambda: self.Set_Mobber()
		self.Mobber_Item_Bar.Show()
				
		self.Mobber_Item_Icon = ui.ExpandedImageBox()
		self.Mobber_Item_Icon.SetParent(self.Mobber_Item_Bar)
		self.Mobber_Item_Icon.SetPosition(0, 0)
		self.Mobber_Item_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Mobber_Item_Icon.OnMouseLeftButtonUp = lambda: self.Set_Mobber()
		self.Mobber_Item_Icon.OnMouseRightButtonDown = lambda: self.Delete_Mobber()		
		self.Mobber_Item_Icon.OnMouseOverIn = lambda: self.Mobber_ShowTip()
		self.Mobber_Item_Icon.OnMouseOverOut = lambda: self.Mobber_HideTip()		
		self.Mobber_Item_Icon.Show()				
			
		### Slid Bar ###		
		self.Slidbar_Mobber = self.comp.SliderBar(self.Mobber, 100 / 10, self.Set_Slidbar_Mobber, 10, 160)			
			
		### ComboBox ###			
		self.Mobber_Mode_ComboBox = self.comp.ComboBox(self.Mobber, 'Pelerynki', 100, 120, 60)	
		global Mobber_Mode_ComboBox
		for Mobber_Mode_ComboBox in Mobber_Mode_Combobox:
			self.Mobber_Mode_ComboBox.InsertItem(1,str(Mobber_Mode_ComboBox)) 		
	
	###############################################################################################
	################################# Pick Up Comp ################################################		
	###############################################################################################		
	
		### Buttons ###
		self.Pick_Up_Plus_Button = self.comp.Button(self.Pick_Up, '', '', 150, 36, self.Pick_Up_Plus_func, 'd:/ymir work/ui/game/windows/btn_plus_up.sub', 'd:/ymir work/ui/game/windows/btn_plus_over.sub', 'd:/ymir work/ui/game/windows/btn_plus_down.sub')
		self.Pick_Up_Minus_Button = self.comp.Button(self.Pick_Up, '', '', 166, 36, self.Pick_Up_Minus_func, 'd:/ymir work/ui/game/windows/btn_minus_up.sub', 'd:/ymir work/ui/game/windows/btn_minus_over.sub', 'd:/ymir work/ui/game/windows/btn_minus_down.sub')
		
		### Text ###
		self.Pick_Up_Delay_Text = self.comp.TextLine(self.Pick_Up, 'Szybkoœæ podnoszenia: xs', 15, 35, self.comp.RGB(255, 255, 255))		
	
	###############################################################################################
	################################# Auto Pot Comp ################################################		
	###############################################################################################			
					
		### Thin Board ###	
		self.Auto_Pot_ThinBoard = self.comp.ThinBoard(self.Auto_Pot, FALSE, 10, 35, 180, 60, FALSE)			
	
		### Slots ###	
		self.Auto_Pot_Red_Bar = ui.ExpandedImageBox()
		self.Auto_Pot_Red_Bar.SetParent(self.Auto_Pot_ThinBoard)	
		self.Auto_Pot_Red_Bar.SetPosition(58, 14)
		self.Auto_Pot_Red_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Auto_Pot_Red_Bar.OnMouseLeftButtonUp = lambda: self.Set_Auto_Pot_Red()
		self.Auto_Pot_Red_Bar.Show()
				
		self.Auto_Pot_Red_Icon = ui.ExpandedImageBox()
		self.Auto_Pot_Red_Icon.SetParent(self.Auto_Pot_Red_Bar)
		self.Auto_Pot_Red_Icon.SetPosition(0, 0)
		self.Auto_Pot_Red_Icon.LoadImage("ZAHON_MOD/Icons/Auto_Pot/Red_Pot_Shadow.tga")
		self.Auto_Pot_Red_Icon.OnMouseLeftButtonUp = lambda: self.Set_Auto_Pot_Red()
		self.Auto_Pot_Red_Icon.OnMouseRightButtonDown = lambda: self.Delete_Auto_Pot_Red()		
		self.Auto_Pot_Red_Icon.OnMouseOverIn = lambda: self.Auto_Pot_Red_ShowTip()
		self.Auto_Pot_Red_Icon.OnMouseOverOut = lambda: self.Auto_Pot_HideTip()		
		self.Auto_Pot_Red_Icon.Show()

		self.Auto_Pot_Blue_Bar = ui.ExpandedImageBox()
		self.Auto_Pot_Blue_Bar.SetParent(self.Auto_Pot_ThinBoard)	
		self.Auto_Pot_Blue_Bar.SetPosition(90, 14)
		self.Auto_Pot_Blue_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Auto_Pot_Blue_Bar.OnMouseLeftButtonUp = lambda: self.Set_Auto_Pot_Blue()
		self.Auto_Pot_Blue_Bar.Show()
				
		self.Auto_Pot_Blue_Icon = ui.ExpandedImageBox()
		self.Auto_Pot_Blue_Icon.SetParent(self.Auto_Pot_Blue_Bar)
		self.Auto_Pot_Blue_Icon.SetPosition(0, 0)
		self.Auto_Pot_Blue_Icon.LoadImage("ZAHON_MOD/Icons/Auto_Pot/Blue_Pot_Shadow.tga")
		self.Auto_Pot_Blue_Icon.OnMouseLeftButtonUp = lambda: self.Set_Auto_Pot_Blue()
		self.Auto_Pot_Blue_Icon.OnMouseRightButtonDown = lambda: self.Delete_Auto_Pot_Blue()		
		self.Auto_Pot_Blue_Icon.OnMouseOverIn = lambda: self.Auto_Pot_Blue_ShowTip()
		self.Auto_Pot_Blue_Icon.OnMouseOverOut = lambda: self.Auto_Pot_HideTip()		
		self.Auto_Pot_Blue_Icon.Show()			
				
		### Text ###		
		self.Auto_Pot_Red_Value_Text = self.comp.TextLine(self.Auto_Pot, 'Przy ilu % u¿ywaæ Red Pot: ', 15, 100, self.comp.RGB(255, 255, 255))		
		self.Auto_Pot_Blue_Value_Text = self.comp.TextLine(self.Auto_Pot, 'Przy ilu % u¿ywaæ Blue Pot: ', 15, 140, self.comp.RGB(255, 255, 255))		
	
		### Slid Bar ###
		self.Slidbar_Auto_Pot_Red_Value = self.comp.SliderBar(self.Auto_Pot, 100 / 10, self.Set_Slidbar_Auto_Pot_Red_Value, 10, 120)	
		self.Slidbar_Auto_Pot_Blue_Value = self.comp.SliderBar(self.Auto_Pot, 100 / 10, self.Set_Slidbar_Auto_Pot_Blue_Value, 10, 160)	
	
	###############################################################################################
	################################### Use Item Comp #############################################		
	###############################################################################################			
					
		### HorizontalBars ###		
		self.Use_Item_Item_Options_HorizontalBar = self.comp.HorizontalBar(self.Use_Item , 10, 195, 188)
		self.Use_Item_Item_Options_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Use_Item_Item_Options_HorizontalBar, 'Ustawienia', 5, 0, 0xFFFFE3AD)			
		
		### Buttons ###				
		self.Use_Item_Delete_All_Button = self.comp.Button(self.Use_Item, '', '', 162, 11, self.Use_Item_Delete_All_func, 'd:/ymir work/ui/game/windows/btn_minus_up.sub', 'd:/ymir work/ui/game/windows/btn_minus_over.sub', 'd:/ymir work/ui/game/windows/btn_minus_down.sub')			
		
		self.Use_Item_Delete_All_Yes_Button = self.comp.Button(self.Use_Item_Delete_All, 'Tak', '', 10, 40, self.Use_Item_Delete_All_Yes_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Use_Item_Delete_All_No_Button = self.comp.Button(self.Use_Item_Delete_All, 'Nie', '', 120, 40, self.Use_Item_Delete_All_No_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
				
		### Text ###					
		self.Use_Item_Delay_Text = self.comp.TextLine(self.Use_Item, 'Co ile u¿ywaæ:', 17, 216, self.comp.RGB(255, 255, 255))		
		
		### Slotbar ###				
		self.slotbar_Use_Item_Delay, self.Use_Item_Delay_EditLine = self.comp.EditLine(self.Use_Item, '1', 155, 215, 35, 15, 5)
				
		### ComboBox ###			
		global Use_Item_Delay_Mode_ComboBox
		
		self.Use_Item_Delay_Mode_ComboBox = self.comp.ComboBox(self.Use_Item, 'Minut', 90, 215, 55)	
	
		for Use_Item_Delay_Mode_ComboBox in Use_Item_Delay_Mode_ComboBox:
			self.Use_Item_Delay_Mode_ComboBox.InsertItem(1,str(Use_Item_Delay_Mode_ComboBox)) 
		
		### Slots ###
		self.Use_Item_Item_1_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_1_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_1_Bar.SetPosition(7, 30)
		self.Use_Item_Item_1_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_1_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_1()
		self.Use_Item_Item_1_Bar.Show()
				
		self.Use_Item_Item_1_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_1_Icon.SetParent(self.Use_Item_Item_1_Bar)
		self.Use_Item_Item_1_Icon.SetPosition(0, 0)
		self.Use_Item_Item_1_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_1_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_1()
		self.Use_Item_Item_1_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_1()		
		self.Use_Item_Item_1_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_1_ShowTip()
		self.Use_Item_Item_1_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()		
		self.Use_Item_Item_1_Icon.Show()	
		
		self.Use_Item_Item_2_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_2_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_2_Bar.SetPosition(39, 30)
		self.Use_Item_Item_2_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_2_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_2()
		self.Use_Item_Item_2_Bar.Show()
				
		self.Use_Item_Item_2_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_2_Icon.SetParent(self.Use_Item_Item_2_Bar)
		self.Use_Item_Item_2_Icon.SetPosition(0, 0)
		self.Use_Item_Item_2_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_2_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_2()
		self.Use_Item_Item_2_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_2()		
		self.Use_Item_Item_2_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_2_ShowTip()
		self.Use_Item_Item_2_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_2_Icon.Show()

		self.Use_Item_Item_3_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_3_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_3_Bar.SetPosition(71, 30)
		self.Use_Item_Item_3_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_3_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_3()
		self.Use_Item_Item_3_Bar.Show()
				
		self.Use_Item_Item_3_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_3_Icon.SetParent(self.Use_Item_Item_3_Bar)
		self.Use_Item_Item_3_Icon.SetPosition(0, 0)
		self.Use_Item_Item_3_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_3_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_3()
		self.Use_Item_Item_3_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_3()		
		self.Use_Item_Item_3_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_3_ShowTip()
		self.Use_Item_Item_3_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_3_Icon.Show()	

		self.Use_Item_Item_4_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_4_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_4_Bar.SetPosition(103, 30)
		self.Use_Item_Item_4_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_4_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_4()
		self.Use_Item_Item_4_Bar.Show()
				
		self.Use_Item_Item_4_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_4_Icon.SetParent(self.Use_Item_Item_4_Bar)
		self.Use_Item_Item_4_Icon.SetPosition(0, 0)
		self.Use_Item_Item_4_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_4_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_4()
		self.Use_Item_Item_4_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_4()		
		self.Use_Item_Item_4_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_4_ShowTip()
		self.Use_Item_Item_4_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_4_Icon.Show()

		self.Use_Item_Item_5_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_5_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_5_Bar.SetPosition(135, 30)
		self.Use_Item_Item_5_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_5_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_5()
		self.Use_Item_Item_5_Bar.Show()
				
		self.Use_Item_Item_5_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_5_Icon.SetParent(self.Use_Item_Item_5_Bar)
		self.Use_Item_Item_5_Icon.SetPosition(0, 0)
		self.Use_Item_Item_5_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_5_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_5()
		self.Use_Item_Item_5_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_5()		
		self.Use_Item_Item_5_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_5_ShowTip()
		self.Use_Item_Item_5_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_5_Icon.Show()		
	
		self.Use_Item_Item_6_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_6_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_6_Bar.SetPosition(167, 30)
		self.Use_Item_Item_6_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_6_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_6()
		self.Use_Item_Item_6_Bar.Show()
				
		self.Use_Item_Item_6_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_6_Icon.SetParent(self.Use_Item_Item_6_Bar)
		self.Use_Item_Item_6_Icon.SetPosition(0, 0)
		self.Use_Item_Item_6_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_6_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_6()
		self.Use_Item_Item_6_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_6()		
		self.Use_Item_Item_6_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_6_ShowTip()
		self.Use_Item_Item_6_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_6_Icon.Show()

		self.Use_Item_Item_7_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_7_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_7_Bar.SetPosition(7, 62)
		self.Use_Item_Item_7_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_7_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_7()
		self.Use_Item_Item_7_Bar.Show()
				
		self.Use_Item_Item_7_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_7_Icon.SetParent(self.Use_Item_Item_7_Bar)
		self.Use_Item_Item_7_Icon.SetPosition(0, 0)
		self.Use_Item_Item_7_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_7_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_7()
		self.Use_Item_Item_7_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_7()		
		self.Use_Item_Item_7_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_7_ShowTip()
		self.Use_Item_Item_7_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_7_Icon.Show()	

		self.Use_Item_Item_8_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_8_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_8_Bar.SetPosition(39, 62)
		self.Use_Item_Item_8_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_8_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_8()
		self.Use_Item_Item_8_Bar.Show()
				
		self.Use_Item_Item_8_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_8_Icon.SetParent(self.Use_Item_Item_8_Bar)
		self.Use_Item_Item_8_Icon.SetPosition(0, 0)
		self.Use_Item_Item_8_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_8_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_8()
		self.Use_Item_Item_8_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_8()		
		self.Use_Item_Item_8_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_8_ShowTip()
		self.Use_Item_Item_8_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_8_Icon.Show()

		self.Use_Item_Item_9_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_9_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_9_Bar.SetPosition(71, 62)
		self.Use_Item_Item_9_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_9_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_9()
		self.Use_Item_Item_9_Bar.Show()
				
		self.Use_Item_Item_9_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_9_Icon.SetParent(self.Use_Item_Item_9_Bar)
		self.Use_Item_Item_9_Icon.SetPosition(0, 0)
		self.Use_Item_Item_9_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_9_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_9()
		self.Use_Item_Item_9_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_9()		
		self.Use_Item_Item_9_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_9_ShowTip()
		self.Use_Item_Item_9_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_9_Icon.Show()

		self.Use_Item_Item_10_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_10_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_10_Bar.SetPosition(103, 62)
		self.Use_Item_Item_10_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_10_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_10()
		self.Use_Item_Item_10_Bar.Show()
				
		self.Use_Item_Item_10_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_10_Icon.SetParent(self.Use_Item_Item_10_Bar)
		self.Use_Item_Item_10_Icon.SetPosition(0, 0)
		self.Use_Item_Item_10_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_10_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_10()
		self.Use_Item_Item_10_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_10()		
		self.Use_Item_Item_10_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_10_ShowTip()
		self.Use_Item_Item_10_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_10_Icon.Show()	

		self.Use_Item_Item_11_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_11_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_11_Bar.SetPosition(135, 62)
		self.Use_Item_Item_11_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_11_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_11()
		self.Use_Item_Item_11_Bar.Show()
				
		self.Use_Item_Item_11_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_11_Icon.SetParent(self.Use_Item_Item_11_Bar)
		self.Use_Item_Item_11_Icon.SetPosition(0, 0)
		self.Use_Item_Item_11_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_11_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_11()
		self.Use_Item_Item_11_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_11()		
		self.Use_Item_Item_11_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_11_ShowTip()
		self.Use_Item_Item_11_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_11_Icon.Show()	

		self.Use_Item_Item_12_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_12_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_12_Bar.SetPosition(167, 62)
		self.Use_Item_Item_12_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_12_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_12()
		self.Use_Item_Item_12_Bar.Show()
				
		self.Use_Item_Item_12_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_12_Icon.SetParent(self.Use_Item_Item_12_Bar)
		self.Use_Item_Item_12_Icon.SetPosition(0, 0)
		self.Use_Item_Item_12_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_12_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_12()
		self.Use_Item_Item_12_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_12()		
		self.Use_Item_Item_12_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_12_ShowTip()
		self.Use_Item_Item_12_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_12_Icon.Show()	

		self.Use_Item_Item_13_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_13_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_13_Bar.SetPosition(7, 94)
		self.Use_Item_Item_13_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_13_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_13()
		self.Use_Item_Item_13_Bar.Show()
				
		self.Use_Item_Item_13_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_13_Icon.SetParent(self.Use_Item_Item_13_Bar)
		self.Use_Item_Item_13_Icon.SetPosition(0, 0)
		self.Use_Item_Item_13_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_13_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_13()
		self.Use_Item_Item_13_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_13()		
		self.Use_Item_Item_13_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_13_ShowTip()
		self.Use_Item_Item_13_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_13_Icon.Show()	

		self.Use_Item_Item_14_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_14_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_14_Bar.SetPosition(39, 94)
		self.Use_Item_Item_14_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_14_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_14()
		self.Use_Item_Item_14_Bar.Show()
				
		self.Use_Item_Item_14_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_14_Icon.SetParent(self.Use_Item_Item_14_Bar)
		self.Use_Item_Item_14_Icon.SetPosition(0, 0)
		self.Use_Item_Item_14_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_14_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_14()
		self.Use_Item_Item_14_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_14()		
		self.Use_Item_Item_14_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_14_ShowTip()
		self.Use_Item_Item_14_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_14_Icon.Show()

		self.Use_Item_Item_15_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_15_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_15_Bar.SetPosition(71, 94)
		self.Use_Item_Item_15_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_15_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_15()
		self.Use_Item_Item_15_Bar.Show()
				
		self.Use_Item_Item_15_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_15_Icon.SetParent(self.Use_Item_Item_15_Bar)
		self.Use_Item_Item_15_Icon.SetPosition(0, 0)
		self.Use_Item_Item_15_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_15_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_15()
		self.Use_Item_Item_15_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_15()		
		self.Use_Item_Item_15_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_15_ShowTip()
		self.Use_Item_Item_15_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_15_Icon.Show()	

		self.Use_Item_Item_16_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_16_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_16_Bar.SetPosition(103, 94)
		self.Use_Item_Item_16_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_16_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_16()
		self.Use_Item_Item_16_Bar.Show()
				
		self.Use_Item_Item_16_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_16_Icon.SetParent(self.Use_Item_Item_16_Bar)
		self.Use_Item_Item_16_Icon.SetPosition(0, 0)
		self.Use_Item_Item_16_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_16_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_16()
		self.Use_Item_Item_16_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_16()		
		self.Use_Item_Item_16_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_16_ShowTip()
		self.Use_Item_Item_16_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_16_Icon.Show()	

		self.Use_Item_Item_17_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_17_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_17_Bar.SetPosition(135, 94)
		self.Use_Item_Item_17_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_17_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_17()
		self.Use_Item_Item_17_Bar.Show()
				
		self.Use_Item_Item_17_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_17_Icon.SetParent(self.Use_Item_Item_17_Bar)
		self.Use_Item_Item_17_Icon.SetPosition(0, 0)
		self.Use_Item_Item_17_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_17_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_17()
		self.Use_Item_Item_17_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_17()		
		self.Use_Item_Item_17_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_17_ShowTip()
		self.Use_Item_Item_17_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_17_Icon.Show()

		self.Use_Item_Item_18_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_18_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_18_Bar.SetPosition(167, 94)
		self.Use_Item_Item_18_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_18_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_18()
		self.Use_Item_Item_18_Bar.Show()
				
		self.Use_Item_Item_18_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_18_Icon.SetParent(self.Use_Item_Item_18_Bar)
		self.Use_Item_Item_18_Icon.SetPosition(0, 0)
		self.Use_Item_Item_18_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_18_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_18()
		self.Use_Item_Item_18_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_18()		
		self.Use_Item_Item_18_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_18_ShowTip()
		self.Use_Item_Item_18_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_18_Icon.Show()	

		self.Use_Item_Item_19_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_19_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_19_Bar.SetPosition(7, 126)
		self.Use_Item_Item_19_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_19_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_19()
		self.Use_Item_Item_19_Bar.Show()
				
		self.Use_Item_Item_19_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_19_Icon.SetParent(self.Use_Item_Item_19_Bar)
		self.Use_Item_Item_19_Icon.SetPosition(0, 0)
		self.Use_Item_Item_19_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_19_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_19()
		self.Use_Item_Item_19_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_19()		
		self.Use_Item_Item_19_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_19_ShowTip()
		self.Use_Item_Item_19_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_19_Icon.Show()	

		self.Use_Item_Item_20_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_20_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_20_Bar.SetPosition(39, 126)
		self.Use_Item_Item_20_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_20_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_20()
		self.Use_Item_Item_20_Bar.Show()
				
		self.Use_Item_Item_20_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_20_Icon.SetParent(self.Use_Item_Item_20_Bar)
		self.Use_Item_Item_20_Icon.SetPosition(0, 0)
		self.Use_Item_Item_20_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_20_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_20()
		self.Use_Item_Item_20_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_20()		
		self.Use_Item_Item_20_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_20_ShowTip()
		self.Use_Item_Item_20_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_20_Icon.Show()	

		self.Use_Item_Item_21_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_21_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_21_Bar.SetPosition(71, 126)
		self.Use_Item_Item_21_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_21_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_21()
		self.Use_Item_Item_21_Bar.Show()
				
		self.Use_Item_Item_21_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_21_Icon.SetParent(self.Use_Item_Item_21_Bar)
		self.Use_Item_Item_21_Icon.SetPosition(0, 0)
		self.Use_Item_Item_21_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_21_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_21()
		self.Use_Item_Item_21_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_21()		
		self.Use_Item_Item_21_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_21_ShowTip()
		self.Use_Item_Item_21_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_21_Icon.Show()	

		self.Use_Item_Item_22_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_22_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_22_Bar.SetPosition(103, 126)
		self.Use_Item_Item_22_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_22_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_22()
		self.Use_Item_Item_22_Bar.Show()
				
		self.Use_Item_Item_22_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_22_Icon.SetParent(self.Use_Item_Item_22_Bar)
		self.Use_Item_Item_22_Icon.SetPosition(0, 0)
		self.Use_Item_Item_22_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_22_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_22()
		self.Use_Item_Item_22_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_22()		
		self.Use_Item_Item_22_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_22_ShowTip()
		self.Use_Item_Item_22_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_22_Icon.Show()		

		self.Use_Item_Item_23_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_23_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_23_Bar.SetPosition(135, 126)
		self.Use_Item_Item_23_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_23_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_23()
		self.Use_Item_Item_23_Bar.Show()
				
		self.Use_Item_Item_23_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_23_Icon.SetParent(self.Use_Item_Item_23_Bar)
		self.Use_Item_Item_23_Icon.SetPosition(0, 0)
		self.Use_Item_Item_23_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_23_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_23()
		self.Use_Item_Item_23_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_23()		
		self.Use_Item_Item_23_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_23_ShowTip()
		self.Use_Item_Item_23_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_23_Icon.Show()	

		self.Use_Item_Item_24_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_24_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_24_Bar.SetPosition(167, 126)
		self.Use_Item_Item_24_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_24_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_24()
		self.Use_Item_Item_24_Bar.Show()
				
		self.Use_Item_Item_24_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_24_Icon.SetParent(self.Use_Item_Item_24_Bar)
		self.Use_Item_Item_24_Icon.SetPosition(0, 0)
		self.Use_Item_Item_24_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_24_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_24()
		self.Use_Item_Item_24_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_24()		
		self.Use_Item_Item_24_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_24_ShowTip()
		self.Use_Item_Item_24_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_24_Icon.Show()	

		self.Use_Item_Item_25_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_25_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_25_Bar.SetPosition(7, 158)
		self.Use_Item_Item_25_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_25_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_25()
		self.Use_Item_Item_25_Bar.Show()
				
		self.Use_Item_Item_25_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_25_Icon.SetParent(self.Use_Item_Item_25_Bar)
		self.Use_Item_Item_25_Icon.SetPosition(0, 0)
		self.Use_Item_Item_25_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_25_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_25()
		self.Use_Item_Item_25_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_25()		
		self.Use_Item_Item_25_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_25_ShowTip()
		self.Use_Item_Item_25_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_25_Icon.Show()	

		self.Use_Item_Item_26_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_26_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_26_Bar.SetPosition(39, 158)
		self.Use_Item_Item_26_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_26_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_26()
		self.Use_Item_Item_26_Bar.Show()
				
		self.Use_Item_Item_26_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_26_Icon.SetParent(self.Use_Item_Item_26_Bar)
		self.Use_Item_Item_26_Icon.SetPosition(0, 0)
		self.Use_Item_Item_26_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_26_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_26()
		self.Use_Item_Item_26_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_26()		
		self.Use_Item_Item_26_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_26_ShowTip()
		self.Use_Item_Item_26_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_26_Icon.Show()			
	
		self.Use_Item_Item_27_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_27_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_27_Bar.SetPosition(71, 158)
		self.Use_Item_Item_27_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_27_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_27()
		self.Use_Item_Item_27_Bar.Show()
				
		self.Use_Item_Item_27_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_27_Icon.SetParent(self.Use_Item_Item_27_Bar)
		self.Use_Item_Item_27_Icon.SetPosition(0, 0)
		self.Use_Item_Item_27_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_27_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_27()
		self.Use_Item_Item_27_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_27()		
		self.Use_Item_Item_27_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_27_ShowTip()
		self.Use_Item_Item_27_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_27_Icon.Show()	

		self.Use_Item_Item_28_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_28_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_28_Bar.SetPosition(103, 158)
		self.Use_Item_Item_28_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_28_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_28()
		self.Use_Item_Item_28_Bar.Show()
				
		self.Use_Item_Item_28_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_28_Icon.SetParent(self.Use_Item_Item_28_Bar)
		self.Use_Item_Item_28_Icon.SetPosition(0, 0)
		self.Use_Item_Item_28_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_28_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_28()
		self.Use_Item_Item_28_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_28()		
		self.Use_Item_Item_28_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_28_ShowTip()
		self.Use_Item_Item_28_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_28_Icon.Show()	

		self.Use_Item_Item_29_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_29_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_29_Bar.SetPosition(135, 158)
		self.Use_Item_Item_29_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_29_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_29()
		self.Use_Item_Item_29_Bar.Show()
				
		self.Use_Item_Item_29_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_29_Icon.SetParent(self.Use_Item_Item_29_Bar)
		self.Use_Item_Item_29_Icon.SetPosition(0, 0)
		self.Use_Item_Item_29_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_29_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_29()
		self.Use_Item_Item_29_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_29()		
		self.Use_Item_Item_29_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_29_ShowTip()
		self.Use_Item_Item_29_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_29_Icon.Show()	

		self.Use_Item_Item_30_Bar = ui.ExpandedImageBox()
		self.Use_Item_Item_30_Bar.SetParent(self.Use_Item)	
		self.Use_Item_Item_30_Bar.SetPosition(167, 158)
		self.Use_Item_Item_30_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_30_Bar.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_30()
		self.Use_Item_Item_30_Bar.Show()
				
		self.Use_Item_Item_30_Icon = ui.ExpandedImageBox()
		self.Use_Item_Item_30_Icon.SetParent(self.Use_Item_Item_30_Bar)
		self.Use_Item_Item_30_Icon.SetPosition(0, 0)
		self.Use_Item_Item_30_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Use_Item_Item_30_Icon.OnMouseLeftButtonUp = lambda: self.Set_Use_Item_Item_30()
		self.Use_Item_Item_30_Icon.OnMouseRightButtonDown = lambda: self.Delete_Use_Item_Item_30()		
		self.Use_Item_Item_30_Icon.OnMouseOverIn = lambda: self.Use_Item_Item_30_ShowTip()
		self.Use_Item_Item_30_Icon.OnMouseOverOut = lambda: self.Use_Item_HideTip()			
		self.Use_Item_Item_30_Icon.Show()			
	
	###############################################################################################
	############################### GM Detector Comp ##############################################		
	###############################################################################################		
	
		### HorizontalBars ###
		self.GM_Detector_Logs_HorizontalBar = self.comp.HorizontalBar(self.GM_Detector_Logs , 10, 35, 320)
		self.GM_Detector_Logs_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.GM_Detector_Logs_HorizontalBar, 'Logi [Godzina, Nazwa, Koordynaty]', 5, 0, 0xFFFFE3AD)			
				
		### Buttons ###
		self.GM_Detector_Show_Logs_Button = self.comp.Button(self.GM_Detector, '', 'Logi', 125, 8, self.GM_Detector_Show_Logs_func, 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_01.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_02.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_03.sub')		
		self.GM_Detector_Plus_Delay_Button = self.comp.Button(self.GM_Detector, '', '', 100, 36, self.GM_Detector_Plus_Delay_func, 'd:/ymir work/ui/game/windows/btn_plus_up.sub', 'd:/ymir work/ui/game/windows/btn_plus_over.sub', 'd:/ymir work/ui/game/windows/btn_plus_down.sub')
		self.GM_Detector_Minus_Delay_Button = self.comp.Button(self.GM_Detector, '', '', 116, 36, self.GM_Detector_Minus_Delay_func, 'd:/ymir work/ui/game/windows/btn_minus_up.sub', 'd:/ymir work/ui/game/windows/btn_minus_over.sub', 'd:/ymir work/ui/game/windows/btn_minus_down.sub')
		self.GM_Detector_Show_List_Button = self.comp.Button(self.GM_Detector, 'Otwórz', '', 100, 75, self.GM_Detector_Show_List_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.GM_Detector_Scan_Button = self.comp.Button(self.GM_Detector, 'Scan', '', 45, 100, self.GM_Detector_Scan_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		
		self.GM_Detector_List_Question_Button = ui.ExpandedImageBox()
		self.GM_Detector_List_Question_Button.SetParent(self.GM_Detector_List)
		self.GM_Detector_List_Question_Button.SetPosition(173, 9)
		self.GM_Detector_List_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_01.tga")
		self.GM_Detector_List_Question_Button.OnMouseOverIn = lambda: self.GM_Detector_List_ShowTip()
		self.GM_Detector_List_Question_Button.OnMouseOverOut = lambda: self.GM_Detector_HideTip()
		self.GM_Detector_List_Question_Button.Show()	
		
		self.GM_Detector_List_Get_Nick_By_VID_Button = self.comp.Button(self.GM_Detector_List, '', 'Zdob¹dz Nick', 140, 240, self.GM_Detector_List_Get_Nick_By_VID_func, 'd:/ymir work/ui/game/windows/messenger_add_friend_01.sub', 'd:/ymir work/ui/game/windows/messenger_add_friend_02.sub', 'd:/ymir work/ui/game/windows/messenger_add_friend_03.sub')		
		self.GM_Detector_List_Add_Nick_Button = self.comp.Button(self.GM_Detector_List, 'Dodaj', '', 165, 240, self.GM_Detector_List_Add_Nick_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')						
		self.GM_Detector_List_Delete_Nick_Button = self.comp.Button(self.GM_Detector_List, 'Usuñ Nick', '', 18, 265, self.GM_Detector_List_Delete_Nick_func, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')						
			
		### Text ###
		self.GM_Detector_Delay_Text = self.comp.TextLine(self.GM_Detector, 'Skanowaæ co x s', 15, 35, self.comp.RGB(255, 255, 255))		
		self.GM_Detector_Mode_Text = self.comp.TextLine(self.GM_Detector, 'Po wykryciu', 15, 55, self.comp.RGB(255, 255, 255))		
		self.GM_Detector_Show_List_Text = self.comp.TextLine(self.GM_Detector, 'Lista szukanych', 15, 77, self.comp.RGB(255, 255, 255))		
	
		self.GM_Detector_Warning_1_Text = self.comp.TextLine(self.GM_Detector_PopUp, 'Wykryto: [GM]Test', 75, 47, self.comp.RGB(255, 255, 255))		
		self.GM_Detector_Warning_2_Text = self.comp.TextLine(self.GM_Detector_PopUp, 'Godzina: 15.47.44', 75, 62, self.comp.RGB(255, 255, 255))		
		self.GM_Detector_Warning_3_Text = self.comp.TextLine(self.GM_Detector_PopUp, 'Koordynaty: 678, 987', 75, 77, self.comp.RGB(255, 255, 255))		
	
	
		### EditLine ###
		self.GM_Detector_List_Nick_SlotBar, self.GM_Detector_List_Nick_EditLine = self.comp.EditLine(self.GM_Detector_List, '', 10, 240, 123, 15, 24)
		
		### ComboBox ###
		self.GM_Detector_Mode_Combobox = self.comp.ComboBox(self.GM_Detector, 'Powiadom', 100, 55, 60)	
	
		global GM_Detector_Mode_Combobox
		for GM_Detector_Mode_Combobox in GM_Detector_Mode_Combobox:
			self.GM_Detector_Mode_Combobox.InsertItem(1,str(GM_Detector_Mode_Combobox))  	
	
		### ListBoxEx ###
		self.GM_Detector_List_Bar, self.GM_Detector_Nick_List = self.comp.ListBoxEx(self.GM_Detector_List, 10, 35, 200, 200)
	
		self.GM_Detector_Logs_Bar, self.GM_Detector_Logs_List = self.comp.ListBoxEx(self.GM_Detector_Logs, 10, 55, 320, 200)

		### Img ###
		self.GM_Detector_Warning_img = self.comp.ExpandedImage(self.GM_Detector_PopUp , 5, 38, 'ZAHON_MOD/Icons/GM_Detector/GM_Detector_Warning.tga')	
		
	###############################################################################################
	################################# Detector Comp ###############################################		
	###############################################################################################			
					
		### HorizontalBars ###				
		self.Detector_HorizontalBar = self.comp.HorizontalBar(self.Detector , 10, 35, 340)
		self.Detector_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Detector_HorizontalBar, 'Logi [Goodzina, VID, Koordynaty, Nazwa]', 5, 0, 0xFFFFE3AD)			
			
		self.Detector_Panel_HorizontalBar = self.comp.HorizontalBar(self.Detector_Panel , 17, 20, 143)
		self.Detector_Panel_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Detector_Panel_HorizontalBar, 'Ustawienia', 5, 0, 0xFFFFE3AD)			
			
		self.Detector_Options_HorizontalBar = self.comp.HorizontalBar(self.Detector_Options , 10, 35, 120)
		self.Detector_Options_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Detector_Options_HorizontalBar, 'Zakres skanowania VID', 5, 0, 0xFFFFE3AD)			
			
		self.Detector_Options_More_Info_HorizontalBar = self.comp.HorizontalBar(self.Detector_Options , 10, 100, 120)
		self.Detector_Options_More_Info_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Detector_Options_More_Info_HorizontalBar, 'Dodatkowe Informacje', 5, 0, 0xFFFFE3AD)			
			
		### Buttons ###
		self.Detector_Show_Options_Button = self.comp.Button(self.Detector, '', 'Ustawienia Dodatkowe', 310, 8, self.Detector_Show_Options_func, 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_01.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_02.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_03.sub')		
		self.Detector_Plus_Delay_Button = self.comp.Button(self.Detector_Panel, '', '', 100, 43, self.Detector_Plus_Delay_func, 'd:/ymir work/ui/game/windows/btn_plus_up.sub', 'd:/ymir work/ui/game/windows/btn_plus_over.sub', 'd:/ymir work/ui/game/windows/btn_plus_down.sub')
		self.Detector_Minus_Delay_Button = self.comp.Button(self.Detector_Panel, '', '', 116, 43, self.Detector_Minus_Delay_func, 'd:/ymir work/ui/game/windows/btn_minus_up.sub', 'd:/ymir work/ui/game/windows/btn_minus_over.sub', 'd:/ymir work/ui/game/windows/btn_minus_down.sub')			
		self.Detector_Show_List_Button = self.comp.Button(self.Detector_Panel, 'Otwórz', '', 99, 85, self.Detector_Show_List_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.Detector_Scan_Button = self.comp.Button(self.Detector_Panel, 'Scan', '', 45, 118, self.Detector_Scan_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Detector_Walk_Button = self.comp.Button(self.Detector_Panel, 'Biegnij', '', 45, 143, self.Detector_Walk_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Detector_Teleport_Button = self.comp.Button(self.Detector_Panel, 'Teleportuj', '', 45, 168, self.Detector_Teleport_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		
		self.Detector_Question_Button = ui.ExpandedImageBox()
		self.Detector_Question_Button.SetParent(self.Detector)
		self.Detector_Question_Button.SetPosition(292, 9)
		self.Detector_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_01.tga")
		self.Detector_Question_Button.OnMouseOverIn = lambda: self.Detector_ShowTip()
		self.Detector_Question_Button.OnMouseOverOut = lambda: self.Detector_HideTip()
		self.Detector_Question_Button.Show()	
		
		self.Detector_List_Metin_List_Button = self.comp.Button(self.Detector_List, 'Metin', '', 17, 35, self.Detector_List_Metin_List_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')		
		self.Detector_List_Boss_List_Button = self.comp.Button(self.Detector_List, 'Boss', '', 64, 35, self.Detector_List_Boss_List_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')		
		self.Detector_List_Ore_List_Button = self.comp.Button(self.Detector_List, 'Ore', '', 111, 35, self.Detector_List_Ore_List_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')		
		self.Detector_List_Player_List_Button = self.comp.Button(self.Detector_List, 'Player', '', 158, 35, self.Detector_List_Player_List_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')		
		
		self.Detector_List_Get_Nick_By_VID_Button = self.comp.Button(self.Detector_List, '', 'Zdob¹dz Nazwê', 140, 261, self.Detector_List_Get_Nick_By_VID_func, 'd:/ymir work/ui/game/windows/messenger_add_friend_01.sub', 'd:/ymir work/ui/game/windows/messenger_add_friend_02.sub', 'd:/ymir work/ui/game/windows/messenger_add_friend_03.sub')		
		self.Detector_List_Add_Nick_Button = self.comp.Button(self.Detector_List, 'Dodaj', '', 165, 260, self.Detector_List_Add_Nick_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')						
		self.Detector_List_Delete_Nick_Button = self.comp.Button(self.Detector_List, 'Usuñ z Listy', '', 18, 285, self.Detector_List_Delete_Nick_func, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')						
			
		self.Detector_Options_Set_More_Info_Button = self.comp.Button(self.Detector_Options, 'Set', '', 27, 180, self.Detector_Options_Set_More_Info_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')		
							
		### Text ###
		self.Detector_Delay_Text = self.comp.TextLine(self.Detector_Panel, 'Skanuj co x s ', 18, 42, self.comp.RGB(255, 255, 255))				
		self.Detector_Mode_Text = self.comp.TextLine(self.Detector_Panel, 'Szukaj z Listy', 18, 63, self.comp.RGB(255, 255, 255))				
		self.Detector_Show_List_Text = self.comp.TextLine(self.Detector_Panel, 'Lista szukanych', 18, 87, self.comp.RGB(255, 255, 255))		
		
		self.Detector_Options_VID_Start_Scan_Text = self.comp.TextLine(self.Detector_Options, 'VID Start Scan', 15, 57, self.comp.RGB(255, 255, 255))		
		self.Detector_Options_VID_End_Scan_Text = self.comp.TextLine(self.Detector_Options, 'VID End Scan', 15, 77, self.comp.RGB(255, 255, 255))		
		
		self.Detector_Options_Level_Text = self.comp.TextLine(self.Detector_Options, 'Level:', 15, 120, self.comp.RGB(255, 255, 255))		
		self.Detector_Options_Distance_Text = self.comp.TextLine(self.Detector_Options, 'Distance:', 15, 140, self.comp.RGB(255, 255, 255))		
		self.Detector_Options_Instance_Type_Text = self.comp.TextLine(self.Detector_Options, 'Instance Type:', 15, 160, self.comp.RGB(255, 255, 255))		
				
		### Edit Line ###
		self.Detector_List_Nick_SlotBar, self.Detector_List_Nick_EditLine = self.comp.EditLine(self.Detector_List, '', 10, 261, 123, 15, 24)
		
		self.Detector_Options_VID_Start_Scan_SlotBar, self.Detector_Options_VID_Start_Scan_EditLine = self.comp.EditLine(self.Detector_Options, '1', 90, 55, 30, 15, 5)
		self.Detector_Options_VID_End_Scan_SlotBar, self.Detector_Options_VID_End_Scan_EditLine = self.comp.EditLine(self.Detector_Options, '40000', 90, 77, 30, 15, 5)
							
		### ComboBox ###	
		self.Detector_Mode_Combobox = self.comp.ComboBox(self.Detector_Panel, 'Wszystko', 100, 63, 57)	
	
		global Detector_Mode_Combobox
		for Detector_Mode_Combobox in Detector_Mode_Combobox:
			self.Detector_Mode_Combobox.InsertItem(1,str(Detector_Mode_Combobox))  	
						
		### List Box ###		
		self.Detector_Change_Log_Bar, self.Detector_Change_Log_List = self.comp.ListBoxEx(self.Detector, 10, 55, 340, 200)

		self.Detector_List_Bar, self.Detector_Name_List = self.comp.ListBoxEx(self.Detector_List, 10, 58, 200, 200)
			
	###############################################################################################
	################################### Teleport Comp #############################################		
	###############################################################################################			
				
		### HorizontalBars ###		
		self.Teleport_Coordinates_HorizontalBar = self.comp.HorizontalBar(self.Teleport_Coordinates , 10, 35, 180)
		self.Teleport_Coordinates_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Teleport_Coordinates_HorizontalBar, 'Zapisane Pozycje', 5, 0, 0xFFFFE3AD)			
				
		self.Teleport_Panel_HorizontalBar = self.comp.HorizontalBar(self.Teleport_Panel , 18, 170, 120)
		self.Teleport_Panel_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Teleport_Panel_HorizontalBar, 'Podaj pozycjê', 5, 0, 0xFFFFE3AD)			
								
		### List Box ###		
		self.Teleport_Coordinates_List_Bar, self.Teleport_Coordinates_List = self.comp.ListBoxEx(self.Teleport_Coordinates, 10, 55, 180, 200)		
				
		### Buttons ###		
		self.Teleport_Panel_Button = self.comp.Button(self.Teleport_Bar, '', '', 197, 106, self.Teleport_Panel_func, 'ZAHON_MOD/Buttons/Gui/Right_Gui_Show_Button_01.tga', 'ZAHON_MOD/Buttons/Gui/Right_Gui_Show_Button_02.tga', 'ZAHON_MOD/Buttons/Gui/Right_Gui_Show_Button_03.tga')
				
		self.Teleport_Coordinates_List_Refresh_Button = self.comp.Button(self.Teleport_Coordinates, '', 'Odœwie¿ Listê', 150, 8, self.Teleport_Coordinates_List_Refresh, 'd:/ymir work/ui/game/guild/Refresh_Button_01.sub', 'd:/ymir work/ui/game/guild/Refresh_Button_02.sub', 'd:/ymir work/ui/game/guild/Refresh_Button_03.sub')				
		self.Teleport_Coordinates_Add_Coords_Button = self.comp.Button(self.Teleport_Coordinates, 'Dodaj', '', 100, 260, self.Teleport_Coordinates_Add_Coords_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Teleport_Coordinates_Delete_Coords_Button = self.comp.Button(self.Teleport_Coordinates, 'Usuñ', '', 145, 260, self.Teleport_Coordinates_Delete_Coords_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Teleport_Coordinates_Teleport_Button = self.comp.Button(self.Teleport_Coordinates, 'Teleportuj', '', 10, 285, self.Teleport_Coordinates_Teleport_func, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')
			
		self.Teleport_Up_Button = self.comp.Button(self.Teleport_Panel, '', '', 62, 25, self.Teleport_Up_func, 'ZAHON_MOD/Buttons/Teleport/Up_Arrow.tga', 'ZAHON_MOD/Buttons/Teleport/Up_Arrow.tga', 'ZAHON_MOD/Buttons/Teleport/Up_Arrow.tga')
		self.Teleport_Down_Button = self.comp.Button(self.Teleport_Panel, '', '', 62, 99, self.Teleport_Down_func, 'ZAHON_MOD/Buttons/Teleport/Down_Arrow.tga', 'ZAHON_MOD/Buttons/Teleport/Down_Arrow.tga', 'ZAHON_MOD/Buttons/Teleport/Down_Arrow.tga')
		self.Teleport_Right_Button = self.comp.Button(self.Teleport_Panel, '', '', 99, 62, self.Teleport_Right_func, 'ZAHON_MOD/Buttons/Teleport/Right_Arrow.tga', 'ZAHON_MOD/Buttons/Teleport/Right_Arrow.tga', 'ZAHON_MOD/Buttons/Teleport/Right_Arrow.tga')
		self.Teleport_Left_Button = self.comp.Button(self.Teleport_Panel, '', '', 25, 62, self.Teleport_Left_func, 'ZAHON_MOD/Buttons/Teleport/Left_Arrow.tga', 'ZAHON_MOD/Buttons/Teleport/Left_Arrow.tga', 'ZAHON_MOD/Buttons/Teleport/Left_Arrow.tga')	
	
		self.Teleport_Plus_Button = self.comp.Button(self.Teleport_Panel, '', '', 102, 152, self.Teleport_Plus_func, 'd:/ymir work/ui/game/windows/btn_plus_up.sub', 'd:/ymir work/ui/game/windows/btn_plus_over.sub', 'd:/ymir work/ui/game/windows/btn_plus_down.sub')
		self.Teleport_Minus_Button = self.comp.Button(self.Teleport_Panel, '', '', 118, 152, self.Teleport_Minus_func, 'd:/ymir work/ui/game/windows/btn_minus_up.sub', 'd:/ymir work/ui/game/windows/btn_minus_over.sub', 'd:/ymir work/ui/game/windows/btn_minus_down.sub')
		
		self.Teleport_Panel_Teleport_Button = self.comp.Button(self.Teleport_Panel, 'Go', '', 97, 190, self.Teleport_Panel_Teleport_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
			
		### Text ###		
		self.Teleport_Distance_Text = self.comp.TextLine(self.Teleport_Panel, 'Dystans:', 20, 152, self.comp.RGB(255, 255, 255))		
			
		### Edit Line ###	
		self.Teleport_Coordinates_Position_Name_SlotBar, self.Teleport_Coordinates_Position_Editline = self.comp.EditLine(self.Teleport_Coordinates, '', 13, 261, 80, 15, 15)
		
		self.Teleport_slotbar_Distance, self.Teleport_EditLine_Distance = self.comp.EditLine(self.Teleport_Panel, '10', 65, 150, 30, 15, 0)
		self.Teleport_X_SlotBar, self.Teleport_X_Editline = self.comp.EditLine(self.Teleport_Panel, '', 20, 192, 30, 15, 4)
		self.Teleport_Y_SlotBar, self.Teleport_Y_Editline = self.comp.EditLine(self.Teleport_Panel, '', 60, 192, 30, 15, 4)
		
	###############################################################################################
	################################ Ghost Mod Comp ###############################################		
	###############################################################################################			
		
		### Buttons ###		
		self.Ghost_Mode_Status_Button = self.comp.Button(self.Ghost_Mode, 'Ghost', '', 10, 18, self.Ghost_Mode_Status_func, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')
			
	###############################################################################################
	################################### Other Comp ################################################	
	###############################################################################################				
			
		### Text ###	
		self.Other_Gui_Item_Clicker_Text = self.comp.TextLine(self.Other_Gui, 'Item Clicker', 15, 35, self.comp.RGB(255, 255, 255))		
		self.Other_Gui_Spam_Bot_Text = self.comp.TextLine(self.Other_Gui, 'Spam Bot', 15, 55, self.comp.RGB(255, 255, 255))		
		self.Other_Gui_Bonus_Switcher_Text = self.comp.TextLine(self.Other_Gui, 'Bonus Switcher', 15, 75, self.comp.RGB(255, 255, 255))		
		self.Other_Gui_Fish_Bot_Text = self.comp.TextLine(self.Other_Gui, 'Fish Bot', 15, 95, self.comp.RGB(255, 255, 255))		
		self.Other_Gui_Buff_Bot_Text = self.comp.TextLine(self.Other_Gui, 'Buff Bot', 15, 115, self.comp.RGB(255, 255, 255))		
		self.Other_Gui_Yang_Bug_Text = self.comp.TextLine(self.Other_Gui, 'Yang Bug', 15, 135, self.comp.RGB(255, 255, 255))		
		self.Other_Gui_Book_Reader_Text = self.comp.TextLine(self.Other_Gui, 'Book Reader', 15, 155, self.comp.RGB(255, 255, 255))		
		self.Other_Gui_Python_Loader_Text = self.comp.TextLine(self.Other_Gui, 'Python Loader', 15, 175, self.comp.RGB(255, 255, 255))		
		
		self.Other_Gui_Exp_Donator_Text = self.comp.TextLine(self.Other_Gui, 'Exp Donator', 155, 35, self.comp.RGB(255, 255, 255))		
		self.Other_Gui_Inventory_Menager_Text = self.comp.TextLine(self.Other_Gui, 'Eq Menager', 155, 55, self.comp.RGB(255, 255, 255))		
		self.Other_Gui_Environment_Text = self.comp.TextLine(self.Other_Gui, 'Environment', 155, 75, self.comp.RGB(255, 255, 255))		
		self.Other_Gui_Item_Info_Text = self.comp.TextLine(self.Other_Gui, 'Item Info', 155, 95, self.comp.RGB(255, 255, 255))		
		self.Other_Gui_Feak_Info_Text = self.comp.TextLine(self.Other_Gui, 'Feak Info', 155, 115, self.comp.RGB(255, 255, 255))		
		
		self.Other_Gui_Another_Text = self.comp.TextLine(self.Other_Gui, 'Another', 155, 175, self.comp.RGB(255, 255, 255))		
		
		### Buttons ###
		self.Other_Gui_Question_Button = ui.ExpandedImageBox()
		self.Other_Gui_Question_Button.SetParent(self.Other_Gui)
		self.Other_Gui_Question_Button.SetPosition(248, 9)
		self.Other_Gui_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_01.tga")
		self.Other_Gui_Question_Button.OnMouseOverIn = lambda: self.Other_Gui_ShowTip()
		self.Other_Gui_Question_Button.OnMouseOverOut = lambda: self.Other_Gui_HideTip()
		self.Other_Gui_Question_Button.Show()			
		
		self.Other_Gui_Item_Clicker_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 100, 32, self.Other_Gui_Item_Clicker_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Other_Gui_Spam_Bot_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 100, 52, self.Other_Gui_Spam_Bot_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Other_Gui_Bonus_Switcher_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 100, 72, self.Other_Gui_Bonus_Switcher_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Other_Gui_Fish_Bot_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 100, 92, self.Other_Gui_Fish_Bot_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Other_Gui_Buff_Bot_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 100, 112, self.Other_Gui_Buff_Bot_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Other_Gui_Yang_Bug_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 100, 132, self.Other_Gui_Yang_Bug_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Other_Gui_Book_Reader_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 100, 152, self.Other_Gui_Book_Reader_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Other_Gui_Python_Loader_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 100, 172, self.Other_Gui_Python_Loader_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		
		self.Other_Gui_Exp_Donator_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 240, 32, self.Other_Gui_Exp_Donator_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Other_Gui_Inventory_Menager_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 240, 52, self.Other_Gui_Inventory_Menager_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Other_Gui_Environment_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 240, 72, self.Other_Gui_Environment_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Other_Gui_Item_Info_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 240, 92, self.Other_Gui_Item_Info_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Other_Gui_Feak_Info_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 240, 112, self.Other_Gui_Feak_Info_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Other_Gui_Another_Button = self.comp.Button(self.Other_Gui, 'Otwórz', '', 240, 172, self.Other_Gui_Another_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		
		### Img ###
		self.Other_Gui_Bar_1_img = self.comp.ExpandedImage(self.Other_Gui , 145, 35, 'ZAHON_MOD/Icons/ETC/Bar.tga')	
		self.Other_Gui_Bar_2_img = self.comp.ExpandedImage(self.Other_Gui , 145, 60, 'ZAHON_MOD/Icons/ETC/Bar.tga')	
						
	###############################################################################################
	################################## Options Comp ###############################################		
	###############################################################################################			
		
		### HorizontalBars ###	
		self.Options_HorizontalBar = self.comp.HorizontalBar(self.Options , 10, 100, 223)
		self.Options_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Options_HorizontalBar, "ZAHON MOD 2.0", 5, 0, 0xFFFFE3AD)			
		
		### Buttons ###
		self.Options_Restart_Button = self.comp.Button(self.Options, '', 'Przywróæ domyœlne ustawienia', 197, 9, self.Options_Restart_Refresh, 'ZAHON_MOD/Buttons/ETC/Restart_Button_01.tga', 'ZAHON_MOD/Buttons/ETC/Restart_Button_02.tga', 'ZAHON_MOD/Buttons/ETC/Restart_Button_03.tga')				
				
		### Text ###
		self.Options_Language_Text = self.comp.TextLine(self.Options, 'Jêzyk (jeszcze nie dzia³a)', 15, 40, self.comp.RGB(255, 255, 255))		
		self.Options_Save_Mode_Text = self.comp.TextLine(self.Options, 'Tryb zapisu ustawieñ', 15, 60, self.comp.RGB(255, 255, 255))		
		self.Options_Gui_Position_Text = self.comp.TextLine(self.Options, 'Po³o¿enie Gui', 15, 80, self.comp.RGB(255, 255, 255))		
				
		### ComboBox ###
		global Options_Gui_Position_Combobox		
		self.Options_Gui_Position_Combobox = self.comp.ComboBox(self.Options, 'Lewo', 170, 80, 60)	
		
		for Options_Gui_Position_Combobox in Options_Gui_Position_Combobox:
			self.Options_Gui_Position_Combobox.InsertItem(1,str(Options_Gui_Position_Combobox)) 		
		
		global Options_Save_Mode_Combobox
		self.Options_Save_Mode_Combobox = self.comp.ComboBox(self.Options, 'Ogólny', 170, 60, 60)	
		
		for Options_Save_Mode_Combobox in Options_Save_Mode_Combobox:
			self.Options_Save_Mode_Combobox.InsertItem(1,str(Options_Save_Mode_Combobox)) 

		global Options_Language_Combobox
		self.Options_Language_Combobox = self.comp.ComboBox(self.Options, 'PL', 170, 40, 60)		
	
		for Options_Language_Combobox in Options_Language_Combobox:
			self.Options_Language_Combobox.InsertItem(1,str(Options_Language_Combobox)) 			

		### Buttons ###	
		self.Options_MPC_Button = self.comp.Button(self.Options, '', '', 21, 120, self.Options_MPC_func, 'ZAHON_MOD/Icons/Info/MPC.tga', 'ZAHON_MOD/Icons/Info/MPC.tga', 'ZAHON_MOD/Icons/Info/MPC.tga')
		self.Options_YouTube_Button = self.comp.Button(self.Options, '', '', 90, 120, self.Options_YouTube_func, 'ZAHON_MOD/Icons/Info/YouTube.tga', 'ZAHON_MOD/Icons/Info/YouTube.tga', 'ZAHON_MOD/Icons/Info/YouTube.tga')
		self.Options_FaceBook_Button = self.comp.Button(self.Options, '', '', 156, 120, self.Options_FaceBook_func, 'ZAHON_MOD/Icons/Info/FaceBook.tga', 'ZAHON_MOD/Icons/Info/FaceBook.tga', 'ZAHON_MOD/Icons/Info/FaceBook.tga')
			
	###############################################################################################
	############################## Restart Options Comp ###########################################		
	###############################################################################################			
			
		### Buttons ###
		self.Restart_Options_Yes_Button = self.comp.Button(self.Restart_Options, 'Tak', '', 20, 40, self.Restart_Options_Yes_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Restart_Options_No_Button = self.comp.Button(self.Restart_Options, 'Nie', '', 130, 40, self.Restart_Options_No_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		
	###############################################################################################
	################################ Info Screen Comp #############################################		
	###############################################################################################		
		
		### Img ###
		self.Info_Screen_img = self.comp.ExpandedImage(self.Info_Screen , 5, 30, 'ZAHON_MOD/Icons/Info_Screen/Info_Screen_01.tga')	
	
		### EditLine ###
		self.Info_Screen_SlotBar, self.Info_Screen_EditLine = self.comp.EditLine(self.Info_Screen, 'W ka¿dej chwili mo¿esz schowaæ lub wysun¹æ panel boczny za pomoc¹ przycisku, który znajduje siê po lewj stronie ekranu', 18, 265, 330, 45, 0)
		
		### Buttons ###
		self.Info_Screen_Back_Button = self.comp.Button(self.Info_Screen, '<<<', '', 15, 320, self.Info_Screen_Back_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Info_Screen_Next_Button = self.comp.Button(self.Info_Screen, '>>>', '', 260, 320, self.Info_Screen_Next_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Info_Screen_End_Button = self.comp.ButtonHide(self.Info_Screen, 'Zakoñcz', '', 140, 320, self.Info_Screen_End_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
				
	###############################################################################################
	################################### Gui Comp ##################################################		
	###############################################################################################					
				
		### Buttons ###
		self.Gui_Button = self.comp.Button(self.Gui, '', '', 60, 171, self.Gui_func, 'ZAHON_MOD/Buttons/Gui/Right_Gui_Show_Button_01.tga', 'ZAHON_MOD/Buttons/Gui/Right_Gui_Show_Button_02.tga', 'ZAHON_MOD/Buttons/Gui/Right_Gui_Show_Button_03.tga')
	
		self.Auto_Attack_img = ui.ExpandedImageBox()
		self.Auto_Attack_img.SetParent(self.Gui)
		self.Auto_Attack_img.SetPosition(16, 30)
		self.Auto_Attack_img.OnMouseLeftButtonDown = lambda: self.Auto_Attack_func()		
		self.Auto_Attack_img.OnMouseRightButtonDown = lambda: self.Auto_Attack_Otions()	
		self.Auto_Attack_img.LoadImage("ZAHON_MOD/Buttons/Function/Auto_Attack.tga")
		self.Auto_Attack_img.Show()	

		self.Mobber_img = ui.ExpandedImageBox()
		self.Mobber_img.SetParent(self.Gui)
		self.Mobber_img.SetPosition(16, 67)
		self.Mobber_img.OnMouseLeftButtonDown = lambda: self.Mobber_func()		
		self.Mobber_img.OnMouseRightButtonDown = lambda: self.Mobber_Options()	
		self.Mobber_img.LoadImage("ZAHON_MOD/Buttons/Function/Mobber.tga")
		self.Mobber_img.Show()		
	
		self.Pick_Up_img = ui.ExpandedImageBox()
		self.Pick_Up_img.SetParent(self.Gui)
		self.Pick_Up_img.SetPosition(16, 104)
		self.Pick_Up_img.OnMouseLeftButtonDown = lambda: self.Pick_Up_func()		
		self.Pick_Up_img.OnMouseRightButtonDown = lambda: self.Pick_Up_Options()		
		self.Pick_Up_img.LoadImage("ZAHON_MOD/Buttons/Function/Pick_Up.tga")
		self.Pick_Up_img.Show()	

		self.Auto_Pot_img = ui.ExpandedImageBox()
		self.Auto_Pot_img.SetParent(self.Gui)
		self.Auto_Pot_img.SetPosition(16, 141)
		self.Auto_Pot_img.OnMouseLeftButtonDown = lambda: self.Auto_Pot_func()		
		self.Auto_Pot_img.OnMouseRightButtonDown = lambda: self.Auto_Pot_Options()		
		self.Auto_Pot_img.LoadImage("ZAHON_MOD/Buttons/Function/Auto_Pot.tga")
		self.Auto_Pot_img.Show()		
	
		self.Restart_img = ui.ExpandedImageBox()
		self.Restart_img.SetParent(self.Gui)
		self.Restart_img.SetPosition(16, 178)
		self.Restart_img.OnMouseLeftButtonDown = lambda: self.Restart_func()			
		self.Restart_img.LoadImage("ZAHON_MOD/Buttons/Function/Restart.tga")
		self.Restart_img.Show()		

		self.Use_Item_img = ui.ExpandedImageBox()
		self.Use_Item_img.SetParent(self.Gui)
		self.Use_Item_img.SetPosition(16, 215)
		self.Use_Item_img.OnMouseLeftButtonDown = lambda: self.Use_Item_func()		
		self.Use_Item_img.OnMouseRightButtonDown = lambda: self.Use_Item_Options()	
		self.Use_Item_img.LoadImage("ZAHON_MOD/Buttons/Function/Use_Item.tga")
		self.Use_Item_img.Show()			
	
		self.GM_Detector_Img = ui.ExpandedImageBox()
		self.GM_Detector_Img.SetParent(self.Gui)
		self.GM_Detector_Img.SetPosition(16, 252)
		self.GM_Detector_Img.OnMouseLeftButtonDown = lambda: self.GM_Detector_func()		
		self.GM_Detector_Img.OnMouseRightButtonDown = lambda: self.GM_Detector_Options()	
		self.GM_Detector_Img.LoadImage("ZAHON_MOD/Buttons/Function/Gm_Detector.tga")
		self.GM_Detector_Img.Show()		

		self.Detector_Img = ui.ExpandedImageBox()
		self.Detector_Img.SetParent(self.Gui)
		self.Detector_Img.SetPosition(16, 289)
		self.Detector_Img.OnMouseLeftButtonDown = lambda: self.Detector_func()		
		self.Detector_Img.OnMouseRightButtonDown = lambda: self.Detector_Options_func()	
		self.Detector_Img.LoadImage("ZAHON_MOD/Buttons/Function/Detector.tga")
		self.Detector_Img.Show()		
	
		self.Teleport_Button = ui.ExpandedImageBox()
		self.Teleport_Button.SetParent(self.Gui)
		self.Teleport_Button.SetPosition(16, 326)
		self.Teleport_Button.OnMouseLeftButtonDown = lambda: self.Teleport_func()	
		self.Teleport_Button.OnMouseOverIn = lambda: self.Teleport_In()
		self.Teleport_Button.OnMouseOverOut = lambda: self.Teleport_Over()		
		self.Teleport_Button.LoadImage("ZAHON_MOD/Buttons/Function/Teleport_Button_01.tga")
		self.Teleport_Button.Show()	

		self.Other_Button = ui.ExpandedImageBox()
		self.Other_Button.SetParent(self.Gui)
		self.Other_Button.SetPosition(16, 363)
		self.Other_Button.OnMouseLeftButtonDown = lambda: self.Other_func()	
		self.Other_Button.OnMouseOverIn = lambda: self.Other_In()
		self.Other_Button.OnMouseOverOut = lambda: self.Other_Over()		
		self.Other_Button.LoadImage("ZAHON_MOD/Buttons/Function/Other_Button_01.tga")
		self.Other_Button.Show()	

		self.Options_Button = ui.ExpandedImageBox()
		self.Options_Button.SetParent(self.Gui)
		self.Options_Button.SetPosition(16, 400)
		self.Options_Button.OnMouseLeftButtonDown = lambda: self.Options_func()	
		self.Options_Button.OnMouseOverIn = lambda: self.Options_In()
		self.Options_Button.OnMouseOverOut = lambda: self.Options_Over()		
		self.Options_Button.LoadImage("ZAHON_MOD/Buttons/Function/Options_Button_01.tga")
		self.Options_Button.Show()		
	
	################################### Gui Func ######################################	
								
	def Gui_func(self):
		global Gui
		if Gui == 0:
			Gui = 1
			self.Gui.SetPosition(-10, 120)	
			self.Gui_Button.SetUpVisual("ZAHON_MOD/Buttons/Gui/Right_Gui_Hide_Button_01.tga")
			self.Gui_Button.SetOverVisual("ZAHON_MOD/Buttons/Gui/Right_Gui_Hide_Button_02.tga")
			self.Gui_Button.SetDownVisual("ZAHON_MOD/Buttons/Gui/Right_Gui_Hide_Button_03.tga")						
		else:
			Gui = 0
			self.Gui.SetPosition(-60, 120)	
			self.Gui_Button.SetUpVisual("ZAHON_MOD/Buttons/Gui/Right_Gui_Show_Button_01.tga")
			self.Gui_Button.SetOverVisual("ZAHON_MOD/Buttons/Gui/Right_Gui_Show_Button_02.tga")
			self.Gui_Button.SetDownVisual("ZAHON_MOD/Buttons/Gui/Right_Gui_Show_Button_03.tga")		
	
	################################### Auto Attack ##########################################		
		
	### Auto Attack Status ###	
	def Auto_Attack_func(self):	
		global Auto_Attack_Status
		if Auto_Attack_Status == 0:
			Auto_Attack_Status = 1
			self.Enable_Auto_Attack()
			chat.AppendChat(2, "Auto Atak W³¹czony")
			self.Auto_Attack_img.LoadImage("ZAHON_MOD/Buttons/Function/Auto_Attack_On.tga")
		else:
			Auto_Attack_Status = 0
			self.Disable_Auto_Attack()
			chat.AppendChat(2, "Auto Atak Wy³¹czony")
			self.Auto_Attack_img.LoadImage("ZAHON_MOD/Buttons/Function/Auto_Attack_Off.tga")
	
	### Auto Attack Enable ###		
	def Enable_Auto_Attack(self):
		global Auto_Attack_Mode
		global Auto_Attack_Delay
	
		Auto_Attack_Mode = self.Auto_Attack_Mode_ComboBox.GetCurrentText()
		
		if Auto_Attack_Mode == "Rotacyjny":
			Direction = app.GetRandom(0,7)
			player.SetAttackKeyState(TRUE)
			chr.SetDirection(Direction)					
			
		if Auto_Attack_Mode == "Zwyk³y":	
				player.SetAttackKeyState(TRUE)	
					
		self.Delay_Auto_Attack = WaitingDialog()
		self.Delay_Auto_Attack.Open(int(Auto_Attack_Delay))
		self.Delay_Auto_Attack.SAFE_SetTimeOverEvent(self.Enable_Auto_Attack)			
			
	def Disable_Auto_Attack(self):
		player.SetAttackKeyState(FALSE)
		
		self.Delay_Auto_Attack = WaitingDialog()
		self.Delay_Auto_Attack.Open(float(99999999999999999))
		self.Delay_Auto_Attack.SAFE_SetTimeOverEvent(self.Disable_Auto_Attack)	
	
	### Auto Attack Plus/Minus ###			
	def Auto_Attack_Plus_func(self):
		global Auto_Attack_Delay
		
		Auto_Attack_Delay = int(int(Auto_Attack_Delay) + 1)	
		self.Auto_Attack_Delay_Text.SetText("Szybkoœæ rotacji " + str(Auto_Attack_Delay) + " s")
						
	def Auto_Attack_Minus_func(self):
		global Auto_Attack_Delay
		
		if Auto_Attack_Delay > 1:
			Auto_Attack_Delay = int(int(Auto_Attack_Delay) - 1)	
			self.Auto_Attack_Delay_Text.SetText("Szybkoœæ rotacji " + str(Auto_Attack_Delay) + " s")
		else:
			chat.AppendChat(2,"Nie mo¿esz zmniejszyæ czasu poni¿j 1 s !")		
	
	### Auto Attack Options ###		
	def Auto_Attack_Otions(self):
		if self.Auto_Attack.IsShow():
			self.Auto_Attack.Hide()
		else:
			self.Auto_Attack.Show()			
			self.Auto_Attack.SetPosition(50, 120)	
	
	################################### Mobber ##########################################		
	
	### Mobber Status ###	
	def Mobber_func(self):
		global Mobber_Status
		if Mobber_Status == 0:
			Mobber_Status = 1
			self.Enable_Mobber()
			chat.AppendChat(2, "Mobber W³¹czony")
			self.Mobber_img.LoadImage("ZAHON_MOD/Buttons/Function/Mobber_On.tga")
		else:
			Mobber_Status = 0
			self.Disable_Mobber()
			chat.AppendChat(2, "Mobber Wy³¹czony")
			self.Mobber_img.LoadImage("ZAHON_MOD/Buttons/Function/Mobber_Off.tga")			
		
	### Mobber Enable ###	
	def Enable_Mobber(self):
		global Mobber_Status, Mobber_Delay, Mobber_ID, Mobber_HP, Mobber_Mode
		
		Mobber_Mode = self.Mobber_Mode_ComboBox.GetCurrentText()
		
		Max_HP = player.GetStatus(player.MAX_HP)
		Actually_HP = player.GetStatus(player.HP)		
		
		if Mobber_Status == 1:
		
			if Mobber_Mode == "Pelerynki":
		
				if (float(Actually_HP) / (float(Max_HP)) * 100) >= int(Mobber_HP):
					for i in xrange(player.INVENTORY_PAGE_SIZE*5):
						ItemValue = player.GetItemIndex(i)
						if ItemValue == (int(Mobber_ID)):
							net.SendItemUsePacket(i)
							break
							
			if Mobber_Mode == "Mobber":	
			
				if (float(Actually_HP) / (float(Max_HP)) * 100) >= int(Mobber_HP):			
					for vid in xrange(1, 100000):
						if chr.IsEnemy(vid) != 0:
							if not (int(player.GetCharacterDistance(vid)) > int(9000)):
								kamer.SendBattlePacket(vid)			

			if Mobber_ID == 0:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Aby wszystko dzia³a³o poprawnie wstaw pelerynki!")				
										
		self.Delay_Mobber = WaitingDialog()
		self.Delay_Mobber.Open(int(Mobber_Delay))
		self.Delay_Mobber.SAFE_SetTimeOverEvent(self.Enable_Mobber)
			
	def Disable_Mobber(self):	
		self.Delay_Mobber = WaitingDialog()
		self.Delay_Mobber.Open(float(99999999999999999))
		self.Delay_Mobber.SAFE_SetTimeOverEvent(self.Disable_Mobber)		
		
	### Mobber Set ###			
	def Set_Mobber(self):
		global Mobber_ID, Mobber_Icon
		
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				
				Mobber_ID = mouseModule.mouseController.GetAttachedItemIndex()
				chat.AppendChat(2,"Pomyœnie dodano " + str(item.GetItemName()) + " o ID: " + str(attachedSlotVnum))					
				
				item.SelectItem(int(attachedSlotVnum))
				Mobber_Icon = item.GetIconImageFileName()
				self.Mobber_Item_Icon.LoadImage(str(Mobber_Icon))
				
				mouseModule.mouseController.DeattachObject()					
						
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿sz wstawiæ przedmiotu")				
		
	def Delete_Mobber(self):
		global Mobber_ID

		Mobber_ID = 0	
		self.Mobber_Item_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Mobber_HideTip()				
		
	### Mobber SliderBar ###
	def Set_Slidbar_Mobber(self):
		global Mobber_HP
		Mobber_HP = int(self.Slidbar_Mobber.GetSliderPos() * 100)
		self.Mobber_HP_Text.SetText("Przestañ u¿ywaæ, jeœli HP < " + str(Mobber_HP) + "%")			
		
	### Mobber Plus/Minus ###	
	def Mobber_Plus_func(self):
		global Mobber_Delay
		Mobber_Delay = int(int(Mobber_Delay) + 1)	
		self.Mobber_Delay_Text.SetText("Szybkoœæ " + str(Mobber_Delay) + " s")	
			
	def Mobber_Minus_func(self):
		global Mobber_Delay	
		if Mobber_Delay > 1:
			Mobber_Delay = int(int(Mobber_Delay) - 1)	
			self.Mobber_Delay_Text.SetText("Szybkoœæ " + str(Mobber_Delay) + " s")	
		else:
			chat.AppendChat(2,"Nie mo¿sz zmniejszyæzasu poni¿j 1 s !")			
		
	### Mobber ToolTip ###	
	def Mobber_ShowTip(self):
		global Mobber_ID
		
		if Mobber_ID > 0:
		
			item.SelectItem(int(Mobber_ID))
		
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Mobber_ID)), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Mobber_ID), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Mobber_ID))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()			
		
		if Mobber_ID == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()			
		
	def Mobber_HideTip(self):
		self.txttooltip.ClearToolTip()
		self.txttooltip.Hide()			
		
	### Mobber Options	###
	def Mobber_Options(self):
		if self.Mobber.IsShow():
			self.Mobber.Hide()
		else:
			self.Mobber.Show()			
			self.Mobber.SetPosition(50, 120)			
	
	################################### Pick Up ##########################################	
	
	### Pick Up Status ###
	def Pick_Up_func(self):
		global Pick_Up_Status
		if Pick_Up_Status == 0:
			Pick_Up_Status = 1
			self.Enable_Pick_Up()
			chat.AppendChat(2, "PickUp W³¹czony")
			self.Pick_Up_img.LoadImage("ZAHON_MOD/Buttons/Function/Pick_Up_On.tga")
		else:
			Pick_Up_Status = 0
			self.Disable_Pick_Up()
			chat.AppendChat(2, "PickUp Wy³¹czony")
			self.Pick_Up_img.LoadImage("ZAHON_MOD/Buttons/Function/Pick_Up_Off.tga")
		
	### Pick Up Enable ###
	def Enable_Pick_Up(self):
		global Pick_Up_Delay
		
		player.PickCloseItem() 
	
		self.Delay_Pick_up = WaitingDialog()
		self.Delay_Pick_up.Open(float(Pick_Up_Delay))
		self.Delay_Pick_up.SAFE_SetTimeOverEvent(self.Enable_Pick_Up)
			
	def Disable_Pick_Up(self):
	
		self.Delay_Pick_up = WaitingDialog()
		self.Delay_Pick_up.Open(float(99999999999999999))
		self.Delay_Pick_up.SAFE_SetTimeOverEvent(self.Disable_Pick_Up)		
		
	### Pick Up Plus/Minus ###
	def Pick_Up_Plus_func(self):
		global Pick_Up_Delay
		
		Pick_Up_Delay = float(float(Pick_Up_Delay) + 0.1)
		self.Pick_Up_Delay_Text.SetText("Szybkoœæ podnoszenia: " + str(Pick_Up_Delay)[0:3] + " s")
		
	def Pick_Up_Minus_func(self):
		global Pick_Up_Delay
		
		if Pick_Up_Delay > 0.1:
			Pick_Up_Delay = float(float(Pick_Up_Delay) - 0.1)
			self.Pick_Up_Delay_Text.SetText("Szybkoœæ podnoszenia: " + str(Pick_Up_Delay)[0:3] + " s")
		else:
			chat.AppendChat(2,"Nie mo¿esz zmniejszyæ czasu poni¿ej 0.1 s !")			
		
	### Pick Up Options ###	
	def Pick_Up_Options(self):
		if self.Pick_Up.IsShow():
			self.Pick_Up.Hide()
		else:
			self.Pick_Up.Show()			
			self.Pick_Up.SetPosition(50, 120)	
		
	################################### Auto Pot ##########################################		
	
	### Auto Pot Status ###
	def Auto_Pot_func(self):
		global Auto_Pot_Status
		if Auto_Pot_Status == 0:
			Auto_Pot_Status = 1
			self.Enable_Auto_Pot()
			chat.AppendChat(2, "Auto Pot W³¹czony")
			self.Auto_Pot_img.LoadImage("ZAHON_MOD/Buttons/Function/Auto_Pot_On.tga")
		else:
			Auto_Pot_Status = 0
			self.Disable_Auto_Pot()
			chat.AppendChat(2, "Auto Pot Wy³¹czony")
			self.Auto_Pot_img.LoadImage("ZAHON_MOD/Buttons/Function/Auto_Pot_Off.tga")
		
	### Auto Pot Enable ###
	def Enable_Auto_Pot(self):
		global Auto_Pot_Status, Auto_Pot_Red_ID, Auto_Pot_Red_Value, Auto_Pot_Blue_ID, Auto_Pot_Blue_Value
				
		Max_HP = player.GetStatus(player.MAX_HP)
		Actually_HP = player.GetStatus(player.HP)
		
		Max_PE = player.GetStatus(player.MAX_SP)
		Actually_PE = player.GetStatus(player.SP)			
		
		if Auto_Pot_Status == 1:		
			if (float(Actually_HP) / (float(Max_HP)) * 100) <= int(Auto_Pot_Red_Value):
				for i in xrange(player.INVENTORY_PAGE_SIZE*5):
					Item_1_Index = player.GetItemIndex(i)
					if Item_1_Index == (int(Auto_Pot_Red_ID)):
						net.SendItemUsePacket(i)	
						break	

			if (float(Actually_PE) / (float(Max_PE)) * 100) <= float(Auto_Pot_Blue_Value):
				for i in xrange(player.INVENTORY_PAGE_SIZE*5):
					Item_2_Index = player.GetItemIndex(i)
					if Item_2_Index == (int(Auto_Pot_Blue_ID)):
						net.SendItemUsePacket(i)	
						break					
			
		self.Delay_Auto_Pot = WaitingDialog()
		self.Delay_Auto_Pot.Open(float(0.1))
		self.Delay_Auto_Pot.SAFE_SetTimeOverEvent(self.Enable_Auto_Pot)
			
	def Disable_Auto_Pot(self):	
		self.Delay_Auto_Pot = WaitingDialog()
		self.Delay_Auto_Pot.Open(float(99999999999999999))
		self.Delay_Auto_Pot.SAFE_SetTimeOverEvent(self.Disable_Auto_Pot)	
		
	### Auto Pot Set Red ###
	def Set_Auto_Pot_Red(self):
		global Auto_Pot_Red_ID
		
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				
				Auto_Pot_Red_ID = mouseModule.mouseController.GetAttachedItemIndex()
				chat.AppendChat(2,"Pomyœlnie dodano " + str(item.GetItemName()) + " o ID: " + str(attachedSlotVnum))					
				
				item.SelectItem(int(attachedSlotVnum))
				Auto_Pot_Red_Icon = item.GetIconImageFileName()
				self.Auto_Pot_Red_Icon.LoadImage(str(Auto_Pot_Red_Icon))
				
				self.Auto_Pot_HideTip()
				
				mouseModule.mouseController.DeattachObject()					
						
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")				
	
	def Delete_Auto_Pot_Red(self):
		global Auto_Pot_Red_ID
		
		Auto_Pot_Red_ID = 0
		
		self.Auto_Pot_Red_Icon.LoadImage("ZAHON_MOD/Icons/Auto_Pot/Red_Pot_Shadow.tga")
		self.Auto_Pot_HideTip()				

	### Auto Pot Set Blue ###
	def Set_Auto_Pot_Blue(self):
		global Auto_Pot_Blue_ID
		
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				
				Auto_Pot_Blue_ID = mouseModule.mouseController.GetAttachedItemIndex()
				chat.AppendChat(2,"Pomyœlnie dodano " + str(item.GetItemName()) + " o ID: " + str(attachedSlotVnum))					
				
				item.SelectItem(int(attachedSlotVnum))
				Auto_Pot_Blue_Icon = item.GetIconImageFileName()
				self.Auto_Pot_Blue_Icon.LoadImage(str(Auto_Pot_Blue_Icon))
				
				self.Auto_Pot_HideTip()
				
				mouseModule.mouseController.DeattachObject()					
						
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")				
	
	def Delete_Auto_Pot_Blue(self):
		global Auto_Pot_Blue_ID
		
		Auto_Pot_Blue_ID = 0
		
		self.Auto_Pot_Blue_Icon.LoadImage("ZAHON_MOD/Icons/Auto_Pot/Blue_Pot_Shadow.tga")
		self.Auto_Pot_HideTip()					
		
	### Auto Pot Set SliderBar ###
	def Set_Slidbar_Auto_Pot_Red_Value(self):
		global Auto_Pot_Red_Value
		Auto_Pot_Red_Value = int(self.Slidbar_Auto_Pot_Red_Value.GetSliderPos() * 100)
		self.Auto_Pot_Red_Value_Text.SetText("Przy ilu % u¿ywaæ Red Pot: " + str(Auto_Pot_Red_Value) + "%")	
		
	def Set_Slidbar_Auto_Pot_Blue_Value(self):
		global Auto_Pot_Blue_Value
		Auto_Pot_Blue_Value = int(self.Slidbar_Auto_Pot_Blue_Value.GetSliderPos() * 100)
		self.Auto_Pot_Blue_Value_Text.SetText("Przy ilu % u¿ywaæ Blue Pot: " + str(Auto_Pot_Blue_Value) + "%")		
		
	### Auto Pot ToolTip ###
	def Auto_Pot_Red_ShowTip(self):
		global Auto_Pot_Red_ID
		
		if Auto_Pot_Red_ID > 0:
			
			item.SelectItem(int(Auto_Pot_Red_ID))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Auto_Pot_Red_ID)), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Auto_Pot_Red_ID), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Auto_Pot_Red_ID))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Auto_Pot_Red_ID == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()			
						
	def Auto_Pot_Blue_ShowTip(self):
		global Auto_Pot_Blue_ID
		
		if Auto_Pot_Blue_ID > 0:
			
			item.SelectItem(int(Auto_Pot_Blue_ID))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Auto_Pot_Blue_ID)), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Auto_Pot_Blue_ID), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Auto_Pot_Blue_ID))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

		if Auto_Pot_Blue_ID == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()					
			
	def Auto_Pot_HideTip(self):
		self.txttooltip.ClearToolTip()
		self.txttooltip.Hide()			
		
	### Auto Pot Options ###	
	def Auto_Pot_Options(self):
		if self.Auto_Pot.IsShow():
			self.Auto_Pot.Hide()
		else:
			self.Auto_Pot.Show()			
			self.Auto_Pot.SetPosition(50, 120)		
		
	#################################### Restart ##########################################		
	
	### Restart Status ###
	def Restart_func(self):
		global Restart_Status
		if Restart_Status == 0:
			Restart_Status = 1
			self.Enable_Restart()
			chat.AppendChat(2, "Wstawanie po œmierci w³¹czone")
			self.Restart_img.LoadImage("ZAHON_MOD/Buttons/Function/Restart_On.tga")
		else:	
			Restart_Status = 0
			self.Disable_Restart()
			chat.AppendChat(2, "Wstawanie po œmierci wy³¹czone")
			self.Restart_img.LoadImage("ZAHON_MOD/Buttons/Function/Restart_Off.tga")
		
	### Restart Enable ###
	def Enable_Restart(self):	

		net.SendChatPacket("/restart_here")
	
		self.Delay_Restart = WaitingDialog()
		self.Delay_Restart.Open(int(1))
		self.Delay_Restart.SAFE_SetTimeOverEvent(self.Enable_Restart)
		
	def Disable_Restart(self):		
		self.Delay_Restart = WaitingDialog()
		self.Delay_Restart.Open(float(99999999999999999))
		self.Delay_Restart.SAFE_SetTimeOverEvent(self.Disable_Restart)
		
	################################### Use Item ##########################################		
	
	### Use Item Status ###
	def Use_Item_func(self):
		global Use_Item_Status
		if Use_Item_Status == 0:
			Use_Item_Status = 1
			self.Enable_Use_Item()
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Use Item Start")
			self.Use_Item_img.LoadImage("ZAHON_MOD/Buttons/Function/Use_Item_On.tga")		
		else:
			Use_Item_Status = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Use Item Stop")	
			self.Use_Item_img.LoadImage("ZAHON_MOD/Buttons/Function/Use_Item_Off.tga")	
			
	### Use Item Enable ###		
	def Enable_Use_Item(self):
		global Use_Item_Status, Use_Item_Delay_OK, Use_Item_ID
	
		if Use_Item_Status == 1:
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_1_Index = player.GetItemIndex(i)
				if Item_1_Index == int(Use_Item_ID[0]):
					net.SendItemUsePacket(i)
					
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_2_Index = player.GetItemIndex(i)
				if Item_2_Index == int(Use_Item_ID[1]):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_3_Index = player.GetItemIndex(i)
				if Item_3_Index == int(Use_Item_ID[2]):
					net.SendItemUsePacket(i)
					break		
					
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_4_Index = player.GetItemIndex(i)
				if Item_4_Index == int(Use_Item_ID[3]):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_5_Index = player.GetItemIndex(i)
				if Item_5_Index == int(Use_Item_ID[4]):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_6_Index = player.GetItemIndex(i)
				if Item_6_Index == int(Use_Item_ID[5]):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_7_Index = player.GetItemIndex(i)
				if Item_7_Index == int(Use_Item_ID[6]):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_8_Index = player.GetItemIndex(i)
				if Item_8_Index == int(Use_Item_ID[7]):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_9_Index = player.GetItemIndex(i)
				if Item_9_Index == int(Use_Item_ID[8]):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_10_Index = player.GetItemIndex(i)
				if Item_10_Index == int(Use_Item_ID[9]):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_11_Index = player.GetItemIndex(i)
				if Item_11_Index == int(Use_Item_ID[10]):
					net.SendItemUsePacket(i)
					break		

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_12_Index = player.GetItemIndex(i)
				if Item_12_Index == int(Use_Item_ID[11]):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_13_Index = player.GetItemIndex(i)
				if Item_13_Index == int(Use_Item_ID[12]):
					net.SendItemUsePacket(i)
					break
			
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_14_Index = player.GetItemIndex(i)
				if Item_14_Index == int(Use_Item_ID[13]):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_15_Index = player.GetItemIndex(i)
				if Item_15_Index == int(Use_Item_ID[14]):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_16_Index = player.GetItemIndex(i)
				if Item_16_Index == int(Use_Item_ID[15]):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_17_Index = player.GetItemIndex(i)
				if Item_17_Index == int(Use_Item_ID[16]):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_18_Index = player.GetItemIndex(i)
				if Item_18_Index == int(Use_Item_ID[17]):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_19_Index = player.GetItemIndex(i)
				if Item_19_Index == int(Use_Item_ID[18]):
					net.SendItemUsePacket(i)
					break		

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_20_Index = player.GetItemIndex(i)
				if Item_20_Index == int(Use_Item_ID[19]):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_21_Index = player.GetItemIndex(i)
				if Item_21_Index == int(Use_Item_ID[20]):
					net.SendItemUsePacket(i)
					break		

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_22_Index = player.GetItemIndex(i)
				if Item_22_Index == int(Use_Item_ID[21]):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_23_Index = player.GetItemIndex(i)
				if Item_23_Index == int(Use_Item_ID[22]):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_24_Index = player.GetItemIndex(i)
				if Item_24_Index == int(Use_Item_ID[23]):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_25_Index = player.GetItemIndex(i)
				if Item_25_Index == int(Use_Item_ID[24]):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_26_Index = player.GetItemIndex(i)
				if Item_26_Index == int(Use_Item_ID[25]):
					net.SendItemUsePacket(i)
					break		

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_27_Index = player.GetItemIndex(i)
				if Item_27_Index == int(Use_Item_ID[26]):
					net.SendItemUsePacket(i)
					break		

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_28_Index = player.GetItemIndex(i)
				if Item_28_Index == int(Use_Item_ID[27]):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_29_Index = player.GetItemIndex(i)
				if Item_29_Index == int(Use_Item_ID[28]):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_30_Index = player.GetItemIndex(i)
				if Item_30_Index == int(Use_Item_ID[29]):
					net.SendItemUsePacket(i)
					break									
		
		self.Delay_Use_Item = WaitingDialog()
		self.Delay_Use_Item.Open(int(Use_Item_Delay_OK))			
		self.Delay_Use_Item.SAFE_SetTimeOverEvent(self.Enable_Use_Item)			
		
	### Use Item Set ID ###
	
	### 1 ###
	def Set_Use_Item_Item_1(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
				
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[0] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_1_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_1_Icon.LoadImage(str(Use_Item_Item_1_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_1(self):
		global Use_Item_ID	
		Use_Item_ID[0] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_1_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		
	### 2 ###
	def Set_Use_Item_Item_2(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[1] = mouseModule.mouseController.GetAttachedItemIndex()				
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_2_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_2_Icon.LoadImage(str(Use_Item_Item_2_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_2(self):
		global Use_Item_ID	
		Use_Item_ID[1] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_2_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 3 ###	
	def Set_Use_Item_Item_3(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
							
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[2] = mouseModule.mouseController.GetAttachedItemIndex()				
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_3_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_3_Icon.LoadImage(str(Use_Item_Item_3_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_3(self):
		global Use_Item_ID	
		Use_Item_ID[2] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_3_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		

	### 4 ###	
	def Set_Use_Item_Item_4(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[3] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_4_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_4_Icon.LoadImage(str(Use_Item_Item_4_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_4(self):
		global Use_Item_ID	
		Use_Item_ID[3] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_4_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 5 ###	
	def Set_Use_Item_Item_5(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()				
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[4] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_5_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_5_Icon.LoadImage(str(Use_Item_Item_5_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_5(self):
		global Use_Item_ID	
		Use_Item_ID[4] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_5_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

	### 6 ###	
	def Set_Use_Item_Item_6(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
							
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[5] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_6_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_6_Icon.LoadImage(str(Use_Item_Item_6_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_6(self):
		global Use_Item_ID	
		Use_Item_ID[5] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_6_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 7 ###	
	def Set_Use_Item_Item_7(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[6] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_7_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_7_Icon.LoadImage(str(Use_Item_Item_7_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_7(self):
		global Use_Item_ID	
		Use_Item_ID[6] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_7_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		

	### 8 ###	
	def Set_Use_Item_Item_8(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
							
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[7] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_8_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_8_Icon.LoadImage(str(Use_Item_Item_8_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_8(self):
		global Use_Item_ID	
		Use_Item_ID[7] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_8_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 9 ###	
	def Set_Use_Item_Item_9(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[8] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_9_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_9_Icon.LoadImage(str(Use_Item_Item_9_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_9(self):
		global Use_Item_ID	
		Use_Item_ID[8] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_9_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 10 ###
	def Set_Use_Item_Item_10(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
						
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[9] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_10_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_10_Icon.LoadImage(str(Use_Item_Item_10_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_10(self):
		global Use_Item_ID	
		Use_Item_ID[9] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_10_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")				
		
	### 11 ###	
	def Set_Use_Item_Item_11(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[10] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_11_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_11_Icon.LoadImage(str(Use_Item_Item_11_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_11(self):
		global Use_Item_ID	
		Use_Item_ID[10] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_11_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 12 ###
	def Set_Use_Item_Item_12(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[11] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_12_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_12_Icon.LoadImage(str(Use_Item_Item_12_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_12(self):
		global Use_Item_ID	
		Use_Item_ID[11] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_12_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

	### 13 ###	
	def Set_Use_Item_Item_13(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
						
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[12] = mouseModule.mouseController.GetAttachedItemIndex()		
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_13_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_13_Icon.LoadImage(str(Use_Item_Item_13_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_13(self):
		global Use_Item_ID	
		Use_Item_ID[12] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_13_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

	### 14 ###	
	def Set_Use_Item_Item_14(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[13] = mouseModule.mouseController.GetAttachedItemIndex()	
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_14_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_14_Icon.LoadImage(str(Use_Item_Item_14_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_14(self):
		global Use_Item_ID	
		Use_Item_ID[13] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_14_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

	### 15 ###
	def Set_Use_Item_Item_15(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[14] = mouseModule.mouseController.GetAttachedItemIndex()
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_15_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_15_Icon.LoadImage(str(Use_Item_Item_15_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_15(self):
		global Use_Item_ID	
		Use_Item_ID[14] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_15_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

	### 16 ###
	def Set_Use_Item_Item_16(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[15] = mouseModule.mouseController.GetAttachedItemIndex()
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_16_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_16_Icon.LoadImage(str(Use_Item_Item_16_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_16(self):
		global Use_Item_ID	
		Use_Item_ID[15] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_16_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

	### 17 ###
	def Set_Use_Item_Item_17(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[16] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_17_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_17_Icon.LoadImage(str(Use_Item_Item_17_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_17(self):
		global Use_Item_ID	
		Use_Item_ID[16] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_17_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 18 ###
	def Set_Use_Item_Item_18(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[17] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_18_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_18_Icon.LoadImage(str(Use_Item_Item_18_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_18(self):
		global Use_Item_ID	
		Use_Item_ID[17] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_18_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 19 ###
	def Set_Use_Item_Item_19(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[18] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_19_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_19_Icon.LoadImage(str(Use_Item_Item_19_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_19(self):
		global Use_Item_ID	
		Use_Item_ID[18] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_19_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 20 ###
	def Set_Use_Item_Item_20(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[19] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_20_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_20_Icon.LoadImage(str(Use_Item_Item_20_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_20(self):
		global Use_Item_ID	
		Use_Item_ID[19] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_20_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

	### 21 ###
	def Set_Use_Item_Item_21(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[20] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_21_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_21_Icon.LoadImage(str(Use_Item_Item_21_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_21(self):
		global Use_Item_ID	
		Use_Item_ID[20] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_21_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

	### 22 ###
	def Set_Use_Item_Item_22(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
						
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[21] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_22_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_22_Icon.LoadImage(str(Use_Item_Item_22_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_22(self):
		global Use_Item_ID	
		Use_Item_ID[21] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_22_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 23 ###
	def Set_Use_Item_Item_23(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[22] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_23_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_23_Icon.LoadImage(str(Use_Item_Item_23_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_23(self):
		global Use_Item_ID	
		Use_Item_ID[22] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_23_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

	### 24 ###	
	def Set_Use_Item_Item_24(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[23] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_24_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_24_Icon.LoadImage(str(Use_Item_Item_24_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_24(self):
		global Use_Item_ID	
		Use_Item_ID[23] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_24_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 25 ###	
	def Set_Use_Item_Item_25(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[24] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_25_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_25_Icon.LoadImage(str(Use_Item_Item_25_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_25(self):
		global Use_Item_ID	
		Use_Item_ID[24] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_25_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 26 ###	
	def Set_Use_Item_Item_26(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[25] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_26_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_26_Icon.LoadImage(str(Use_Item_Item_26_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_26(self):
		global Use_Item_ID	
		Use_Item_ID[25] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_26_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

	### 27 ###
	def Set_Use_Item_Item_27(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[26] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_27_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_27_Icon.LoadImage(str(Use_Item_Item_27_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_27(self):
		global Use_Item_ID	
		Use_Item_ID[26] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_27_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

	### 28 ###	
	def Set_Use_Item_Item_28(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
							
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[27] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_28_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_28_Icon.LoadImage(str(Use_Item_Item_28_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_28(self):
		global Use_Item_ID	
		Use_Item_ID[27] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_28_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 29 ###
	def Set_Use_Item_Item_29(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[28] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_29_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_29_Icon.LoadImage(str(Use_Item_Item_29_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_29(self):
		global Use_Item_ID	
		Use_Item_ID[28] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_29_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

	### 30 ###
	def Set_Use_Item_Item_30(self):
		global Use_Item_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
						
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
			
				Use_Item_ID[29] = mouseModule.mouseController.GetAttachedItemIndex()			
			
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Use_Item_Item_30_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_30_Icon.LoadImage(str(Use_Item_Item_30_Icon))	
			else:		
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")	

	def Delete_Use_Item_Item_30(self):
		global Use_Item_ID	
		Use_Item_ID[29] = 0
		self.Use_Item_HideTip()
		self.Use_Item_Item_30_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")			
			
	### Use Item ToolTip ###	
	
	### 1 ###	
	def Use_Item_Item_1_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[0] > 0:
			
			item.SelectItem(int(Use_Item_ID[0]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[0])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[0]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[0]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[0] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 2 ###		
	def Use_Item_Item_2_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[1] > 0:
			
			item.SelectItem(int(Use_Item_ID[1]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[1])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[1]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[1]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[1] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 3 ###	
	def Use_Item_Item_3_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[2] > 0:
			
			item.SelectItem(int(Use_Item_ID[2]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[2])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[2]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[2]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[2] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 4 ###	
	def Use_Item_Item_4_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[3] > 0:
			
			item.SelectItem(int(Use_Item_ID[3]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[3])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[3]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[3]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[3] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()		

	### 5 ###		
	def Use_Item_Item_5_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[4] > 0:
			
			item.SelectItem(int(Use_Item_ID[4]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[4])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[4]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[4]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[4] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 6 ###	
	def Use_Item_Item_6_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[5] > 0:
			
			item.SelectItem(int(Use_Item_ID[5]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[5])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[5]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[5]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[5] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()						
									
	### 7 ###	
	def Use_Item_Item_7_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[6] > 0:
			
			item.SelectItem(int(Use_Item_ID[6]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[6])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[6]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[6]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[6] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 8 ###		
	def Use_Item_Item_8_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[7] > 0:
			
			item.SelectItem(int(Use_Item_ID[7]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[7])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[7]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[7]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[7] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()		

	### 9 ###	
	def Use_Item_Item_9_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[8] > 0:
			
			item.SelectItem(int(Use_Item_ID[8]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[8])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[8]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[8]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[8] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()		

	### 10 ###	
	def Use_Item_Item_10_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[9] > 0:
			
			item.SelectItem(int(Use_Item_ID[9]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[9])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[9]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[9]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[9] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 11 ###	
	def Use_Item_Item_11_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[10] > 0:
			
			item.SelectItem(int(Use_Item_ID[10]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[10])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[10]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[10]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[10] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()

	### 12 ###	
	def Use_Item_Item_12_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[11] > 0:
			
			item.SelectItem(int(Use_Item_ID[11]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[11])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[11]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[11]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[11] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()		

	### 13 ###	
	def Use_Item_Item_13_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[12] > 0:
			
			item.SelectItem(int(Use_Item_ID[12]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[12])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[12]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[12]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[12] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 14 ###		
	def Use_Item_Item_14_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[13] > 0:
			
			item.SelectItem(int(Use_Item_ID[13]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[13])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[13]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[13]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[13] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 15 ###	
	def Use_Item_Item_15_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[14] > 0:
			
			item.SelectItem(int(Use_Item_ID[14]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[14])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[14]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[14]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[14] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 16 ###	
	def Use_Item_Item_16_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[15] > 0:
			
			item.SelectItem(int(Use_Item_ID[15]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[15])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[15]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[15]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[15] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()							
									
	### 17 ###	
	def Use_Item_Item_17_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[16] > 0:
			
			item.SelectItem(int(Use_Item_ID[16]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[16])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[16]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[16]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[16] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 18 ###	
	def Use_Item_Item_18_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[17] > 0:
			
			item.SelectItem(int(Use_Item_ID[17]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[17])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[17]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[17]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[17] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()		

	### 19 ###	
	def Use_Item_Item_19_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[18] > 0:
			
			item.SelectItem(int(Use_Item_ID[18]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[18])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[18]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[18]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[18] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()

	### 20 ###	
	def Use_Item_Item_20_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[19] > 0:
			
			item.SelectItem(int(Use_Item_ID[19]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[19])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[19]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[19]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[19] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()				
									
	### 21 ###	
	def Use_Item_Item_21_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[20] > 0:
			
			item.SelectItem(int(Use_Item_ID[20]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[20])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[20]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[20]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[20] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 22 ###	
	def Use_Item_Item_22_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[21] > 0:
			
			item.SelectItem(int(Use_Item_ID[21]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[21])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[21]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[21]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[21] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 23 ###	
	def Use_Item_Item_23_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[22] > 0:
			
			item.SelectItem(int(Use_Item_ID[22]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[22])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[22]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[22]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[22] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 24 ###	
	def Use_Item_Item_24_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[23] > 0:
			
			item.SelectItem(int(Use_Item_ID[23]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[23])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[23]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[23]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[23] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()		

	### 25 ###	
	def Use_Item_Item_25_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[24] > 0:
			
			item.SelectItem(int(Use_Item_ID[24]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[24])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[24]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[24]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[24] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 26 ###	
	def Use_Item_Item_26_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[25] > 0:
			
			item.SelectItem(int(Use_Item_ID[25]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[25])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[25]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[25]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[25] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()		

	### 27 ###	
	def Use_Item_Item_27_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[26] > 0:
			
			item.SelectItem(int(Use_Item_ID[26]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[26])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[26]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[26]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[26] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()

	### 28 ###	
	def Use_Item_Item_28_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[27] > 0:
			
			item.SelectItem(int(Use_Item_ID[27]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[27])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[27]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[27]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[27] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 29 ###	
	def Use_Item_Item_29_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[28] > 0:
			
			item.SelectItem(int(Use_Item_ID[28]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[28])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[28]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[28]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[28] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	

	### 30 ###		
	def Use_Item_Item_30_ShowTip(self):
		global Use_Item_ID
		
		if Use_Item_ID[29] > 0:
			
			item.SelectItem(int(Use_Item_ID[29]))
			
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Use_Item_ID[29])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Use_Item_ID[29]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Use_Item_ID[29]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))			
			#self.txttooltip.AppendTextLine("Wartoœæ: " + str(player.GetItemMetinSocket(0, 1)), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()	
			
		if Use_Item_ID[29] == "0":
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()				
									
	def Use_Item_HideTip(self):
		self.txttooltip.ClearToolTip()
		self.txttooltip.Hide()						
		
	### Use Item Delete All Show ###
	def Use_Item_Delete_All_func(self):
		self.Use_Item_Delete_All.Show()

	### Use Item Delete All Yes ###
	def Use_Item_Delete_All_Yes_func(self):
		global Use_Item_ID
	
		for i in xrange(30):
			Use_Item_ID[i] = 0 
		
			self.Use_Item_Item_1_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_2_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_3_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_4_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_5_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_6_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_7_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_8_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_9_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_10_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_11_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_12_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_13_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_14_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_15_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_16_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_17_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_18_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_19_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_20_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_21_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_22_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_23_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_24_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_25_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_26_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_27_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_28_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_29_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_30_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

			self.Use_Item_Delete_All.Hide()	

	### Use Item Delete All No ###
	def Use_Item_Delete_All_No_func(self):
		self.Use_Item_Delete_All.Hide()		
		
	### Use Item Options ###		
	def Use_Item_Options(self):
		if self.Use_Item.IsShow():
			self.Use_Item.Hide()
		else:
			self.Use_Item.Show()			
			self.Use_Item.SetPosition(50, 120)	
			
	################################# GM Detector #########################################	
	
	### GM Detector Status ###
	def GM_Detector_func(self):
		global GM_Detector_Status
		if GM_Detector_Status == 0:
			GM_Detector_Status = 1
			self.Enable_GM_Detector()
			chat.AppendChat(2, "GM Detector W³¹czony")
			self.GM_Detector_Img.LoadImage("ZAHON_MOD/Buttons/Function/Gm_Detector_On.tga")
		else:
			GM_Detector_Status = 0
			self.Disable_GM_Detector()
			chat.AppendChat(2, "GM Detector Wy³¹czony")
			self.GM_Detector_Img.LoadImage("ZAHON_MOD/Buttons/Function/Gm_Detector_Off.tga")
	
	### GM Detector Enable ###	
	def Enable_GM_Detector(self):
		global GM_Detector_Delay
	
		self.GM_Detector_Scan_func()	
			
		self.Delay_GM_Detector = WaitingDialog()
		self.Delay_GM_Detector.Open(int(GM_Detector_Delay))
		self.Delay_GM_Detector.SAFE_SetTimeOverEvent(self.Enable_GM_Detector)
			
	def Disable_GM_Detector(self):
		
		self.Delay_GM_Detector = WaitingDialog()
		self.Delay_GM_Detector.Open(float(99999999999999999))
		self.Delay_GM_Detector.SAFE_SetTimeOverEvent(self.Disable_GM_Detector)		
	
	### GM Detector Scan ###
	def GM_Detector_Scan_func(self):
		global GM_Detector_Mode, GM_Detector_Info, GM_Detector_PopUp_Time
		
		GM_Detector_Mode = self.GM_Detector_Mode_Combobox.GetCurrentText()
		
		if os.path.exists("ZAHON_MOD/Config/GM_Detector/GM_Detector_List.txt"):
			GM_Detector_Load = open("ZAHON_MOD/Config/GM_Detector/GM_Detector_List.txt", "r")
			for GM_Detector_Line in GM_Detector_Load.readlines():
				GM_Detector_Line = GM_Detector_Line.strip()	
				
				for i in xrange(int(40000)):
					Name = chr.GetNameByVID(i)
					
					if Name[0] == "[" or Name == str(GM_Detector_Line):
						
						(X, Y, Z) = chr.GetPixelPosition(i)					
						X = X / 100
						Y = Y / 100
						X = str(round(X))
						Y = str(round(Y))
						X = X.replace('.0', '')
						Y = Y.replace('.0', '')
							
						Actually_Time = time.strftime("%H:%M:%S")
											
						if GM_Detector_Info[0] == str(Name):
							pass
						else:
							GM_Detector_Info[0] = str(Name)							
							GM_Detector_Info[1] = str(X)							
							GM_Detector_Info[2] = str(Y)							
			
							self.GM_Detector_Logs_List.AppendItem(Item("[" + str(Actually_Time) + "] " + str(Name) + " " + str(X) + " " + str(Y)))			

							self.GM_Detector_PopUp.Show()	
							self.GM_Detector_Warning_1_Text.SetText("Wykryto: " + str(Name))
							self.GM_Detector_Warning_2_Text.SetText("Godzina: " + str(Actually_Time))
							self.GM_Detector_Warning_3_Text.SetText("Koordynaty: " + str(X) + ", " + str(Y))			
			
							GM_Detector_PopUp_Time = int(int(app.GetTime()) + 15)
			
							if GM_Detector_Mode == "Powiadom":
								pass
									
							if GM_Detector_Mode == "Wy³¹cz_Grê":
								app.Exit()								
		
	### GM Detector Plus/Minus Delay ###
	def GM_Detector_Plus_Delay_func(self):
		global GM_Detector_Delay
		GM_Detector_Delay = int(int(GM_Detector_Delay) + 1)
		self.GM_Detector_Delay_Text.SetText("Skanowaæ co " + str(GM_Detector_Delay) + " s")	
	
	def GM_Detector_Minus_Delay_func(self):
		global GM_Detector_Delay
		if GM_Detector_Delay > 5:
			GM_Detector_Delay = int(int(GM_Detector_Delay) - 1)
			self.GM_Detector_Delay_Text.SetText("Skanowaæ co " + str(GM_Detector_Delay) + " s")	
		else:
			chat.AppendChat(2,"Nie mo¿esz zmniejszyæ czasu poni¿ej 5 s !")		
	
	### GM Detector Show List ###
	def GM_Detector_Show_List_func(self):
		if self.GM_Detector_List.IsShow():
			pass
		else:
			self.GM_Detector_List.Show()
	
  	### GM Detector List Get Nick By VID ###				
	def	GM_Detector_List_Get_Nick_By_VID_func(self):
		VID = player.GetTargetVID()
		if VID == 0:
			chat.AppendChat(2, "Najpierw zaznacz postaæ!")
		else:
			Nickname = chr.GetNameByVID(int(VID))
			self.GM_Detector_List_Nick_EditLine.SetText(str(Nickname))
		
	### GM Detector List Add Nick ### 				
	def GM_Detector_List_Add_Nick_func(self):
		Add_Item = self.GM_Detector_List_Nick_EditLine.GetText()
		if Add_Item == "":
			chat.AppendChat(2, "Najpierw podaj nick!")
		else:	
			self.GM_Detector_Nick_List.AppendItem(Item(str(Add_Item)))
			GM_Detector_List_Load = open("ZAHON_MOD/Config/GM_Detector/GM_Detector_List.txt", "r").read()
			open('ZAHON_MOD/Config/GM_Detector/GM_Detector_List.txt', 'w').write('%s\n%s' % (str(GM_Detector_List_Load), str(Add_Item)))
			self.GM_Detector_List_Refresh()		
		
	### GM Detector List Delete Nick ###
	def GM_Detector_List_Delete_Nick_func(self):
		if self.GM_Detector_Nick_List.IsEmpty():
			chat.AppendChat(2, "Lista jest pusta!")
		else:
			ItemIndex = self.GM_Detector_Nick_List.GetSelectedItem()
			Selected_Item_TxT = ItemIndex.GetText()
			
			GM_Detector_List_Load = open("ZAHON_MOD/Config/GM_Detector/GM_Detector_List.txt", "r").read()
			GM_Detector_List_Save = str(GM_Detector_List_Load).replace(str(Selected_Item_TxT), str(""))
			open('ZAHON_MOD/Config/GM_Detector/GM_Detector_List.txt', 'w+').write('%s' % (str(GM_Detector_List_Save)))	
			self.GM_Detector_List_Refresh()

	### GM Detector List Refresh ###		
	def GM_Detector_List_Refresh(self):
		self.GM_Detector_Nick_List.RemoveAllItems()
		if os.path.exists("ZAHON_MOD/Config/GM_Detector/GM_Detector_List.txt"):
			GM_Detector_List_Load = open("ZAHON_MOD/Config/GM_Detector/GM_Detector_List.txt", "r")
			for GM_Detector_List_Line in GM_Detector_List_Load.readlines():
				GM_Detector_List_Line = GM_Detector_List_Line.strip()
				self.GM_Detector_Nick_List.AppendItem(Item(str(GM_Detector_List_Line)))	
		else:
			open('ZAHON_MOD/Config/GM_Detector/GM_Detector_List.txt', 'w+').write('%s' % (""))	
	
	### GM Detector Show Logs ###
	def GM_Detector_Show_Logs_func(self):
		if self.GM_Detector_Logs.IsShow():
			pass
		else:
			self.GM_Detector_Logs.Show()
	
	### ToolTip ###
	def GM_Detector_List_ShowTip(self):
		self.txttooltip.ClearToolTip()
		self.txttooltip.AppendTextLine("GM Detector 2.2", grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 	
		self.txttooltip.AppendTextLine("Je¿eli GM ma nick bez prefiksu", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("(, [, {, dodaj jego nick do listy", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.Show()		
	
		self.GM_Detector_List_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_02.tga")
		
	def GM_Detector_HideTip(self):
		self.txttooltip.ClearToolTip()
		self.txttooltip.Hide()	
		self.GM_Detector_List_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_01.tga")	
	
	### GM Detector Options ###
	def GM_Detector_Options(self):
		if self.GM_Detector.IsShow():
			self.GM_Detector.Hide()
		else:
			self.GM_Detector.Show()			
			self.GM_Detector.SetPosition(50, 120)
		
	################################### Detector ##########################################			
		
	### Detector Status ###
	def Detector_func(self):
		global Detector_Status
		if Detector_Status == 0:
			Detector_Status = 1
			self.Enable_Detector()
			chat.AppendChat(2, "Detector W³¹czony")
			self.Detector_Img.LoadImage("ZAHON_MOD/Buttons/Function/Detector_On.tga")
		else:
			Detector_Status = 0
			self.Disable_Detector()
			chat.AppendChat(2, "Detector Wy³¹czony")
			self.Detector_Img.LoadImage("ZAHON_MOD/Buttons/Function/Detector_Off.tga")
			
	### Detector Enable ###	
	def Enable_Detector(self):
		global Detector_Delay
	
		self.Detector_Scan_func()	
			
		self.Delay_Detector = WaitingDialog()
		self.Delay_Detector.Open(int(Detector_Delay))
		self.Delay_Detector.SAFE_SetTimeOverEvent(self.Enable_Detector)
			
	def Disable_Detector(self):
		
		self.Delay_Detector = WaitingDialog()
		self.Delay_Detector.Open(float(99999999999999999))
		self.Delay_Detector.SAFE_SetTimeOverEvent(self.Disable_Detector)				
			
	### Detector Plus/Minus Delay ###
	def Detector_Plus_Delay_func(self):
		global Detector_Delay
		Detector_Delay = int(int(Detector_Delay) + 1)
		self.Detector_Delay_Text.SetText("Skanuj co " + str(Detector_Delay) + " s")	
	
	def Detector_Minus_Delay_func(self):
		global Detector_Delay
		if Detector_Delay > 5:
			Detector_Delay = int(int(Detector_Delay) - 1)
			self.Detector_Delay_Text.SetText("Skanuj co " + str(Detector_Delay) + " s")	
		else:
			chat.AppendChat(2,"Nie mo¿esz zmniejszyæ czasu poni¿ej 5 s !")	
	
	### Detector Scan ###
	def Detector_Scan_func(self):
		global Detector_Mode
		
		Detector_Mode = self.Detector_Mode_Combobox.GetCurrentText()
 		Detector_VID_Start_Scan = self.Detector_Options_VID_Start_Scan_EditLine.GetText()
 		Detector_VID_End_Scan = self.Detector_Options_VID_End_Scan_EditLine.GetText()		
		
		self.Detector_Change_Log_List.RemoveAllItems()
		
		if Detector_Mode == "Metin":
			if os.path.exists("ZAHON_MOD/Config/Detector/Metin_List.txt"):
				Metin_List_Load = open("ZAHON_MOD/Config/Detector/Metin_List.txt", "r")
				for Metin_List_Line in Metin_List_Load.readlines():
					Metin_List_Line = Metin_List_Line.strip()
	
					for i in xrange(int(Detector_VID_End_Scan)):	
						Name = chr.GetNameByVID(i)
							
						if Name == str(Metin_List_Line):
							(X, Y, Z) = chr.GetPixelPosition(i)							
							X = X / 100
							Y = Y / 100
							X = str(round(X))
							Y = str(round(Y))
							X = X.replace('.0', '')
							Y = Y.replace('.0', '')
																	
							Actually_Time = time.strftime("%H:%M:%S")
																								
							self.Detector_Change_Log_List.AppendItem(Item("[" + str(Actually_Time) + "] " + str(i) + " " + str(X) + " " + str(Y) + " " + str(Name)))
			
		if Detector_Mode == "Boss":
			if os.path.exists("ZAHON_MOD/Config/Detector/Boss_List.txt"):
				Boss_List_Load = open("ZAHON_MOD/Config/Detector/Boss_List.txt", "r")
				for Boss_List_Line in Boss_List_Load.readlines():
					Boss_List_Line = Boss_List_Line.strip()
	
					for i in xrange(int(Detector_VID_End_Scan)):
						Name = chr.GetNameByVID(i)
							
						if Name == str(Boss_List_Line):
							(X, Y, Z) = chr.GetPixelPosition(i)							
							X = X / 100
							Y = Y / 100
							X = str(round(X))
							Y = str(round(Y))
							X = X.replace('.0', '')
							Y = Y.replace('.0', '')
																	
							Actually_Time = time.strftime("%H:%M:%S")
																								
							self.Detector_Change_Log_List.AppendItem(Item("[" + str(Actually_Time) + "] " + str(i) + " " + str(X) + " " + str(Y) + " " + str(Name)))

		if Detector_Mode == "Ore":
			if os.path.exists("ZAHON_MOD/Config/Detector/Ore_List.txt"):
				Ore_List_Load = open("ZAHON_MOD/Config/Detector/Ore_List.txt", "r")
				for Ore_List_Line in Ore_List_Load.readlines():
					Ore_List_Line = Ore_List_Line.strip()
	
					for i in xrange(int(Detector_VID_End_Scan)):
						Name = chr.GetNameByVID(i)
							
						if Name == str(Ore_List_Line):
							(X, Y, Z) = chr.GetPixelPosition(i)							
							X = X / 100
							Y = Y / 100
							X = str(round(X))
							Y = str(round(Y))
							X = X.replace('.0', '')
							Y = Y.replace('.0', '')
																	
							Actually_Time = time.strftime("%H:%M:%S")
																								
							self.Detector_Change_Log_List.AppendItem(Item("[" + str(Actually_Time) + "] " + str(i) + " " + str(X) + " " + str(Y) + " " + str(Name)))
							
		if Detector_Mode == "Player":
			if os.path.exists("ZAHON_MOD/Config/Detector/Player_List.txt"):
				Player_List_Load = open("ZAHON_MOD/Config/Detector/Player_List.txt", "r")
				for Player_List_Line in Player_List_Load.readlines():
					Player_List_Line = Player_List_Line.strip()
	
					for i in xrange(int(Detector_VID_End_Scan)):
						Name = chr.GetNameByVID(i)
							
						if Name == str(Player_List_Line):
							(X, Y, Z) = chr.GetPixelPosition(i)							
							X = X / 100
							Y = Y / 100
							X = str(round(X))
							Y = str(round(Y))
							X = X.replace('.0', '')
							Y = Y.replace('.0', '')
																	
							Actually_Time = time.strftime("%H:%M:%S")
																								
							self.Detector_Change_Log_List.AppendItem(Item("[" + str(Actually_Time) + "] " + str(i) + " " + str(X) + " " + str(Y) + " " + str(Name)))
	
		if Detector_Mode == "Wszystko":
			if os.path.exists("ZAHON_MOD/Config/Detector/All_List.txt"):
				All_List_Load = open("ZAHON_MOD/Config/Detector/All_List.txt", "r")
				for All_List_Line in All_List_Load.readlines():
					All_List_Line = All_List_Line.strip()
	
					for i in xrange(int(Detector_VID_End_Scan)):
					#for i in range(int(Detector_VID_Start_Scan), int(Detector_VID_End_Scan)):	
						Name = chr.GetNameByVID(i)
							
						if Name == str(All_List_Line):
							(X, Y, Z) = chr.GetPixelPosition(i)							
							X = X / 100
							Y = Y / 100
							X = str(round(X))
							Y = str(round(Y))
							X = X.replace('.0', '')
							Y = Y.replace('.0', '')
																	
							Actually_Time = time.strftime("%H:%M:%S")
																								
							self.Detector_Change_Log_List.AppendItem(Item("[" + str(Actually_Time) + "] " + str(i) + " " + str(X) + " " + str(Y) + " " + str(Name)))
			
	### Detector Walk To Target ###	
	def Detector_Walk_func(self):
		if self.Detector_Change_Log_List.IsEmpty():
			chat.AppendChat(2, "Lista jest pusta!")
		else:
			ItemIndex = self.Detector_Change_Log_List.GetSelectedItem()
			Selected_Item_TxT = ItemIndex.GetText()
			Selected_Item_TxT_Split = Selected_Item_TxT.split()		
		
			My_VID = player.GetMainCharacterIndex()	
			(My_X, My_Y, My_Z) = chr.GetPixelPosition(My_VID)	
			(Search_X, Search_Y, Search_Z) = chr.GetPixelPosition(int(Selected_Item_TxT_Split[1]))	
			chr.MoveToDestPosition(int(My_VID), int(Search_X), int(Search_Y))	
		
	### Detector Teleport To Target ###	
	def Detector_Teleport_func(self):
		if self.Detector_Change_Log_List.IsEmpty():
			chat.AppendChat(2, "Lista jest pusta!")
		else:
			ItemIndex = self.Detector_Change_Log_List.GetSelectedItem()
			Selected_Item_TxT = ItemIndex.GetText()
			Selected_Item_TxT_Split = Selected_Item_TxT.split()
			
		My_VID = player.GetMainCharacterIndex()	
		(My_X, My_Y, My_Z) = chr.GetPixelPosition(My_VID)			
		My_X = int(My_X / 100)
		My_Y = int(My_Y / 100)	
		
		(Search_X, Search_Y, Search_Z) = chr.GetPixelPosition(int(Selected_Item_TxT_Split[1]))			
		Search_X = int(Search_X / 100)
		Search_Y = int(Search_Y / 100)

		# Zabezpieczenie przed teleportowaniem siê w metin
		Search_X = int(Search_X + int(app.GetRandom(1,3)))
		Search_Y = int(Search_Y + int(app.GetRandom(1,3)))

		# Ustawianie pozycji X
		if My_X > Search_X:
			X_Distance = int(My_X - Search_X)
						
			if X_Distance >= 20:
				X_Distance = int(X_Distance / 20)
				X_Distance_Rest = int(X_Distance % 20)
						
				(x, y, z) = player.GetMainCharacterPosition()
				chr.SetPixelPosition(int(x) - int(X_Distance_Rest * 100), int(y), int(z))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
						
				for i in xrange(int(X_Distance)):
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x) - int(2000), int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)										
			else:		
				for i in xrange(int(X_Distance)):
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x) - int(100), int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)			
		else:
			X_Distance = int(Search_X - My_X)
						
			if X_Distance >= 20:
				X_Distance = int(X_Distance / 20)
				X_Distance_Rest = int(X_Distance % 20)
						
				(x, y, z) = player.GetMainCharacterPosition()
				chr.SetPixelPosition(int(x) + int(X_Distance_Rest * 100), int(y), int(z))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
						
				for i in xrange(int(X_Distance)):
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x) + int(2000), int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
			else:									
				for i in xrange(int(X_Distance)):	
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x) + int(100), int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
						
		# Ustawianie pozycji Y
		if My_Y > Search_Y:		
			Y_Distance = int(My_Y - Search_Y)
							
			if Y_Distance >= 20:
				Y_Distance = int(Y_Distance / 20)
				Y_Distance_Rest = int(Y_Distance % 20)
					
				(x, y, z) = player.GetMainCharacterPosition()
				chr.SetPixelPosition(int(x), int(y) - int(Y_Distance_Rest * 100), int(z))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
						
				for i in xrange(int(Y_Distance)):
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x), int(y) - int(2000), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
			else:
				for i in xrange(int(Y_Distance)):	
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x), int(y) - int(100), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)			
		else:
			Y_Distance = int(Search_Y - My_Y)
					
			if Y_Distance >= 20:
				Y_Distance = int(Y_Distance / 20)
				Y_Distance_Rest = int(Y_Distance % 20)
					
				(x, y, z) = player.GetMainCharacterPosition()
				chr.SetPixelPosition(int(x), int(y) + int(Y_Distance_Rest * 100), int(z))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
						
				for i in xrange(int(Y_Distance)):
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x), int(y) + int(2000), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)					
			else:
				for i in xrange(int(Y_Distance)):	
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x), int(y) + int(100), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)				
		
	### Detector List Show ###
	def Detector_Show_List_func(self):
		if self.Detector_List.IsShow():
			pass
		else:
			self.Detector_List.Show()		
		
	### Teleport List Type ###
	def Detector_List_Metin_List_func(self):
		global Detector_List_Type
		Detector_List_Type = 1
		self.Detector_List.SetTitleName('Metin List')
		self.Detector_List_Refresh()
		
	def Detector_List_Boss_List_func(self):
		global Detector_List_Type
		Detector_List_Type = 2
		self.Detector_List.SetTitleName('Boss List')
		self.Detector_List_Refresh()
		
	def Detector_List_Ore_List_func(self):
		global Detector_List_Type
		Detector_List_Type = 3
		self.Detector_List.SetTitleName('Ore List')
		self.Detector_List_Refresh()
		
	def Detector_List_Player_List_func(self):
		global Detector_List_Type
		Detector_List_Type = 4
		self.Detector_List.SetTitleName('Player List')
		self.Detector_List_Refresh()		
		
	### Detector List Get Nick By VID ####			
	def	Detector_List_Get_Nick_By_VID_func(self):
		global Detector_List_Type
		VID = player.GetTargetVID()
		if VID == 0:
			if Detector_List_Type == 1:
				chat.AppendChat(2, "Najpierw zaznacz Metina!")
			if Detector_List_Type == 2:
				chat.AppendChat(2, "Najpierw zaznacz Bossa!")	
			if Detector_List_Type == 3:
				chat.AppendChat(2, "Najpierw zaznacz ¯y³ê!")
			if Detector_List_Type == 4:
				chat.AppendChat(2, "Najpierw zaznacz Gracza!")					
		else:
			Nickname = chr.GetNameByVID(int(VID))
			self.Detector_List_Nick_EditLine.SetText(str(Nickname))
			
	### Detector List Add Nick ####	
	def Detector_List_Add_Nick_func(self):
		global Detector_List_Type
		Add_Item = self.Detector_List_Nick_EditLine.GetText()
		if Add_Item == "":
			chat.AppendChat(2, "Najpierw podaj nazwê!")
		else:	
			if Detector_List_Type == 0:	
				chat.AppendChat(2, "Najpierw wybierz listê!")	
			
			if Detector_List_Type == 1:		
				self.Detector_Name_List.AppendItem(Item(str(Add_Item)))
				Metin_List_Load = open("ZAHON_MOD/Config/Detector/Metin_List.txt", "r").read()
				open('ZAHON_MOD/Config/Detector/Metin_List.txt', 'w').write('%s\n%s' % (str(Metin_List_Load), str(Add_Item)))
				self.Detector_List_Refresh()		

			if Detector_List_Type == 2:		
				self.Detector_Name_List.AppendItem(Item(str(Add_Item)))
				Boss_List_Load = open("ZAHON_MOD/Config/Detector/Boss_List.txt", "r").read()
				open('ZAHON_MOD/Config/Detector/Boss_List.txt', 'w').write('%s\n%s' % (str(Boss_List_Load), str(Add_Item)))
				self.Detector_List_Refresh()

			if Detector_List_Type == 3:		
				self.Detector_Name_List.AppendItem(Item(str(Add_Item)))
				Ore_List_Load = open("ZAHON_MOD/Config/Detector/Ore_List.txt", "r").read()
				open('ZAHON_MOD/Config/Detector/Ore_List.txt', 'w').write('%s\n%s' % (str(Ore_List_Load), str(Add_Item)))
				self.Detector_List_Refresh()				

			if Detector_List_Type == 4:		
				self.Detector_Name_List.AppendItem(Item(str(Add_Item)))
				Player_List_Load = open("ZAHON_MOD/Config/Detector/Player_List.txt", "r").read()
				open('ZAHON_MOD/Config/Detector/Player_List.txt', 'w').write('%s\n%s' % (str(Player_List_Load), str(Add_Item)))
				self.Detector_List_Refresh()					
	
	### Detector List Delete Nick ####
	def Detector_List_Delete_Nick_func(self):
		global Detector_List_Type
		if self.Detector_Name_List.IsEmpty():
			chat.AppendChat(2, "Lista jest pusta!")
		else:
			ItemIndex = self.Detector_Name_List.GetSelectedItem()
			Selected_Item_TxT = ItemIndex.GetText()
			
			if Detector_List_Type == 1:			
				Metin_List_Load = open("ZAHON_MOD/Config/Detector/Metin_List.txt", "r").read()
				Metin_List_Save = str(Metin_List_Load).replace(str(Selected_Item_TxT), str(""))
				open('ZAHON_MOD/Config/Detector/Metin_List.txt', 'w+').write('%s' % (str(Metin_List_Save)))	
				self.Detector_List_Refresh()
				
			if Detector_List_Type == 2:			
				Boss_List_Load = open("ZAHON_MOD/Config/Detector/Boss_List.txt", "r").read()
				Boss_List_Save = str(Boss_List_Load).replace(str(Selected_Item_TxT), str(""))
				open('ZAHON_MOD/Config/Detector/Boss_List.txt', 'w+').write('%s' % (str(Boss_List_Save)))	
				self.Detector_List_Refresh()				

			if Detector_List_Type == 3:			
				Ore_List_Load = open("ZAHON_MOD/Config/Detector/Ore_List.txt", "r").read()
				Ore_List_Save = str(Ore_List_Load).replace(str(Selected_Item_TxT), str(""))
				open('ZAHON_MOD/Config/Detector/Ore_List.txt', 'w+').write('%s' % (str(Ore_List_Save)))	
				self.Detector_List_Refresh()	

			if Detector_List_Type == 4:			
				Player_List_Load = open("ZAHON_MOD/Config/Detector/Player_List.txt", "r").read()
				Player_List_Save = str(Player_List_Load).replace(str(Selected_Item_TxT), str(""))
				open('ZAHON_MOD/Config/Detector/Player_List.txt', 'w+').write('%s' % (str(Player_List_Save)))	
				self.Detector_List_Refresh()					
				
	#### Detector List Refresh ####		
	def Detector_List_Refresh(self):
		global Detector_List_Type
		
		self.Detector_Name_List.RemoveAllItems()
		self.Detector_List_Create_All_List()
		
		if Detector_List_Type == 1:
			if os.path.exists("ZAHON_MOD/Config/Detector/Metin_List.txt"):
				Metin_List_Load = open("ZAHON_MOD/Config/Detector/Metin_List.txt", "r")
				for Metin_List_Line in Metin_List_Load.readlines():
					Metin_List_Line = Metin_List_Line.strip()	
					self.Detector_Name_List.AppendItem(Item(str(Metin_List_Line)))

		if Detector_List_Type == 2: 
			if os.path.exists("ZAHON_MOD/Config/Detector/Boss_List.txt"):
				Boss_List_Load = open("ZAHON_MOD/Config/Detector/Boss_List.txt", "r")
				for Boss_List_Line in Boss_List_Load.readlines():
					Boss_List_Line = Boss_List_Line.strip()				
					self.Detector_Name_List.AppendItem(Item(str(Boss_List_Line)))

		if Detector_List_Type == 3: 
			if os.path.exists("ZAHON_MOD/Config/Detector/Ore_List.txt"):
				Ore_List_Load = open("ZAHON_MOD/Config/Detector/Ore_List.txt", "r")
				for Ore_List_Line in Ore_List_Load.readlines():
					Ore_List_Line = Ore_List_Line.strip()				
					self.Detector_Name_List.AppendItem(Item(str(Ore_List_Line)))					
		
		if Detector_List_Type == 4: 
			if os.path.exists("ZAHON_MOD/Config/Detector/Player_List.txt"):
				Player_List_Load = open("ZAHON_MOD/Config/Detector/Player_List.txt", "r")
				for Player_List_Line in Player_List_Load.readlines():
					Player_List_Line = Player_List_Line.strip()				
					self.Detector_Name_List.AppendItem(Item(str(Player_List_Line)))		
			
	### Detector List Create All List ###
	def Detector_List_Create_All_List(self):
		Metin_List_Load = open("ZAHON_MOD/Config/Detector/Metin_List.txt", "r").read()		
		Boss_List_Load = open("ZAHON_MOD/Config/Detector/Boss_List.txt", "r").read()			
		Ore_List_Load = open("ZAHON_MOD/Config/Detector/Ore_List.txt", "r").read()
		Player_List_Load = open("ZAHON_MOD/Config/Detector/Player_List.txt", "r").read()
				
		open('ZAHON_MOD/Config/Detector/All_List.txt', 'w+').write('%s\n%s\n%s\n%s' % (str(Metin_List_Load), str(Boss_List_Load), str(Ore_List_Load), str(Player_List_Load)))			
		
	### Detector Show Options ###	
	def Detector_Show_Options_func(self):
		if self.Detector_Options.IsShow():
			pass
		else:
			self.Detector_Options.Show()
		
	### Detector Options Set More Info ###
	def Detector_Options_Set_More_Info_func(self):
		if self.Detector_Change_Log_List.IsEmpty():
			chat.AppendChat(2, "Lista jest pusta!")
		else:
			ItemIndex = self.Detector_Change_Log_List.GetSelectedItem()
			
			if ItemIndex:
				pass
			else:
				chat.AppendChat(2, "Najpierw zaznacz pozycjê z listy!")					
			
			Selected_Item_TxT = ItemIndex.GetText()
			Selected_Item_TxT_Split = Selected_Item_TxT.split()		
		
			VID = int(Selected_Item_TxT_Split[1])
	
			self.Detector_Options_Level_Text.SetText("Level: " + str(nonplayer.GetLevelByVID(int(VID))))
			self.Detector_Options_Distance_Text.SetText("Distance: " + str(player.GetCharacterDistance(int(VID))))
			self.Detector_Options_Instance_Type_Text.SetText("Instance Type: " + str(chr.GetInstanceType(int(VID))))
		
	### Detector Show ToolTip ###	
	def Detector_ShowTip(self):
	
		self.txttooltip.ClearToolTip()
		self.txttooltip.AppendTextLine("Detector 1.1", grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
		self.txttooltip.AppendTextLine("Code by ZAHON 2016", grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)) 		
		self.txttooltip.AppendTextLine("Bot skanuje obszar w postaci ko³a", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("o promieniu oko³o 80 jednostek,", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("pozwala wykryæ metiny, bossy,", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("¿y³y, graczy a nastêpnie siê do", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("nich teleportowaæ lub pobiec", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.Show()		
	
		self.Gm_Detector_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_02.tga")
		
	### Detector Hide ToolTip ###		
	def Detector_HideTip(self):
		self.txttooltip.ClearToolTip()
		self.txttooltip.Hide()	
		self.Gm_Detector_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_01.tga")
						
	### Detector Options ###		
	def Detector_Options_func(self):
		if self.Detector_Bar.IsShow():
			self.Detector_Bar.Hide()
		else:
			self.Detector_Bar.Show()			
			self.Detector_Bar.SetPosition(50, 120)	
			
	################################### Teleport #########################################		
	
	### Teleport Show ###
	def Teleport_func(self):
		self.Teleport_Button.LoadImage("ZAHON_MOD/Buttons/Function/Teleport_Button_03.tga")
		if self.Teleport_Bar.IsShow():
			pass
		else:
			self.Teleport_Bar.Show()
			self.Teleport_Info()			
			
	### Teleport Coordinates Add Coords List ###	
	def Teleport_Coordinates_Add_Coords_func(self):
		global My_Coords_Info 
		
		My_VID = player.GetMainCharacterIndex()	
		(My_X, My_Y, My_Z) = chr.GetPixelPosition(My_VID) 

		My_X = int(My_X / 100) 
		My_Y = int(My_Y / 100)
		
		Current_Map_Name = background.GetCurrentMapName()		
		Position_Name = self.Teleport_Coordinates_Position_Editline.GetText()
		
		if My_Coords_Info[0] == str(Current_Map_Name) and My_Coords_Info[1] == str(My_X) and My_Coords_Info[2] == str(My_Y):
			chat.AppendChat(2, "Ta pozycja zosta³a ju¿ zapisana!")	
		else: 
			self.Teleport_Coordinates_List.AppendItem(Item(str(My_X) + " " + str(My_Y) + " " + str(Position_Name)))
			
			Teleport_Coordinates_List_Load = open("ZAHON_MOD/Config/Teleport/" + str(Current_Map_Name) + "_Teleport_Coordinates.txt", "r").read()
			open("ZAHON_MOD/Config/Teleport/" + str(Current_Map_Name) + "_Teleport_Coordinates.txt", 'w').write('%s\n%s%s%s%s%s' % (str(Teleport_Coordinates_List_Load), str(My_X), " ", str(My_Y), " ", str(Position_Name)))
			self.Teleport_Coordinates_List_Refresh()			

			My_Coords_Info[0] = str(Current_Map_Name)
			My_Coords_Info[1] = str(My_X)
			My_Coords_Info[2] = str(My_Y)			
			
	def Teleport_Coordinates_Delete_Coords_func(self):
		
		Current_Map_Name = background.GetCurrentMapName()			
		if self.Teleport_Coordinates_List.IsEmpty():
			chat.AppendChat(2, "Lista jest pusta!")
		else:
			ItemIndex = self.Teleport_Coordinates_List.GetSelectedItem()
			
			if ItemIndex:
				pass
			else:
				chat.AppendChat(2, "Najpierw zaznacz pozycjê z listy!")			
			
			Selected_Item_TxT = ItemIndex.GetText()
		
			Teleport_Coordinates_List_Load = open("ZAHON_MOD/Config/Teleport/" + str(Current_Map_Name) + "_Teleport_Coordinates.txt", "r").read()
			Teleport_Coordinates_List_Save = str(Teleport_Coordinates_List_Load).replace(str(Selected_Item_TxT), str(""))
			open("ZAHON_MOD/Config/Teleport/" + str(Current_Map_Name) + "_Teleport_Coordinates.txt", 'w+').write('%s' % (str(Teleport_Coordinates_List_Save)))	
			self.Teleport_Coordinates_List_Refresh()
		
	def Teleport_Coordinates_Teleport_func(self):
		
		if self.Teleport_Coordinates_List.IsEmpty():
			chat.AppendChat(2, "Lista jest pusta!")
		else:
			ItemIndex = self.Teleport_Coordinates_List.GetSelectedItem()
			
			if ItemIndex:
				pass
			else:
				chat.AppendChat(2, "Najpierw zaznacz pozycjê z listy!")
					
			Selected_Item_TxT = ItemIndex.GetText()
			Selected_Item_TxT_Split = Selected_Item_TxT.split()	
		
			Position_X = int(Selected_Item_TxT_Split[0])
			Position_Y = int(Selected_Item_TxT_Split[1])
		
			My_VID = player.GetMainCharacterIndex()	
			(My_X, My_Y, My_Z) = chr.GetPixelPosition(My_VID)			
			My_X = int(My_X / 100)
			My_Y = int(My_Y / 100)		
										
			# Ustawianie pozycji X
			if My_X > Position_X:
				X_Distance = int(My_X - Position_X)
						
				if X_Distance >= 20:
					X_Distance = int(X_Distance / 20)
					X_Distance_Rest = int(X_Distance % 20)
						
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x) - int(X_Distance_Rest * 100), int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
						
					for i in xrange(int(X_Distance)):
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x) - int(2000), int(y), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)										
				else:		
					for i in xrange(int(X_Distance)):
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x) - int(100), int(y), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)			
			else:
				X_Distance = int(Position_X - My_X)
						
				if X_Distance >= 20:
					X_Distance = int(X_Distance / 20)
					X_Distance_Rest = int(X_Distance % 20)
						
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x) + int(X_Distance_Rest * 100), int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
						
					for i in xrange(int(X_Distance)):
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x) + int(2000), int(y), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
				else:									
					for i in xrange(int(X_Distance)):	
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x) + int(100), int(y), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
						
			# Ustawianie pozycji Y
			if My_Y > Position_Y:		
				Y_Distance = int(My_Y - Position_Y)
							
				if Y_Distance >= 20:
					Y_Distance = int(Y_Distance / 20)
					Y_Distance_Rest = int(Y_Distance % 20)
					
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x), int(y) - int(Y_Distance_Rest * 100), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
						
					for i in xrange(int(Y_Distance)):
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x), int(y) - int(2000), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				else:
					for i in xrange(int(Y_Distance)):	
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x), int(y) - int(100), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)			
			else:
				Y_Distance = int(Position_Y - My_Y)
					
				if Y_Distance >= 20:
					Y_Distance = int(Y_Distance / 20)
					Y_Distance_Rest = int(Y_Distance % 20)
					
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x), int(y) + int(Y_Distance_Rest * 100), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
						
					for i in xrange(int(Y_Distance)):
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x), int(y) + int(2000), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)					
				else:
					for i in xrange(int(Y_Distance)):	
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x), int(y) + int(100), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							

	
	### Teleport Coordinates List Refresh ###
	def Teleport_Coordinates_List_Refresh(self):
		self.Teleport_Coordinates_List.RemoveAllItems()
		
		Current_Map_Name = background.GetCurrentMapName()	
		if os.path.exists("ZAHON_MOD/Config/Teleport/" + str(Current_Map_Name) + "_Teleport_Coordinates.txt"):
			self.Teleport_Coordinates_List.RemoveAllItems()
			Teleport_Coordinates_List_Load = open("ZAHON_MOD/Config/Teleport/" + str(Current_Map_Name) + "_Teleport_Coordinates.txt", "r")
			for Teleport_Coordinates_Line in Teleport_Coordinates_List_Load.readlines():
				Teleport_Coordinates_Line = Teleport_Coordinates_Line.strip()	
				self.Teleport_Coordinates_List.AppendItem(Item(str(Teleport_Coordinates_Line)))	
		else:
			open("ZAHON_MOD/Config/Teleport/" + str(Current_Map_Name) + "_Teleport_Coordinates.txt", 'w').write('%s' % (""))			
		
	###########################################	
		
	### Teleport Panel Show/Hide ###
	def Teleport_Panel_func(self):
		if self.Teleport_Panel.IsShow():
			self.Teleport_Panel.Hide()
			
			self.Teleport_Panel_Button.SetPosition(197, 106)
			self.Teleport_Panel_Button.SetUpVisual("ZAHON_MOD/Buttons/Gui/Right_Gui_Show_Button_01.tga")
			self.Teleport_Panel_Button.SetOverVisual("ZAHON_MOD/Buttons/Gui/Right_Gui_Show_Button_02.tga")
			self.Teleport_Panel_Button.SetDownVisual("ZAHON_MOD/Buttons/Gui/Right_Gui_Show_Button_03.tga")			
		else:
			self.Teleport_Panel.Show()	
			
			self.Teleport_Panel_Button.SetPosition(332, 106)
			self.Teleport_Panel_Button.SetUpVisual("ZAHON_MOD/Buttons/Gui/Right_Gui_Hide_Button_01.tga")
			self.Teleport_Panel_Button.SetOverVisual("ZAHON_MOD/Buttons/Gui/Right_Gui_Hide_Button_02.tga")
			self.Teleport_Panel_Button.SetDownVisual("ZAHON_MOD/Buttons/Gui/Right_Gui_Hide_Button_03.tga")
	
	### Teleport Panel Tele Func ###
	def Teleport_Up_func(self):
		Distance = int(int(self.Teleport_EditLine_Distance.GetText()) / 10)	
		for i in xrange(int(Distance)):
	
			(x, y, z) = player.GetMainCharacterPosition()
			chr.SetPixelPosition(int(x), int(y) - int(1000), int(z))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
		
	def Teleport_Down_func(self):
		Distance = int(int(self.Teleport_EditLine_Distance.GetText()) / 10)	
		for i in xrange(int(Distance)):	
	
			(x, y, z) = player.GetMainCharacterPosition()
			chr.SetPixelPosition(int(x), int(y) + int(1000), int(z))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

	def Teleport_Right_func(self):
		Distance = int(int(self.Teleport_EditLine_Distance.GetText()) / 10)	
		for i in xrange(int(Distance)):	
	
			(x, y, z) = player.GetMainCharacterPosition()
			chr.SetPixelPosition(int(x) + int(1000), int(y), int(z))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

	def Teleport_Left_func(self):
		Distance = int(int(self.Teleport_EditLine_Distance.GetText()) / 10)	
		for i in xrange(int(Distance)):	
	
			(x, y, z) = player.GetMainCharacterPosition()
			chr.SetPixelPosition(int(x) - int(1000), int(y), int(z))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)	
		
	### Teleport Panel Plus/Minus Delay ###	
	def Teleport_Plus_func(self):
		Get_Distance = self.Teleport_EditLine_Distance.GetText()
		
		if Get_Distance == "100":	
			chat.AppendChat(2,"Nie mo¿esz zwiêkszyæ dystansu powy¿ej 100!")			
		else:
			Set_Distance = int(int(Get_Distance) + 10)	
			self.Teleport_EditLine_Distance.SetText(str(Set_Distance))		
					
	def Teleport_Minus_func(self):
		Get_Distance = self.Teleport_EditLine_Distance.GetText()
		
		if Get_Distance > "10":
			Set_Distance = int(int(Get_Distance) - 10)	
			self.Teleport_EditLine_Distance.SetText(str(Set_Distance))
		else:
			chat.AppendChat(2,"Nie mo¿esz zmniejszyæ dystansu poni¿ej 10!")				
		
	def Teleport_Panel_Teleport_func(self):
		
		Position_X = int(self.Teleport_X_Editline.GetText())
		Position_Y = int(self.Teleport_Y_Editline.GetText())
		
		My_VID = player.GetMainCharacterIndex()	
		(My_X, My_Y, My_Z) = chr.GetPixelPosition(My_VID)			
		My_X = int(My_X / 100)
		My_Y = int(My_Y / 100)	
		
		if Position_X == "" and Position_Y == "":
			chat.AppendChat(2, "Najpierw podaj pozycjê")

		if Position_X == "" and Position_Y != "":
			chat.AppendChat(2, "Najpierw podaj wspó³rzêdn¹ X")				
			
		if Position_X != "" and Position_Y == "":
			chat.AppendChat(2, "Najpierw podaj wspó³rzêdn¹ Y")	

		if Position_X != "" and Position_Y != "":
			# Ustawianie pozycji X
			if My_X > Position_X:
				X_Distance = int(My_X - Position_X)
						
				if X_Distance >= 20:
					X_Distance = int(X_Distance / 20)
					X_Distance_Rest = int(X_Distance % 20)
						
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x) - int(X_Distance_Rest * 100), int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
						
					for i in xrange(int(X_Distance)):
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x) - int(2000), int(y), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)										
				else:		
					for i in xrange(int(X_Distance)):
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x) - int(100), int(y), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)			
			else:
				X_Distance = int(Position_X - My_X)
						
				if X_Distance >= 20:
					X_Distance = int(X_Distance / 20)
					X_Distance_Rest = int(X_Distance % 20)
						
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x) + int(X_Distance_Rest * 100), int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
						
					for i in xrange(int(X_Distance)):
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x) + int(2000), int(y), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
				else:									
					for i in xrange(int(X_Distance)):	
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x) + int(100), int(y), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
						
			# Ustawianie pozycji Y
			if My_Y > Position_Y:		
				Y_Distance = int(My_Y - Position_Y)
							
				if Y_Distance >= 20:
					Y_Distance = int(Y_Distance / 20)
					Y_Distance_Rest = int(Y_Distance % 20)
					
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x), int(y) - int(Y_Distance_Rest * 100), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
						
					for i in xrange(int(Y_Distance)):
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x), int(y) - int(2000), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				else:
					for i in xrange(int(Y_Distance)):	
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x), int(y) - int(100), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)			
			else:
				Y_Distance = int(Position_Y - My_Y)
					
				if Y_Distance >= 20:
					Y_Distance = int(Y_Distance / 20)
					Y_Distance_Rest = int(Y_Distance % 20)
					
					(x, y, z) = player.GetMainCharacterPosition()
					chr.SetPixelPosition(int(x), int(y) + int(Y_Distance_Rest * 100), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)							
						
					for i in xrange(int(Y_Distance)):
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x), int(y) + int(2000), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)					
				else:
					for i in xrange(int(Y_Distance)):	
						(x, y, z) = player.GetMainCharacterPosition()
						chr.SetPixelPosition(int(x), int(y) + int(100), int(z))
						player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
						player.SetSingleDIKKeyState(app.DIK_UP, FALSE)				
			
	### Teleport Mouse In ###		
	def Teleport_In(self):
		self.Teleport_Button.LoadImage("ZAHON_MOD/Buttons/Function/Teleport_Button_02.tga")
		
	### Teleport Mouse Over ###			
	def Teleport_Over(self):
		self.Teleport_Button.LoadImage("ZAHON_MOD/Buttons/Function/Teleport_Button_01.tga")			
			
	################################### Other #########################################				
		
	### Other Show ###
	def Other_func(self):
		self.Other_Button.LoadImage("ZAHON_MOD/Buttons/Function/Other_Button_03.tga")
		if self.Other_Gui.IsShow():
			pass
		else:
			self.Other_Gui.Show()		
			
	### Other Mouse In ###		
	def Other_In(self):
		self.Other_Button.LoadImage("ZAHON_MOD/Buttons/Function/Other_Button_02.tga")
		
	### Other Mouse Over ###			
	def Other_Over(self):
		self.Other_Button.LoadImage("ZAHON_MOD/Buttons/Function/Other_Button_01.tga")		
		
	def Other_Gui_Item_Clicker_func(self):
		Item_Clicker().Show()
	
	def Other_Gui_Spam_Bot_func(self):
		pass
	
	def Other_Gui_Bonus_Switcher_func(self):
		pass
	
	def Other_Gui_Fish_Bot_func(self):
		pass
	
	def Other_Gui_Buff_Bot_func(self):
		Buff_Bot().Show()
	
	def Other_Gui_Yang_Bug_func(self):
		Yang_Bug().Show()
	
	def Other_Gui_Book_Reader_func(self):
		Book_Reader().Show()
	
	def Other_Gui_Python_Loader_func(self):
		Python_Loader().Show()
	
	def Other_Gui_Exp_Donator_func(self):
		Exp_Donator().Show()
	
	def Other_Gui_Inventory_Menager_func(self):
		Inventory_Manager().Show()
	
	def Other_Gui_Environment_func(self):
		Environment().Show()
	
	def Other_Gui_Item_Info_func(self):
		Item_Info().Show()
	
	def Other_Gui_Feak_Info_func(self):
		Fake_Info().Show()
	
	def Other_Gui_Another_func(self):
		Another().Show()
	
	def Other_Gui_ShowTip(self):
		self.txttooltip.ClearToolTip()
		self.txttooltip.AppendTextLine("Other Function 2.1", grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
		self.txttooltip.AppendTextLine("Code by ZAHON 2016", grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)) 		
		self.txttooltip.AppendTextLine("Niktóre funkcje mog¹ nie dzia³aæ", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("w aktualnej wersji, je¿eli znalaz³eœ", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("b³¹d w dzia³aniu proszê zg³oœ mi go", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("W aktualnej wersji nie dzia³a:", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("-Spam Bot", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("-Bonus Switcher", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("-Fish Bot", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.Show()			
	
		self.Other_Gui_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_02.tga")
	
	def Other_Gui_HideTip(self):
		self.txttooltip.ClearToolTip()
		self.txttooltip.Hide()	
		self.Other_Gui_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_01.tga")			
		
	################################### Ghost Mod #########################################		
		
	def Ghost_Mode_Status_func(self):
		chr.Revive()		
	
	################################### Info Screen #########################################	
	
	def Info_Screen_Load(self):
		global Info_Screen
		if Info_Screen == "0" or Info_Screen == 0:
			self.Info_Screen.Show()	
			self.Info_Screen_Bar.Show()	
			self.Info_Screen_Set_Resolution()
		else:
			pass
	
	### Info Screen Set Resolution ###		
	def Info_Screen_Set_Resolution(self):
		Resolution = systemSetting.GetCurrentResolution()
		#chat.AppendChat(2, str(Resolution))		
	
		self.Info_Screen_Bar.SetSize(Resolution[0], Resolution[1])	
		
	### Info Screen Back ###	 
	def Info_Screen_Back_func(self):
		global Info_Screen_Page
		
		if Info_Screen_Page == 2:
			Info_Screen_Page = 1
			self.Info_Screen_img.LoadImage("ZAHON_MOD/Icons/Info_Screen/Info_Screen_02.tga")
			self.Info_Screen_EditLine.SetText("Aby aktywowaæ wybran¹ funkcjê kliknij na jej ikonê lewym przyciskiem myszy")
		elif Info_Screen_Page == 1:
			Info_Screen_Page = 0
			self.Info_Screen_img.LoadImage("ZAHON_MOD/Icons/Info_Screen/Info_Screen_01.tga")
			self.Info_Screen_EditLine.SetText("W ka¿dej chwili mo¿esz schowaæ lub wysun¹æ panel boczny za pomoc¹ przycisku, który znajduje siê po lewj stronie ekranu")
		
	### Info Screen Next ###	 
	def Info_Screen_Next_func(self):
		global Info_Screen_Page
		
		if Info_Screen_Page == 0:
			Info_Screen_Page = 1
			self.Info_Screen_img.LoadImage("ZAHON_MOD/Icons/Info_Screen/Info_Screen_02.tga")
			self.Info_Screen_EditLine.SetText("Aby aktywowaæ wybran¹ funkcjê kliknij na jej ikonê lewym przyciskiem myszy")
		elif Info_Screen_Page == 1:
			Info_Screen_Page = 2
			self.Info_Screen_img.LoadImage("ZAHON_MOD/Icons/Info_Screen/Info_Screen_03.tga")
			self.Info_Screen_EditLine.SetText("Aby wejœæ w ustawienia danej funkcji kliknij na jej ikonê prawym przyciskiem myszy")
			
			self.Info_Screen_End_Button.Show()

	### Info Screen End ###
	def Info_Screen_End_func(self):
		global Info_Screen
	
		Info_Screen = 1
		self.Info_Screen_Bar.Hide()
		self.Info_Screen.Hide()	
		self.Save_ZAHON_MOD_func()
		
	################################### Options #########################################				
		
	### Options Show ###
	def Options_func(self):
		self.Options_Button.LoadImage("ZAHON_MOD/Buttons/Function/Options_Button_03.tga")
		if self.Options.IsShow():
			pass
		else:
			self.Options.Show()				
		
	### Options Retart Show ###
	def Options_Restart_Refresh(self):
		if self.Restart_Options.IsShow():
			pass
		else:
			self.Restart_Options.Show()	
	
	### Options Retart Yes ###	
	def Restart_Options_Yes_func(self):
		global Language, Save_Mode, Info_Screen
		global Auto_Attack_Mode, Auto_Attack_Delay
		global Mobber_Delay, Mobber_ID, Mobber_HP, Mobber_Mode		
		global Pick_Up_Delay	
		global Auto_Pot_Red_ID, Auto_Pot_Red_Value, Auto_Pot_Blue_ID, Auto_Pot_Blue_Value
		global Use_Item_Delay, Use_Item_ID, Use_Item_Delay_Mode	
		global GM_Detector_Mode, GM_Detector_Delay	
		global Detector_Mode, Detector_Delay
		
		### Gui ###
		Save_Mode = "Ogólny"
		self.Options_Save_Mode_Combobox.SetCurrentItem(str(Save_Mode))		
		
		### Auto Attack ###
		Auto_Attack_Mode = "Rotacyjny"
		self.Auto_Attack_Mode_ComboBox.SetCurrentItem(str(Auto_Attack_Mode))			
			
		Auto_Attack_Delay = 1
		self.Auto_Attack_Delay_Text.SetText("Szybkoœæ rotacji " + str(Auto_Attack_Delay) + " s")
		
		### Mobber ###
		Mobber_Mode = "Pelerynki"
		self.Mobber_Mode_ComboBox.SetCurrentItem(str(Mobber_Mode))		
		
		Mobber_Delay = 1
		self.Mobber_Delay_Text.SetText("Szybkoœæ " + str(Mobber_Delay) + " s")	
			
		Mobber_ID = 0			
			
		if Mobber_ID == "0":
			self.Mobber_Item_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		else:
			item.SelectItem(int(Mobber_ID))
			Mobber_Item_Icon = item.GetIconImageFileName()
			self.Mobber_Item_Icon.LoadImage(str(Mobber_Item_Icon))			
			
		Mobber_HP = 0
		self.Slidbar_Mobber.SetSliderPos(float(float(Mobber_HP) / 100))	
		self.Mobber_HP_Text.SetText("Przestañ u¿ywaæ, jeœli HP < " + str(Mobber_HP) + "%")			
		
		### Pick Up ###
		Pick_Up_Delay = 0.1
		self.Pick_Up_Delay_Text.SetText("Szybkoœæ podnoszenia: " + str(Pick_Up_Delay)[0:3] + " s")			
		
		### Auto Pot ###
		Auto_Pot_Red_ID = 0			
					
		if Auto_Pot_Red_ID == "0":
			self.Auto_Pot_Red_Icon.LoadImage("ZAHON_MOD/Icons/Auto_Pot/Red_Pot_Shadow.tga")
		else:	
			item.SelectItem(int(Auto_Pot_Red_ID))
			Auto_Pot_Red_Icon = item.GetIconImageFileName()
			self.Auto_Pot_Red_Icon.LoadImage(str(Auto_Pot_Red_Icon))			
			
		Auto_Pot_Red_Value = 100	
		self.Slidbar_Auto_Pot_Red_Value.SetSliderPos(float(float(Auto_Pot_Red_Value) / 100))		
		self.Auto_Pot_Red_Value_Text.SetText("Przy ilu % u¿ywaæ Red Pot: " + str(Auto_Pot_Red_Value) + "%")				
						
		Auto_Pot_Blue_ID = 0

		if Auto_Pot_Blue_ID == "0":
			self.Auto_Pot_Blue_Icon.LoadImage("ZAHON_MOD/Icons/Auto_Pot/Blue_Pot_Shadow.tga")
		else:
			item.SelectItem(int(Auto_Pot_Blue_ID))
			Auto_Pot_Blue_Icon = item.GetIconImageFileName()
			self.Auto_Pot_Blue_Icon.LoadImage(str(Auto_Pot_Blue_Icon))
			
		Auto_Pot_Blue_Value = 100	
		self.Slidbar_Auto_Pot_Blue_Value.SetSliderPos(float(float(Auto_Pot_Blue_Value) / 100))	
		self.Auto_Pot_Blue_Value_Text.SetText("Przy ilu % u¿ywaæ Blue Pot: " + str(Auto_Pot_Blue_Value) + "%")				

		### Use Item ###
		Use_Item_Delay = 1
		self.Use_Item_Delay_EditLine.SetText(str(Use_Item_Delay))	

		Use_Item_Delay_Mode = "Minut"
		self.Use_Item_Delay_Mode_ComboBox.SetCurrentItem(str(Use_Item_Delay_Mode))	
		
		for i in xrange(30):
			Use_Item_ID[i] = 0 
		
			self.Use_Item_Item_1_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_2_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_3_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_4_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_5_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_6_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_7_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_8_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_9_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_10_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_11_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_12_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_13_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_14_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_15_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_16_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_17_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_18_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_19_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_20_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_21_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_22_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_23_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_24_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_25_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_26_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_27_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_28_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_29_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
			self.Use_Item_Item_30_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		
		
		### GM Detector ###
		GM_Detector_Mode = "Powiadom"
		self.GM_Detector_Mode_Combobox.SetCurrentItem(str(GM_Detector_Mode))			
		
		GM_Detector_Delay = 15
		self.GM_Detector_Delay_Text.SetText("Skanowaæ co " + str(GM_Detector_Delay) + " s")			
		
		### Detector ###
		Detector_Mode = "Wszystko"
		self.Detector_Mode_Combobox.SetCurrentItem(str(Detector_Mode))			
		
		Detector_Delay = "15"
		self.Detector_Delay_Text.SetText("Skanuj co " + str(Detector_Delay) + " s")			
		
		Detector_VID_Start_Scan = 1
		self.Detector_Options_VID_Start_Scan_EditLine.SetText(str(Detector_VID_Start_Scan))
		
		Detector_VID_End_Scan = 40000
		self.Detector_Options_VID_End_Scan_EditLine.SetText(str(Detector_VID_End_Scan))				
		
		### Teleport ###
		self.Teleport_EditLine_Distance.SetText(str(40))			
		
		self.Save_ZAHON_MOD_func()
		self.Load_ZAHON_MOD_func()
		
		self.Restart_Options.Hide()	
		
	### Options Retart No ###	
	def Restart_Options_No_func(self):
		self.Restart_Options.Hide()	
			
	### Options Buttons Func ###
	def Options_MPC_func(self):
		os.system('start http://www.mpcforum.pl/user/258957-zahon/')
		
	def Options_YouTube_func(self):
		os.system('start https://www.youtube.com/channel/UC23pks_7oQXPvR1J4domS3Q')
		
	def Options_FaceBook_func(self):
		os.system('start https://www.facebook.com/xZAHON')		
		
	### Options Mouse In ###		
	def Options_In(self):
		self.Options_Button.LoadImage("ZAHON_MOD/Buttons/Function/Options_Button_02.tga")
		
	### Options Mouse Over ###			
	def Options_Over(self):
		self.Options_Button.LoadImage("ZAHON_MOD/Buttons/Function/Options_Button_01.tga")		
		
	################################### OnUpdate #########################################		
	
	def OnUpdate(self):
		
		### Use Item ###
		global Use_Item_Delay, Use_Item_Delay_OK
		Use_Item_Delay_Mode = self.Use_Item_Delay_Mode_ComboBox.GetCurrentText()			
		Use_Item_Delay = self.Use_Item_Delay_EditLine.GetText()
		
		if Use_Item_Delay_Mode == "Minut":
			Use_Item_Delay_OK = int(int(Use_Item_Delay) * 60)
			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(Use_Item_Delay))
		else:
			Use_Item_Delay_OK = int(Use_Item_Delay)
			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(Use_Item_Delay))				
		
		### GM Detector PopUp Time ###
		global GM_Detector_PopUp_Time	
		
		Actually_Time = int(app.GetTime())
		if Actually_Time >= int(GM_Detector_PopUp_Time):
			self.GM_Detector_PopUp.Hide()			
		
		### Ghost Mod ###
		Actually_HP = player.GetStatus(player.HP)		
	
		if Actually_HP > 0:
			self.Ghost_Mode.Hide()
		else:
			self.Ghost_Mode.Show()		
		
	################################### Save func #########################################	
		
	def Save_ZAHON_MOD_func(self):
		global Language, Save_Mode, Info_Screen
		Save_Mode = self.Options_Save_Mode_Combobox.GetCurrentText()		
		
		global Auto_Attack_Mode, Auto_Attack_Delay
		Auto_Attack_Mode = self.Auto_Attack_Mode_ComboBox.GetCurrentText()
		
		global Mobber_Delay, Mobber_ID, Mobber_HP, Mobber_Mode		
		Mobber_Mode = self.Mobber_Mode_ComboBox.GetCurrentText()
		Mobber_HP = int(self.Slidbar_Mobber.GetSliderPos() * 100)		
		
		global Pick_Up_Delay
		
		global Auto_Pot_Red_ID, Auto_Pot_Red_Value, Auto_Pot_Blue_ID, Auto_Pot_Blue_Value		
		
		global Use_Item_ID	
		Use_Item_Delay = self.Use_Item_Delay_EditLine.GetText()
		Use_Item_Delay_Mode = self.Use_Item_Delay_Mode_ComboBox.GetCurrentText()			
		
		global GM_Detector_Mode, GM_Detector_Delay
		GM_Detector_Mode = self.GM_Detector_Mode_Combobox.GetCurrentText()		
		
		global Detector_Mode, Detector_Delay
		Detector_Mode = self.Detector_Mode_Combobox.GetCurrentText()
 		Detector_VID_Start_Scan = self.Detector_Options_VID_Start_Scan_EditLine.GetText()
 		Detector_VID_End_Scan = self.Detector_Options_VID_End_Scan_EditLine.GetText()		
		
		if Save_Mode == "Ogólny":
			open('ZAHON_MOD/Config/Save/ZAHON_MOD.cfg', 'w').write('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s' % (
			"###ZAHON_MOD###",
			"Language=" + str(Language),
			"Save_Mode=" + str(Save_Mode),
			"Info_Screen=" + str(Info_Screen),
			"###Auto_Attack###",
			"Auto_Attack_Mode=" + str(Auto_Attack_Mode),
			"Auto_Attack_Delay=" + str(Auto_Attack_Delay),
			"###Mobber###", 
			"Mobber_Mode=" + str(Mobber_Mode),
			"Mobber_Delay=" + str(Mobber_Delay), 
			"Mobber_ID=" + str(Mobber_ID),
			"Mobber_HP=" + str(Mobber_HP),	
			"###Pick_Up###",
			"Pick_Up_Delay=" + str(Pick_Up_Delay),
			"###Auto_Pot###",
			"Auto_Pot_Red_ID=" + str(Auto_Pot_Red_ID),
			"Auto_Pot_Red_Value=" + str(Auto_Pot_Red_Value),
			"Auto_Pot_Blue_ID=" + str(Auto_Pot_Blue_ID),
			"Auto_Pot_Blue_Value=" + str(Auto_Pot_Blue_Value),
			"###Use_Item###",
			"Use_Item_Delay=" + str(Use_Item_Delay),
			"Use_Item_Delay_Mode=" + str(Use_Item_Delay_Mode),
			"Use_Item_1_ID=" + str(Use_Item_ID[0]),	
			"Use_Item_2_ID=" + str(Use_Item_ID[1]),	
			"Use_Item_3_ID=" + str(Use_Item_ID[2]),	
			"Use_Item_4_ID=" + str(Use_Item_ID[3]),	
			"Use_Item_5_ID=" + str(Use_Item_ID[4]),	
			"Use_Item_6_ID=" + str(Use_Item_ID[5]),	
			"Use_Item_7_ID=" + str(Use_Item_ID[6]),	
			"Use_Item_8_ID=" + str(Use_Item_ID[7]),	
			"Use_Item_9_ID=" + str(Use_Item_ID[8]),
			"Use_Item_10_ID=" + str(Use_Item_ID[9]),	
			"Use_Item_11_ID=" + str(Use_Item_ID[10]),	
			"Use_Item_12_ID=" + str(Use_Item_ID[11]),		
			"Use_Item_13_ID=" + str(Use_Item_ID[12]),	
			"Use_Item_14_ID=" + str(Use_Item_ID[13]),	
			"Use_Item_15_ID=" + str(Use_Item_ID[14]),	
			"Use_Item_16_ID=" + str(Use_Item_ID[15]),	
			"Use_Item_17_ID=" + str(Use_Item_ID[16]),	
			"Use_Item_18_ID=" + str(Use_Item_ID[17]),	
			"Use_Item_19_ID=" + str(Use_Item_ID[18]),	
			"Use_Item_20_ID=" + str(Use_Item_ID[19]),	
			"Use_Item_21_ID=" + str(Use_Item_ID[20]),	
			"Use_Item_22_ID=" + str(Use_Item_ID[21]),	
			"Use_Item_23_ID=" + str(Use_Item_ID[22]),	
			"Use_Item_24_ID=" + str(Use_Item_ID[23]),	
			"Use_Item_25_ID=" + str(Use_Item_ID[24]),	
			"Use_Item_26_ID=" + str(Use_Item_ID[25]),	
			"Use_Item_27_ID=" + str(Use_Item_ID[26]),	
			"Use_Item_28_ID=" + str(Use_Item_ID[27]),	
			"Use_Item_29_ID=" + str(Use_Item_ID[28]),	
			"Use_Item_30_ID=" + str(Use_Item_ID[29]),
			"###GM_Detector###",
			"GM_Detector_Mode=" + str(GM_Detector_Mode),
			"GM_Detector_Delay=" + str(GM_Detector_Delay),
			"###Detector###",
			"Detector_Mode=" + str(Detector_Mode),
			"Detector_Delay=" + str(Detector_Delay),
			"Detector_VID_Start_Scan=" + str(Detector_VID_Start_Scan),
			"Detector_VID_End_Scan=" + str(Detector_VID_End_Scan),
			"###Teleport###",
			"Distance=" + str(self.Teleport_EditLine_Distance.GetText())
			))
			
			chat.AppendChat(2, "Pomyœlnie zapisano ustawienia")
		
			
		if Save_Mode == "Postaæ":
			Player_Name = player.GetMainCharacterName()

			open('ZAHON_MOD/Config/Save/' + str(Player_Name) + '_ZAHON_MOD.cfg', 'w').write('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s' % (
			"###ZAHON_MOD###",
			"Language=" + str(Language),
			"Save_Mode=" + str(Save_Mode),
			"Info_Screen=" + str(Info_Screen),
			"###Auto_Attack###",
			"Auto_Attack_Mode=" + str(Auto_Attack_Mode),
			"Auto_Attack_Delay=" + str(Auto_Attack_Delay),
			"###Mobber###", 
			"Mobber_Mode=" + str(Mobber_Mode),
			"Mobber_Delay=" + str(Mobber_Delay), 
			"Mobber_ID=" + str(Mobber_ID),
			"Mobber_HP=" + str(Mobber_HP),	
			"###Pick_Up###",
			"Pick_Up_Delay=" + str(Pick_Up_Delay),
			"###Auto_Pot###",
			"Auto_Pot_Red_ID=" + str(Auto_Pot_Red_ID),
			"Auto_Pot_Red_Value=" + str(Auto_Pot_Red_Value),
			"Auto_Pot_Blue_ID=" + str(Auto_Pot_Blue_ID),
			"Auto_Pot_Blue_Value=" + str(Auto_Pot_Blue_Value),
			"###Use_Item###",
			"Use_Item_Delay=" + str(Use_Item_Delay),
			"Use_Item_Delay_Mode=" + str(Use_Item_Delay_Mode),
			"Use_Item_1_ID=" + str(Use_Item_ID[0]),	
			"Use_Item_2_ID=" + str(Use_Item_ID[1]),	
			"Use_Item_3_ID=" + str(Use_Item_ID[2]),	
			"Use_Item_4_ID=" + str(Use_Item_ID[3]),	
			"Use_Item_5_ID=" + str(Use_Item_ID[4]),	
			"Use_Item_6_ID=" + str(Use_Item_ID[5]),	
			"Use_Item_7_ID=" + str(Use_Item_ID[6]),	
			"Use_Item_8_ID=" + str(Use_Item_ID[7]),	
			"Use_Item_9_ID=" + str(Use_Item_ID[8]),
			"Use_Item_10_ID=" + str(Use_Item_ID[9]),	
			"Use_Item_11_ID=" + str(Use_Item_ID[10]),	
			"Use_Item_12_ID=" + str(Use_Item_ID[11]),		
			"Use_Item_13_ID=" + str(Use_Item_ID[12]),	
			"Use_Item_14_ID=" + str(Use_Item_ID[13]),	
			"Use_Item_15_ID=" + str(Use_Item_ID[14]),	
			"Use_Item_16_ID=" + str(Use_Item_ID[15]),	
			"Use_Item_17_ID=" + str(Use_Item_ID[16]),	
			"Use_Item_18_ID=" + str(Use_Item_ID[17]),	
			"Use_Item_19_ID=" + str(Use_Item_ID[18]),	
			"Use_Item_20_ID=" + str(Use_Item_ID[19]),	
			"Use_Item_21_ID=" + str(Use_Item_ID[20]),	
			"Use_Item_22_ID=" + str(Use_Item_ID[21]),	
			"Use_Item_23_ID=" + str(Use_Item_ID[22]),	
			"Use_Item_24_ID=" + str(Use_Item_ID[23]),	
			"Use_Item_25_ID=" + str(Use_Item_ID[24]),	
			"Use_Item_26_ID=" + str(Use_Item_ID[25]),	
			"Use_Item_27_ID=" + str(Use_Item_ID[26]),	
			"Use_Item_28_ID=" + str(Use_Item_ID[27]),	
			"Use_Item_29_ID=" + str(Use_Item_ID[28]),	
			"Use_Item_30_ID=" + str(Use_Item_ID[29]),
			"###GM_Detector###",
			"GM_Detector_Mode=" + str(GM_Detector_Mode),
			"GM_Detector_Delay=" + str(GM_Detector_Delay),
			"###Detector###",
			"Detector_Mode=" + str(Detector_Mode),
			"Detector_Delay=" + str(Detector_Delay),
			"Detector_VID_Start_Scan=" + str(Detector_VID_Start_Scan),
			"Detector_VID_End_Scan=" + str(Detector_VID_End_Scan),
			"###Teleport###",
			"Distance=" + str(self.Teleport_EditLine_Distance.GetText())
			))
			
			chat.AppendChat(2, str(Player_Name))	
			chat.AppendChat(2, "Pomyœlnie zapisano ustawienia")			
		
	################################### Load func #########################################	
	
	def Load_ZAHON_MOD_func(self):	
		global Language, Save_Mode, Info_Screen
		global Auto_Attack_Mode, Auto_Attack_Delay
		global Mobber_Delay, Mobber_ID, Mobber_HP, Mobber_Mode		
		global Pick_Up_Delay	
		global Auto_Pot_Red_ID, Auto_Pot_Red_Value, Auto_Pot_Blue_ID, Auto_Pot_Blue_Value
		global Use_Item_Delay, Use_Item_ID	
		global GM_Detector_Mode, GM_Detector_Delay	
		global Detector_Mode, Detector_Delay
		
		Player_Name = player.GetMainCharacterName()		
		
		if os.path.exists("ZAHON_MOD/Config/Save/" + str(Player_Name) + "_ZAHON_MOD.cfg"):
			ZAHON_MOD_Load = open("ZAHON_MOD/Config/Save/" + str(Player_Name) + "_ZAHON_MOD.cfg", "r").read().split()		

			### Gui ###
			Save_Mode = ZAHON_MOD_Load[2].replace("Save_Mode=", "")
			self.Options_Save_Mode_Combobox.SetCurrentItem(str(Save_Mode))							
			
			Info_Screen = ZAHON_MOD_Load[3].replace("Info_Screen=", "")
			
			# if Info_Screen == 0:
				# chat.AppendChat(2, "Test")
				# self.Info_Screen.Show()	
				# self.Info_Screen_Bar.Show()	
				# self.Info_Screen_Set_Resolution()
			# else:
				# pass
			
			### Auto Attack ###
			Auto_Attack_Mode = ZAHON_MOD_Load[5].replace("Auto_Attack_Mode=", "")
			self.Auto_Attack_Mode_ComboBox.SetCurrentItem(str(Auto_Attack_Mode))			
			
			Auto_Attack_Delay = ZAHON_MOD_Load[6].replace("Auto_Attack_Delay=", "")
			self.Auto_Attack_Delay_Text.SetText("Szybkoœæ rotacji " + str(Auto_Attack_Delay) + " s")		
	
			### Mobber ###
			Mobber_Mode = ZAHON_MOD_Load[8].replace("Mobber_Mode=", "")
			self.Mobber_Mode_ComboBox.SetCurrentItem(str(Mobber_Mode))			
			
			Mobber_Delay = ZAHON_MOD_Load[9].replace("Mobber_Delay=", "")
			self.Mobber_Delay_Text.SetText("Szybkoœæ " + str(Mobber_Delay) + " s")	
			
			Mobber_ID = ZAHON_MOD_Load[10].replace("Mobber_ID=", "")			
			
			if Mobber_ID == "0":
				self.Mobber_Item_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Mobber_ID))
				Mobber_Item_Icon = item.GetIconImageFileName()
				self.Mobber_Item_Icon.LoadImage(str(Mobber_Item_Icon))			
			
			Mobber_HP = ZAHON_MOD_Load[11].replace("Mobber_HP=", "")
			self.Slidbar_Mobber.SetSliderPos(float(float(Mobber_HP) / 100))	
			self.Mobber_HP_Text.SetText("Przestañ u¿ywaæ, jeœli HP < " + str(Mobber_HP) + "%")		
	
			### Pick Up ###
			Pick_Up_Delay = ZAHON_MOD_Load[13].replace("Pick_Up_Delay=", "")
			self.Pick_Up_Delay_Text.SetText("Szybkoœæ podnoszenia: " + str(Pick_Up_Delay)[0:3] + " s")		
	
			### Auto Pot ###
			Auto_Pot_Red_ID = ZAHON_MOD_Load[15].replace("Auto_Pot_Red_ID=", "")				
					
			if Auto_Pot_Red_ID == "0":
				self.Auto_Pot_Red_Icon.LoadImage("ZAHON_MOD/Icons/Auto_Pot/Red_Pot_Shadow.tga")
			else:	
				item.SelectItem(int(Auto_Pot_Red_ID))
				Auto_Pot_Red_Icon = item.GetIconImageFileName()
				self.Auto_Pot_Red_Icon.LoadImage(str(Auto_Pot_Red_Icon))			
			
			Auto_Pot_Red_Value = ZAHON_MOD_Load[16].replace("Auto_Pot_Red_Value=", "")	
			self.Slidbar_Auto_Pot_Red_Value.SetSliderPos(float(float(Auto_Pot_Red_Value) / 100))		
			self.Auto_Pot_Red_Value_Text.SetText("Przy ilu % u¿ywaæ Red Pot: " + str(Auto_Pot_Red_Value) + "%")				
						
			Auto_Pot_Blue_ID = ZAHON_MOD_Load[17].replace("Auto_Pot_Blue_ID=", "")

			if Auto_Pot_Blue_ID == "0":
				self.Auto_Pot_Blue_Icon.LoadImage("ZAHON_MOD/Icons/Auto_Pot/Blue_Pot_Shadow.tga")
			else:
				item.SelectItem(int(Auto_Pot_Blue_ID))
				Auto_Pot_Blue_Icon = item.GetIconImageFileName()
				self.Auto_Pot_Blue_Icon.LoadImage(str(Auto_Pot_Blue_Icon))

			Auto_Pot_Blue_Value = ZAHON_MOD_Load[18].replace("Auto_Pot_Blue_Value=", "")	
			self.Slidbar_Auto_Pot_Blue_Value.SetSliderPos(float(float(Auto_Pot_Blue_Value) / 100))	
			self.Auto_Pot_Blue_Value_Text.SetText("Przy ilu % u¿ywaæ Blue Pot: " + str(Auto_Pot_Blue_Value) + "%")		
	
			### Use Item ###
			Use_Item_Delay = ZAHON_MOD_Load[20].replace("Use_Item_Delay=", "")
			self.Use_Item_Delay_EditLine.SetText(str(Use_Item_Delay))	

			Use_Item_Delay_Mode = ZAHON_MOD_Load[21].replace("Use_Item_Delay_Mode=", "")
			self.Use_Item_Delay_Mode_ComboBox.SetCurrentItem(str(Use_Item_Delay_Mode))				
		
			Use_Item_ID[0] = ZAHON_MOD_Load[22].replace("Use_Item_1_ID=", "")
			if Use_Item_ID[0] == "0":
				self.Use_Item_Item_1_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[0]))
				Use_Item_Item_1_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_1_Icon.LoadImage(str(Use_Item_Item_1_Icon))	

			Use_Item_ID[1] = ZAHON_MOD_Load[23].replace("Use_Item_2_ID=", "")
			if Use_Item_ID[1] == "0":
				self.Use_Item_Item_2_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[1]))
				Use_Item_Item_2_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_2_Icon.LoadImage(str(Use_Item_Item_2_Icon))	

			Use_Item_ID[2] = ZAHON_MOD_Load[24].replace("Use_Item_3_ID=", "")
			if Use_Item_ID[2] == "0":
				self.Use_Item_Item_3_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[2]))
				Use_Item_Item_3_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_3_Icon.LoadImage(str(Use_Item_Item_3_Icon))	

			Use_Item_ID[3] = ZAHON_MOD_Load[25].replace("Use_Item_4_ID=", "")
			if Use_Item_ID[3] == "0":
				self.Use_Item_Item_4_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[3]))
				Use_Item_Item_4_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_4_Icon.LoadImage(str(Use_Item_Item_4_Icon))	

			Use_Item_ID[4] = ZAHON_MOD_Load[26].replace("Use_Item_5_ID=", "")
			if Use_Item_ID[4] == "0":
				self.Use_Item_Item_5_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[4]))
				Use_Item_Item_5_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_5_Icon.LoadImage(str(Use_Item_Item_5_Icon))	

			Use_Item_ID[5] = ZAHON_MOD_Load[27].replace("Use_Item_6_ID=", "")
			if Use_Item_ID[5] == "0":
				self.Use_Item_Item_6_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[5]))
				Use_Item_Item_6_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_6_Icon.LoadImage(str(Use_Item_Item_6_Icon))	

			Use_Item_ID[6] = ZAHON_MOD_Load[28].replace("Use_Item_7_ID=", "")
			if Use_Item_ID[6] == "0":
				self.Use_Item_Item_7_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[6]))
				Use_Item_Item_7_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_7_Icon.LoadImage(str(Use_Item_Item_7_Icon))

			Use_Item_ID[7] = ZAHON_MOD_Load[29].replace("Use_Item_8_ID=", "")
			if Use_Item_ID[7] == "0":
				self.Use_Item_Item_8_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[7]))
				Use_Item_Item_8_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_8_Icon.LoadImage(str(Use_Item_Item_8_Icon))	

			Use_Item_ID[8] = ZAHON_MOD_Load[30].replace("Use_Item_9_ID=", "")
			if Use_Item_ID[8] == "0":
				self.Use_Item_Item_9_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[8]))
				Use_Item_Item_9_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_9_Icon.LoadImage(str(Use_Item_Item_9_Icon))	

			Use_Item_ID[9] = ZAHON_MOD_Load[31].replace("Use_Item_10_ID=", "")
			if Use_Item_ID[9] == "0":
				self.Use_Item_Item_10_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[9]))
				Use_Item_Item_10_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_10_Icon.LoadImage(str(Use_Item_Item_10_Icon))	

			Use_Item_ID[10] = ZAHON_MOD_Load[32].replace("Use_Item_11_ID=", "")
			if Use_Item_ID[10] == "0":
				self.Use_Item_Item_11_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[10]))
				Use_Item_Item_11_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_11_Icon.LoadImage(str(Use_Item_Item_11_Icon))	

			Use_Item_ID[11] = ZAHON_MOD_Load[33].replace("Use_Item_12_ID=", "")
			if Use_Item_ID[11] == "0":
				self.Use_Item_Item_12_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[11]))
				Use_Item_Item_12_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_12_Icon.LoadImage(str(Use_Item_Item_12_Icon))

			Use_Item_ID[12] = ZAHON_MOD_Load[34].replace("Use_Item_13_ID=", "")
			if Use_Item_ID[12] == "0":
				self.Use_Item_Item_13_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[12]))
				Use_Item_Item_13_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_13_Icon.LoadImage(str(Use_Item_Item_13_Icon))

			Use_Item_ID[13] = ZAHON_MOD_Load[35].replace("Use_Item_14_ID=", "")
			if Use_Item_ID[13] == "0":
				self.Use_Item_Item_14_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[13]))
				Use_Item_Item_14_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_14_Icon.LoadImage(str(Use_Item_Item_14_Icon))

			Use_Item_ID[14] = ZAHON_MOD_Load[36].replace("Use_Item_15_ID=", "")
			if Use_Item_ID[14] == "0":
				self.Use_Item_Item_15_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[14]))
				Use_Item_Item_15_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_15_Icon.LoadImage(str(Use_Item_Item_15_Icon))	

			Use_Item_ID[15] = ZAHON_MOD_Load[37].replace("Use_Item_16_ID=", "")
			if Use_Item_ID[15] == "0":
				self.Use_Item_Item_16_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[15]))
				Use_Item_Item_16_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_16_Icon.LoadImage(str(Use_Item_Item_16_Icon))

			Use_Item_ID[16] = ZAHON_MOD_Load[38].replace("Use_Item_17_ID=", "")
			if Use_Item_ID[16] == "0":
				self.Use_Item_Item_17_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[16]))
				Use_Item_Item_17_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_17_Icon.LoadImage(str(Use_Item_Item_17_Icon))

			Use_Item_ID[17] = ZAHON_MOD_Load[39].replace("Use_Item_18_ID=", "")
			if Use_Item_ID[17] == "0":
				self.Use_Item_Item_18_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[17]))
				Use_Item_Item_18_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_18_Icon.LoadImage(str(Use_Item_Item_18_Icon))

			Use_Item_ID[18] = ZAHON_MOD_Load[40].replace("Use_Item_19_ID=", "")
			if Use_Item_ID[18] == "0":
				self.Use_Item_Item_19_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[18]))
				Use_Item_Item_19_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_19_Icon.LoadImage(str(Use_Item_Item_19_Icon))

			Use_Item_ID[19] = ZAHON_MOD_Load[41].replace("Use_Item_20_ID=", "")
			if Use_Item_ID[19] == "0":
				self.Use_Item_Item_20_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[19]))
				Use_Item_Item_20_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_20_Icon.LoadImage(str(Use_Item_Item_20_Icon))	

			Use_Item_ID[20] = ZAHON_MOD_Load[42].replace("Use_Item_21_ID=", "")
			if Use_Item_ID[20] == "0":
				self.Use_Item_Item_21_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[20]))
				Use_Item_Item_21_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_21_Icon.LoadImage(str(Use_Item_Item_21_Icon))	

			Use_Item_ID[21] = ZAHON_MOD_Load[43].replace("Use_Item_22_ID=", "")
			if Use_Item_ID[21] == "0":
				self.Use_Item_Item_22_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[21]))
				Use_Item_Item_22_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_22_Icon.LoadImage(str(Use_Item_Item_22_Icon))

			Use_Item_ID[22] = ZAHON_MOD_Load[44].replace("Use_Item_23_ID=", "")
			if Use_Item_ID[22] == "0":
				self.Use_Item_Item_23_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[22]))
				Use_Item_Item_23_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_23_Icon.LoadImage(str(Use_Item_Item_23_Icon))

			Use_Item_ID[23] = ZAHON_MOD_Load[45].replace("Use_Item_24_ID=", "")
			if Use_Item_ID[23] == "0":
				self.Use_Item_Item_24_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[23]))
				Use_Item_Item_24_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_24_Icon.LoadImage(str(Use_Item_Item_24_Icon))					
		
			Use_Item_ID[24] = ZAHON_MOD_Load[46].replace("Use_Item_25_ID=", "")
			if Use_Item_ID[24] == "0":
				self.Use_Item_Item_25_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[24]))
				Use_Item_Item_25_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_25_Icon.LoadImage(str(Use_Item_Item_25_Icon))

			Use_Item_ID[25] = ZAHON_MOD_Load[47].replace("Use_Item_26_ID=", "")
			if Use_Item_ID[25] == "0":
				self.Use_Item_Item_26_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[25]))
				Use_Item_Item_26_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_26_Icon.LoadImage(str(Use_Item_Item_26_Icon))

			Use_Item_ID[26] = ZAHON_MOD_Load[48].replace("Use_Item_27_ID=", "")
			if Use_Item_ID[26] == "0":
				self.Use_Item_Item_27_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[26]))
				Use_Item_Item_27_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_27_Icon.LoadImage(str(Use_Item_Item_27_Icon))

			Use_Item_ID[27] = ZAHON_MOD_Load[49].replace("Use_Item_28_ID=", "")
			if Use_Item_ID[27] == "0":
				self.Use_Item_Item_28_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[27]))
				Use_Item_Item_28_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_28_Icon.LoadImage(str(Use_Item_Item_28_Icon))

			Use_Item_ID[28] = ZAHON_MOD_Load[50].replace("Use_Item_29_ID=", "")
			if Use_Item_ID[28] == "0":
				self.Use_Item_Item_29_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[28]))
				Use_Item_Item_29_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_29_Icon.LoadImage(str(Use_Item_Item_29_Icon))

			Use_Item_ID[29] = ZAHON_MOD_Load[51].replace("Use_Item_30_ID=", "")
			if Use_Item_ID[29] == "0":
				self.Use_Item_Item_30_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
			else:
				item.SelectItem(int(Use_Item_ID[29]))
				Use_Item_Item_30_Icon = item.GetIconImageFileName()
				self.Use_Item_Item_30_Icon.LoadImage(str(Use_Item_Item_30_Icon))				
	
			### GM Detector ###
			GM_Detector_Mode = ZAHON_MOD_Load[53].replace("GM_Detector_Mode=", "")
			self.GM_Detector_Mode_Combobox.SetCurrentItem(str(GM_Detector_Mode))			
		
			GM_Detector_Delay = ZAHON_MOD_Load[54].replace("GM_Detector_Delay=", "")
			self.GM_Detector_Delay_Text.SetText("Skanowaæ co " + str(GM_Detector_Delay) + " s")				
	
			### Detector ###
			Detector_Mode = ZAHON_MOD_Load[56].replace("Detector_Mode=", "")
			self.Detector_Mode_Combobox.SetCurrentItem(str(Detector_Mode))			
		
			Detector_Delay = ZAHON_MOD_Load[57].replace("Detector_Delay=", "")
			self.Detector_Delay_Text.SetText("Skanuj co " + str(Detector_Delay) + " s")			
		
			Detector_VID_Start_Scan = ZAHON_MOD_Load[58].replace("Detector_VID_Start_Scan=", "")
			self.Detector_Options_VID_Start_Scan_EditLine.SetText(str(Detector_VID_Start_Scan))
		
			Detector_VID_End_Scan = ZAHON_MOD_Load[59].replace("Detector_VID_End_Scan=", "")
			self.Detector_Options_VID_End_Scan_EditLine.SetText(str(Detector_VID_End_Scan))			
		
			### Teleport ###
			self.Teleport_EditLine_Distance.SetText(str(ZAHON_MOD_Load[61].replace("Distance=", "")))	
	
			chat.AppendChat(2, "Pomyœlnie wczytano ustawienia")				
			chat.AppendChat(2, str(Player_Name))				
			
		else:
		
		
			if os.path.exists("ZAHON_MOD/Config/Save/ZAHON_MOD.cfg"):
				ZAHON_MOD_Load = open("ZAHON_MOD/Config/Save/ZAHON_MOD.cfg", "r").read().split()
				
				### Gui ###
				Save_Mode = ZAHON_MOD_Load[2].replace("Save_Mode=", "")
				self.Options_Save_Mode_Combobox.SetCurrentItem(str(Save_Mode))							
				
				Info_Screen = ZAHON_MOD_Load[3].replace("Info_Screen=", "")
								
				### Auto Attack ###
				Auto_Attack_Mode = ZAHON_MOD_Load[5].replace("Auto_Attack_Mode=", "")
				self.Auto_Attack_Mode_ComboBox.SetCurrentItem(str(Auto_Attack_Mode))			
				
				Auto_Attack_Delay = ZAHON_MOD_Load[6].replace("Auto_Attack_Delay=", "")
				self.Auto_Attack_Delay_Text.SetText("Szybkoœæ rotacji " + str(Auto_Attack_Delay) + " s")		
		
				### Mobber ###
				Mobber_Mode = ZAHON_MOD_Load[8].replace("Mobber_Mode=", "")
				self.Mobber_Mode_ComboBox.SetCurrentItem(str(Mobber_Mode))			
				
				Mobber_Delay = ZAHON_MOD_Load[9].replace("Mobber_Delay=", "")
				self.Mobber_Delay_Text.SetText("Szybkoœæ " + str(Mobber_Delay) + " s")	
				
				Mobber_ID = ZAHON_MOD_Load[10].replace("Mobber_ID=", "")			
				
				if Mobber_ID == "0":
					self.Mobber_Item_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Mobber_ID))
					Mobber_Item_Icon = item.GetIconImageFileName()
					self.Mobber_Item_Icon.LoadImage(str(Mobber_Item_Icon))			
				
				Mobber_HP = ZAHON_MOD_Load[11].replace("Mobber_HP=", "")
				self.Slidbar_Mobber.SetSliderPos(float(float(Mobber_HP) / 100))	
				self.Mobber_HP_Text.SetText("Przestañ u¿ywaæ, jeœli HP < " + str(Mobber_HP) + "%")		
		
				### Pick Up ###
				Pick_Up_Delay = ZAHON_MOD_Load[13].replace("Pick_Up_Delay=", "")
				self.Pick_Up_Delay_Text.SetText("Szybkoœæ podnoszenia: " + str(Pick_Up_Delay)[0:3] + " s")		
		
				### Auto Pot ###
				Auto_Pot_Red_ID = ZAHON_MOD_Load[15].replace("Auto_Pot_Red_ID=", "")				
						
				if Auto_Pot_Red_ID == "0":
					self.Auto_Pot_Red_Icon.LoadImage("ZAHON_MOD/Icons/Auto_Pot/Red_Pot_Shadow.tga")
				else:	
					item.SelectItem(int(Auto_Pot_Red_ID))
					Auto_Pot_Red_Icon = item.GetIconImageFileName()
					self.Auto_Pot_Red_Icon.LoadImage(str(Auto_Pot_Red_Icon))			
				
				Auto_Pot_Red_Value = ZAHON_MOD_Load[16].replace("Auto_Pot_Red_Value=", "")	
				self.Slidbar_Auto_Pot_Red_Value.SetSliderPos(float(float(Auto_Pot_Red_Value) / 100))		
				self.Auto_Pot_Red_Value_Text.SetText("Przy ilu % u¿ywaæ Red Pot: " + str(Auto_Pot_Red_Value) + "%")				
							
				Auto_Pot_Blue_ID = ZAHON_MOD_Load[17].replace("Auto_Pot_Blue_ID=", "")

				if Auto_Pot_Blue_ID == "0":
					self.Auto_Pot_Blue_Icon.LoadImage("ZAHON_MOD/Icons/Auto_Pot/Blue_Pot_Shadow.tga")
				else:
					item.SelectItem(int(Auto_Pot_Blue_ID))
					Auto_Pot_Blue_Icon = item.GetIconImageFileName()
					self.Auto_Pot_Blue_Icon.LoadImage(str(Auto_Pot_Blue_Icon))

				Auto_Pot_Blue_Value = ZAHON_MOD_Load[18].replace("Auto_Pot_Blue_Value=", "")	
				self.Slidbar_Auto_Pot_Blue_Value.SetSliderPos(float(float(Auto_Pot_Blue_Value) / 100))	
				self.Auto_Pot_Blue_Value_Text.SetText("Przy ilu % u¿ywaæ Blue Pot: " + str(Auto_Pot_Blue_Value) + "%")		
		
				### Use Item ###
				Use_Item_Delay = ZAHON_MOD_Load[20].replace("Use_Item_Delay=", "")
				self.Use_Item_Delay_EditLine.SetText(str(Use_Item_Delay))	

				Use_Item_Delay_Mode = ZAHON_MOD_Load[21].replace("Use_Item_Delay_Mode=", "")
				self.Use_Item_Delay_Mode_ComboBox.SetCurrentItem(str(Use_Item_Delay_Mode))				
			
				Use_Item_ID[0] = ZAHON_MOD_Load[22].replace("Use_Item_1_ID=", "")
				if Use_Item_ID[0] == "0":
					self.Use_Item_Item_1_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[0]))
					Use_Item_Item_1_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_1_Icon.LoadImage(str(Use_Item_Item_1_Icon))	

				Use_Item_ID[1] = ZAHON_MOD_Load[23].replace("Use_Item_2_ID=", "")
				if Use_Item_ID[1] == "0":
					self.Use_Item_Item_2_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[1]))
					Use_Item_Item_2_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_2_Icon.LoadImage(str(Use_Item_Item_2_Icon))	

				Use_Item_ID[2] = ZAHON_MOD_Load[24].replace("Use_Item_3_ID=", "")
				if Use_Item_ID[2] == "0":
					self.Use_Item_Item_3_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[2]))
					Use_Item_Item_3_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_3_Icon.LoadImage(str(Use_Item_Item_3_Icon))	

				Use_Item_ID[3] = ZAHON_MOD_Load[25].replace("Use_Item_4_ID=", "")
				if Use_Item_ID[3] == "0":
					self.Use_Item_Item_4_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[3]))
					Use_Item_Item_4_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_4_Icon.LoadImage(str(Use_Item_Item_4_Icon))	

				Use_Item_ID[4] = ZAHON_MOD_Load[26].replace("Use_Item_5_ID=", "")
				if Use_Item_ID[4] == "0":
					self.Use_Item_Item_5_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[4]))
					Use_Item_Item_5_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_5_Icon.LoadImage(str(Use_Item_Item_5_Icon))	

				Use_Item_ID[5] = ZAHON_MOD_Load[27].replace("Use_Item_6_ID=", "")
				if Use_Item_ID[5] == "0":
					self.Use_Item_Item_6_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[5]))
					Use_Item_Item_6_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_6_Icon.LoadImage(str(Use_Item_Item_6_Icon))	

				Use_Item_ID[6] = ZAHON_MOD_Load[28].replace("Use_Item_7_ID=", "")
				if Use_Item_ID[6] == "0":
					self.Use_Item_Item_7_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[6]))
					Use_Item_Item_7_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_7_Icon.LoadImage(str(Use_Item_Item_7_Icon))

				Use_Item_ID[7] = ZAHON_MOD_Load[29].replace("Use_Item_8_ID=", "")
				if Use_Item_ID[7] == "0":
					self.Use_Item_Item_8_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[7]))
					Use_Item_Item_8_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_8_Icon.LoadImage(str(Use_Item_Item_8_Icon))	

				Use_Item_ID[8] = ZAHON_MOD_Load[30].replace("Use_Item_9_ID=", "")
				if Use_Item_ID[8] == "0":
					self.Use_Item_Item_9_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[8]))
					Use_Item_Item_9_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_9_Icon.LoadImage(str(Use_Item_Item_9_Icon))	

				Use_Item_ID[9] = ZAHON_MOD_Load[31].replace("Use_Item_10_ID=", "")
				if Use_Item_ID[9] == "0":
					self.Use_Item_Item_10_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[9]))
					Use_Item_Item_10_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_10_Icon.LoadImage(str(Use_Item_Item_10_Icon))	

				Use_Item_ID[10] = ZAHON_MOD_Load[32].replace("Use_Item_11_ID=", "")
				if Use_Item_ID[10] == "0":
					self.Use_Item_Item_11_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[10]))
					Use_Item_Item_11_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_11_Icon.LoadImage(str(Use_Item_Item_11_Icon))	

				Use_Item_ID[11] = ZAHON_MOD_Load[33].replace("Use_Item_12_ID=", "")
				if Use_Item_ID[11] == "0":
					self.Use_Item_Item_12_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[11]))
					Use_Item_Item_12_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_12_Icon.LoadImage(str(Use_Item_Item_12_Icon))

				Use_Item_ID[12] = ZAHON_MOD_Load[34].replace("Use_Item_13_ID=", "")
				if Use_Item_ID[12] == "0":
					self.Use_Item_Item_13_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[12]))
					Use_Item_Item_13_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_13_Icon.LoadImage(str(Use_Item_Item_13_Icon))

				Use_Item_ID[13] = ZAHON_MOD_Load[35].replace("Use_Item_14_ID=", "")
				if Use_Item_ID[13] == "0":
					self.Use_Item_Item_14_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[13]))
					Use_Item_Item_14_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_14_Icon.LoadImage(str(Use_Item_Item_14_Icon))

				Use_Item_ID[14] = ZAHON_MOD_Load[36].replace("Use_Item_15_ID=", "")
				if Use_Item_ID[14] == "0":
					self.Use_Item_Item_15_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[14]))
					Use_Item_Item_15_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_15_Icon.LoadImage(str(Use_Item_Item_15_Icon))	

				Use_Item_ID[15] = ZAHON_MOD_Load[37].replace("Use_Item_16_ID=", "")
				if Use_Item_ID[15] == "0":
					self.Use_Item_Item_16_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[15]))
					Use_Item_Item_16_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_16_Icon.LoadImage(str(Use_Item_Item_16_Icon))

				Use_Item_ID[16] = ZAHON_MOD_Load[38].replace("Use_Item_17_ID=", "")
				if Use_Item_ID[16] == "0":
					self.Use_Item_Item_17_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[16]))
					Use_Item_Item_17_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_17_Icon.LoadImage(str(Use_Item_Item_17_Icon))

				Use_Item_ID[17] = ZAHON_MOD_Load[39].replace("Use_Item_18_ID=", "")
				if Use_Item_ID[17] == "0":
					self.Use_Item_Item_18_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[17]))
					Use_Item_Item_18_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_18_Icon.LoadImage(str(Use_Item_Item_18_Icon))

				Use_Item_ID[18] = ZAHON_MOD_Load[40].replace("Use_Item_19_ID=", "")
				if Use_Item_ID[18] == "0":
					self.Use_Item_Item_19_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[18]))
					Use_Item_Item_19_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_19_Icon.LoadImage(str(Use_Item_Item_19_Icon))

				Use_Item_ID[19] = ZAHON_MOD_Load[41].replace("Use_Item_20_ID=", "")
				if Use_Item_ID[19] == "0":
					self.Use_Item_Item_20_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[19]))
					Use_Item_Item_20_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_20_Icon.LoadImage(str(Use_Item_Item_20_Icon))	

				Use_Item_ID[20] = ZAHON_MOD_Load[42].replace("Use_Item_21_ID=", "")
				if Use_Item_ID[20] == "0":
					self.Use_Item_Item_21_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[20]))
					Use_Item_Item_21_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_21_Icon.LoadImage(str(Use_Item_Item_21_Icon))	

				Use_Item_ID[21] = ZAHON_MOD_Load[43].replace("Use_Item_22_ID=", "")
				if Use_Item_ID[21] == "0":
					self.Use_Item_Item_22_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[21]))
					Use_Item_Item_22_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_22_Icon.LoadImage(str(Use_Item_Item_22_Icon))

				Use_Item_ID[22] = ZAHON_MOD_Load[44].replace("Use_Item_23_ID=", "")
				if Use_Item_ID[22] == "0":
					self.Use_Item_Item_23_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[22]))
					Use_Item_Item_23_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_23_Icon.LoadImage(str(Use_Item_Item_23_Icon))

				Use_Item_ID[23] = ZAHON_MOD_Load[45].replace("Use_Item_24_ID=", "")
				if Use_Item_ID[23] == "0":
					self.Use_Item_Item_24_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[23]))
					Use_Item_Item_24_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_24_Icon.LoadImage(str(Use_Item_Item_24_Icon))					
			
				Use_Item_ID[24] = ZAHON_MOD_Load[46].replace("Use_Item_25_ID=", "")
				if Use_Item_ID[24] == "0":
					self.Use_Item_Item_25_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[24]))
					Use_Item_Item_25_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_25_Icon.LoadImage(str(Use_Item_Item_25_Icon))

				Use_Item_ID[25] = ZAHON_MOD_Load[47].replace("Use_Item_26_ID=", "")
				if Use_Item_ID[25] == "0":
					self.Use_Item_Item_26_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[25]))
					Use_Item_Item_26_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_26_Icon.LoadImage(str(Use_Item_Item_26_Icon))

				Use_Item_ID[26] = ZAHON_MOD_Load[48].replace("Use_Item_27_ID=", "")
				if Use_Item_ID[26] == "0":
					self.Use_Item_Item_27_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[26]))
					Use_Item_Item_27_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_27_Icon.LoadImage(str(Use_Item_Item_27_Icon))

				Use_Item_ID[27] = ZAHON_MOD_Load[49].replace("Use_Item_28_ID=", "")
				if Use_Item_ID[27] == "0":
					self.Use_Item_Item_28_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[27]))
					Use_Item_Item_28_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_28_Icon.LoadImage(str(Use_Item_Item_28_Icon))

				Use_Item_ID[28] = ZAHON_MOD_Load[50].replace("Use_Item_29_ID=", "")
				if Use_Item_ID[28] == "0":
					self.Use_Item_Item_29_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[28]))
					Use_Item_Item_29_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_29_Icon.LoadImage(str(Use_Item_Item_29_Icon))

				Use_Item_ID[29] = ZAHON_MOD_Load[51].replace("Use_Item_30_ID=", "")
				if Use_Item_ID[29] == "0":
					self.Use_Item_Item_30_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
				else:
					item.SelectItem(int(Use_Item_ID[29]))
					Use_Item_Item_30_Icon = item.GetIconImageFileName()
					self.Use_Item_Item_30_Icon.LoadImage(str(Use_Item_Item_30_Icon))				
		
				### GM Detector ###
				GM_Detector_Mode = ZAHON_MOD_Load[53].replace("GM_Detector_Mode=", "")
				self.GM_Detector_Mode_Combobox.SetCurrentItem(str(GM_Detector_Mode))			
			
				GM_Detector_Delay = ZAHON_MOD_Load[54].replace("GM_Detector_Delay=", "")
				self.GM_Detector_Delay_Text.SetText("Skanowaæ co " + str(GM_Detector_Delay) + " s")				
		
				### Detector ###
				Detector_Mode = ZAHON_MOD_Load[56].replace("Detector_Mode=", "")
				self.Detector_Mode_Combobox.SetCurrentItem(str(Detector_Mode))			
			
				Detector_Delay = ZAHON_MOD_Load[57].replace("Detector_Delay=", "")
				self.Detector_Delay_Text.SetText("Skanuj co " + str(Detector_Delay) + " s")			
			
				Detector_VID_Start_Scan = ZAHON_MOD_Load[58].replace("Detector_VID_Start_Scan=", "")
				self.Detector_Options_VID_Start_Scan_EditLine.SetText(str(Detector_VID_Start_Scan))
			
				Detector_VID_End_Scan = ZAHON_MOD_Load[59].replace("Detector_VID_End_Scan=", "")
				self.Detector_Options_VID_End_Scan_EditLine.SetText(str(Detector_VID_End_Scan))			
			
				### Teleport ###
				self.Teleport_EditLine_Distance.SetText(str(ZAHON_MOD_Load[61].replace("Distance=", "")))	
		
				chat.AppendChat(2, "Pomyœlnie wczytano ustawienia")						


	
	def __BuildKeyDict(self):
		onPressKeyDict = {}
		onPressKeyDict[app.DIK_F5]	= lambda : self.OpenWindow()
		self.onPressKeyDict = onPressKeyDict
	
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
	
	def Auto_Attack_Close(self):
		self.Save_ZAHON_MOD_func()
		self.Auto_Attack.SetPosition(50, 120)
		self.Auto_Attack.Hide()

	def Mobber_Close(self):
		self.Save_ZAHON_MOD_func()
		self.Mobber.SetPosition(50, 120)
		self.Mobber.Hide()		
		
	def Pick_Up_Close(self):
		self.Save_ZAHON_MOD_func()
		self.Pick_Up.SetPosition(50, 120)
		self.Pick_Up.Hide()	
		
	def Auto_Pot_Close(self):
		self.Save_ZAHON_MOD_func()
		self.Auto_Pot.SetPosition(50, 120)
		self.Auto_Pot.Hide()	

	def Use_Item_Close(self):
		self.Save_ZAHON_MOD_func()
		self.Use_Item.SetPosition(50, 120)
		self.Use_Item.Hide()	

	def Use_Item_Delete_All_Close(self):
		self.Save_ZAHON_MOD_func()
		self.Use_Item_Delete_All.Hide()			
		
	def GM_Detector_Close(self):
		self.Save_ZAHON_MOD_func()
		self.GM_Detector.SetPosition(50, 120)
		self.GM_Detector.Hide()	

	def GM_Detector_List_Close(self):
		self.Save_ZAHON_MOD_func()
		self.GM_Detector_List.Hide()	

	def GM_Detector_Logs_Close(self):
		self.Save_ZAHON_MOD_func()
		self.GM_Detector_Logs.Hide()	

	def GM_Detector_PopUp_Close(self):
		self.GM_Detector_PopUp.Hide()			
		
	def Detector_Close(self):
		self.Save_ZAHON_MOD_func()
		self.Detector_Bar.SetPosition(50, 120)
		self.Detector_Bar.Hide()

	def Detector_List_Close(self):
		self.Save_ZAHON_MOD_func()
		self.Detector_List.Hide()
		
	def Detector_Options_Close(self):
		self.Save_ZAHON_MOD_func()
		self.Detector_Options.Hide()		
		
	def Teleport_Coordinates_Close(self):
		self.Save_ZAHON_MOD_func()
		self.Teleport_Bar.SetPosition(50, 120)
		self.Teleport_Bar.Hide()	

	def Other_Gui_Close(self):
		self.Other_Gui.SetPosition(50, 120)	
		self.Other_Gui.Hide()		
		
	def Options_Close(self):
		self.Save_ZAHON_MOD_func()
		self.Options.SetPosition(50, 120)
		self.Options.Hide()			
		
	def Restart_Options_Close(self):
		self.Restart_Options.Hide()		
		
	def Info_Screen_Close(self):
		global Info_Screen_Page
		
		if Info_Screen_Page == 2:
			self.Info_Screen_Bar.Hide()
			self.Info_Screen.Hide()
			self.Save_ZAHON_MOD_func()
		else:
			pass			
		
class Item_Clicker(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Item_Clicker = ui.BoardWithTitleBar()
		self.Item_Clicker.SetSize(148, 120)
		self.Item_Clicker.SetCenterPosition()
		self.Item_Clicker.AddFlag('movable')
		self.Item_Clicker.AddFlag('float')
		self.Item_Clicker.SetTitleName('Item Clicker')
		self.Item_Clicker.SetCloseEvent(self.Item_Clicker_Close)
		self.Item_Clicker.Show()
		self.__BuildKeyDict()
		self.comp = Component()

		### Too lTip ###		
		self.txttooltip = uiToolTip.ToolTip()
		self.txttooltip.Hide()				
					
		### HorizontalBars ###		
		self.Item_Clicker_HorizontalBar = self.comp.HorizontalBar(self.Item_Clicker , 10, 35, 128)
		self.Item_Clicker_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Item_Clicker_HorizontalBar, 'Wstaw przedmioty', 5, 0, 0xFFFFE3AD)			
						
		### Slots ###
		self.Item_Clicker_Item_1_Bar = ui.ExpandedImageBox()
		self.Item_Clicker_Item_1_Bar.SetParent(self.Item_Clicker)	
		self.Item_Clicker_Item_1_Bar.SetPosition(10, 55)
		self.Item_Clicker_Item_1_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Clicker_Item_1_Bar.OnMouseLeftButtonUp = lambda: self.Set_Item_Clicker_1()
		self.Item_Clicker_Item_1_Bar.Show()
				
		self.Item_Clicker_Item_1_Icon = ui.ExpandedImageBox()
		self.Item_Clicker_Item_1_Icon.SetParent(self.Item_Clicker_Item_1_Bar)
		self.Item_Clicker_Item_1_Icon.SetPosition(0, 0)
		self.Item_Clicker_Item_1_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Clicker_Item_1_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_Clicker_1()
		self.Item_Clicker_Item_1_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_Clicker_1()		
		self.Item_Clicker_Item_1_Icon.OnMouseOverIn = lambda: self.Item_Clicker_1_ShowTip()
		self.Item_Clicker_Item_1_Icon.OnMouseOverOut = lambda: self.Item_Clicker_HideTip()		
		self.Item_Clicker_Item_1_Icon.Show()		
	
		self.Item_Clicker_Item_2_Bar = ui.ExpandedImageBox()
		self.Item_Clicker_Item_2_Bar.SetParent(self.Item_Clicker)	
		self.Item_Clicker_Item_2_Bar.SetPosition(42, 55)
		self.Item_Clicker_Item_2_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Clicker_Item_2_Bar.OnMouseLeftButtonUp = lambda: self.Set_Item_Clicker_2()
		self.Item_Clicker_Item_2_Bar.Show()
				
		self.Item_Clicker_Item_2_Icon = ui.ExpandedImageBox()
		self.Item_Clicker_Item_2_Icon.SetParent(self.Item_Clicker_Item_2_Bar)
		self.Item_Clicker_Item_2_Icon.SetPosition(0, 0)
		self.Item_Clicker_Item_2_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Clicker_Item_2_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_Clicker_2()
		self.Item_Clicker_Item_2_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_Clicker_2()		
		self.Item_Clicker_Item_2_Icon.OnMouseOverIn = lambda: self.Item_Clicker_2_ShowTip()
		self.Item_Clicker_Item_2_Icon.OnMouseOverOut = lambda: self.Item_Clicker_HideTip()		
		self.Item_Clicker_Item_2_Icon.Show()	
		
		self.Item_Clicker_Item_3_Bar = ui.ExpandedImageBox()
		self.Item_Clicker_Item_3_Bar.SetParent(self.Item_Clicker)	
		self.Item_Clicker_Item_3_Bar.SetPosition(74, 55)
		self.Item_Clicker_Item_3_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Clicker_Item_3_Bar.OnMouseLeftButtonUp = lambda: self.Set_Item_Clicker_3()
		self.Item_Clicker_Item_3_Bar.Show()
				
		self.Item_Clicker_Item_3_Icon = ui.ExpandedImageBox()
		self.Item_Clicker_Item_3_Icon.SetParent(self.Item_Clicker_Item_3_Bar)
		self.Item_Clicker_Item_3_Icon.SetPosition(0, 0)
		self.Item_Clicker_Item_3_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Clicker_Item_3_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_Clicker_3()
		self.Item_Clicker_Item_3_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_Clicker_3()		
		self.Item_Clicker_Item_3_Icon.OnMouseOverIn = lambda: self.Item_Clicker_3_ShowTip()
		self.Item_Clicker_Item_3_Icon.OnMouseOverOut = lambda: self.Item_Clicker_HideTip()		
		self.Item_Clicker_Item_3_Icon.Show()			
	
		self.Item_Clicker_Item_4_Bar = ui.ExpandedImageBox()
		self.Item_Clicker_Item_4_Bar.SetParent(self.Item_Clicker)	
		self.Item_Clicker_Item_4_Bar.SetPosition(106, 55)
		self.Item_Clicker_Item_4_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Clicker_Item_4_Bar.OnMouseLeftButtonUp = lambda: self.Set_Item_Clicker_4()
		self.Item_Clicker_Item_4_Bar.Show()
				
		self.Item_Clicker_Item_4_Icon = ui.ExpandedImageBox()
		self.Item_Clicker_Item_4_Icon.SetParent(self.Item_Clicker_Item_4_Bar)
		self.Item_Clicker_Item_4_Icon.SetPosition(0, 0)
		self.Item_Clicker_Item_4_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Clicker_Item_4_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_Clicker_4()
		self.Item_Clicker_Item_4_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_Clicker_4()		
		self.Item_Clicker_Item_4_Icon.OnMouseOverIn = lambda: self.Item_Clicker_4_ShowTip()
		self.Item_Clicker_Item_4_Icon.OnMouseOverOut = lambda: self.Item_Clicker_HideTip()		
		self.Item_Clicker_Item_4_Icon.Show()	
	
		### Buttons ###
		self.Item_Clicker_Status_Button = self.comp.Button(self.Item_Clicker, 'Start', '', 30, 90, self.Item_Clicker_Status_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		
	#################################### Item Clicker Func  ##############################	
	
	### Set and Delete Item 1 ###
	def Set_Item_Clicker_1(self):
		global Item_Clicker_ID
		
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			Item_Clicker_ID[0] = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()

				chat.AppendChat(2,"Pomyœlnie dodano " + str(item.GetItemName()) + " o ID: " + str(attachedSlotVnum))					
				
				item.SelectItem(int(attachedSlotVnum))
				Item_Clicker_Item_1_Icon = item.GetIconImageFileName()
				self.Item_Clicker_Item_1_Icon.LoadImage(str(Item_Clicker_Item_1_Icon))
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")		
	
	def Delete_Item_Clicker_1(self):
		global Item_Clicker_ID	
		Item_Clicker_ID[0] = 0
		self.Item_Clicker_Item_1_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Clicker_HideTip()	

	### Set and Delete Item 2 ###		
	def Set_Item_Clicker_2(self):
		global Item_Clicker_ID
		
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			Item_Clicker_ID[1] = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()

				chat.AppendChat(2,"Pomyœlnie dodano " + str(item.GetItemName()) + " o ID: " + str(attachedSlotVnum))					
				
				item.SelectItem(int(attachedSlotVnum))
				Item_Clicker_Item_2_Icon = item.GetIconImageFileName()
				self.Item_Clicker_Item_2_Icon.LoadImage(str(Item_Clicker_Item_2_Icon))
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")		
	
	def Delete_Item_Clicker_2(self):
		global Item_Clicker_ID	
		Item_Clicker_ID[1] = 0
		self.Item_Clicker_Item_2_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Clicker_HideTip()				
	
	### Set and Delete Item 3 ###	
	def Set_Item_Clicker_3(self):
		global Item_Clicker_ID
		
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			Item_Clicker_ID[2] = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()

				chat.AppendChat(2,"Pomyœlnie dodano " + str(item.GetItemName()) + " o ID: " + str(attachedSlotVnum))					
				
				item.SelectItem(int(attachedSlotVnum))
				Item_Clicker_Item_3_Icon = item.GetIconImageFileName()
				self.Item_Clicker_Item_3_Icon.LoadImage(str(Item_Clicker_Item_3_Icon))
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")		
	
	def Delete_Item_Clicker_3(self):
		global Item_Clicker_ID	
		Item_Clicker_ID[2] = 0
		self.Item_Clicker_Item_3_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Clicker_HideTip()				
	
	### Set and Delete Item 4 ###	
	def Set_Item_Clicker_4(self):
		global Item_Clicker_ID
		
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			Item_Clicker_ID[3] = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()

				chat.AppendChat(2,"Pomyœlnie dodano " + str(item.GetItemName()) + " o ID: " + str(attachedSlotVnum))					
				
				item.SelectItem(int(attachedSlotVnum))
				Item_Clicker_Item_4_Icon = item.GetIconImageFileName()
				self.Item_Clicker_Item_4_Icon.LoadImage(str(Item_Clicker_Item_4_Icon))
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")		
	
	def Delete_Item_Clicker_4(self):
		global Item_Clicker_ID	
		Item_Clicker_ID[3] = 0
		self.Item_Clicker_Item_4_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Clicker_HideTip()					
	
	### Item Clicker Status ###
	def Item_Clicker_Status_func(self):
		global Item_Clicker_Status
		global Item_Clicker_ID
		if Item_Clicker_Status == 0:
			Item_Clicker_Status = 1	
			if Item_Clicker_ID[0] == 0 and Item_Clicker_ID[1] == 0 and Item_Clicker_ID[2] == 0 and Item_Clicker_ID[3] == 0:
				chat.AppendChat(2, "Najpierw wstaw przedmioty do otworzenia!")
			else:	
				self.Enable_Item_Clicker()
				chat.AppendChat(2, "Item Clicker Start!")
				self.Item_Clicker_Status_Button.SetText("Stop")
		else:
			Item_Clicker_Status = 0
			chat.AppendChat(2, "Item Clicker Stop!")
			self.Item_Clicker_Status_Button.SetText("Start")
	
	### Item Clicker Enable ###	
	def Enable_Item_Clicker(self):
		global Item_Clicker_Status
		global Item_Clicker_ID
	
		if Item_Clicker_Status == 1:
		
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_Clicker_Item_Index = player.GetItemIndex(i)
				if Item_Clicker_Item_Index == (int(Item_Clicker_ID[0])):
					net.SendItemUsePacket(i)	
					break				
			
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_Clicker_Item_Index = player.GetItemIndex(i)
				if Item_Clicker_Item_Index == (int(Item_Clicker_ID[1])):
					net.SendItemUsePacket(i)	
					break		
					
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_Clicker_Item_Index = player.GetItemIndex(i)
				if Item_Clicker_Item_Index == (int(Item_Clicker_ID[2])):
					net.SendItemUsePacket(i)	
					break		

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_Clicker_Item_Index = player.GetItemIndex(i)
				if Item_Clicker_Item_Index == (int(Item_Clicker_ID[3])):
					net.SendItemUsePacket(i)	
					break							
			
		self.Delay_Item_Clicker = WaitingDialog()
		self.Delay_Item_Clicker.Open(float(0.1))
		self.Delay_Item_Clicker.SAFE_SetTimeOverEvent(self.Enable_Item_Clicker)
			
	def Disable_Item_Clicker(self):	
		self.Delay_Item_Clicker = WaitingDialog()
		self.Delay_Item_Clicker.Open(float(99999999999999999))
		self.Delay_Item_Clicker.SAFE_SetTimeOverEvent(self.Disable_Item_Clicker)		
	
	### Item Clicker ToolTip ###		
	def Item_Clicker_1_ShowTip(self):
		
		global Item_Clicker_ID
		
		if Item_Clicker_ID[0] > 0:
		
			item.SelectItem(int(Item_Clicker_ID[0]))
		
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Item_Clicker_ID[0])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Item_Clicker_ID[0]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Item_Clicker_ID[0]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()			
	
	def Item_Clicker_2_ShowTip(self):
		
		global Item_Clicker_ID
		
		if Item_Clicker_ID[1] > 0:
		
			item.SelectItem(int(Item_Clicker_ID[1]))
		
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Item_Clicker_ID[1])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Item_Clicker_ID[1]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Item_Clicker_ID[1]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()		
	
	def Item_Clicker_3_ShowTip(self):
		
		global Item_Clicker_ID
		
		if Item_Clicker_ID[2] > 0:
		
			item.SelectItem(int(Item_Clicker_ID[2]))
		
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Item_Clicker_ID[2])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Item_Clicker_ID[2]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Item_Clicker_ID[2]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()			
	
	def Item_Clicker_4_ShowTip(self):
		
		global Item_Clicker_ID
		
		if Item_Clicker_ID[3] > 0:
		
			item.SelectItem(int(Item_Clicker_ID[3]))
		
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Item_Clicker_ID[3])), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Item_Clicker_ID[3]), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Item_Clicker_ID[3]))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()				
	
	def Item_Clicker_HideTip(self):
		self.txttooltip.ClearToolTip()
		self.txttooltip.Hide()			
	
	def OnUpdate(self):				
		pass
	
	def __BuildKeyDict(self):
		onPressKeyDict = {}
		onPressKeyDict[app.DIK_F5]	= lambda : self.OpenWindow()
		self.onPressKeyDict = onPressKeyDict
	
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
	
	def Item_Clicker_Close(self):
		self.Item_Clicker.Hide()		
	
class Buff_Bot(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Buff_Bot = ui.BoardWithTitleBar()
		self.Buff_Bot.SetSize(156, 126)
		self.Buff_Bot.SetCenterPosition()
		self.Buff_Bot.AddFlag('movable')
		self.Buff_Bot.AddFlag('float')
		self.Buff_Bot.SetTitleName('Buff Bot')
		self.Buff_Bot.SetCloseEvent(self.Buff_Bot_Close)
		self.Buff_Bot.Show()
		self.__BuildKeyDict()
		self.comp = Component()
		
		### Too lTip ###
		self.txttooltip = uiToolTip.ToolTip()	
		self.txttooltip.Hide()			
			
		### HorizontalBars ###		
		self.Buff_Bot_Info_HorizontalBar = self.comp.HorizontalBar(self.Buff_Bot , 10, 35, 136)
		self.Buff_Bot_Info_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Buff_Bot_Info_HorizontalBar, 'Wybierz Skille', 5, 0, 0xFFFFE3AD)			
					
		### Img ###
		self.Buff_Bot_Skill_1_img = self.comp.ExpandedImage(self.Buff_Bot , 15, 60, 'd:/ymir work/ui/skill/shaman/gicheon_01.sub')	
		self.Buff_Bot_Skill_2_img = self.comp.ExpandedImage(self.Buff_Bot , 62, 60, 'd:/ymir work/ui/skill/shaman/hosin_01.sub')	
		self.Buff_Bot_Skill_3_img = self.comp.ExpandedImage(self.Buff_Bot , 109, 60, 'd:/ymir work/ui/skill/shaman/boho_01.sub')	
				
		### Buttons ###
		self.Buff_Bot_Skill_1_Button = self.comp.Button(self.Buff_Bot, '', '', 15, 60, self.Buff_Bot_Skill_1_func, 'ZAHON_MOD/Icons/ETC/Empty_Slot.tga', 'ZAHON_MOD/Icons/ETC/Empty_Slot.tga', 'ZAHON_MOD/Icons/ETC/Empty_Slot.tga')
		self.Buff_Bot_Skill_2_Button = self.comp.Button(self.Buff_Bot, '', '', 62, 60, self.Buff_Bot_Skill_2_func, 'ZAHON_MOD/Icons/ETC/Empty_Slot.tga', 'ZAHON_MOD/Icons/ETC/Empty_Slot.tga', 'ZAHON_MOD/Icons/ETC/Empty_Slot.tga')
		self.Buff_Bot_Skill_3_Button = self.comp.Button(self.Buff_Bot, '', '', 109, 60, self.Buff_Bot_Skill_3_func, 'ZAHON_MOD/Icons/ETC/Empty_Slot.tga', 'ZAHON_MOD/Icons/ETC/Empty_Slot.tga', 'ZAHON_MOD/Icons/ETC/Empty_Slot.tga')
	
		self.Buff_Bot_Target_Button = self.comp.Button(self.Buff_Bot, 'Cel', '', 15, 95, self.Buff_Bot_Target_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.Buff_Bot_Status_Button = self.comp.Button(self.Buff_Bot, 'Start', '', 80, 95, self.Buff_Bot_Status_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		
	### Buff Bot Skill 1 Status ###
	def Buff_Bot_Skill_1_func(self):
		global Buff_Bot_Skill_1
		if Buff_Bot_Skill_1 == 0:
			Buff_Bot_Skill_1 = 1
			chat.AppendChat(2, "Ten Skill bêdzie u¿ywany!")
			self.Buff_Bot_Skill_1_Button.SetUpVisual("ZAHON_MOD/Buttons/ETC/On_Button.tga")
			self.Buff_Bot_Skill_1_Button.SetOverVisual("ZAHON_MOD/Buttons/ETC/On_Button.tga")
			self.Buff_Bot_Skill_1_Button.SetDownVisual("ZAHON_MOD/Buttons/ETC/On_Button.tga")
		else:
			Buff_Bot_Skill_1 = 0
			chat.AppendChat(2, "Ten Skill nie bêdzie u¿ywany!")
			self.Buff_Bot_Skill_1_Button.SetUpVisual("ZAHON_MOD/Buttons/ETC/Off_Button.tga")
			self.Buff_Bot_Skill_1_Button.SetOverVisual("ZAHON_MOD/Buttons/ETC/Off_Button.tga")
			self.Buff_Bot_Skill_1_Button.SetDownVisual("ZAHON_MOD/Buttons/ETC/Off_Button.tga")
	
	### Buff Bot Skill 2 Status ###	
	def Buff_Bot_Skill_2_func(self):
		global Buff_Bot_Skill_2
		if Buff_Bot_Skill_2 == 0:
			Buff_Bot_Skill_2 = 1
			chat.AppendChat(2, "Ten Skill bêdzie u¿ywany!")
			self.Buff_Bot_Skill_2_Button.SetUpVisual("ZAHON_MOD/Buttons/ETC/On_Button.tga")
			self.Buff_Bot_Skill_2_Button.SetOverVisual("ZAHON_MOD/Buttons/ETC/On_Button.tga")
			self.Buff_Bot_Skill_2_Button.SetDownVisual("ZAHON_MOD/Buttons/ETC/On_Button.tga")
		else:
			Buff_Bot_Skill_2 = 0
			chat.AppendChat(2, "Ten Skill nie bêdzie u¿ywany!")
			self.Buff_Bot_Skill_2_Button.SetUpVisual("ZAHON_MOD/Buttons/ETC/Off_Button.tga")
			self.Buff_Bot_Skill_2_Button.SetOverVisual("ZAHON_MOD/Buttons/ETC/Off_Button.tga")
			self.Buff_Bot_Skill_2_Button.SetDownVisual("ZAHON_MOD/Buttons/ETC/Off_Button.tga")
	
	### Buff Bot Skill 3 Status ###
	def Buff_Bot_Skill_3_func(self):
		global Buff_Bot_Skill_3
		if Buff_Bot_Skill_3 == 0:
			Buff_Bot_Skill_3 = 1
			chat.AppendChat(2, "Ten Skill bêdzie u¿ywany!")
			self.Buff_Bot_Skill_3_Button.SetUpVisual("ZAHON_MOD/Buttons/ETC/On_Button.tga")
			self.Buff_Bot_Skill_3_Button.SetOverVisual("ZAHON_MOD/Buttons/ETC/On_Button.tga")
			self.Buff_Bot_Skill_3_Button.SetDownVisual("ZAHON_MOD/Buttons/ETC/On_Button.tga")
		else:
			Buff_Bot_Skill_3 = 0
			chat.AppendChat(2, "Ten Skill nie bêdzie u¿ywany!")
			self.Buff_Bot_Skill_3_Button.SetUpVisual("ZAHON_MOD/Buttons/ETC/Off_Button.tga")
			self.Buff_Bot_Skill_3_Button.SetOverVisual("ZAHON_MOD/Buttons/ETC/Off_Button.tga")
			self.Buff_Bot_Skill_3_Button.SetDownVisual("ZAHON_MOD/Buttons/ETC/Off_Button.tga")		
		
	def Buff_Bot_Target_func(self):
		global Buff_Bot_Target_VID
		Buff_Bot_Target_VID = player.GetTargetVID()
		NickName = chr.GetNameByVID(Buff_Bot_Target_VID)
		chat.AppendChat(2, "Ustalono Cel: " + str(NickName) + " VID: " + str(Buff_Bot_Target_VID))
		
	def Buff_Bot_Status_func(self):
		global Buff_Bot_Status, Buff_Bot_Target_VID
		
		if Buff_Bot_Target_VID == 0:
			chat.AppendChat(2, "Najpierw ustal cel!")
		else:	
			if Buff_Bot_Status == 0:
				Buff_Bot_Status = 1
				self.Enable_Buff_Bot_Skill_1()			
				self.Enable_Buff_Bot_Skill_2()			
				self.Enable_Buff_Bot_Skill_3()			
				chat.AppendChat(2, "Buff Bot Start")	
				self.Buff_Bot_Status_Button.SetText("Stop")		
			else:	
				Buff_Bot_Status = 0
				self.Disable_Buff_Bot()				
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Buff Bot Stop")	
				self.Buff_Bot_Status_Button.SetText("Start")
	
	def Enable_Buff_Bot_Skill_1(self):
		global Buff_Bot_Skill_1, Buff_Bot_Type, Buff_Bot_Target_VID
	
		player.SetTarget(int(Buff_Bot_Target_VID))
		player.OpenCharacterMenu(int(Buff_Bot_Target_VID))	
	
		if Buff_Bot_Skill_1 == 1:
			if Buff_Bot_Type == 1:
				player.ClickSkillSlot(6)			
			
			if Buff_Bot_Type == 2:
				player.ClickSkillSlot(5)
	
		self.Delay_Buff_Bot_Skill_1 = WaitingDialog()
		self.Delay_Buff_Bot_Skill_1.Open(int(5))
		self.Delay_Buff_Bot_Skill_1.SAFE_SetTimeOverEvent(self.Enable_Buff_Bot_Skill_1)	
	
	def Enable_Buff_Bot_Skill_2(self):
		global Buff_Bot_Skill_2, Buff_Bot_Type, Buff_Bot_Target_VID
	
		player.SetTarget(int(Buff_Bot_Target_VID))
		player.OpenCharacterMenu(int(Buff_Bot_Target_VID))	
	
		if Buff_Bot_Skill_2 == 1:
			if Buff_Bot_Type == 1:
				player.ClickSkillSlot(4)			
			
			if Buff_Bot_Type == 2:
				player.ClickSkillSlot(6)
	
		self.Delay_Buff_Bot_Skill_2 = WaitingDialog()
		self.Delay_Buff_Bot_Skill_2.Open(int(5))
		self.Delay_Buff_Bot_Skill_2.SAFE_SetTimeOverEvent(self.Enable_Buff_Bot_Skill_2)		
	
	def Enable_Buff_Bot_Skill_3(self):
		global Buff_Bot_Skill_3, Buff_Bot_Type, Buff_Bot_Target_VID
	
		player.SetTarget(int(Buff_Bot_Target_VID))
		player.OpenCharacterMenu(int(Buff_Bot_Target_VID))	
	
		if Buff_Bot_Skill_3 == 1:
			if Buff_Bot_Type == 1:
				player.ClickSkillSlot(5)			
			
			if Buff_Bot_Type == 2:
				pass
	
		self.Delay_Buff_Bot_Skill_3 = WaitingDialog()
		self.Delay_Buff_Bot_Skill_3.Open(int(5))
		self.Delay_Buff_Bot_Skill_3.SAFE_SetTimeOverEvent(self.Enable_Buff_Bot_Skill_3)		
	
	### Buff Bot Disable ###
	def Disable_Buff_Bot(self):
	
		self.Delay_Buff_Bot_Skill_1 = WaitingDialog()
		self.Delay_Buff_Bot_Skill_1.Open(float(99999999999999999))
		self.Delay_Buff_Bot_Skill_1.SAFE_SetTimeOverEvent(self.Disable_Buff_Bot)			
		
		self.Delay_Buff_Bot_Skill_2 = WaitingDialog()
		self.Delay_Buff_Bot_Skill_2.Open(float(99999999999999999))
		self.Delay_Buff_Bot_Skill_2.SAFE_SetTimeOverEvent(self.Disable_Buff_Bot)	

		self.Delay_Buff_Bot_Skill_3 = WaitingDialog()
		self.Delay_Buff_Bot_Skill_3.Open(float(99999999999999999))
		self.Delay_Buff_Bot_Skill_3.SAFE_SetTimeOverEvent(self.Disable_Buff_Bot)		
		
	def OnUpdate(self):			
		global Buff_Bot_Type
		
		### Sprawdzanie Race i Group ###
		
		#global Race, Group
		
		Race = net.GetMainActorRace()	
		Group = net.GetMainActorSkillGroup()			
	
		### Szaman Smok ###
		if (Race == 3 and Group == 1) or (Race == 7 and Group == 1):
				
			Buff_Bot_Type = 1	
				
			self.Buff_Bot_Skill_1_img.SetPosition(15,58)
			self.Buff_Bot_Skill_2_img.SetPosition(62,58)
			self.Buff_Bot_Skill_3_img.SetPosition(109,58)
			self.Buff_Bot_Skill_3_img.Show()
		
			self.Buff_Bot_Skill_1_Button.SetPosition(15,60)
			self.Buff_Bot_Skill_2_Button.SetPosition(62,60)	
			self.Buff_Bot_Skill_3_Button.SetPosition(109,60)
			self.Buff_Bot_Skill_3_Button.Show()	
			
			Buff_Bot_Skill_1_Grade = player.GetSkillGrade(6)			
			
			if Buff_Bot_Skill_1_Grade == 0:
				self.Buff_Bot_Skill_1_img.LoadImage("d:/ymir work/ui/skill/shaman/gicheon_01.sub")	
	
			if Buff_Bot_Skill_1_Grade == 1:
				self.Buff_Bot_Skill_1_img.LoadImage("d:/ymir work/ui/skill/shaman/gicheon_02.sub")	
				
			if Buff_Bot_Skill_1_Grade == 2:
				self.Buff_Bot_Skill_1_img.LoadImage("d:/ymir work/ui/skill/shaman/gicheon_03.sub")	

			if Buff_Bot_Skill_1_Grade == 3:
				self.Buff_Bot_Skill_1_img.LoadImage("d:/ymir work/ui/skill/shaman/gicheon_03.sub")		

			Buff_Bot_Skill_2_Grade = player.GetSkillGrade(4)			
			
			if Buff_Bot_Skill_2_Grade == 0:
				self.Buff_Bot_Skill_2_img.LoadImage("d:/ymir work/ui/skill/shaman/hosin_01.sub")	
	
			if Buff_Bot_Skill_2_Grade == 1:
				self.Buff_Bot_Skill_2_img.LoadImage("d:/ymir work/ui/skill/shaman/hosin_02.sub")	
				
			if Buff_Bot_Skill_2_Grade == 2:
				self.Buff_Bot_Skill_2_img.LoadImage("d:/ymir work/ui/skill/shaman/hosin_03.sub")	

			if Buff_Bot_Skill_2_Grade == 3:
				self.Buff_Bot_Skill_2_img.LoadImage("d:/ymir work/ui/skill/shaman/hosin_03.sub")		

			Buff_Bot_Skill_3_Grade = player.GetSkillGrade(5)			
			
			if Buff_Bot_Skill_3_Grade == 0:
				self.Buff_Bot_Skill_3_img.LoadImage("d:/ymir work/ui/skill/shaman/boho_01.sub")	
	
			if Buff_Bot_Skill_3_Grade == 1:
				self.Buff_Bot_Skill_3_img.LoadImage("d:/ymir work/ui/skill/shaman/boho_02.sub")	
				
			if Buff_Bot_Skill_3_Grade == 2:
				self.Buff_Bot_Skill_3_img.LoadImage("d:/ymir work/ui/skill/shaman/boho_03.sub")	

			if Buff_Bot_Skill_3_Grade == 3:
				self.Buff_Bot_Skill_3_img.LoadImage("d:/ymir work/ui/skill/shaman/boho_03.sub")					
	
		### Szaman Leczenie ###
		if (Race == 3 and Group == 2) or (Race == 7 and Group == 2):

			Buff_Bot_Type = 2
		
			self.Buff_Bot_Skill_1_img.SetPosition(28,60)
			self.Buff_Bot_Skill_2_img.SetPosition(95,60)
			self.Buff_Bot_Skill_3_img.Hide()			
		
			self.Buff_Bot_Skill_1_Button.SetPosition(28,60)
			self.Buff_Bot_Skill_2_Button.SetPosition(95,60)	
			self.Buff_Bot_Skill_3_Button.Hide()		
			
			Buff_Bot_Skill_1_Grade = player.GetSkillGrade(5)			
			
			if Buff_Bot_Skill_1_Grade == 0:
				self.Buff_Bot_Skill_1_img.LoadImage("d:/ymir work/ui/skill/shaman/kwaesok_01.sub")	
	
			if Buff_Bot_Skill_1_Grade == 1:
				self.Buff_Bot_Skill_1_img.LoadImage("d:/ymir work/ui/skill/shaman/kwaesok_02.sub")	
				
			if Buff_Bot_Skill_1_Grade == 2:
				self.Buff_Bot_Skill_1_img.LoadImage("d:/ymir work/ui/skill/shaman/kwaesok_03.sub")	

			if Buff_Bot_Skill_1_Grade == 3:
				self.Buff_Bot_Skill_1_img.LoadImage("d:/ymir work/ui/skill/shaman/kwaesok_03.sub")		

			Buff_Bot_Skill_2_Grade = player.GetSkillGrade(6)			
			
			if Buff_Bot_Skill_2_Grade == 0:
				self.Buff_Bot_Skill_2_img.LoadImage("d:/ymir work/ui/skill/shaman/jeungryeok_01.sub")	
	
			if Buff_Bot_Skill_2_Grade == 1:
				self.Buff_Bot_Skill_2_img.LoadImage("d:/ymir work/ui/skill/shaman/jeungryeok_02.sub")	
				
			if Buff_Bot_Skill_2_Grade == 2:
				self.Buff_Bot_Skill_2_img.LoadImage("d:/ymir work/ui/skill/shaman/jeungryeok_03.sub")	

			if Buff_Bot_Skill_2_Grade == 3:
				self.Buff_Bot_Skill_2_img.LoadImage("d:/ymir work/ui/skill/shaman/jeungryeok_03.sub")						
	
		
	def __BuildKeyDict(self):
		onPressKeyDict = {}
		onPressKeyDict[app.DIK_F5]	= lambda : self.OpenWindow()
		self.onPressKeyDict = onPressKeyDict
	
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
	
	def Buff_Bot_Close(self):
		self.Buff_Bot.Hide()
	
class Yang_Bug(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()
		self.Yang_Bug_Check_Actually_Time()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):			
		self.Yang_Bug = ui.BoardWithTitleBar()
		self.Yang_Bug.SetSize(220, 260)
		self.Yang_Bug.SetCenterPosition()
		self.Yang_Bug.AddFlag('movable')
		self.Yang_Bug.AddFlag('float')
		self.Yang_Bug.SetTitleName('Yang Bug')
		self.Yang_Bug.SetCloseEvent(self.Yang_Bug_Close)
		self.Yang_Bug.Show()		
		
		self.__BuildKeyDict()
		self.comp = Component()
				
		### Too lTip ###
		self.txttooltip = uiToolTip.ToolTip()	
		self.txttooltip.Hide()			
			
		### HorizontalBars ###
		self.Yang_Bug_Info_HorizontalBar = self.comp.HorizontalBar(self.Yang_Bug , 10, 39, 200)
		self.Yang_Bug_Info_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Yang_Bug_Info_HorizontalBar, 'Lista przedmiotów w sklepie', 5, 0, 0xFFFFE3AD)			
				
		### Buttons ###
		self.Yang_Bug_Question_Button = ui.ExpandedImageBox()
		self.Yang_Bug_Question_Button.SetParent(self.Yang_Bug)
		self.Yang_Bug_Question_Button.SetPosition(152, 9)
		self.Yang_Bug_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_01.tga")
		self.Yang_Bug_Question_Button.OnMouseOverIn = lambda: self.Yang_Bug_ShowTip()
		self.Yang_Bug_Question_Button.OnMouseOverOut = lambda: self.Yang_Bug_HideTip()
		self.Yang_Bug_Question_Button.Show()
		
		self.Yang_Bug_Refresh_Button = self.comp.Button(self.Yang_Bug, '', 'Odœwie¿ Listê', 190, 38, self.Yang_Bug_Refresh_func, 'd:/ymir work/ui/game/guild/Refresh_Button_01.sub', 'd:/ymir work/ui/game/guild/Refresh_Button_02.sub', 'd:/ymir work/ui/game/guild/Refresh_Button_03.sub')
		self.Yang_Bug_Status_Button = self.comp.Button(self.Yang_Bug, 'Start', '', 120, 229, self.Yang_Bug_Status_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Yang_Bug_Test_Item_Button = self.comp.Button(self.Yang_Bug, '', 'Test Item', 170, 8, self.Yang_Bug_Test_Item_func, 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_01.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_02.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_03.sub')		
		
		### Text ###				
		self.Yang_Bug_Delay_Text = self.comp.TextLine(self.Yang_Bug, 'Szybkoœæ:', 15, 231, self.comp.RGB(255, 255, 255))		

		### EditLine ###
		self.slotbar_Yang_Bug_Delay, self.Yang_Bug_Delay_EditLine = self.comp.EditLine(self.Yang_Bug, '0.1', 75, 230, 30, 15, 3)
			
		### List Box ###				
		self.bar_Yang_Bug_List, self.Yang_Bug_List = self.comp.ListBoxEx(self.Yang_Bug, 10, 60, 200, 160)
		
	### Yang Bug Refresh List ###	
	def Yang_Bug_Refresh_func(self):
		if not shop.IsOpen():
			chat.AppendChat(2, "Najpierw otwórz sklep!")
			return

		self.Yang_Bug_List.RemoveAllItems()
		for i in xrange(shop.SHOP_SLOT_COUNT):
			ItemIndex = shop.GetItemID(i)
			if ItemIndex != 0:
				ItemName = item.GetItemName(item.SelectItem(int(ItemIndex)))
				self.Yang_Bug_List.AppendItem(Item(str(ItemIndex) + '    ' + ItemName))
		
	### Yang Bug Status ###			
	def Yang_Bug_Status_func(self):

		ItemIndex = self.Yang_Bug_List.GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(2, "Nie zaznaczono przedmiotu!")
			return
			
		if not shop.IsOpen():
			chat.AppendChat(2, "Najpierw otwórz sklep!")
			return			
	
		global Yang_Bug_Status
		global Yang_Bug_Item_ID
		
		if Yang_Bug_Status == 0:
			Yang_Bug_Status = 1
			self.Enable_Yang_Bug()
			self.Yang_Bug_Status_Button.SetText("Stop")	
			Yang_Bug_Item_ID = int(ItemIndex.GetText().split("    ")[0])
			chat.AppendChat(2, str(Yang_Bug_Item_ID))
		else:
			Yang_Bug_Status = 0
			self.Disable_Yang_Bug()
			self.Yang_Bug_Status_Button.SetText("Start")	
		
	### Yang Bug Enable ###		
	def Enable_Yang_Bug(self):
		
		global Yang_Bug_Status 
		global Yang_Bug_Item_ID 		
		
		Yang_Bug_Delay = self.Yang_Bug_Delay_EditLine.GetText()	
		
		for i in xrange(int(2)):
			for eachSlot in xrange(shop.SHOP_SLOT_COUNT):
				getShopItemID = shop.GetItemID(eachSlot)
				if getShopItemID == int(Yang_Bug_Item_ID):
						net.SendShopBuyPacket(eachSlot)		
			
						for EachInventorySlot in xrange(90): 
							ItemIndex = player.GetItemIndex(EachInventorySlot) 
							if ItemIndex == int(Yang_Bug_Item_ID): 
								net.SendShopSellPacket(EachInventorySlot) 	
			
		self.Delay_Yang_Bug = WaitingDialog()
		self.Delay_Yang_Bug.Open(float(Yang_Bug_Delay))
		self.Delay_Yang_Bug.SAFE_SetTimeOverEvent(self.Enable_Yang_Bug)		
		
	### Yang Bug Disable ###			
	def Disable_Yang_Bug(self):
		
		self.Delay_Yang_Bug = WaitingDialog()
		self.Delay_Yang_Bug.Open(float(99999999999999999))
		self.Delay_Yang_Bug.SAFE_SetTimeOverEvent(self.Disable_Yang_Bug)
		
	### Yang Bug Buy Item ###		
	def Yang_Bug_Buy_Item(self):
		global Yang_Bug_Item_ID
		global Yang_Bug_Past_Yang
		
		ItemIndex = self.Yang_Bug_List.GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(2, "Nie zaznaczono przedmiotu!")
			return
			
		if not shop.IsOpen():
			chat.AppendChat(2, "Najpierw otwórz sklep!")
			return	
		
		Yang_Bug_Item_ID = int(ItemIndex.GetText().split("    ")[0])
		chat.AppendChat(2, str(Yang_Bug_Item_ID))		
		
		Yang_Bug_Past_Yang = player.GetStatus(player.ELK)
		
		for eachSlot in xrange(shop.SHOP_SLOT_COUNT):
			getShopItemID = shop.GetItemID(eachSlot)
			if getShopItemID == int(Yang_Bug_Item_ID):
					net.SendShopBuyPacket(eachSlot)		
		
					for EachInventorySlot in xrange(90): 
						ItemIndex = player.GetItemIndex(EachInventorySlot) 
						if ItemIndex == int(Yang_Bug_Item_ID): 
							net.SendShopSellPacket(EachInventorySlot) 			

							self.Yang_Bug_Set_Check_Time()
							
	### Yang Bug Sell Item ###		
	def Yang_Bug_Sell_Item(self):
		global Yang_Bug_Item_ID
		for EachInventorySlot in xrange(90): 
			ItemIndex = player.GetItemIndex(EachInventorySlot) 
			if ItemIndex == int(Yang_Bug_Item_ID): 
				net.SendShopSellPacket(EachInventorySlot) 		
		
	### Yang Bug Test Item ###
	def Yang_Bug_Test_Item_func(self):
		self.Yang_Bug_Buy_Item()
	
	### Yang Bug Set Check Time ###
	def Yang_Bug_Set_Check_Time(self):
		global Yang_Bug_Check_Time
		
		Actually_Time = int(app.GetTime())
		Yang_Bug_Check_Time = int(int(Actually_Time) + 1)
		
	### Yang Bug Check Actually Time ###
	def Yang_Bug_Check_Actually_Time(self):	
		global Yang_Bug_Check_Time
		global Yang_Bug_Past_Yang
		
		Actually_Time = int(app.GetTime())
		
		if Actually_Time == int(Yang_Bug_Check_Time):
			Yang_Bug_Past_Actually_Yang = player.GetStatus(player.ELK)
			
			if Yang_Bug_Past_Yang > Yang_Bug_Past_Actually_Yang:
				chat.AppendChat(1, "Na ten przedmiot nie ma buga!")
			else:
				chat.AppendChat(7, "Na ten przedmiot dzia³a buga!")
				
		
		self.Delay_Yang_Bug_Check_Actually_Time = WaitingDialog()
		self.Delay_Yang_Bug_Check_Actually_Time.Open(int(1))
		self.Delay_Yang_Bug_Check_Actually_Time.SAFE_SetTimeOverEvent(self.Yang_Bug_Check_Actually_Time)			
			
	### Yang Bug Show ShowTip ###
	def Yang_Bug_ShowTip(self):
		
		self.txttooltip.ClearToolTip()
		self.txttooltip.AppendTextLine("Yang Bug 1.1", grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 		
		self.txttooltip.AppendTextLine("Bug polega na kupowaniu itemu", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))  
		self.txttooltip.AppendTextLine("a nastêpnie sprzedawaniu z zyskiem", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))  
		self.txttooltip.AppendTextLine("[Nie dzia³a na wiêkszoœci serwerów]", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.Show()
		
		self.Yang_Bug_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_02.tga")
	
	### Yang Bug Show HideTip ###	
	def Yang_Bug_HideTip(self):
	
		self.Yang_Bug_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_01.tga")
		self.txttooltip.ClearToolTip()
		self.txttooltip.Hide()	
		
	def OnUpdate(self):			
		pass
	
	def __BuildKeyDict(self):
		onPressKeyDict = {}
		onPressKeyDict[app.DIK_F5]	= lambda : self.OpenWindow()
		self.onPressKeyDict = onPressKeyDict
	
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
	
	def Yang_Bug_Close(self):
		self.Yang_Bug.Hide()	
	
class Book_Reader(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Book_Reader = ui.BoardWithTitleBar()
		self.Book_Reader.SetSize(160, 185)
		self.Book_Reader.SetCenterPosition()
		self.Book_Reader.AddFlag('movable')
		self.Book_Reader.AddFlag('float')
		self.Book_Reader.SetTitleName('Book Reader')
		self.Book_Reader.SetCloseEvent(self.Book_Reader_Close)
		self.Book_Reader.Show()
		self.__BuildKeyDict()
		self.comp = Component()
		
		### Too lTip ###
		self.txttooltip = uiToolTip.ToolTip()
		self.txttooltip.Hide()				
		
		### Thin Board ###
		self.Book_Reader_ThinBoard = self.comp.ThinBoard(self.Book_Reader, FALSE, 10, 35, 140, 70, FALSE)			
		
		### Slots ###
		self.Book_Reader_Item_Bar = ui.ExpandedImageBox()
		self.Book_Reader_Item_Bar.SetParent(self.Book_Reader_ThinBoard)	
		self.Book_Reader_Item_Bar.SetPosition(54, 19)
		self.Book_Reader_Item_Bar.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Book_Reader_Item_Bar.OnMouseLeftButtonUp = lambda: self.Set_Book_Reader_Item()
		self.Book_Reader_Item_Bar.Show()
				
		self.Book_Reader_Item_Icon = ui.ExpandedImageBox()
		self.Book_Reader_Item_Icon.SetParent(self.Book_Reader_Item_Bar)
		self.Book_Reader_Item_Icon.SetPosition(0, 0)
		self.Book_Reader_Item_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Book_Reader_Item_Icon.OnMouseLeftButtonUp = lambda: self.Set_Book_Reader_Item()
		self.Book_Reader_Item_Icon.OnMouseRightButtonDown = lambda: self.Delete_Book_Reader_Item()		
		self.Book_Reader_Item_Icon.OnMouseOverIn = lambda: self.Book_Reader_ShowTip()
		self.Book_Reader_Item_Icon.OnMouseOverOut = lambda: self.Book_Reader_HideTip()		
		self.Book_Reader_Item_Icon.Show()			
		
		### Buttons ###
		self.Book_Reader_Egzo_Button = self.comp.Button(self.Book_Reader, '', 'U¿ywaj Zwojów Egzorcyzmu', 20, 110, self.Book_Reader_Egzo_func, 'ZAHON_MOD/Buttons/Other/Book_Reader/Egzo_On.tga', 'ZAHON_MOD/Buttons/Other/Book_Reader/Egzo_On.tga', 'ZAHON_MOD/Buttons/Other/Book_Reader/Egzo_On.tga')
		self.Book_Reader_Rada_Button = self.comp.Button(self.Book_Reader, '', 'U¿ywaj Rad Pustelnika', 62, 110, self.Book_Reader_Rada_func, 'ZAHON_MOD/Buttons/Other/Book_Reader/Rada_On.tga', 'ZAHON_MOD/Buttons/Other/Book_Reader/Rada_On.tga', 'ZAHON_MOD/Buttons/Other/Book_Reader/Rada_On.tga')
		self.Book_Reader_Buy_Button = self.comp.Button(self.Book_Reader, '', 'Kupuj ksi¹¿ki w sklepie', 104, 110, self.Book_Reader_Buy_func, 'ZAHON_MOD/Buttons/Other/Book_Reader/Buy_On.tga', 'ZAHON_MOD/Buttons/Other/Book_Reader/Buy_On.tga', 'ZAHON_MOD/Buttons/Other/Book_Reader/Buy_On.tga')
	
		self.Book_Reader_Status_Button = self.comp.Button(self.Book_Reader, 'Start', '', 36, 152, self.Book_Reader_Status_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		
	### Book Reader Set Item ###
	def Set_Book_Reader_Item(self):
		global Book_Reader_Book_ID
		
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
					
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				
				Book_Reader_Book_ID = mouseModule.mouseController.GetAttachedItemIndex()				
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano " + str(item.GetItemName()) + " o ID: " + str(attachedSlotVnum))					
				
				item.SelectItem(int(attachedSlotVnum))
				Book_Reader_Item_Icon = item.GetIconImageFileName()
				self.Book_Reader_Item_Icon.LoadImage(str(Book_Reader_Item_Icon))
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")		
	
	### Book Reader Delete Item ###
	def Delete_Book_Reader_Item(self):
		global Book_Reader_Book_ID	
		Book_Reader_Book_ID = 0
		self.Book_Reader_HideTip()
		self.Book_Reader_Item_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
	
	### Book Reader Egzo func ###	
	def Book_Reader_Egzo_func(self):
		global Book_Reader_Egzo
		if Book_Reader_Egzo == 1:
			Book_Reader_Egzo = 0
			chat.AppendChat(2, "Zwój Egzorcyzmu nie bêdzie u¿ywany!")
			self.Book_Reader_Egzo_Button.SetUpVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Egzo_Off.tga")
			self.Book_Reader_Egzo_Button.SetOverVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Egzo_Off.tga")
			self.Book_Reader_Egzo_Button.SetDownVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Egzo_Off.tga")
		else:
			Book_Reader_Egzo = 1
			chat.AppendChat(2, "Zwój Egzorcyzmu bêdzie u¿ywany!")
			self.Book_Reader_Egzo_Button.SetUpVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Egzo_On.tga")
			self.Book_Reader_Egzo_Button.SetOverVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Egzo_On.tga")
			self.Book_Reader_Egzo_Button.SetDownVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Egzo_On.tga")
	
	### Book Reader Rada func ###		
	def Book_Reader_Rada_func(self):
		global Book_Reader_Rada
		if Book_Reader_Rada == 1:
			Book_Reader_Rada = 0
			chat.AppendChat(2, "Rada Pustelnika nie bêdzie u¿ywana!")
			self.Book_Reader_Rada_Button.SetUpVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Rada_Off.tga")
			self.Book_Reader_Rada_Button.SetOverVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Rada_Off.tga")
			self.Book_Reader_Rada_Button.SetDownVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Rada_Off.tga")
		else:
			Book_Reader_Rada = 1
			chat.AppendChat(2, "Rada Pustelnika bêdzie u¿ywana!")
			self.Book_Reader_Rada_Button.SetUpVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Rada_On.tga")
			self.Book_Reader_Rada_Button.SetOverVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Rada_On.tga")
			self.Book_Reader_Rada_Button.SetDownVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Rada_On.tga")
	
	### Book Reader Buy func ###		
	def Book_Reader_Buy_func(self):
		global Book_Reader_Buy
		if Book_Reader_Buy == 1:
			Book_Reader_Buy = 0
			chat.AppendChat(2, "Ksi¹¿ki nie bêd¹ kupowane ze sklepu!")
			self.Book_Reader_Rada_Button.SetUpVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Buy_Off.tga")
			self.Book_Reader_Rada_Button.SetOverVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Buy_Off.tga")
			self.Book_Reader_Rada_Button.SetDownVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Buy_Off.tga")
		else:
			Book_Reader_Buy = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Ksi¹¿ki bêd¹ kupowane ze sklepu!")
			self.Book_Reader_Rada_Button.SetUpVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Buy_On.tga")
			self.Book_Reader_Rada_Button.SetOverVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Buy_On.tga")
			self.Book_Reader_Rada_Button.SetDownVisual("ZAHON_MOD/Buttons/Other/Book_Reader/Buy_On.tga")
	
	### Book Reader Status ###
	def Book_Reader_Status_func(self):
		global Book_Reader_Status
		
		if Book_Reader_Status == 0:
			Book_Reader_Status = 1
			self.Enable_Book_Reader()
			self.Book_Reader_Status_Button.SetText("Stop")
		else:
			Book_Reader_Status = 0
			self.Book_Reader_Status_Button.SetText("Start")	
	
	### Book Reader Enable ###
	def Enable_Book_Reader(self):	
		global Book_Reader_Status
	
		if Book_Reader_Status == 1:
			self.Book_Reader_Read()	
	
		self.Delay_Book_Reader = WaitingDialog()
		self.Delay_Book_Reader.Open(float(0.1))
		self.Delay_Book_Reader.SAFE_SetTimeOverEvent(self.Enable_Book_Reader)	
	
	### Book Reader Read ###
	def Book_Reader_Read(self):
		global Book_Reader_Status
		global Book_Reader_Book_ID
		
		if Book_Reader_Book_ID == 0:
			Book_Reader_Status = 0
			self.Book_Reader_Status_Button.SetText("Start")	
			chat.AppendChat(2, "Najpierw wstaw ksia¿kê aby pobraæ jej ID!")
		else:
			
			### Buy ###
			if Book_Reader_Buy == 1:
				for eachSlot in xrange(shop.SHOP_SLOT_COUNT):
					getShopItemID = shop.GetItemID(eachSlot)
					if getShopItemID == int(Book_Reader_Book_ID):
							net.SendShopBuyPacket(eachSlot)	

			
			### Use Egzo ###
			if Book_Reader_Egzo == 1:
				for i in xrange(player.INVENTORY_PAGE_SIZE*5):
					Book_Reader_Item_1_Index = player.GetItemIndex(i)
					if Book_Reader_Item_1_Index == (int(71001)):
						net.SendItemUsePacket(i)	
						break

			### Use Rada ###	
			if Book_Reader_Rada == 1:
				for i in xrange(player.INVENTORY_PAGE_SIZE*5):
					Book_Reader_Item_2_Index = player.GetItemIndex(i)
					if Book_Reader_Item_2_Index == (int(71094)):
						net.SendItemUsePacket(i)	
						break			

			### Use Book ###
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Book_Reader_Book_Index = player.GetItemIndex(i)
				if Book_Reader_Book_Index == (int(Book_Reader_Book_ID)):
					net.SendItemUsePacket(i)	
					break				
	
	### Book Reader Show ToolTip ###	
	def Book_Reader_ShowTip(self):
		global Book_Reader_Book_ID
		
		if Book_Reader_Book_ID > 0:
		
			item.SelectItem(int(Book_Reader_Book_ID))		
		
			self.txttooltip.ClearToolTip()
			self.txttooltip.AppendTextLine(str(item.GetItemName(Book_Reader_Book_ID)), grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
			self.txttooltip.AppendTextLine("ID: " + str(Book_Reader_Book_ID), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.AppendTextLine("Iloœæ: " + str(player.GetItemCountByVnum(int(Book_Reader_Book_ID))), grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0))
			self.txttooltip.Show()	
		else:
			self.txttooltip.ClearToolTip()
			self.txttooltip.Hide()
	
	### Book Reader Hide ToolTip ###	
	def Book_Reader_HideTip(self):
		self.txttooltip.ClearToolTip()
		self.txttooltip.Hide()	
	
	def __BuildKeyDict(self):
		onPressKeyDict = {}
		onPressKeyDict[app.DIK_F5]	= lambda : self.OpenWindow()
		self.onPressKeyDict = onPressKeyDict
	
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
	
	def Book_Reader_Close(self):
		self.Book_Reader.Hide()	
	
class Python_Loader(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()
		self.Python_Loader_Refresh_func()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Python_Loader = ui.BoardWithTitleBar()
		self.Python_Loader.SetSize(220, 300)
		self.Python_Loader.SetCenterPosition()
		self.Python_Loader.AddFlag('movable')
		self.Python_Loader.AddFlag('float')
		self.Python_Loader.SetTitleName('Python Loader')
		self.Python_Loader.SetCloseEvent(self.Python_Loader_Close)
		self.Python_Loader.Show()
		self.comp = Component()
				
		### Too lTip ###
		self.txttooltip = uiToolTip.ToolTip()			
		self.txttooltip.Hide()				
			
		### HorizontalBars ###		
		self.Python_Loader_Info_HorizontalBar = self.comp.HorizontalBar(self.Python_Loader , 10, 38, 200)
		self.Python_Loader_Info_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Python_Loader_Info_HorizontalBar, 'Lista Plików Python', 5, 0, 0xFFFFE3AD)			

		### Buttons ###
		self.Python_Loader_Question_Button = ui.ExpandedImageBox()
		self.Python_Loader_Question_Button.SetParent(self.Python_Loader)
		self.Python_Loader_Question_Button.SetPosition(173, 9)
		self.Python_Loader_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_01.tga")
		self.Python_Loader_Question_Button.OnMouseOverIn = lambda: self.Python_Loader_ShowTip()
		self.Python_Loader_Question_Button.OnMouseOverOut = lambda: self.Python_Loader_HideTip()
		self.Python_Loader_Question_Button.Show()	
	
		self.Python_Loader_Refresh_Button = self.comp.Button(self.Python_Loader, '', 'Odœwie¿ Listê', 190, 38, self.Python_Loader_Refresh_func, 'd:/ymir work/ui/game/guild/Refresh_Button_01.sub', 'd:/ymir work/ui/game/guild/Refresh_Button_02.sub', 'd:/ymir work/ui/game/guild/Refresh_Button_03.sub')
		self.Python_Loader_Load_Button = self.comp.Button(self.Python_Loader, 'Load', '', 18, 265, self.Python_Loader_Load_func, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')
			
		### List Box ###
		self.Python_Loader_List_Bar, self.Python_Loader_List = self.comp.ListBoxEx(self.Python_Loader, 10, 60, 200, 200)
					
	### Python Loader Refresh List ###					
	def Python_Loader_Refresh_func(self):
		self.Python_Loader_List.RemoveAllItems()
		fileNameList=app.GetFileList("ZAHON_MOD/Python/"+"*."+"py")
		for fileName in fileNameList:
			self.Python_Loader_List.AppendItem(Item(fileName))
			
	### Python Loader Load ###				
	def Python_Loader_Load_func(self):
		if self.Python_Loader_List.IsEmpty():
			chat.AppendChat(2, "Lista jest pusta!")
		else:
			ItemIndex = self.Python_Loader_List.GetSelectedItem()
			
			if ItemIndex:
				pass
			else:
				chat.AppendChat(2, "Najpierw zaznacz pozycjê z listy!")			
			
			Selected_Item_TxT = ItemIndex.GetText()
	
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, str(Selected_Item_TxT))	
	
	### Python Loader Show ToolTip ###	
	def Python_Loader_ShowTip(self):
	
		self.txttooltip.ClearToolTip()
		self.txttooltip.AppendTextLine("Python Loader 1.0", grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 
		self.txttooltip.AppendTextLine("Code by ZAHON 2016", grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)) 		
		self.txttooltip.AppendTextLine("Pliki .py nale¿y dodaæ do folderu", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("ZAHON_MOD/Python", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.Show()		
	
		self.Python_Loader_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_02.tga")
		
	### Python Loader ToolTip ###		
	def Python_Loader_HideTip(self):
		self.txttooltip.ClearToolTip()
		self.txttooltip.Hide()	
		self.Python_Loader_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_01.tga")
	
	def OpenWindow(self):
		if self.Board.IsShow():
			self.Board.Hide()
		else:
			self.Board.Show()
	
	def Python_Loader_Close(self):
		self.Python_Loader.Hide()	
	
class Exp_Donator(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Exp_Donator = ui.BoardWithTitleBar()
		self.Exp_Donator.SetSize(140, 90)
		self.Exp_Donator.SetCenterPosition()
		self.Exp_Donator.AddFlag('movable')
		self.Exp_Donator.AddFlag('float')
		self.Exp_Donator.SetTitleName('Exp Donator')
		self.Exp_Donator.SetCloseEvent(self.Exp_Donator_Close)
		self.Exp_Donator.Show()
		self.__BuildKeyDict()
		self.comp = Component()
			
		### Buttons ###
		self.Exp_Donator_Status_Button = self.comp.Button(self.Exp_Donator, 'Start', '', 25, 45, self.Exp_Donator_Status_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		
	def Exp_Donator_Status_func(self):
		global Exp_Donator_Status
		if Exp_Donator_Status == 0:
		
			Guild_Name = player.GetGuildName()	
			if Guild_Name == "":
				chat.AppendChat(2, "Nie jesteœ cz³onkiem gildii!")
			else:		
				Exp_Donator_Status = 1
				self.Enable_Exp_Donator()
				chat.AppendChat(2, "Exp Donator Start")
				self.Exp_Donator_Status_Button.SetText("Stop")
		else:
			Exp_Donator_Status = 0
			self.Disable_Exp_Donator()
			chat.AppendChat(2, "Exp Donator Stop")
			self.Exp_Donator_Status_Button.SetText("Start")		
		
	def Enable_Exp_Donator(self):

		Current_Exp = player.GetStatus(player.EXP)
		
		if Current_Exp > 100:
			net.SendGuildOfferPacket(int(Current_Exp))
		else:
			pass
				
		self.Delay_Exp_Donator = WaitingDialog()
		self.Delay_Exp_Donator.Open(float(0.1))
		self.Delay_Exp_Donator.SAFE_SetTimeOverEvent(self.Enable_Exp_Donator)
			
	def Disable_Exp_Donator(self):	
		self.Delay_Exp_Donator = WaitingDialog()
		self.Delay_Exp_Donator.Open(float(99999999999999999))
		self.Delay_Exp_Donator.SAFE_SetTimeOverEvent(self.Disable_Exp_Donator)			
		
		
	def __BuildKeyDict(self):
		onPressKeyDict = {}
		onPressKeyDict[app.DIK_F5]	= lambda : self.OpenWindow()
		self.onPressKeyDict = onPressKeyDict
	
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
	
	def Exp_Donator_Close(self):
		self.Exp_Donator.Hide()	
	
class Inventory_Manager(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()
		self.Inventory_Manager_Refresh_func()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Inventory_Manager = ui.BoardWithTitleBar()
		self.Inventory_Manager.SetSize(220, 390)
		self.Inventory_Manager.SetCenterPosition()
		self.Inventory_Manager.AddFlag('movable')
		self.Inventory_Manager.AddFlag('float')
		self.Inventory_Manager.SetTitleName('Mened¿er Ekwipunku')
		self.Inventory_Manager.SetCloseEvent(self.Inventory_Manager_Close)
		self.Inventory_Manager.Show()
		self.comp = Component()
			
		### HorizontalBars ###		
		self.Inventory_Manager_Info_HorizontalBar = self.comp.HorizontalBar(self.Inventory_Manager , 10, 38, 200)
		self.Inventory_Manager_Info_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Inventory_Manager_Info_HorizontalBar, 'Lista Przedmiotów w Ekwipunku', 5, 0, 0xFFFFE3AD)			

		self.Inventory_Manager_Options_HorizontalBar = self.comp.HorizontalBar(self.Inventory_Manager , 10, 260, 200)
		self.Inventory_Manager_Options_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Inventory_Manager_Options_HorizontalBar, 'Dostêpne Opcje', 5, 0, 0xFFFFE3AD)			

		self.Inventory_Manager_Options_2_HorizontalBar = self.comp.HorizontalBar(self.Inventory_Manager , 10, 340, 200)
		self.Inventory_Manager_Options_2_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Inventory_Manager_Options_2_HorizontalBar, 'Opcje Ulepszania', 5, 0, 0xFFFFE3AD)			

		### Thin Board ###
		self.Inventory_Manager_ThinBoard = self.comp.ThinBoardHide(self.Inventory_Manager, FALSE, 10, 335, 200, 60, FALSE)			
		
		### Buttons ###
		self.Inventory_Manager_Refresh_Button = self.comp.Button(self.Inventory_Manager, '', 'Odœwie¿ Listê', 190, 38, self.Inventory_Manager_Refresh_func, 'd:/ymir work/ui/game/guild/Refresh_Button_01.sub', 'd:/ymir work/ui/game/guild/Refresh_Button_02.sub', 'd:/ymir work/ui/game/guild/Refresh_Button_03.sub')
		
		self.Inventory_Manager_Drop_Select_Button = self.comp.Button(self.Inventory_Manager, 'Wyrzuæ Wybrany', '', 10, 280, self.Inventory_Manager_Drop_Select_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Inventory_Manager_Drop_All_Button = self.comp.Button(self.Inventory_Manager, 'Wyrzuæ Wszystko', '', 120, 280, self.Inventory_Manager_Drop_All_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Inventory_Manager_Drop_All_Yes_Button = self.comp.ButtonHide(self.Inventory_Manager_ThinBoard, 'Tak', '', 5, 25, self.Inventory_Manager_Drop_All_Yes_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Inventory_Manager_Drop_All_No_Button = self.comp.ButtonHide(self.Inventory_Manager_ThinBoard, 'Nie', '', 105, 25, self.Inventory_Manager_Drop_All_No_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		
		self.Inventory_Manager_Sell_Select_Button = self.comp.Button(self.Inventory_Manager, 'Sprzedaj Wybrany', '', 10, 310, self.Inventory_Manager_Sell_Select_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Inventory_Manager_Sell_All_Button = self.comp.Button(self.Inventory_Manager, 'Sprzedaj Wszystko', '', 120, 310, self.Inventory_Manager_Sell_All_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Inventory_Manager_Sell_All_Yes_Button = self.comp.ButtonHide(self.Inventory_Manager_ThinBoard, 'Tak', '', 5, 25, self.Inventory_Manager_Sell_All_Yes_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Inventory_Manager_Sell_All_No_Button = self.comp.ButtonHide(self.Inventory_Manager_ThinBoard, 'Nie', '', 105, 25, self.Inventory_Manager_Sell_All_No_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')

		self.Inventory_Manager_Upgrade_Button = self.comp.Button(self.Inventory_Manager, 'Ulepsz', '', 120, 360, self.Inventory_Manager_Upgrade_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		
		### TxT ###
		self.Inventory_Manager_Infon_TextLine = self.comp.TextLineHide(self.Inventory_Manager_ThinBoard, 'Wyrzuciæ wszystkie przedmioty?', 23, 10, self.comp.RGB(255, 255, 255))		
			
		### Editline ###	
		self.Inventory_Manager_Input_TxT, self.Inventory_Manager_Input_TxT_EditLine = self.comp.EditLine(self.Inventory_Manager, '1', 95, 361, 20, 15, 1)
							
		### List Box ###		
		self.Inventory_Manager_bar_Item_List, self.Inventory_Manager_list_Item_List = self.comp.ListBoxEx(self.Inventory_Manager, 10, 60, 200, 200)
				
		### ComboBox ###
		self.Inventory_Manager_Upgrade_Mode_ComboBox = self.comp.ComboBox(self.Inventory_Manager, 'Kowal', 10, 361, 80)	
	
		global Inventory_Manager_Upgrade_Mode_ComboBox
		for Inventory_Manager_Upgrade_Mode_ComboBox in Inventory_Manager_Upgrade_Mode_ComboBox:
			self.Inventory_Manager_Upgrade_Mode_ComboBox.InsertItem(1,str(Inventory_Manager_Upgrade_Mode_ComboBox)) 			
			
	### Inventory Manager Refresh Func ###				
	def Inventory_Manager_Refresh_func(self):
		self.Inventory_Manager_list_Item_List.RemoveAllItems()
		for i in xrange(player.INVENTORY_PAGE_SIZE*5):
			ItemIndex = player.GetItemIndex(i)
			if ItemIndex != 0:
				item.SelectItem(ItemIndex)
				item.GetItemName(ItemIndex)
				ItemName = item.GetItemName()
				self.Inventory_Manager_list_Item_List.AppendItem(Item(str(i) + " " + str(ItemIndex) + " " + ItemName))	
					
	### Inventory Manager Drop Select Func ###
	def Inventory_Manager_Drop_Select_func(self):
		ItemIndex = self.Inventory_Manager_list_Item_List.GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Przedmiot musi byæ zaznaczony!")
		SelectedItem = ItemIndex.GetText().split()
		net.SendItemDropPacket(int(SelectedItem[0]))
		self.Inventory_Manager_Refresh_func()
		
	### Inventory Manager Drop All Func ###
	def Inventory_Manager_Drop_All_func(self):
		self.Inventory_Manager.SetSize(220, 455)
		
		self.Inventory_Manager_ThinBoard.Show()
		self.Inventory_Manager_Drop_All_Yes_Button.Show()
		self.Inventory_Manager_Drop_All_No_Button.Show()
		self.Inventory_Manager_Infon_TextLine.Show()
		self.Inventory_Manager_Infon_TextLine.SetText("Wyrzuciæ wszystkie przedmioty?")
		
		self.Inventory_Manager_Input_TxT.SetPosition(95, 421)	
		self.Inventory_Manager_Options_2_HorizontalBar.SetPosition(10, 400)
		self.Inventory_Manager_Upgrade_Button.SetPosition(120, 420)
		self.Inventory_Manager_Upgrade_Mode_ComboBox.SetPosition(10, 421)
		
	def Inventory_Manager_Drop_All_Yes_func(self):
		for i in xrange(player.INVENTORY_PAGE_SIZE*5):
			net.SendItemDropPacket(i)
			self.Inventory_Manager_Refresh_func()
		
			self.Inventory_Manager.SetSize(220, 390)
			
			self.Inventory_Manager_ThinBoard.Hide()
			self.Inventory_Manager_Drop_All_Yes_Button.Hide()
			self.Inventory_Manager_Drop_All_No_Button.Hide()
			self.Inventory_Manager_Infon_TextLine.Hide()
			
			self.Inventory_Manager_Input_TxT.SetPosition(95, 361)	
			self.Inventory_Manager_Options_2_HorizontalBar.SetPosition(10, 340)
			self.Inventory_Manager_Upgrade_Button.SetPosition(120, 360)
			self.Inventory_Manager_Upgrade_Mode_ComboBox.SetPosition(10, 361)		
		
	def Inventory_Manager_Drop_All_No_func(self):
		self.Inventory_Manager.SetSize(220, 390)
		
		self.Inventory_Manager_ThinBoard.Hide()
		self.Inventory_Manager_Drop_All_Yes_Button.Hide()
		self.Inventory_Manager_Drop_All_No_Button.Hide()
		self.Inventory_Manager_Infon_TextLine.Hide()
		
		self.Inventory_Manager_Input_TxT.SetPosition(95, 361)	
		self.Inventory_Manager_Options_2_HorizontalBar.SetPosition(10, 340)
		self.Inventory_Manager_Upgrade_Button.SetPosition(120, 360)
		self.Inventory_Manager_Upgrade_Mode_ComboBox.SetPosition(10, 361)	
		
	### Inventory Manager Sell Select Func ###
	def Inventory_Manager_Sell_Select_func(self):
		ItemIndex = self.Inventory_Manager_list_Item_List.GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Sklep musi byæ otwarty!")
		SelectedItem = ItemIndex.GetText().split()
		net.SendShopSellPacket(int(SelectedItem[0]))
		self.Inventory_Manager_Refresh_func()
	
	### Inventory Manager Sell All Func ###
	def Inventory_Manager_Sell_All_func(self):
		self.Inventory_Manager.SetSize(220, 455)
		
		self.Inventory_Manager_ThinBoard.Show()
		self.Inventory_Manager_Sell_All_Yes_Button.Show()
		self.Inventory_Manager_Sell_All_No_Button.Show()
		self.Inventory_Manager_Infon_TextLine.Show()
		self.Inventory_Manager_Infon_TextLine.SetText("Sprzedaæ wszystkie przedmioty?")
		
		self.Inventory_Manager_Input_TxT.SetPosition(95, 421)	
		self.Inventory_Manager_Options_2_HorizontalBar.SetPosition(10, 400)
		self.Inventory_Manager_Upgrade_Button.SetPosition(120, 420)
		self.Inventory_Manager_Upgrade_Mode_ComboBox.SetPosition(10, 421)
		
	def Inventory_Manager_Sell_All_Yes_func(self):
		for i in xrange(player.INVENTORY_PAGE_SIZE*5):
			net.SendShopSellPacket(i)
			
			self.Inventory_Manager.SetSize(220, 390)
			
			self.Inventory_Manager_ThinBoard.Hide()
			self.Inventory_Manager_Sell_All_Yes_Button.Hide()
			self.Inventory_Manager_Sell_All_No_Button.Hide()
			self.Inventory_Manager_Infon_TextLine.Hide()
			
			self.Inventory_Manager_Input_TxT.SetPosition(95, 361)	
			self.Inventory_Manager_Options_2_HorizontalBar.SetPosition(10, 340)
			self.Inventory_Manager_Upgrade_Button.SetPosition(120, 360)
			self.Inventory_Manager_Upgrade_Mode_ComboBox.SetPosition(10, 361)				
		
	def Inventory_Manager_Sell_All_No_func(self):
		self.Inventory_Manager.SetSize(220, 390)
		
		self.Inventory_Manager_ThinBoard.Hide()
		self.Inventory_Manager_Sell_All_Yes_Button.Hide()
		self.Inventory_Manager_Sell_All_No_Button.Hide()
		self.Inventory_Manager_Infon_TextLine.Hide()
		
		self.Inventory_Manager_Input_TxT.SetPosition(95, 361)	
		self.Inventory_Manager_Options_2_HorizontalBar.SetPosition(10, 340)
		self.Inventory_Manager_Upgrade_Button.SetPosition(120, 360)
		self.Inventory_Manager_Upgrade_Mode_ComboBox.SetPosition(10, 361)			
	
	### Inventory Manager Upgrade Func ###
	def Inventory_Manager_Upgrade_func(self):
	
		Inventory_Manager_Upgrade_Mode = self.Inventory_Manager_Upgrade_Mode_ComboBox.GetCurrentText()
		Inventory_Manager_Upgrade_Plus = self.Inventory_Manager_Input_TxT_EditLine.GetText()
				
		for i in xrange(int(Inventory_Manager_Upgrade_Plus)):
			if Inventory_Manager_Upgrade_Mode == "Kowal":
			
				ItemIndex = self.Inventory_Manager_list_Item_List.GetSelectedItem()
				if ItemIndex:
					pass
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Przedmiot musi byæ zaznaczony!")
				SelectedItem = ItemIndex.GetText().split(" ")
				net.SendRefinePacket(int(SelectedItem[0]), int(0))	
				self.Inventory_Manager_Refresh_func()

				
				
			if Inventory_Manager_Upgrade_Mode == "Kowal DT":
			
				ItemIndex = self.list_Item_List.GetSelectedItem()
				if ItemIndex:
					pass
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Przedmiot musi byæ zaznaczony!")
				SelectedItem = ItemIndex.GetText().split(" ")
				net.SendRefinePacket(int(SelectedItem[0]), int(4))
				self.Inventory_Manager_Refresh_func()

			if Inventory_Manager_Upgrade_Mode == "Kowal Gildijny":
			
				ItemIndex = self.list_Item_List.GetSelectedItem()
				if ItemIndex:
					pass
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Przedmiot musi byæ zaznaczony!")
				SelectedItem = ItemIndex.GetText().split(" ")
				net.SendRefinePacket(int(SelectedItem[0]), int(1))
				self.Inventory_Manager_Refresh_func()				

			if Inventory_Manager_Upgrade_Mode == "Bodzio":	
				ItemIndex = self.Inventory_Manager_list_Item_List.GetSelectedItem()
				if ItemIndex:
					pass
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Przedmiot musi byæ zaznaczony!")
				SelectedItem = ItemIndex.GetText().split(" ")			
			
				for i in xrange(player.INVENTORY_PAGE_SIZE*5):
					Item_Vnum = player.GetItemIndex(i)
					if Item_Vnum == 25040:
						chat.AppendChat(2, str(i))
						net.SendItemUseToItemPacket(int(i), int(SelectedItem[0]))
						net.SendRefinePacket(int(SelectedItem[0]), 2)	
						self.Inventory_Manager_Refresh_func()
						break							
					
					


					
	
	def OpenWindow(self):
		if self.Board.IsShow():
			self.Board.Hide()
		else:
			self.Board.Show()
	
	def Inventory_Manager_Close(self):
		self.Inventory_Manager.Hide()		
	
class Environment(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()
		self.Change_Environment_Add_Item()
		
	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Environment = ui.BoardWithTitleBar()
		self.Environment.SetSize(160, 190)
		self.Environment.SetCenterPosition()
		self.Environment.AddFlag('movable')
		self.Environment.AddFlag('float')
		self.Environment.SetTitleName('Œrodowisko')
		self.Environment.SetCloseEvent(self.Environment_Close)
		self.Environment.Show()
		
		self.Environment_Shadow_Level = ui.BoardWithTitleBar()
		self.Environment_Shadow_Level.SetSize(200, 80)
		self.Environment_Shadow_Level.SetCenterPosition()
		self.Environment_Shadow_Level.AddFlag('movable')
		self.Environment_Shadow_Level.AddFlag('float')
		self.Environment_Shadow_Level.SetTitleName('Poziom Cieni')
		self.Environment_Shadow_Level.SetCloseEvent(self.Environment_Shadow_Level_Close)
		self.Environment_Shadow_Level.Hide()		
		
		self.Environment_Change_Environment = ui.BoardWithTitleBar()
		self.Environment_Change_Environment.SetSize(220, 280)
		self.Environment_Change_Environment.SetCenterPosition()
		self.Environment_Change_Environment.AddFlag('movable')
		self.Environment_Change_Environment.AddFlag('float')
		self.Environment_Change_Environment.SetTitleName('Zmieñ Œrodowisko')
		self.Environment_Change_Environment.SetCloseEvent(self.Environment_Change_Environment_Close)
		self.Environment_Change_Environment.Hide()		
		
		self.__BuildKeyDict()
		self.comp = Component()

		### Text ###
		self.Environment_Day_Text = self.comp.TextLine(self.Environment, 'Dzieñ', 15, 41, self.comp.RGB(255, 255, 255))		
		self.Environment_Night_Text = self.comp.TextLine(self.Environment, 'Noc', 15, 61, self.comp.RGB(255, 255, 255))		
		self.Environment_Snow_Text = self.comp.TextLine(self.Environment, 'Œnieg', 15, 81, self.comp.RGB(255, 255, 255))		
		self.Environment_Fog_Text = self.comp.TextLine(self.Environment, 'Mg³a', 15, 101, self.comp.RGB(255, 255, 255))		
		self.Environment_Crash_Map_Text = self.comp.TextLine(self.Environment, 'Crash Map', 15, 121, self.comp.RGB(255, 255, 255))		
		self.Environment_Shadow_Level_1_Text = self.comp.TextLine(self.Environment, 'Poziom Cieni', 15, 141, self.comp.RGB(255, 255, 255))		
		self.Environment_Change_Environment_Text = self.comp.TextLine(self.Environment, 'Zmieñ Œrodowisko', 15, 161, self.comp.RGB(255, 255, 255))		
		
		self.Environment_Shadow_Level_Text = self.comp.TextLine(self.Environment_Shadow_Level, '', 15, 60, self.comp.RGB(255, 255, 255))		
					
		### Buttons ###
		self.Environment_Day_Button = self.comp.Button(self.Environment, 'Ustaw', '', 105, 39, self.Environment_Day_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Environment_Night_Button = self.comp.Button(self.Environment, 'Ustaw', '', 105, 59, self.Environment_Night_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Environment_Snow_Button = self.comp.Button(self.Environment, 'W³¹cz', '', 105, 79, self.Environment_Snow_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Environment_Fog_Button = self.comp.Button(self.Environment, 'Wy³¹cz', '', 105, 99, self.Environment_Fog_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Environment_Crash_Map_Button = self.comp.Button(self.Environment, 'Crash', '', 105, 119, self.Environment_Crash_Map_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Environment_Shadow_Level_Button = self.comp.Button(self.Environment, 'Ustaw', '', 105, 139, self.Environment_Shadow_Level_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Environment_Change_Environment_Button = self.comp.Button(self.Environment, 'Zmieñ', '', 105, 158, self.Environment_Change_Environment_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		
		self.Change_Environment_Button = self.comp.Button(self.Environment_Change_Environment, 'Zmieñ Œrodowisko', '', 18, 245, self.Change_Environment_func, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')
							
		### EditLine ###
		self.Slidbar_Environment_Shadow_Level = self.comp.SliderBar(self.Environment_Shadow_Level, 100 / 10, self.Set_Environment_Shadow_Level, 10, 40)
				
		### List Box ###		
		self.Environment_Change_Environment_List_Bar, self.Environment_Change_Environment_List = self.comp.ListBoxEx(self.Environment_Change_Environment, 10, 35, 200, 200)
		
		
	def Environment_Day_func(self):
		background.SetEnvironmentData(0)
		chat.AppendChat(2, "Dzieñ W³¹czony")
		
	def Environment_Night_func(self):
		background.SetEnvironmentData(1)
		background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
		chat.AppendChat(2, "Noc W³¹czony")		
		
	def Environment_Snow_func(self):
		global Environment_Snow
		if Environment_Snow == 0:
			Environment_Snow = 1
			background.EnableSnow(1)
			self.Environment_Snow_Button.SetText("Wy³¹cz")
			chat.AppendChat(2, "Œnieg W³¹czony")
		else:	
			Environment_Snow = 0
			background.EnableSnow(0)
			self.Environment_Snow_Button.SetText("W³¹cz")
			chat.AppendChat(2, "Œnieg Wy³¹czony")

	def Environment_Fog_func(self):
		global Environment_Fog
		if Environment_Fog == 0:
			Environment_Fog = 1
			app.SetMinFog(900000)
			self.Environment_Fog_Button.SetText("W³¹cz")
			chat.AppendChat(2, "Mg³a Wy³¹czona")
		else:
			Environment_Fog = 0
			app.SetMinFog(2500)
			self.Environment_Fog_Button.SetText("Wy³¹cz")
			chat.AppendChat(2, "Mg³a W³¹czona")	
		
	def Environment_Crash_Map_func(self):
		global Environment_Crash_Map
		
		Current_Map_Name = background.GetCurrentMapName()
		
		if Environment_Crash_Map == 0:
			Environment_Crash_Map = 1
			self.Environment_Crash_Map_Button.SetText("Normal")
			x,y = player.GetMainCharacterPosition()[:2]
			background.LoadMap(str(Current_Map_Name), x, y, 0)
		else:
			Environment_Crash_Map = 0
			self.Environment_Crash_Map_Button.SetText("Crash")	
			background.LoadMap(str(Current_Map_Name), 100, 100, 100)	
	
	### Shadow Level ###
	def Environment_Shadow_Level_func(self):
		if self.Environment_Shadow_Level.IsShow():
			self.Environment_Shadow_Level.Hide()
		else:
			self.Environment_Shadow_Level.Show()
		
	def Set_Environment_Shadow_Level(self):
		global Environment_Shadow_Level 	
		Environment_Shadow_Level = int(self.Slidbar_Environment_Shadow_Level.GetSliderPos() * 3)
		background.SetShadowLevel(int(Environment_Shadow_Level))		
		
		if Environment_Shadow_Level == 0:
			self.Environment_Shadow_Level_Text.SetText("Shadow Level 0, None")
			
		if Environment_Shadow_Level == 1:
			self.Environment_Shadow_Level_Text.SetText("Shadow Level 1, Background")

		if Environment_Shadow_Level == 2:
			self.Environment_Shadow_Level_Text.SetText("Shadow Level 2, Background + Player")	

		if Environment_Shadow_Level == 3:
			self.Environment_Shadow_Level_Text.SetText("Shadow Level 3, All")			
		
	### Change Environment ###	
	def Environment_Change_Environment_func(self):
		if self.Environment_Change_Environment.IsShow():
			self.Environment_Change_Environment.Hide()
		else:
			self.Environment_Change_Environment.Show()	
	
	def Change_Environment_func(self):
		ItemIndex = self.Environment_Change_Environment_List.GetSelectedItem()
		if ItemIndex:
			SelectedItem = ItemIndex.GetText()
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Najpierw zaznacz item z listy!")
			
			
		if SelectedItem == "gm_guild_build":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/A1.msenv")
			background.SetEnvironmentData(0)	
			
		if SelectedItem == "map_a2":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/A2.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "map_b2":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/B2.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "map_c2":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/C2.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "map_n_snowm_01":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/N-snowm01.msenv")
			background.SetEnvironmentData(0)					
		
		if SelectedItem == "metin2_guild_village":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/guild_village.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_a1":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/A1.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_a3":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/A3.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_b1":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/B1.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_b3":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/B3.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_bayblacksand":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/bayblacksand.msenv")
			background.SetEnvironmentData(0)				
		
		if SelectedItem == "metin2_map_c1":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/C1.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_c3":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/C3.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_capedragonhead":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/CapeDragonHead.msenv")
			background.SetEnvironmentData(0)		
			
		if SelectedItem == "metin2_map_dawnmistwood":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/DawnMistWood.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_devilscatacomb":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/map_devilsCatacomb.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_deviltower1":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/dark.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_duel":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/A1.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_guild_01":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/A2.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_guild_02":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/C1.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_guild_03":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/B1.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_milgyo":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/milgyo.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_monkeydungeon":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/dark.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_monkeydungeon_02":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/monkeydungeon_02.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_monkeydungeon_03":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/monkeydungeon_03.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_mt_thunder":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/mtthunder.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_n_desert_01":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/milgyo.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_n_flame_01":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/map_n_flame_01.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_skipia_dungeon_02":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/skipia_dungeon.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_skipia_dungeon_boss":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/skipia_dungeon.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_spiderdungeon":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/dark.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_spiderdungeon_03":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/dark.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_t1":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/map_b_fielddungeon2.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_t2":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/t2.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_t3":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/moonlight05.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_trent":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/trent.msenv")
			background.SetEnvironmentData(0)

		if SelectedItem == "metin2_map_trent02":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/trent02.msenv")
			background.SetEnvironmentData(0)	

		if SelectedItem == "metin2_map_wedding_01":
			background.RegisterEnvironmentData(0, "d:/ymir work/environment/A1.msenv")
			background.SetEnvironmentData(0)
	
	def Change_Environment_Add_Item(self):
		self.Environment_Change_Environment_List.AppendItem(Item("gm_guild_build")) # A1.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("map_a2")) # A2.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("map_b2")) # B2.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("map_c2")) # C2.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("map_n_snowm_01")) # N-snowm01.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_guild_village")) # guild_village.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_a1")) # A1.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_a3")) # A3.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_b1")) # B1.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_b3")) # B3.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_bayblacksand")) # bayblacksand.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_c1")) # C1.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_c3")) # C3.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_capedragonhead")) # CapeDragonHead.msenv		
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_dawnmistwood")) # DawnMistWood.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_devilscatacomb")) # map_devilsCatacomb.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_deviltower1")) # dark.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_duel")) # A1.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_guild_01")) # A2.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_guild_02")) # C1.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_guild_03")) # B1.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_milgyo")) # milgyo.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_monkeydungeon")) # dark.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_monkeydungeon_02")) # monkeydungeon_02.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_monkeydungeon_03")) # monkeydungeon_03.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_mt_thunder")) # mtthunder.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_n_desert_01")) # milgyo.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_n_flame_01")) # map_n_flame_01.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_skipia_dungeon_02")) # skipia_dungeon.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_skipia_dungeon_boss")) # skipia_dungeon.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_spiderdungeon")) # dark.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_spiderdungeon_03")) # dark.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_t1")) # map_b_fielddungeon2.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_t2")) # t2.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_t3")) # moonlight05.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_trent")) # trent.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_trent02")) # trent02.msenv
		self.Environment_Change_Environment_List.AppendItem(Item("metin2_map_wedding_01")) # A1.msenv
	
	
	def __BuildKeyDict(self):
		onPressKeyDict = {}
		onPressKeyDict[app.DIK_F5]	= lambda : self.OpenWindow()
		self.onPressKeyDict = onPressKeyDict
	
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
	
	def Environment_Close(self):
		self.Environment.Hide()

	def Environment_Shadow_Level_Close(self):
		self.Environment_Shadow_Level.Hide()
		
	def Environment_Change_Environment_Close(self):
		self.Environment_Change_Environment.Hide()	
	
class Item_Info(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Item_Info = ui.BoardWithTitleBar()
		self.Item_Info.SetSize(305, 145)
		self.Item_Info.SetCenterPosition()
		self.Item_Info.AddFlag('movable')
		self.Item_Info.AddFlag('float')
		self.Item_Info.SetTitleName('Informacje o Przedmiocie')
		self.Item_Info.SetCloseEvent(self.Item_Info_Close)
		self.Item_Info.Show()
		self.__BuildKeyDict()
		self.comp = Component()
					
		### Too lTip ###
		self.txttooltip = uiToolTip.ToolTip()			
		self.txttooltip.Hide()				
			
		### Slots ###			
		self.Item_Info_Bar_1 = ui.ExpandedImageBox()
		self.Item_Info_Bar_1.SetParent(self.Item_Info)
		self.Item_Info_Bar_1.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Info_Bar_1.OnMouseLeftButtonUp = lambda: self.Item_Info_Set_Item()
		self.Item_Info_Bar_1.SetPosition(20,35)
		self.Item_Info_Bar_1.Show()	
		
		self.Item_Info_Bar_2 = ui.ExpandedImageBox()
		self.Item_Info_Bar_2.SetParent(self.Item_Info)
		self.Item_Info_Bar_2.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Info_Bar_2.OnMouseLeftButtonUp = lambda: self.Item_Info_Set_Item()
		self.Item_Info_Bar_2.SetPosition(20,67)
		self.Item_Info_Bar_2.Show()	

		self.Item_Info_Bar_3 = ui.ExpandedImageBox()
		self.Item_Info_Bar_3.SetParent(self.Item_Info)
		self.Item_Info_Bar_3.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_Info_Bar_3.OnMouseLeftButtonUp = lambda: self.Item_Info_Set_Item()
		self.Item_Info_Bar_3.SetPosition(20,99)
		self.Item_Info_Bar_3.Show()			
			
		self.Item_Info_Bar = ui.Bar()
		self.Item_Info_Bar.SetParent(self.Item_Info)		
		self.Item_Info_Bar.SetSize(32, 96)
		self.Item_Info_Bar.SetPosition(20,35)		
		self.Item_Info_Bar.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.0))
		self.Item_Info_Bar.OnMouseLeftButtonUp = lambda: self.Item_Info_Set_Item()		
		self.Item_Info_Bar.Show()				
			
		self.Item_Info_Icon = ui.ExpandedImageBox()
		self.Item_Info_Icon.SetParent(self.Item_Info_Bar)
		self.Item_Info_Icon.SetPosition(0, 33)
		self.Item_Info_Icon.LoadImage("")
		self.Item_Info_Icon.OnMouseLeftButtonUp = lambda: self.Item_Info_Set_Item()
		self.Item_Info_Icon.Show()		
			
		### Buttons ###	
		self.Item_Info_Question_Button = ui.ExpandedImageBox()
		self.Item_Info_Question_Button.SetParent(self.Item_Info)
		self.Item_Info_Question_Button.SetPosition(258, 9)
		self.Item_Info_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_01.tga")
		self.Item_Info_Question_Button.OnMouseOverIn = lambda: self.Item_Info_ShowTip()
		self.Item_Info_Question_Button.OnMouseOverOut = lambda: self.Item_Info_HideTip()
		self.Item_Info_Question_Button.Show()			
		
		### Text ###
		self.Item_Info_Name_Item_TextLine = self.comp.TextLine(self.Item_Info, 'Nazwa Przedmiotu', 65, 45, self.comp.RGB(255, 255, 255))		
		self.Item_Info_ID_Item_TextLine = self.comp.TextLine(self.Item_Info, 'ID Przedmiotu', 65, 60, self.comp.RGB(255, 255, 255))		
		self.Item_Info_Number_Slot_Item_TextLine = self.comp.TextLine(self.Item_Info, 'Zajmowany Slot', 65, 75, self.comp.RGB(255, 255, 255))		
		self.Item_Info_Yang_Sell_Item_TextLine = self.comp.TextLine(self.Item_Info, 'Cena Sprzeda¿y', 65, 90, self.comp.RGB(255, 255, 255))		
		self.Item_Info_Icon_Name_TextLine = self.comp.TextLine(self.Item_Info, 'Lokalizacja Ikony', 65, 105, self.comp.RGB(255, 255, 255))		
	

	### Item Info Set Item ###
	def Item_Info_Set_Item(self):
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			item.SelectItem(attachedSlotVnum)

			### Ustawianie Ikony ###
			item.SelectItem(int(attachedSlotVnum))
			self.Item_Info_Icon.LoadImage(str(item.GetIconImageFileName()))
					
			### Ustawianie Po³o¿enia ###
			Size = item.GetItemSize()	
			if Size == (1, 1):
				self.Item_Info_Icon.SetPosition(0, 32)	

			if Size == (1, 2):
				self.Item_Info_Icon.SetPosition(0, 0)	
					
			if Size == (1, 3):
				self.Item_Info_Icon.SetPosition(0, 0)
				
			### Informacje ###
			Yang_Sell_Item = item.GetISellItemPrice()
			Yang_Sell_Item = str(('.'.join([ i-3<0 and str(Yang_Sell_Item)[:i] or str(Yang_Sell_Item)[i-3:i] for i in range(len(str(Yang_Sell_Item))%3, len(str(Yang_Sell_Item))+1, 3) if i ])))
				
			
			self.Item_Info_Name_Item_TextLine.SetText(str(item.GetItemName()))
			self.Item_Info_ID_Item_TextLine.SetText("ID Przedmiotu: " + str(attachedSlotVnum))
			self.Item_Info_Number_Slot_Item_TextLine.SetText("Zajmowany Slot: " + str(attachedSlotPos))
			self.Item_Info_Yang_Sell_Item_TextLine.SetText("Cena Sprzeda¿y: " + str(Yang_Sell_Item) + " Yang")
			self.Item_Info_Icon_Name_TextLine.SetText("Lokalizacja Ikony: " + str(item.GetIconImageFileName()))
			
	
			mouseModule.mouseController.DeattachObject()
	
	### Item Info Show ToolTip ###		
	def Item_Info_ShowTip(self):
		self.txttooltip.ClearToolTip()
		self.txttooltip.AppendTextLine("Item Info 2.1", grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)) 		
		self.txttooltip.AppendTextLine("Bot umo¿liwia w prosty sposób", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("pobranie wielu informacji o przedmiocie", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.AppendTextLine("wystarczy jedynie wstawiæ item w slot", grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)) 
		self.txttooltip.Show()		
	
		self.Item_Info_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_02.tga")
		
	### Item Info ToolTip ###		
	def Item_Info_HideTip(self):
		self.txttooltip.ClearToolTip()
		self.txttooltip.Hide()	
		self.Item_Info_Question_Button.LoadImage("ZAHON_MOD/Buttons/ETC/Question_Mark_Button_01.tga")
		
	def __BuildKeyDict(self):
		onPressKeyDict = {}
		onPressKeyDict[app.DIK_F5]	= lambda : self.OpenWindow()
		self.onPressKeyDict = onPressKeyDict
	
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
	
	def Item_Info_Close(self):
		self.Item_Info.Hide()	
	
class Fake_Info(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Fake_Info = ui.BoardWithTitleBar()
		self.Fake_Info.SetSize(205, 190)
		self.Fake_Info.SetCenterPosition()
		self.Fake_Info.AddFlag('movable')
		self.Fake_Info.AddFlag('float')
		self.Fake_Info.SetTitleName('Fake Info')
		self.Fake_Info.SetCloseEvent(self.Fake_Info_Close)
		self.Fake_Info.Show()
		self.__BuildKeyDict()
		self.comp = Component()
	
		### HorizontalBars ###
		self.Fake_Info_HorizontalBar = self.comp.HorizontalBar(self.Fake_Info , 10, 35, 185)
		self.Fake_Info_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Fake_Info_HorizontalBar, 'Zmiana tylko wizualna!', 5, 0, 0xFFFFE3AD)			
	
		### Text ###
		self.Fake_Info_Set_Nick_Text = self.comp.TextLine(self.Fake_Info, 'Nick Postaci', 15, 56, self.comp.RGB(255, 255, 255))		
		self.Fake_Info_Set_Level_Text = self.comp.TextLine(self.Fake_Info, 'Level Postaci', 15, 76, self.comp.RGB(255, 255, 255))		
		self.Fake_Info_Set_Weapon_Text = self.comp.TextLine(self.Fake_Info, 'Wygl¹d Broni', 15, 96, self.comp.RGB(255, 255, 255))		
		self.Fake_Info_Set_Armor_Text = self.comp.TextLine(self.Fake_Info, 'Wygl¹d Zbroi', 15, 116, self.comp.RGB(255, 255, 255))		
		self.Fake_Info_Set_Visual_Text = self.comp.TextLine(self.Fake_Info, 'Wygl¹d', 15, 136, self.comp.RGB(255, 255, 255))		

		### EditLine ###	
		self.slotbar_Fake_Info_Set_Nick, self.Fake_Info_Set_Nick_EditLine = self.comp.EditLine(self.Fake_Info, '', 80, 55, 60, 15, 100)
		self.slotbar_Fake_Info_Set_Level, self.Fake_Info_Set_Level_EditLine = self.comp.EditLine(self.Fake_Info, '', 80, 75, 60, 15, 100)
		self.slotbar_Fake_Info_Set_Weapon, self.Fake_Info_Set_Weapon_EditLine = self.comp.EditLine(self.Fake_Info, '', 80, 95, 60, 15, 100)
		self.slotbar_Fake_Info_Set_Armor, self.Fake_Info_Set_Armor_EditLine = self.comp.EditLine(self.Fake_Info, '', 80, 115, 60, 15, 100)
		self.slotbar_Fake_Info_Set_Visual, self.Fake_Info_Set_Visual_EditLine = self.comp.EditLine(self.Fake_Info, '', 80, 135, 60, 15, 100)
			
		### Buttons ###
		self.Fake_Info_Set_Nick_Button = self.comp.Button(self.Fake_Info, 'Ustaw', '', 150, 55, self.Fake_Info_Set_Nick_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Fake_Info_Set_Level_Button = self.comp.Button(self.Fake_Info, 'Ustaw', '', 150, 75, self.Fake_Info_Set_Level_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Fake_Info_Set_Weapon_Button = self.comp.Button(self.Fake_Info, 'Ustaw', '', 150, 95, self.Fake_Info_Set_Weapon_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Fake_Info_Set_Armor_Button = self.comp.Button(self.Fake_Info, 'Ustaw', '', 150, 115, self.Fake_Info_Set_Armor_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Fake_Info_Set_Visual_Button = self.comp.Button(self.Fake_Info, 'Ustaw', '', 150, 135, self.Fake_Info_Set_Visual_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Fake_Info_Set_GM_Button = self.comp.Button(self.Fake_Info, 'Ustaw znaczek GM', '', 12, 155, self.Fake_Info_GM_func, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')
			
	################################## Fake Info Func #########################################			
	
	### Fake Info Set Nick ### 
	def Fake_Info_Set_Nick_func(self):
		chr.SetNameString(str(self.Fake_Info_Set_Nick_EditLine.GetText()))
		chat.AppendChat(2, "Aby zatwierdziæ zmianê wykonaj akcjê na koncie - u¿yj dopalacza, zdejmij item itp.")
	
	### Fake Info Set Level ### 	
	def Fake_Info_Set_Level_func(self):
		player.SetStatus(player.LEVEL, int(self.Fake_Info_Set_Level_EditLine.GetText()))			
	
	### Fake Info Set Weapon ### 	
	def Fake_Info_Set_Weapon_func(self):
		if self.Fake_Info_Set_Weapon_EditLine.GetText() == "" or self.Fake_Info_Set_Weapon_EditLine.GetText() == "0":
			chat.AppendChat(2, "Najpierw podaj ID broni")	
		else:
			chr.SetWeapon(int(self.Fake_Info_Set_Weapon_EditLine.GetText()))
		
	### Fake Info Set Armor ### 
	def Fake_Info_Set_Armor_func(self):
		if self.Fake_Info_Set_Armor_EditLine.GetText() == "" or self.Fake_Info_Set_Armor_EditLine.GetText() == "0":
			chat.AppendChat(2, "Najpierw podaj ID zbroi")	
		else:	
			chr.SetArmor(int(self.Fake_Info_Set_Armor_EditLine.GetText()))
	
	### Fake Info Set Visual ### 	
	def Fake_Info_Set_Visual_func(self):
		chr.SetRace(int(self.Fake_Info_Set_Visual_EditLine.GetText()))
	
	### Feak Info Set GM Mark ###
	def Fake_Info_GM_func(self):
		global Fake_Info_GM
		if Fake_Info_GM == 0:
			Fake_Info_GM = 1
			chrmgr.SetAffect(-1, 0, 1)
			chat.AppendChat(2, "Ustawiony znaczem Gm")
			self.Fake_Info_Set_GM_Button.SetText("Zabierz znaczek Gm")
		else:	
			Fake_Info_GM = 0
			chrmgr.SetAffect(-1, 0, 0)
			chat.AppendChat(2, "Zabrano znaczek Gm")
			self.Fake_Info_Set_GM_Button.SetText("Ustaw znaczem GM")
	
	def __BuildKeyDict(self):
		onPressKeyDict = {}
		onPressKeyDict[app.DIK_F5]	= lambda : self.OpenWindow()
		self.onPressKeyDict = onPressKeyDict
	
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
	
	def Fake_Info_Close(self):
		self.Fake_Info.Hide()	

class Another(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Another_Gui = ui.BoardWithTitleBar()
		self.Another_Gui.SetSize(125, 200)
		self.Another_Gui.SetCenterPosition()
		self.Another_Gui.AddFlag('movable')
		self.Another_Gui.AddFlag('float')
		self.Another_Gui.SetTitleName('Inne')
		self.Another_Gui.SetCloseEvent(self.Another_Gui_Close)
		self.Another_Gui.Show()
		self.__BuildKeyDict()
		self.comp = Component()
			
		self.File_Extractor = ui.BoardWithTitleBar()
		self.File_Extractor.SetSize(295, 80)
		self.File_Extractor.SetCenterPosition()
		self.File_Extractor.AddFlag('movable')
		self.File_Extractor.AddFlag('float')
		self.File_Extractor.SetTitleName('File Extractor')
		self.File_Extractor.SetCloseEvent(self.File_Extractor_Close)
		self.File_Extractor.Hide()
		
		self.__BuildKeyDict()
		self.comp = Component()		
										
		### Buttons ###			
		self.Another_Get_Ip_Button = self.comp.Button(self.Another_Gui, 'IP Serwera', '', 20, 40, self.Another_Get_Ip_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')				
		self.Another_Get_Bonus_ID_Button = self.comp.Button(self.Another_Gui, 'ID Bonów', '', 20, 65, self.Another_Get_Bonus_ID_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')				
		self.Another_Get_Item_ID_Button = self.comp.Button(self.Another_Gui, 'ID Itemów', '', 20, 90, self.Another_Another_Get_Item_ID_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')				
		self.Another_Get_Mob_ID_Button = self.comp.Button(self.Another_Gui, 'ID Mobów', '', 20, 115, self.Another_Another_Get_Mob_ID_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')				
		self.Another_Get_All_Modules_Button = self.comp.Button(self.Another_Gui, 'All Modules', '', 20, 140, self.Another_Get_All_Modules_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')				
		self.Another_File_Extractor_Button = self.comp.Button(self.Another_Gui, 'File Extractor', '', 20, 165, self.Another_File_Extractor_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')				
		
		self.File_Extractor_Status_Button = self.comp.Button(self.File_Extractor, 'Extract', '', 220, 40, self.File_Extractor_Status_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
					
		### EditLine ###			
		self.slotbar_File_Extractor_Input_TxT, self.File_Extractor_Input_TxT_EditLine = self.comp.EditLine(self.File_Extractor, '', 15, 40, 200, 15, 39)
						
	################################### Another Gui ##########################################			
		
	def Another_Get_Ip_func(self):
		server = open('ZAHON_MOD/Config/Another/Server_IP.txt', 'w')
		for s in range(1, 40):
			try:
				serverName = serverInfo.REGION_DICT[0][s]["name"]
				account_addr_new = serverInfo.REGION_AUTH_SERVER_DICT[0][s]['ip']
				account_port_new = serverInfo.REGION_AUTH_SERVER_DICT[0][s]['port']

				server.write("### Script by KamerMod - http://metin2mod.tk/ ### \n")
				server.write("\n")
				server.write("--- " + str(s) + ". " + serverName + "--- \n")
				server.write("Login IP: " + account_addr_new + " Port: " + str(account_port_new) + "\n")
			except:
				pass

			for i in range(1, 6):
				try:
					addr_new = serverInfo.REGION_DICT[0][s]['channel'][i]['ip']
					port_new = serverInfo.REGION_DICT[0][s]['channel'][i]['tcp_port']
					server.write("CH" + str(i) + " IP: " + addr_new + " Port: " + str(port_new) + "\n")
				except:
					pass
		server.close()

		dbg.LogBox("Gotowe, IP i porty znajdziesz w ZAHON_MOD/Config/Another/Server_IP.txt")
		try:
			os.startfile("ZAHON_MOD/Config/Another/Server_IP.txt")
		except:
			pass	
			
	def Another_Get_Bonus_ID_func(self):
		global BONUS_LIST_CUSTOM, BONUS_LIST_ALL
		out = open("ZAHON_MOD/Config/Another/Bonus_ID.txt","w")
		for x in AFFECT_DICT:
			if BONUS_LIST_ALL:
				out.write(str(AFFECT_DICT[x](0) +  "\n" + str(x)) + "\n")
			else:
				if x in BONUS_LIST_CUSTOM:
					out.write(str(AFFECT_DICT[x](0) +  "\n" + str(x)) + "\n")
		out.close()	
		dbg.LogBox("Gotowe, ID bonów znajdziesz w ZAHON_MOD/Config/Another/Bonus_ID.txt")
		try:
			os.startfile("ZAHON_MOD/Config/Another/Bonus_ID.txt")
		except:
			pass	

	def Another_Another_Get_Item_ID_func(self):
		f = open('ZAHON_MOD/Config/Another/Item_ID.txt','w+')
		for i in xrange(0,250000):
			item.SelectItem(i)
			if item.GetItemType() != 6:
				n = item.GetItemName()
				if n!= "":
					f.write(n + "\n" + str(i) + "\n")
		f.close()
		dbg.LogBox("Gotowe, ID itemów znajdziesz w ZAHON_MOD/Config/Another/Item_ID.txt")
		try:
			os.startfile("ZAHON_MOD/Config/Another/Item_ID.txt")
		except:
			pass	

	def Another_Another_Get_Mob_ID_func(self):
		f = open('ZAHON_MOD/Config/Another/Mob_ID.txt','w+')
		for i in xrange(0,100000):
			n = nonplayer.GetMonsterName(i)
			if n != "":
				f.write(n + "\n" + str(i) + "\n")
		f.close()
		dbg.LogBox("Gotowe, ID mobów znajdziesz w ZAHON_MOD/Config/Another/Mob_ID.txt")
		try:
			os.startfile("ZAHON_MOD/Config/Another/Mob_ID.txt")
		except:
			pass		

	def Another_Get_All_Modules_func(self):
		b = '\n'.join(sys.modules.keys())
		f = open('ZAHON_MOD/Config/Another/All_Modules.txt','w')
		f.write(str(b))
		f.close()
		dbg.LogBox("Gotowe, wszystkie modu³y znajdziesz w ZAHON_MOD/Config/Another/All_Modules.txt")
		try:
			os.startfile("ZAHON_MOD/Config/Another/All_Modules.txt")
		except:
			pass			
		
	def Another_File_Extractor_func(self):
		if self.File_Extractor.IsShow():
			self.File_Extractor.Hide()
		else:
			self.File_Extractor.Show()	
		
	################################### File Extractor ##########################################			
		
	def File_Extractor_Status_func(self):
		File_Name = self.File_Extractor_Input_TxT_EditLine.GetText()
		if len(File_Name) == 0:
			self.Popup("You should enter a file name.")
			return
		add = ""
		if str(File_Name).find("d:/") != -1:
			File_Name = str(File_Name).replace("d:/", "")
			add = "d:/"
		if pack.Exist(add + File_Name):
			if not os.path.exists("ZAHON_MOD/Config/Another/" + File_Name):
				os.makedirs("ZAHON_MOD/Config/Another/" + File_Name)
			if os.path.exists("ZAHON_MOD/Config/Another/" + File_Name):
				if os.path.isfile("ZAHON_MOD/Config/Another/" + File_Name):
					os.remove("ZAHON_MOD/Config/Another/" + File_Name)
				else:
					os.rmdir("ZAHON_MOD/Config/Another/" + File_Name)
			if self.IsBinary(File_Name) == 0:
				lines = pack_open(add + File_Name, "r").readlines()
				f = open("ZAHON_MOD/Config/Another/" + File_Name, "a+")		
				for line in lines:
					tokens = line
					f.write(str(tokens))		
				f.close()
			else:
				Binary = pack_open(add + File_Name, 'rb')
				Bytes = Binary.read()
				if len(Bytes) == 0:
					if self.Errortype != "ending":
						self.Errortype = "read"
						self.Popup(str(add + File_Name)+" couldn't read.")
					return
				else:
					f = open("ZAHON_MOD/Config/Another/" + File_Name, "wb")		
					f.write(str(Bytes))		
					f.close()
		else:
			self.Errortype = "exist"
			self.Popup(str(add + File_Name)+" doesn't exist.")
			return
			
		self.Popup("Extraction successfully completed.")

	def IsBinary(self, File_Name):
		if str(File_Name).count(".") == 0:
			self.Errortype = "ending"
			self.Popup(str(File_Name)+" has no file extension.")
			File_Name = File_Name + ".binary"
		Split = File_Name.split(".")
		end = str(Split[1])
		end = end.lower()
		
		if end == ".py": 
			return 0 
		else:
			return 1
			
			
	### Popup ###		
			
	def Popup(self, error=""):
		Popup_Dialog = uiCommon.PopupDialog()
		Popup_Dialog.SetText(error)
		Popup_Dialog.SetAcceptEvent(self.Close_Popup_Dialog)
		Popup_Dialog.Open()
		self.Popup_Dialog = Popup_Dialog
		
	def Close_Popup_Dialog(self):
		self.pop = None		
				
	def OnUpdate(self):			
		pass
	
	def __BuildKeyDict(self):
		onPressKeyDict = {}
		onPressKeyDict[app.DIK_F5]	= lambda : self.OpenWindow()
		self.onPressKeyDict = onPressKeyDict
	
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
	
	def Another_Gui_Close(self):
		self.Another_Gui.Hide()
		
	def File_Extractor_Close(self):
		self.File_Extractor.Hide()		

	def File_Extractor_List_Close(self):
		self.File_Extractor_List.Hide()
				
		
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
			return		
		
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
		
	def ButtonHide(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Hide()
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
		return SlotBar, Value

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
		
	def EditLineHide(self, parent, editlineText, x, y, width, heigh, max):
		SlotBarHide = ui.SlotBar()
		if parent != None:
			SlotBarHide.SetParent(parent)
		SlotBarHide.SetSize(width, heigh)
		SlotBarHide.SetPosition(x, y)
		SlotBarHide.Hide()
		Value = ui.EditLine()
		Value.SetParent(SlotBarHide)
		Value.SetSize(width, heigh)
		Value.SetPosition(1, 1)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetMultiLine()
		Value.SetText(editlineText)
		Value.Show()
		return SlotBarHide, Value

	def TextLineHide(self, parent, textlineText, x, y, color):
		textline = ui.TextLine()
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.Hide()
		return textline

	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)

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
		
	def ComboBoxHide(self, parent, text, x, y, width):
		combo = ui.ComboBox()
		if parent != None:
			combo.SetParent(parent)
		combo.SetPosition(x, y)
		combo.SetSize(width, 15)
		combo.SetCurrentItem(text)
		combo.Hide()
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
		
	def ThinBoardHide(self, parent, moveable, x, y, width, heigh, center):
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
		thin.Hide()
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
		bar.SetColor(0x77000000)
		bar.Show()
		ListBox=ui.ListBoxEx()
		ListBox.SetParent(bar)
		ListBox.SetPosition(0, 0)
		ListBox.SetSize(width, heigh)
		ListBox.Show()
		scroll = ui.ScrollBar()
		scroll.SetParent(ListBox)
		scroll.SetPosition(width-15, 0)
		scroll.SetScrollBarSize(heigh)
		scroll.Show()
		ListBox.SetScrollBar(scroll)
		return bar, ListBox
		
	def HorizontalBar(self, parent, x, y, Create):
		horizontalBar = ui.HorizontalBar()
		if parent != None:
			horizontalBar.SetParent(parent)
		horizontalBar.SetPosition(x, y)
		horizontalBar.Create(Create)
		horizontalBar.Show()
		return horizontalBar
		
	def TextLine_SetPackedFontColor(self, parent, textlineText, x, y, color):
		TextLine_SetPackedFontColor = ui.TextLine()
		if parent != None:
			TextLine_SetPackedFontColor.SetParent(parent)
		TextLine_SetPackedFontColor.SetPosition(x, y)
		TextLine_SetPackedFontColor.SetPackedFontColor(color)
		TextLine_SetPackedFontColor.SetText(textlineText)
		TextLine_SetPackedFontColor.Show()
		return TextLine_SetPackedFontColor
		
	def HorizontalBarHide(self, parent, x, y, Create):
		horizontalBar = ui.HorizontalBar()
		if parent != None:
			horizontalBar.SetParent(parent)
		horizontalBar.SetPosition(x, y)
		horizontalBar.Create(Create)
		horizontalBar.Hide()
		return horizontalBar
		
	def TextLine_SetPackedFontColorHide(self, parent, textlineText, x, y, color):
		TextLine_SetPackedFontColor = ui.TextLine()
		if parent != None:
			TextLine_SetPackedFontColor.SetParent(parent)
		TextLine_SetPackedFontColor.SetPosition(x, y)
		TextLine_SetPackedFontColor.SetPackedFontColor(color)
		TextLine_SetPackedFontColor.SetText(textlineText)
		TextLine_SetPackedFontColor.Hide()
		return TextLine_SetPackedFontColor
		
	def GetCurrentText(self):
		return self.textLine.GetText()
	def OnSelectItem(self, index, name):
		self.SetCurrentItem(name)
		self.CloseListBox()
		self.event()
	ui.ComboBox.GetCurrentText = GetCurrentText
	ui.ComboBox.OnSelectItem = OnSelectItem	
		
class Item(ui.ListBoxEx.Item):
	def __init__(self, text):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=text
		self.textLine=self.__CreateTextLine(text[:50])
	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)
	def GetText(self):
		return self.text
	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 5*len(self.textLine.GetText()) + 4, height)
	def __CreateTextLine(self, text):
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 0)
		textLine.SetText(text)
		textLine.Show()
		return textLine		

ZAHON_MOD().Show()
