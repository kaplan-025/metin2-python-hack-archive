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

Auto_Attack = 0

Mobber = 0
Mobber_Mode = 1
Mobber_Delay = 0
Mobber_ID = 0
Mobber_Icon = 0
Mobber_Mode_Combobox = ["Pelerynki", "1_Slot"]

Pick_Up = 0

Poty = 0
Poty_1_ID = 27003
Poty_1_Icon = 0
Poty_2_ID = 27006
Poty_2_Icon = 0

Restart = 0

Use_Item = 0
Use_Item_Delay = 1
Use_Item_Delay_ok = 1
Use_Item_Delay_Mode_ComboBox = ["Minut", "Sekund"]

Item_1_ID = 0
Item_2_ID = 0
Item_3_ID = 0
Item_4_ID = 0
Item_5_ID = 0
Item_6_ID = 0
Item_7_ID = 0
Item_8_ID = 0
Item_9_ID = 0
Item_10_ID = 0
Item_11_ID = 0
Item_12_ID = 0
Item_13_ID = 0
Item_14_ID = 0
Item_15_ID = 0
Item_16_ID = 0
Item_17_ID = 0
Item_18_ID = 0
Item_19_ID = 0
Item_20_ID = 0
Item_21_ID = 0
Item_22_ID = 0
Item_23_ID = 0
Item_24_ID = 0
Item_25_ID = 0

Item_1_Icon = 0
Item_2_Icon = 0
Item_3_Icon = 0
Item_4_Icon = 0
Item_5_Icon = 0
Item_6_Icon = 0
Item_7_Icon = 0
Item_8_Icon = 0
Item_9_Icon = 0
Item_10_Icon = 0
Item_11_Icon = 0
Item_12_Icon = 0
Item_13_Icon = 0
Item_14_Icon = 0
Item_15_Icon = 0
Item_16_Icon = 0
Item_17_Icon = 0
Item_18_Icon = 0
Item_19_Icon = 0
Item_20_Icon = 0
Item_21_Icon = 0
Item_22_Icon = 0
Item_23_Icon = 0
Item_24_Icon = 0
Item_25_Icon = 0

# d:/ymir work/ui/public/Slot_Base.sub

class Mini_MH(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()
		self.Load_func()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(200, 275)
		self.Board.SetCenterPosition()
		self.Board.AddFlag('movable')
		self.Board.AddFlag('float')
		self.Board.SetTitleName('Mini MultiHack')
		self.Board.SetCloseEvent(self.Close)
		self.Board.Show()
		
		self.About = ui.BoardWithTitleBar()
		self.About.SetSize(200, 90)
		self.About.SetCenterPosition()
		self.About.AddFlag('movable')
		self.About.AddFlag('float')
		self.About.SetTitleName('Informacje')
		self.About.SetCloseEvent(self.About_Close)
		self.About.Hide()		
		
		self.__BuildKeyDict()
		self.comp = Component()
		
		# self.tooltipItem = uiToolTip.ItemToolTip()		
				
	################################### Slot #######################################		
		
	### Mobber ###	
		self.Mobber_Slot = ui.ExpandedImageBox()
		self.Mobber_Slot.SetParent(self.Board)
		self.Mobber_Slot.SetPosition(80, 60)
		self.Mobber_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Mobber_Slot.OnMouseLeftButtonUp = lambda: self.Set_Mobber_ID()
		self.Mobber_Slot.OnMouseRightButtonDown = lambda: self.Delete_Mobber_ID()
		self.Mobber_Slot.Hide()
		
		item.SelectItem(int(Mobber_ID))
		Mobber_Icon = item.GetIconImageFileName()		
		self.Item_Mobber_Slot = ui.ExpandedImageBox()
		self.Item_Mobber_Slot.SetParent(self.Board)
		self.Item_Mobber_Slot.SetPosition(80, 60)
		self.Item_Mobber_Slot.LoadImage(str(Mobber_Icon))
		self.Item_Mobber_Slot.OnMouseLeftButtonUp = lambda: self.Set_Mobber_ID()
		self.Item_Mobber_Slot.OnMouseRightButtonDown = lambda: self.Delete_Mobber_ID()
		self.Item_Mobber_Slot.Hide()	
		
	### Poty ###	
		self.Poty_1_Slot = ui.ExpandedImageBox()
		self.Poty_1_Slot.SetParent(self.Board)
		self.Poty_1_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Poty_1_Slot.OnMouseLeftButtonUp = lambda: self.Set_Poty_1_ID()
		self.Poty_1_Slot.OnMouseRightButtonDown = lambda: self.Delete_Poty_1_ID()
		self.Poty_1_Slot.SetPosition(60,172)
		self.Poty_1_Slot.Hide()	

		item.SelectItem(int(Poty_1_ID))
		Poty_1_Icon = item.GetIconImageFileName()		
		self.Item_Poty_1_Slot = ui.ExpandedImageBox()
		self.Item_Poty_1_Slot.SetParent(self.Board)
		self.Item_Poty_1_Slot.SetPosition(60, 172)
		self.Item_Poty_1_Slot.LoadImage(str(Poty_1_Icon))
		self.Item_Poty_1_Slot.OnMouseLeftButtonUp = lambda: self.Set_Poty_1_ID()
		self.Item_Poty_1_Slot.OnMouseRightButtonDown = lambda: self.Delete_Poty_1_ID()
		self.Item_Poty_1_Slot.Hide()

		self.Poty_2_Slot = ui.ExpandedImageBox()
		self.Poty_2_Slot.SetParent(self.Board)
		self.Poty_2_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Poty_2_Slot.OnMouseLeftButtonUp = lambda: self.Set_Poty_2_ID()
		self.Poty_2_Slot.OnMouseRightButtonDown = lambda: self.Delete_Poty_2_ID()
		self.Poty_2_Slot.SetPosition(92,172)
		self.Poty_2_Slot.Hide()	

		item.SelectItem(int(Poty_2_ID))
		Poty_2_Icon = item.GetIconImageFileName()		
		self.Item_Poty_2_Slot = ui.ExpandedImageBox()
		self.Item_Poty_2_Slot.SetParent(self.Board)
		self.Item_Poty_2_Slot.SetPosition(92, 172)
		self.Item_Poty_2_Slot.LoadImage(str(Poty_2_Icon))
		self.Item_Poty_2_Slot.OnMouseLeftButtonUp = lambda: self.Set_Poty_2_ID()
		self.Item_Poty_2_Slot.OnMouseRightButtonDown = lambda: self.Delete_Poty_2_ID()
		self.Item_Poty_2_Slot.Hide()		
				
	################################### Sloty #############################################
			
		self.Item_1_Slot = ui.ExpandedImageBox()
		self.Item_1_Slot.SetParent(self.Board)
		self.Item_1_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		# self.Item_1_Slot.OnMouseLeftButtonUp = lambda: self.Set_Item_1_ID()
		# self.Item_1_Slot.OnMouseRightButtonUp = lambda: self.Delete_Item_1_ID()
		self.Item_1_Slot.SetPosition(19,60)
		self.Item_1_Slot.Hide()	

		item.SelectItem(int(Item_1_ID))
		Item_1_Icon = item.GetIconImageFileName()		
		self.Item_1_Icon = ui.ExpandedImageBox()
		self.Item_1_Icon.SetParent(self.Board)
		self.Item_1_Icon.SetPosition(19, 60)
		self.Item_1_Icon.LoadImage(str(Item_1_Icon))
		self.Item_1_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_1_ID()
		self.Item_1_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_1_ID()
		self.Item_1_Icon.Hide()	
		
		self.Item_2_Slot = ui.ExpandedImageBox()
		self.Item_2_Slot.SetParent(self.Board)
		self.Item_2_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_2_Slot.SetPosition(51,60)
		self.Item_2_Slot.Hide()	

		item.SelectItem(int(Item_2_ID))
		Item_2_Icon = item.GetIconImageFileName()		
		self.Item_2_Icon = ui.ExpandedImageBox()
		self.Item_2_Icon.SetParent(self.Board)
		self.Item_2_Icon.SetPosition(51, 60)
		self.Item_2_Icon.LoadImage(str(Item_2_Icon))
		self.Item_2_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_2_ID()
		self.Item_2_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_2_ID()
		self.Item_2_Icon.Hide()	
		
		self.Item_3_Slot = ui.ExpandedImageBox()
		self.Item_3_Slot.SetParent(self.Board)
		self.Item_3_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_3_Slot.SetPosition(83,60)
		self.Item_3_Slot.Hide()	

		item.SelectItem(int(Item_3_ID))
		Item_3_Icon = item.GetIconImageFileName()		
		self.Item_3_Icon = ui.ExpandedImageBox()
		self.Item_3_Icon.SetParent(self.Board)
		self.Item_3_Icon.SetPosition(83, 60)
		self.Item_3_Icon.LoadImage(str(Item_3_Icon))
		self.Item_3_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_3_ID()
		self.Item_3_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_3_ID()
		self.Item_3_Icon.Hide()	
		
		self.Item_4_Slot = ui.ExpandedImageBox()
		self.Item_4_Slot.SetParent(self.Board)
		self.Item_4_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_4_Slot.SetPosition(115,60)
		self.Item_4_Slot.Hide()	

		item.SelectItem(int(Item_4_ID))
		Item_4_Icon = item.GetIconImageFileName()		
		self.Item_4_Icon = ui.ExpandedImageBox()
		self.Item_4_Icon.SetParent(self.Board)
		self.Item_4_Icon.SetPosition(115, 60)
		self.Item_4_Icon.LoadImage(str(Item_4_Icon))
		self.Item_4_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_4_ID()
		self.Item_4_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_4_ID()
		self.Item_4_Icon.Hide()	
		
		self.Item_5_Slot = ui.ExpandedImageBox()
		self.Item_5_Slot.SetParent(self.Board)
		self.Item_5_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_5_Slot.SetPosition(147,60)
		self.Item_5_Slot.Hide()	

		item.SelectItem(int(Item_5_ID))
		Item_5_Icon = item.GetIconImageFileName()		
		self.Item_5_Icon = ui.ExpandedImageBox()
		self.Item_5_Icon.SetParent(self.Board)
		self.Item_5_Icon.SetPosition(147, 60)
		self.Item_5_Icon.LoadImage(str(Item_5_Icon))
		self.Item_5_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_5_ID()
		self.Item_5_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_5_ID()
		self.Item_5_Icon.Hide()					
				
		self.Item_6_Slot = ui.ExpandedImageBox()
		self.Item_6_Slot.SetParent(self.Board)
		self.Item_6_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_6_Slot.SetPosition(19,92)
		self.Item_6_Slot.Hide()	

		item.SelectItem(int(Item_6_ID))
		Item_6_Icon = item.GetIconImageFileName()		
		self.Item_6_Icon = ui.ExpandedImageBox()
		self.Item_6_Icon.SetParent(self.Board)
		self.Item_6_Icon.SetPosition(19, 92)
		self.Item_6_Icon.LoadImage(str(Item_6_Icon))
		self.Item_6_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_6_ID()
		self.Item_6_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_6_ID()
		self.Item_6_Icon.Hide()	
		
		self.Item_7_Slot = ui.ExpandedImageBox()
		self.Item_7_Slot.SetParent(self.Board)
		self.Item_7_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_7_Slot.SetPosition(51,92)
		self.Item_7_Slot.Hide()	

		item.SelectItem(int(Item_7_ID))
		Item_7_Icon = item.GetIconImageFileName()		
		self.Item_7_Icon = ui.ExpandedImageBox()
		self.Item_7_Icon.SetParent(self.Board)
		self.Item_7_Icon.SetPosition(51, 92)
		self.Item_7_Icon.LoadImage(str(Item_7_Icon))
		self.Item_7_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_7_ID()
		self.Item_7_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_7_ID()
		self.Item_7_Icon.Hide()	
		
		self.Item_8_Slot = ui.ExpandedImageBox()
		self.Item_8_Slot.SetParent(self.Board)
		self.Item_8_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_8_Slot.SetPosition(83,92)
		self.Item_8_Slot.Hide()	

		item.SelectItem(int(Item_8_ID))
		Item_8_Icon = item.GetIconImageFileName()		
		self.Item_8_Icon = ui.ExpandedImageBox()
		self.Item_8_Icon.SetParent(self.Board)
		self.Item_8_Icon.SetPosition(83, 92)
		self.Item_8_Icon.LoadImage(str(Item_8_Icon))
		self.Item_8_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_8_ID()
		self.Item_8_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_8_ID()
		self.Item_8_Icon.Hide()	
		
		self.Item_9_Slot = ui.ExpandedImageBox()
		self.Item_9_Slot.SetParent(self.Board)
		self.Item_9_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_9_Slot.SetPosition(115,92)
		self.Item_9_Slot.Hide()	

		item.SelectItem(int(Item_9_ID))
		Item_9_Icon = item.GetIconImageFileName()		
		self.Item_9_Icon = ui.ExpandedImageBox()
		self.Item_9_Icon.SetParent(self.Board)
		self.Item_9_Icon.SetPosition(115, 92)
		self.Item_9_Icon.LoadImage(str(Item_9_Icon))
		self.Item_9_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_9_ID()
		self.Item_9_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_9_ID()
		self.Item_9_Icon.Hide()	
		
		self.Item_10_Slot = ui.ExpandedImageBox()
		self.Item_10_Slot.SetParent(self.Board)
		self.Item_10_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_10_Slot.SetPosition(147,92)
		self.Item_10_Slot.Hide()	

		item.SelectItem(int(Item_10_ID))
		Item_10_Icon = item.GetIconImageFileName()		
		self.Item_10_Icon = ui.ExpandedImageBox()
		self.Item_10_Icon.SetParent(self.Board)
		self.Item_10_Icon.SetPosition(147, 92)
		self.Item_10_Icon.LoadImage(str(Item_10_Icon))
		self.Item_10_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_10_ID()
		self.Item_10_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_10_ID()
		self.Item_10_Icon.Hide()	

		self.Item_11_Slot = ui.ExpandedImageBox()
		self.Item_11_Slot.SetParent(self.Board)
		self.Item_11_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_11_Slot.SetPosition(19,124)
		self.Item_11_Slot.Hide()	

		item.SelectItem(int(Item_11_ID))
		Item_11_Icon = item.GetIconImageFileName()		
		self.Item_11_Icon = ui.ExpandedImageBox()
		self.Item_11_Icon.SetParent(self.Board)
		self.Item_11_Icon.SetPosition(19, 124)
		self.Item_11_Icon.LoadImage(str(Item_11_Icon))
		self.Item_11_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_11_ID()
		self.Item_11_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_11_ID()
		self.Item_11_Icon.Hide()	

		self.Item_12_Slot = ui.ExpandedImageBox()
		self.Item_12_Slot.SetParent(self.Board)
		self.Item_12_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_12_Slot.SetPosition(51,124)
		self.Item_12_Slot.Hide()	

		item.SelectItem(int(Item_12_ID))
		Item_12_Icon = item.GetIconImageFileName()		
		self.Item_12_Icon = ui.ExpandedImageBox()
		self.Item_12_Icon.SetParent(self.Board)
		self.Item_12_Icon.SetPosition(51, 124)
		self.Item_12_Icon.LoadImage(str(Item_12_Icon))
		self.Item_12_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_12_ID()
		self.Item_12_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_12_ID()
		self.Item_12_Icon.Hide()

		self.Item_13_Slot = ui.ExpandedImageBox()
		self.Item_13_Slot.SetParent(self.Board)
		self.Item_13_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_13_Slot.SetPosition(83,124)
		self.Item_13_Slot.Hide()	

		item.SelectItem(int(Item_13_ID))
		Item_13_Icon = item.GetIconImageFileName()		
		self.Item_13_Icon = ui.ExpandedImageBox()
		self.Item_13_Icon.SetParent(self.Board)
		self.Item_13_Icon.SetPosition(83, 124)
		self.Item_13_Icon.LoadImage(str(Item_13_Icon))
		self.Item_13_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_13_ID()
		self.Item_13_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_13_ID()
		self.Item_13_Icon.Hide()

		self.Item_14_Slot = ui.ExpandedImageBox()
		self.Item_14_Slot.SetParent(self.Board)
		self.Item_14_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_14_Slot.SetPosition(115,124)
		self.Item_14_Slot.Hide()	

		item.SelectItem(int(Item_14_ID))
		Item_14_Icon = item.GetIconImageFileName()		
		self.Item_14_Icon = ui.ExpandedImageBox()
		self.Item_14_Icon.SetParent(self.Board)
		self.Item_14_Icon.SetPosition(115, 124)
		self.Item_14_Icon.LoadImage(str(Item_14_Icon))
		self.Item_14_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_14_ID()
		self.Item_14_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_14_ID()
		self.Item_14_Icon.Hide()	

		self.Item_15_Slot = ui.ExpandedImageBox()
		self.Item_15_Slot.SetParent(self.Board)
		self.Item_15_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_15_Slot.SetPosition(147,124)
		self.Item_15_Slot.Hide()	

		item.SelectItem(int(Item_15_ID))
		Item_15_Icon = item.GetIconImageFileName()		
		self.Item_15_Icon = ui.ExpandedImageBox()
		self.Item_15_Icon.SetParent(self.Board)
		self.Item_15_Icon.SetPosition(147, 124)
		self.Item_15_Icon.LoadImage(str(Item_15_Icon))
		self.Item_15_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_15_ID()
		self.Item_15_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_15_ID()
		self.Item_15_Icon.Hide()

		self.Item_16_Slot = ui.ExpandedImageBox()
		self.Item_16_Slot.SetParent(self.Board)
		self.Item_16_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_16_Slot.SetPosition(19,156)
		self.Item_16_Slot.Hide()	

		item.SelectItem(int(Item_16_ID))
		Item_16_Icon = item.GetIconImageFileName()		
		self.Item_16_Icon = ui.ExpandedImageBox()
		self.Item_16_Icon.SetParent(self.Board)
		self.Item_16_Icon.SetPosition(19, 156)
		self.Item_16_Icon.LoadImage(str(Item_16_Icon))
		self.Item_16_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_16_ID()
		self.Item_16_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_16_ID()
		self.Item_16_Icon.Hide()

		self.Item_17_Slot = ui.ExpandedImageBox()
		self.Item_17_Slot.SetParent(self.Board)
		self.Item_17_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_17_Slot.SetPosition(51,156)
		self.Item_17_Slot.Hide()	

		item.SelectItem(int(Item_17_ID))
		Item_17_Icon = item.GetIconImageFileName()		
		self.Item_17_Icon = ui.ExpandedImageBox()
		self.Item_17_Icon.SetParent(self.Board)
		self.Item_17_Icon.SetPosition(51, 156)
		self.Item_17_Icon.LoadImage(str(Item_17_Icon))
		self.Item_17_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_17_ID()
		self.Item_17_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_17_ID()
		self.Item_17_Icon.Hide()		
	
		self.Item_18_Slot = ui.ExpandedImageBox()
		self.Item_18_Slot.SetParent(self.Board)
		self.Item_18_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_18_Slot.SetPosition(83,156)
		self.Item_18_Slot.Hide()	

		item.SelectItem(int(Item_18_ID))
		Item_18_Icon = item.GetIconImageFileName()		
		self.Item_18_Icon = ui.ExpandedImageBox()
		self.Item_18_Icon.SetParent(self.Board)
		self.Item_18_Icon.SetPosition(83, 156)
		self.Item_18_Icon.LoadImage(str(Item_18_Icon))
		self.Item_18_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_18_ID()
		self.Item_18_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_18_ID()
		self.Item_18_Icon.Hide()		
	
		self.Item_19_Slot = ui.ExpandedImageBox()
		self.Item_19_Slot.SetParent(self.Board)
		self.Item_19_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_19_Slot.SetPosition(115,156)
		self.Item_19_Slot.Hide()	

		item.SelectItem(int(Item_19_ID))
		Item_19_Icon = item.GetIconImageFileName()		
		self.Item_19_Icon = ui.ExpandedImageBox()
		self.Item_19_Icon.SetParent(self.Board)
		self.Item_19_Icon.SetPosition(115, 156)
		self.Item_19_Icon.LoadImage(str(Item_19_Icon))
		self.Item_19_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_19_ID()
		self.Item_19_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_19_ID()
		self.Item_19_Icon.Hide()
		
		self.Item_20_Slot = ui.ExpandedImageBox()
		self.Item_20_Slot.SetParent(self.Board)
		self.Item_20_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_20_Slot.SetPosition(147,156)
		self.Item_20_Slot.Hide()	

		item.SelectItem(int(Item_20_ID))
		Item_20_Icon = item.GetIconImageFileName()		
		self.Item_20_Icon = ui.ExpandedImageBox()
		self.Item_20_Icon.SetParent(self.Board)
		self.Item_20_Icon.SetPosition(147, 156)
		self.Item_20_Icon.LoadImage(str(Item_20_Icon))
		self.Item_20_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_20_ID()
		self.Item_20_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_20_ID()
		self.Item_20_Icon.Hide()	

		self.Item_21_Slot = ui.ExpandedImageBox()
		self.Item_21_Slot.SetParent(self.Board)
		self.Item_21_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_21_Slot.SetPosition(19,188)
		self.Item_21_Slot.Hide()	

		item.SelectItem(int(Item_21_ID))
		Item_21_Icon = item.GetIconImageFileName()		
		self.Item_21_Icon = ui.ExpandedImageBox()
		self.Item_21_Icon.SetParent(self.Board)
		self.Item_21_Icon.SetPosition(19, 188)
		self.Item_21_Icon.LoadImage(str(Item_21_Icon))
		self.Item_21_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_21_ID()
		self.Item_21_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_21_ID()
		self.Item_21_Icon.Hide()
		
		self.Item_22_Slot = ui.ExpandedImageBox()
		self.Item_22_Slot.SetParent(self.Board)
		self.Item_22_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_22_Slot.SetPosition(51,188)
		self.Item_22_Slot.Hide()	

		item.SelectItem(int(Item_22_ID))
		Item_22_Icon = item.GetIconImageFileName()		
		self.Item_22_Icon = ui.ExpandedImageBox()
		self.Item_22_Icon.SetParent(self.Board)
		self.Item_22_Icon.SetPosition(51, 188)
		self.Item_22_Icon.LoadImage(str(Item_22_Icon))
		self.Item_22_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_22_ID()
		self.Item_22_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_22_ID()
		self.Item_22_Icon.Hide()
		
		self.Item_23_Slot = ui.ExpandedImageBox()
		self.Item_23_Slot.SetParent(self.Board)
		self.Item_23_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_23_Slot.SetPosition(83,188)
		self.Item_23_Slot.Hide()	

		item.SelectItem(int(Item_23_ID))
		Item_23_Icon = item.GetIconImageFileName()		
		self.Item_23_Icon = ui.ExpandedImageBox()
		self.Item_23_Icon.SetParent(self.Board)
		self.Item_23_Icon.SetPosition(83, 188)
		self.Item_23_Icon.LoadImage(str(Item_23_Icon))
		self.Item_23_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_23_ID()
		self.Item_23_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_23_ID()
		self.Item_23_Icon.Hide()
		
		self.Item_24_Slot = ui.ExpandedImageBox()
		self.Item_24_Slot.SetParent(self.Board)
		self.Item_24_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_24_Slot.SetPosition(115,188)
		self.Item_24_Slot.Hide()	

		item.SelectItem(int(Item_24_ID))
		Item_24_Icon = item.GetIconImageFileName()		
		self.Item_24_Icon = ui.ExpandedImageBox()
		self.Item_24_Icon.SetParent(self.Board)
		self.Item_24_Icon.SetPosition(115, 188)
		self.Item_24_Icon.LoadImage(str(Item_24_Icon))
		self.Item_24_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_24_ID()
		self.Item_24_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_24_ID()
		self.Item_24_Icon.Hide()
		
		self.Item_25_Slot = ui.ExpandedImageBox()
		self.Item_25_Slot.SetParent(self.Board)
		self.Item_25_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")
		self.Item_25_Slot.SetPosition(147,188)
		self.Item_25_Slot.Hide()	

		item.SelectItem(int(Item_25_ID))
		Item_25_Icon = item.GetIconImageFileName()		
		self.Item_25_Icon = ui.ExpandedImageBox()
		self.Item_25_Icon.SetParent(self.Board)
		self.Item_25_Icon.SetPosition(147, 188)
		self.Item_25_Icon.LoadImage(str(Item_25_Icon))
		self.Item_25_Icon.OnMouseLeftButtonUp = lambda: self.Set_Item_25_ID()
		self.Item_25_Icon.OnMouseRightButtonDown = lambda: self.Delete_Item_25_ID()
		self.Item_25_Icon.Hide()		
				
	################################### HorizontalBars ###################################		
				
		self.Mobber_HorizontalBar = self.comp.HorizontalBarHide(self.Board , 10, 40, 180)
		self.Mobber_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Mobber_HorizontalBar, 'Mobber', 5, 0, 0xFFFFE3AD)			

		self.Use_Item_HorizontalBar = self.comp.HorizontalBarHide(self.Board , 10, 40, 180)
		self.Use_Item_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Use_Item_HorizontalBar, 'U¿ywanie Dopalaczy', 5, 0, 0xFFFFE3AD)			
				
		self.Poty_HorizontalBar = self.comp.HorizontalBarHide(self.Board , 10, 152, 180)
		self.Poty_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Poty_HorizontalBar, 'Automatyczne Potowanie', 5, 0, 0xFFFFE3AD)			
		
		self.Site_HorizontalBar = self.comp.HorizontalBar(self.Board , 10, 220, 180)
		self.Site_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Site_HorizontalBar, 'Strony', 5, 0, 0xFFFFE3AD)			
	
	### About ###
	
		self.About_HorizontalBar = self.comp.HorizontalBar(self.About , 10, 40, 180)
		self.About_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.About_HorizontalBar, 'Mini MultiHack v1.0 by ZAHON', 5, 0, 0xFFFFE3AD)			
		
	################################### Buttony #########################################	
		
		self.Auto_Attack_Button = self.comp.Button(self.Board, 'Auto Atak', '', 10, 40, self.Auto_Attack_func, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')		
		self.Mobber_Button = self.comp.Button(self.Board, 'Mobber', '', 10, 70, self.Mobber_func, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')
		self.Pick_Up_Button = self.comp.Button(self.Board, 'Pick Up', '', 10, 100, self.Pick_Up_func, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')
		self.Poty_Button = self.comp.Button(self.Board, 'Automatyczne Potowanie', '', 10, 130, self.Poty_func, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')
		self.Restart_Button = self.comp.Button(self.Board, 'Automatyczne Wstawanie', '', 10, 160, self.Restart_func, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')
		self.Use_Item_Button = self.comp.Button(self.Board, 'U¿ywanie Dopalaczy', '', 10, 190, self.Use_Item_func, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')
		
		self.Site_1_Button = self.comp.Button(self.Board, 'I', '', 10, 240, self.Site_1_func, 'd:/ymir work/ui/game/windows/tab_button_middle_01.sub', 'd:/ymir work/ui/game/windows/tab_button_middle_02.sub', 'd:/ymir work/ui/game/windows/tab_button_middle_03.sub')
		self.Site_2_Button = self.comp.Button(self.Board, 'II', '', 73, 240, self.Site_2_func, 'd:/ymir work/ui/game/windows/tab_button_middle_01.sub', 'd:/ymir work/ui/game/windows/tab_button_middle_02.sub', 'd:/ymir work/ui/game/windows/tab_button_middle_03.sub')
		self.Site_3_Button = self.comp.Button(self.Board, 'III', '', 135, 240, self.Site_3_func, 'd:/ymir work/ui/game/windows/tab_button_middle_01.sub', 'd:/ymir work/ui/game/windows/tab_button_middle_02.sub', 'd:/ymir work/ui/game/windows/tab_button_middle_03.sub')
		
		self.About_Button = self.comp.Button(self.Board, '', 'Informacje', 150, 8, self.About_func, 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_01.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_02.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_03.sub')
		
	### About ###

		self.FaceBook_Button = self.comp.Button(self.About, 'FB', '', 10, 60, self.FaceBook_func, 'd:/ymir work/ui/game/windows/tab_button_middle_01.sub', 'd:/ymir work/ui/game/windows/tab_button_middle_02.sub', 'd:/ymir work/ui/game/windows/tab_button_middle_03.sub')
		self.YouTube_Button = self.comp.Button(self.About, 'YT', '', 73, 60, self.YouTube_func, 'd:/ymir work/ui/game/windows/tab_button_middle_01.sub', 'd:/ymir work/ui/game/windows/tab_button_middle_02.sub', 'd:/ymir work/ui/game/windows/tab_button_middle_03.sub')
		self.MPC_Button = self.comp.Button(self.About, 'MPC', '', 135, 60, self.MPC_func, 'd:/ymir work/ui/game/windows/tab_button_middle_01.sub', 'd:/ymir work/ui/game/windows/tab_button_middle_02.sub', 'd:/ymir work/ui/game/windows/tab_button_middle_03.sub')
		
	################################## Slotbar i Text ###################################	

		self.Mobber_Info_Text = self.comp.TextLineHide(self.Board, 'Przeci¹gnij pelerynki aby pobraæ ich id', 14, 92, self.comp.RGB(255, 255, 255))			
		self.Mobber_Mode_Text = self.comp.TextLineHide(self.Board, 'Rodzaj Mobbera', 14, 112, self.comp.RGB(255, 255, 255))			
		self.Mobber_Delay_Text = self.comp.TextLineHide(self.Board, 'OpóŸnienie:', 14, 132, self.comp.RGB(255, 255, 255))		
		self.slotbar_Mobber_Delay, self.Mobber_Delay_EditLine = self.comp.EditLineHide(self.Board, '0.1', 125, 132, 60, 15, 10)

		self.Poty_1_Text = self.comp.TextLineHide(self.Board, '0', 74, 204, self.comp.RGB(255, 255, 255))			
		self.Poty_2_Text = self.comp.TextLineHide(self.Board, '0', 106, 204, self.comp.RGB(255, 255, 255))			
		
		self.Use_Item_Delay_Text = self.comp.TextLineHide(self.Board, 'Co ile u¿ywaæ:', 14, 222, self.comp.RGB(255, 255, 255))		
		self.slotbar_Use_Item_Delay, self.Use_Item_Delay_EditLine = self.comp.EditLineHide(self.Board, '1', 145, 222, 30, 15, 5)
						
	################################## Combo Box ###################################		
		
		self.Mobber_Mode_ComboBox = self.comp.ComboBoxHide(self.Board, 'Pelerynki', 125, 112, 60)	
	
		for Mobber_Mode_ComboBox in Mobber_Mode_Combobox:
			self.Mobber_Mode_ComboBox.InsertItem(1,str(Mobber_Mode_ComboBox)) 	
			
		global Use_Item_Delay_Mode_ComboBox
		
		self.Use_Item_Delay_Mode_ComboBox = self.comp.ComboBoxHide(self.Board, 'Minut', 85, 222, 45)	
	
		for Use_Item_Delay_Mode_ComboBox in Use_Item_Delay_Mode_ComboBox:
			self.Use_Item_Delay_Mode_ComboBox.InsertItem(1,str(Use_Item_Delay_Mode_ComboBox)) 			
		
	################################### Auto Attack Func ##########################################		
	
	def Auto_Attack_func(self):	
		global Auto_Attack
		if Auto_Attack == 0:
			Auto_Attack = 1
			self.Enable_Auto_Attack()
			self.Auto_Attack_Button.SetUpVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
			self.Auto_Attack_Button.SetOverVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
			self.Auto_Attack_Button.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		else:
			Auto_Attack = 0
			self.Disable_Auto_Attack()
			self.Auto_Attack_Button.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
			self.Auto_Attack_Button.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")
			self.Auto_Attack_Button.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
					
	def Enable_Auto_Attack(self):
	
		player.SetAttackKeyState(TRUE)
				
		self.Delay_Auto_Attack = WaitingDialog()
		self.Delay_Auto_Attack.Open(float(0.1))
		self.Delay_Auto_Attack.SAFE_SetTimeOverEvent(self.Enable_Auto_Attack)
			
	def Disable_Auto_Attack(self):
	
		player.SetAttackKeyState(FALSE)
		
		self.Delay_Auto_Attack = WaitingDialog()
		self.Delay_Auto_Attack.Open(float(99999999999999999))
		self.Delay_Auto_Attack.SAFE_SetTimeOverEvent(self.Disable_Auto_Attack)		
	
	################################### Mobber Func ##########################################	

	def Mobber_func(self):
		global Mobber
		if Mobber == 0:
			Mobber = 1
			self.Enable_Mobber()
			self.Mobber_Button.SetUpVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
			self.Mobber_Button.SetOverVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
			self.Mobber_Button.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		else:
			Mobber = 0
			self.Mobber_Button.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
			self.Mobber_Button.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")
			self.Mobber_Button.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
	
	
	def Enable_Mobber(self):
		global Mobber
		global Mobber_Mode
		global Mobber_Delay
		global Mobber_ID
		
		if Mobber == 1:
		
			if Mobber_Mode == 1:
				for i in xrange(player.INVENTORY_PAGE_SIZE*5):
					ItemValue = player.GetItemIndex(i)
					if ItemValue == (int(Mobber_ID)):
						net.SendItemUsePacket(i)
						break
						
			if Mobber_Mode == 2:
				net.SendItemUsePacket(0)
								
		self.Delay_Mobber = WaitingDialog()
		self.Delay_Mobber.Open(float(Mobber_Delay))
		self.Delay_Mobber.SAFE_SetTimeOverEvent(self.Enable_Mobber)
				
	def Disable_Mobber(self):
		
		self.Delay_Mobber = WaitingDialog()
		self.Delay_Mobber.Open(float(99999999999999999))
		self.Delay_Mobber.SAFE_SetTimeOverEvent(self.Disable_Mobber)

	################################### Pick Up Func ###################################	

	def Pick_Up_func(self):
		global Pick_Up
		if Pick_Up == 0:
			Pick_Up = 1
			self.Enable_Pick_Up()
			self.Pick_Up_Button.SetUpVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
			self.Pick_Up_Button.SetOverVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
			self.Pick_Up_Button.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		else:	
			Pick_Up = 0
			self.Disable_Pick_Up()
			self.Pick_Up_Button.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
			self.Pick_Up_Button.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")
			self.Pick_Up_Button.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		
	def Enable_Pick_Up(self):
		
		player.PickCloseItem() 

		self.Delay_Pick_up = WaitingDialog()
		self.Delay_Pick_up.Open(float(0.1))
		self.Delay_Pick_up.SAFE_SetTimeOverEvent(self.Enable_Pick_Up)
			
	def Disable_Pick_Up(self):
	
		self.Delay_Pick_up = WaitingDialog()
		self.Delay_Pick_up.Open(float(99999999999999999))
		self.Delay_Pick_up.SAFE_SetTimeOverEvent(self.Disable_Pick_Up)				

	################################### Poty Func ###################################	

	def Poty_func(self):
		global Poty
		if Poty == 0:
			Poty = 1
			self.Enable_Poty()
			self.Poty_Button.SetUpVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
			self.Poty_Button.SetOverVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
			self.Poty_Button.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		else:
			Poty = 0
			self.Disable_Poty()
			self.Poty_Button.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
			self.Poty_Button.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")
			self.Poty_Button.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
			
	def Enable_Poty(self):
		global Poty 
		global Poty_1_ID
		global Poty_2_ID
		
		Max_HP = player.GetStatus(player.MAX_HP)
		Actually_HP = player.GetStatus(player.HP)
		
		Max_PE = player.GetStatus(player.MAX_SP)
		Actually_PE = player.GetStatus(player.SP)
			
		if Poty == 1:
			if (float(Actually_HP) / (float(Max_HP)) * 100) < int(100):
				for i in xrange(player.INVENTORY_PAGE_SIZE*3):
					Red_Poty_ID = player.GetItemIndex(i)
					if Red_Poty_ID == (int(Poty_1_ID)):
						net.SendItemUsePacket(i)
						break
						
		if Poty == 1:
			if (float(Actually_PE) / (float(Max_PE)) * 100) < int(100):
				for i in xrange(player.INVENTORY_PAGE_SIZE*3):
					Blue_Poty_ID = player.GetItemIndex(i)
					if Blue_Poty_ID == (int(Poty_2_ID)):
						net.SendItemUsePacket(i)
						break
			
		self.Delay_Poty = WaitingDialog()
		self.Delay_Poty.Open(float(0.1))
		self.Delay_Poty.SAFE_SetTimeOverEvent(self.Enable_Poty)
			
	def Disable_Poty(self):	
		self.Delay_Poty = WaitingDialog()
		self.Delay_Poty.Open(float(99999999999999999))
		self.Delay_Poty.SAFE_SetTimeOverEvent(self.Disable_Poty)	
		
	################################### Restart Func ###################################	

	def Restart_func(self):
		global Restart
		if Restart == 0:
			Restart = 1
			self.Enable_Restart()
			self.Restart_Button.SetUpVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
			self.Restart_Button.SetOverVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
			self.Restart_Button.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		else:	
			Restart = 0
			self.Disable_Restart()
			self.Restart_Button.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
			self.Restart_Button.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")
			self.Restart_Button.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
								
	def Enable_Restart(self):	

		net.SendChatPacket("/restart_here")
	
		self.Delay_Restart = WaitingDialog()
		self.Delay_Restart.Open(int(2.5))
		self.Delay_Restart.SAFE_SetTimeOverEvent(self.Enable_Restart)
		
	def Disable_Restart(self):		
		self.Delay_Restart = WaitingDialog()
		self.Delay_Restart.Open(float(99999999999999999))
		self.Delay_Restart.SAFE_SetTimeOverEvent(self.Disable_Restart)	

	################################### Use_Item Func ###################################	

	def Use_Item_func(self):
		global Use_Item
		global Use_Item_Delay
		global Use_Item_Delay_ok
		
		if Use_Item == 0:
			Use_Item = 1
			self.Enable_Use_Item()
			self.Use_Item_Button.SetUpVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
			self.Use_Item_Button.SetOverVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
			self.Use_Item_Button.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		else:
			Use_Item = 0
			self.Use_Item_Button.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
			self.Use_Item_Button.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")
			self.Use_Item_Button.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")		
			
		Delay = self.Use_Item_Delay_Mode_ComboBox.GetCurrentText()			
		
		if Delay == "Minut":
			Use_Item_Delay_ok = int(Use_Item_Delay * 60)
			# chat.AppendChat(chat.CHAT_TYPE_INFO, str(Use_Item_Delay_ok))
		else:
			Use_Item_Delay_ok = int(Use_Item_Delay)
			# chat.AppendChat(chat.CHAT_TYPE_INFO, str(Use_Item_Delay_ok))
					
	def Enable_Use_Item(self):
		global Item_1_ID
		global Item_2_ID
		global Item_3_ID
		global Item_4_ID
		global Item_5_ID
		global Item_6_ID
		global Item_7_ID
		global Item_8_ID
		global Item_9_ID
		global Item_10_ID
		global Item_11_ID
		global Item_12_ID
		global Item_13_ID
		global Item_14_ID
		global Item_15_ID
		global Item_16_ID
		global Item_17_ID
		global Item_18_ID
		global Item_19_ID
		global Item_20_ID
		global Item_21_ID
		global Item_22_ID
		global Item_23_ID
		global Item_24_ID
		global Item_25_ID
		global Item_26_ID
		global Item_27_ID
		global Item_28_ID
		global Item_29_ID
		global Item_30_ID
		global Use_Item_Status
		global Use_Item_Delay_ok
		
		if Use_Item == 1:
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_1_Index = player.GetItemIndex(i)
				if Item_1_Index == (int(Item_1_ID)):
					net.SendItemUsePacket(i)
					
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_2_Index = player.GetItemIndex(i)
				if Item_2_Index == (int(Item_2_ID)):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_3_Index = player.GetItemIndex(i)
				if Item_3_Index == (int(Item_3_ID)):
					net.SendItemUsePacket(i)
					break		

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_4_Index = player.GetItemIndex(i)
				if Item_4_Index == (int(Item_4_ID)):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_5_Index = player.GetItemIndex(i)
				if Item_5_Index == (int(Item_5_ID)):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_6_Index = player.GetItemIndex(i)
				if Item_6_Index == (int(Item_6_ID)):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_7_Index = player.GetItemIndex(i)
				if Item_7_Index == (int(Item_7_ID)):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_8_Index = player.GetItemIndex(i)
				if Item_8_Index == (int(Item_8_ID)):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_9_Index = player.GetItemIndex(i)
				if Item_9_Index == (int(Item_9_ID)):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_10_Index = player.GetItemIndex(i)
				if Item_10_Index == (int(Item_10_ID)):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_11_Index = player.GetItemIndex(i)
				if Item_11_Index == (int(Item_11_ID)):
					net.SendItemUsePacket(i)
					break		

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_12_Index = player.GetItemIndex(i)
				if Item_12_Index == (int(Item_12_ID)):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_13_Index = player.GetItemIndex(i)
				if Item_13_Index == (int(Item_13_ID)):
					net.SendItemUsePacket(i)
					break
			
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_14_Index = player.GetItemIndex(i)
				if Item_14_Index == (int(Item_14_ID)):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_15_Index = player.GetItemIndex(i)
				if Item_15_Index == (int(Item_15_ID)):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_16_Index = player.GetItemIndex(i)
				if Item_16_Index == (int(Item_16_ID)):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_17_Index = player.GetItemIndex(i)
				if Item_17_Index == (int(Item_17_ID)):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_18_Index = player.GetItemIndex(i)
				if Item_18_Index == (int(Item_18_ID)):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_19_Index = player.GetItemIndex(i)
				if Item_19_Index == (int(Item_19_ID)):
					net.SendItemUsePacket(i)
					break		

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_20_Index = player.GetItemIndex(i)
				if Item_20_Index == (int(Item_20_ID)):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_21_Index = player.GetItemIndex(i)
				if Item_21_Index == (int(Item_21_ID)):
					net.SendItemUsePacket(i)
					break		

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_22_Index = player.GetItemIndex(i)
				if Item_22_Index == (int(Item_22_ID)):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_23_Index = player.GetItemIndex(i)
				if Item_23_Index == (int(Item_23_ID)):
					net.SendItemUsePacket(i)
					break

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_24_Index = player.GetItemIndex(i)
				if Item_24_Index == (int(Item_24_ID)):
					net.SendItemUsePacket(i)
					break	

			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Item_25_Index = player.GetItemIndex(i)
				if Item_25_Index == (int(Item_25_ID)):
					net.SendItemUsePacket(i)
					break								
							
		self.Delay_Slot_1 = WaitingDialog()
		self.Delay_Slot_1.Open(int(Use_Item_Delay_ok))			
		self.Delay_Slot_1.SAFE_SetTimeOverEvent(self.Enable_Use_Item)	

	################################## About Func ##########################################			
		
	def About_func(self):
		self.About.Show()	
		
	def FaceBook_func(self):
		os.system('start https://www.facebook.com/xZAHON')

	def YouTube_func(self):
		os.system('start https://www.youtube.com/channel/UC23pks_7oQXPvR1J4domS3Q')		
		
	def MPC_func(self):
		os.system('start http://www.mpcforum.pl/user/258957-zahon/')

	######################################################################################
	################################### Site 2 - Opcje ###################################	
	######################################################################################	
		
	def Set_Mobber_ID(self):
		global Mobber_ID
		global Mobber_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Mobber_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			# 1 i 2 oznacza, ¿e nie da siê w³o¿yæ w slot przedmiotów zak³adanych (broni, tarczy, butów itp.), je¿eli bêdzie samo if item.GetItemType() != 0 bêdzie mo¿na wszystko dodaæ
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano peleryny mêstwa o ID: " + str(attachedSlotVnum))
												
				item.SelectItem(int(attachedSlotVnum))
				Mobber_Icon = item.GetIconImageFileName()
				self.Item_Mobber_Slot.LoadImage(str(Mobber_Icon))
				
				self.Mobber_HorizontalBar_Text.SetText("Mobber, ID - " + str(attachedSlotVnum))
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")		
				
	
	def Delete_Mobber_ID(self):
		global Mobber_ID	
		Mobber_ID = 0	
		self.Mobber_HorizontalBar_Text.SetText("Mobber")	

	################################## Poty Func ##########################################	
		
	def Set_Poty_1_ID(self):
		global Poty_1_ID
		global Poty_1_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Poty_1_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			# 1 i 2 oznacza, ¿e nie da siê w³o¿yæ w slot przedmiotów zak³adanych (broni, tarczy, butów itp.), je¿eli bêdzie samo if item.GetItemType() != 0 bêdzie mo¿na wszystko dodaæ
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano poty o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Poty_1_Icon = item.GetIconImageFileName()
				self.Item_Poty_1_Slot.LoadImage(str(Poty_1_Icon))
				
				self.Poty_1_Text.SetText(str(attachedSlotVnum))
				self.Poty_1_Text.SetPosition(64, 204)
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Poty_1_ID(self):
		global Poty_1_ID	
		Poty_1_ID = 0					
				
	def Set_Poty_2_ID(self):
		global Poty_2_ID
		global Poty_2_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Poty_2_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			# 1 i 2 oznacza, ¿e nie da siê w³o¿yæ w slot przedmiotów zak³adanych (broni, tarczy, butów itp.), je¿eli bêdzie samo if item.GetItemType() != 0 bêdzie mo¿na wszystko dodaæ
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano poty o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Poty_2_Icon = item.GetIconImageFileName()
				self.Item_Poty_2_Slot.LoadImage(str(Poty_2_Icon))
				
				self.Poty_2_Text.SetText(str(attachedSlotVnum))
				self.Poty_2_Text.SetPosition(96, 204)				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Poty_2_ID(self):
		global Poty_2_ID	
		Poty_2_ID = 0	
		
		
	################################### Use Item #######################################			

	### 1 ###
	
	def Set_Item_1_ID(self):
		global Item_1_ID
		global Item_1_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_1_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_1_Icon = item.GetIconImageFileName()
				self.Item_1_Icon.LoadImage(str(Item_1_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_1_ID(self):
		global Item_1_ID	
		Item_1_ID = 0
		
	### 2 ###	
		
	def Set_Item_2_ID(self):
		global Item_2_ID
		global Item_2_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_2_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_2_Icon = item.GetIconImageFileName()
				self.Item_2_Icon.LoadImage(str(Item_2_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_2_ID(self):
		global Item_2_ID	
		Item_2_ID = 0
	
	### 3 ###	
	
	def Set_Item_3_ID(self):
		global Item_3_ID
		global Item_3_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_3_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_3_Icon = item.GetIconImageFileName()
				self.Item_3_Icon.LoadImage(str(Item_3_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_3_ID(self):
		global Item_3_ID	
		Item_3_ID = 0

	### 4 ###	
	
	def Set_Item_4_ID(self):
		global Item_4_ID
		global Item_4_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_4_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_4_Icon = item.GetIconImageFileName()
				self.Item_4_Icon.LoadImage(str(Item_4_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_4_ID(self):
		global Item_4_ID	
		Item_4_ID = 0	

	### 5 ###	
	
	def Set_Item_5_ID(self):
		global Item_5_ID
		global Item_5_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_5_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_5_Icon = item.GetIconImageFileName()
				self.Item_5_Icon.LoadImage(str(Item_5_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_5_ID(self):
		global Item_5_ID	
		Item_5_ID = 0	

	### 6 ###	
	
	def Set_Item_6_ID(self):
		global Item_6_ID
		global Item_6_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_6_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_6_Icon = item.GetIconImageFileName()
				self.Item_6_Icon.LoadImage(str(Item_6_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_6_ID(self):
		global Item_6_ID	
		Item_6_ID = 0

	### 7 ###	
	
	def Set_Item_7_ID(self):
		global Item_7_ID
		global Item_7_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_7_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_7_Icon = item.GetIconImageFileName()
				self.Item_7_Icon.LoadImage(str(Item_7_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_7_ID(self):
		global Item_7_ID	
		Item_7_ID = 0	

	### 8 ###	
	
	def Set_Item_8_ID(self):
		global Item_8_ID
		global Item_8_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_8_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_8_Icon = item.GetIconImageFileName()
				self.Item_8_Icon.LoadImage(str(Item_8_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_8_ID(self):
		global Item_8_ID	
		Item_8_ID = 0	

	### 9 ###	
	
	def Set_Item_9_ID(self):
		global Item_9_ID
		global Item_9_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_9_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_9_Icon = item.GetIconImageFileName()
				self.Item_9_Icon.LoadImage(str(Item_9_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_9_ID(self):
		global Item_9_ID	
		Item_9_ID = 0	

	### 10 ###	
	
	def Set_Item_10_ID(self):
		global Item_10_ID
		global Item_10_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_10_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_10_Icon = item.GetIconImageFileName()
				self.Item_10_Icon.LoadImage(str(Item_10_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_10_ID(self):
		global Item_10_ID	
		Item_10_ID = 0		

	### 11 ###	
	
	def Set_Item_11_ID(self):
		global Item_11_ID
		global Item_11_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_11_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_11_Icon = item.GetIconImageFileName()
				self.Item_11_Icon.LoadImage(str(Item_11_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_11_ID(self):
		global Item_11_ID	
		Item_11_ID = 0	

	### 12 ###	
	
	def Set_Item_12_ID(self):
		global Item_12_ID
		global Item_12_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_12_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_12_Icon = item.GetIconImageFileName()
				self.Item_12_Icon.LoadImage(str(Item_12_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_12_ID(self):
		global Item_12_ID	
		Item_12_ID = 0			
				
	### 13 ###	
	
	def Set_Item_13_ID(self):
		global Item_13_ID
		global Item_13_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_13_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_13_Icon = item.GetIconImageFileName()
				self.Item_13_Icon.LoadImage(str(Item_13_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_13_ID(self):
		global Item_13_ID	
		Item_13_ID = 0

	### 14 ###	
	
	def Set_Item_14_ID(self):
		global Item_14_ID
		global Item_14_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_14_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_14_Icon = item.GetIconImageFileName()
				self.Item_14_Icon.LoadImage(str(Item_14_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_14_ID(self):
		global Item_14_ID	
		Item_14_ID = 0	

	### 15 ###	
	
	def Set_Item_15_ID(self):
		global Item_15_ID
		global Item_15_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_15_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_15_Icon = item.GetIconImageFileName()
				self.Item_15_Icon.LoadImage(str(Item_15_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_15_ID(self):
		global Item_15_ID	
		Item_15_ID = 0

	### 16 ###	
	
	def Set_Item_16_ID(self):
		global Item_16_ID
		global Item_16_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_16_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_16_Icon = item.GetIconImageFileName()
				self.Item_16_Icon.LoadImage(str(Item_16_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_16_ID(self):
		global Item_16_ID	
		Item_16_ID = 0	

	### 17 ###	
	
	def Set_Item_17_ID(self):
		global Item_17_ID
		global Item_17_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_17_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_17_Icon = item.GetIconImageFileName()
				self.Item_17_Icon.LoadImage(str(Item_17_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_17_ID(self):
		global Item_17_ID	
		Item_17_ID = 0

	### 18 ###	
	
	def Set_Item_18_ID(self):
		global Item_18_ID
		global Item_18_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_18_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_18_Icon = item.GetIconImageFileName()
				self.Item_18_Icon.LoadImage(str(Item_18_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_18_ID(self):
		global Item_18_ID	
		Item_18_ID = 0

	### 19 ###	
	
	def Set_Item_19_ID(self):
		global Item_19_ID
		global Item_19_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_19_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_19_Icon = item.GetIconImageFileName()
				self.Item_19_Icon.LoadImage(str(Item_19_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_19_ID(self):
		global Item_19_ID	
		Item_19_ID = 0	

	### 20 ###	
	
	def Set_Item_20_ID(self):
		global Item_20_ID
		global Item_20_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_20_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_20_Icon = item.GetIconImageFileName()
				self.Item_20_Icon.LoadImage(str(Item_20_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_20_ID(self):
		global Item_20_ID	
		Item_20_ID = 0	

	### 21 ###	
	
	def Set_Item_21_ID(self):
		global Item_21_ID
		global Item_21_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_21_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_21_Icon = item.GetIconImageFileName()
				self.Item_21_Icon.LoadImage(str(Item_21_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_21_ID(self):
		global Item_21_ID	
		Item_21_ID = 0

	### 22 ###	
	
	def Set_Item_22_ID(self):
		global Item_22_ID
		global Item_22_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_22_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_22_Icon = item.GetIconImageFileName()
				self.Item_22_Icon.LoadImage(str(Item_22_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_22_ID(self):
		global Item_22_ID	
		Item_22_ID = 0	

	### 23 ###	
	
	def Set_Item_23_ID(self):
		global Item_23_ID
		global Item_23_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_23_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_23_Icon = item.GetIconImageFileName()
				self.Item_23_Icon.LoadImage(str(Item_23_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_23_ID(self):
		global Item_23_ID	
		Item_23_ID = 0	

	### 24 ###	
	
	def Set_Item_24_ID(self):
		global Item_24_ID
		global Item_24_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_24_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_24_Icon = item.GetIconImageFileName()
				self.Item_24_Icon.LoadImage(str(Item_24_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_24_ID(self):
		global Item_24_ID	
		Item_24_ID = 0	

	### 25 ###	
	
	def Set_Item_25_ID(self):
		global Item_25_ID
		global Item_25_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			
			Item_25_ID = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Pomyœlnie dodano item o ID: " + str(attachedSlotVnum))

				item.SelectItem(int(attachedSlotVnum))
				Item_25_Icon = item.GetIconImageFileName()
				self.Item_25_Icon.LoadImage(str(Item_25_Icon))
				
				
			else:
				
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Nie mo¿esz wstawiæ tego przedmiotu")
				
	def Delete_Item_25_ID(self):
		global Item_25_ID	
		Item_25_ID = 0			
		
	################################### Site Func ###################################			
		
	def Site_1_func(self):
	
		self.Site_1_Button.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")
		self.Site_1_Button.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")
		self.Site_1_Button.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")	
		
		self.Site_2_Button.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_middle_01.sub")
		self.Site_2_Button.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_middle_02.sub")
		self.Site_2_Button.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")	

		self.Site_3_Button.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_middle_01.sub")
		self.Site_3_Button.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_middle_02.sub")
		self.Site_3_Button.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")	

		self.Site_1_Button.SetPosition(10, 240)
		self.Site_2_Button.SetPosition(73, 240)
		self.Site_3_Button.SetPosition(135, 240)
		
		self.Site_HorizontalBar.SetPosition(10, 220)
		
		self.Board.SetSize(200, 275)		
	
	### 1 ###	
	
		self.Auto_Attack_Button.Show()
		self.Mobber_Button.Show()
		self.Pick_Up_Button.Show()
		self.Poty_Button.Show()
		self.Restart_Button.Show()
		self.Use_Item_Button.Show()
		
	### 2 ###		
		
		self.Mobber_Slot.Hide()	
		self.Item_Mobber_Slot.Hide()	
		self.Poty_1_Slot.Hide()	
		self.Item_Poty_1_Slot.Hide()	
		self.Poty_2_Slot.Hide()	
		self.Item_Poty_2_Slot.Hide()	

		self.Mobber_HorizontalBar.Hide()	
		self.Poty_HorizontalBar.Hide()	

		self.Mobber_Info_Text.Hide()	
		self.Mobber_Mode_Text.Hide()	
		self.Mobber_Delay_Text.Hide()	
		self.slotbar_Mobber_Delay.Hide()	
		self.Poty_1_Text.Hide()
		self.Poty_2_Text.Hide()

		self.Mobber_Mode_ComboBox.Hide()
		
	### 3 ###		
				
		self.Use_Item_HorizontalBar.Hide()
		
		self.Use_Item_Delay_Text.Hide()
		self.slotbar_Use_Item_Delay.Hide()
		self.Use_Item_Delay_Mode_ComboBox.Hide()

		self.Item_1_Slot.Hide()	
		self.Item_1_Icon.Hide()	
		self.Item_2_Slot.Hide()	
		self.Item_2_Icon.Hide()	
		self.Item_3_Slot.Hide()	
		self.Item_3_Icon.Hide()
		self.Item_4_Slot.Hide()			
		self.Item_4_Icon.Hide()	
		self.Item_5_Slot.Hide()	
		self.Item_5_Icon.Hide()	
		self.Item_6_Slot.Hide()	
		self.Item_6_Icon.Hide()	
		self.Item_7_Slot.Hide()	
		self.Item_7_Icon.Hide()	
		self.Item_8_Slot.Hide()	
		self.Item_8_Icon.Hide()
		self.Item_9_Slot.Hide()	
		self.Item_9_Icon.Hide()	
		self.Item_10_Slot.Hide()	
		self.Item_10_Icon.Hide()	
		self.Item_11_Slot.Hide()	
		self.Item_11_Icon.Hide()
		self.Item_12_Slot.Hide()	
		self.Item_12_Icon.Hide()
		self.Item_13_Slot.Hide()	
		self.Item_13_Icon.Hide()
		self.Item_14_Slot.Hide()	
		self.Item_14_Icon.Hide()
		self.Item_15_Slot.Hide()	
		self.Item_15_Icon.Hide()
		self.Item_16_Slot.Hide()	
		self.Item_16_Icon.Hide()
		self.Item_17_Slot.Hide()	
		self.Item_17_Icon.Hide()
		self.Item_18_Slot.Hide()	
		self.Item_18_Icon.Hide()
		self.Item_19_Slot.Hide()	
		self.Item_19_Icon.Hide()
		self.Item_20_Slot.Hide()	
		self.Item_20_Icon.Hide()
		self.Item_21_Slot.Hide()	
		self.Item_21_Icon.Hide()
		self.Item_22_Slot.Hide()	
		self.Item_22_Icon.Hide()
		self.Item_23_Slot.Hide()	
		self.Item_23_Icon.Hide()	
		self.Item_24_Slot.Hide()	
		self.Item_24_Icon.Hide()
		self.Item_25_Slot.Hide()	
		self.Item_25_Icon.Hide()		
		
	def Site_2_func(self):
	
		self.Site_2_Button.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")
		self.Site_2_Button.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")
		self.Site_2_Button.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")	
		
		self.Site_1_Button.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_middle_01.sub")
		self.Site_1_Button.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_middle_02.sub")
		self.Site_1_Button.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")	

		self.Site_3_Button.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_middle_01.sub")
		self.Site_3_Button.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_middle_02.sub")
		self.Site_3_Button.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")		

		self.Site_1_Button.SetPosition(10, 240)
		self.Site_2_Button.SetPosition(73, 240)
		self.Site_3_Button.SetPosition(135, 240)
		
		self.Site_HorizontalBar.SetPosition(10, 220)
		
		self.Board.SetSize(200, 275)		
	
	### 1 ###
	
		self.Auto_Attack_Button.Hide()
		self.Mobber_Button.Hide()
		self.Pick_Up_Button.Hide()
		self.Poty_Button.Hide()
		self.Restart_Button.Hide()
		self.Use_Item_Button.Hide()		
		
	### 2 ###		
		
		self.Mobber_Slot.Show()	
		self.Item_Mobber_Slot.Show()	
		self.Poty_1_Slot.Show()	
		self.Item_Poty_1_Slot.Show()	
		self.Poty_2_Slot.Show()	
		self.Item_Poty_2_Slot.Show()	

		self.Mobber_HorizontalBar.Show()	
		self.Poty_HorizontalBar.Show()	

		self.Mobber_Info_Text.Show()	
		self.Mobber_Mode_Text.Show()	
		self.Mobber_Delay_Text.Show()	
		self.slotbar_Mobber_Delay.Show()
		self.Poty_1_Text.Show()
		self.Poty_2_Text.Show()		

		self.Mobber_Mode_ComboBox.Show()
		
	### 3 ###		
		
		self.Use_Item_HorizontalBar.Hide()	
		
		self.Use_Item_Delay_Text.Hide()
		self.slotbar_Use_Item_Delay.Hide()
		self.Use_Item_Delay_Mode_ComboBox.Hide()		

		self.Item_1_Slot.Hide()	
		self.Item_1_Icon.Hide()	
		self.Item_2_Slot.Hide()	
		self.Item_2_Icon.Hide()	
		self.Item_3_Slot.Hide()	
		self.Item_3_Icon.Hide()
		self.Item_4_Slot.Hide()			
		self.Item_4_Icon.Hide()	
		self.Item_5_Slot.Hide()	
		self.Item_5_Icon.Hide()	
		self.Item_6_Slot.Hide()	
		self.Item_6_Icon.Hide()	
		self.Item_7_Slot.Hide()	
		self.Item_7_Icon.Hide()	
		self.Item_8_Slot.Hide()	
		self.Item_8_Icon.Hide()
		self.Item_9_Slot.Hide()	
		self.Item_9_Icon.Hide()	
		self.Item_10_Slot.Hide()	
		self.Item_10_Icon.Hide()	
		self.Item_11_Slot.Hide()	
		self.Item_11_Icon.Hide()
		self.Item_12_Slot.Hide()	
		self.Item_12_Icon.Hide()
		self.Item_13_Slot.Hide()	
		self.Item_13_Icon.Hide()
		self.Item_14_Slot.Hide()	
		self.Item_14_Icon.Hide()
		self.Item_15_Slot.Hide()	
		self.Item_15_Icon.Hide()
		self.Item_16_Slot.Hide()	
		self.Item_16_Icon.Hide()
		self.Item_17_Slot.Hide()	
		self.Item_17_Icon.Hide()
		self.Item_18_Slot.Hide()	
		self.Item_18_Icon.Hide()
		self.Item_19_Slot.Hide()	
		self.Item_19_Icon.Hide()
		self.Item_20_Slot.Hide()	
		self.Item_20_Icon.Hide()
		self.Item_21_Slot.Hide()	
		self.Item_21_Icon.Hide()
		self.Item_22_Slot.Hide()	
		self.Item_22_Icon.Hide()
		self.Item_23_Slot.Hide()	
		self.Item_23_Icon.Hide()	
		self.Item_24_Slot.Hide()	
		self.Item_24_Icon.Hide()
		self.Item_25_Slot.Hide()	
		self.Item_25_Icon.Hide()		

	def Site_3_func(self):	
	
		self.Site_1_Button.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_middle_01.sub")
		self.Site_1_Button.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_middle_02.sub")
		self.Site_1_Button.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")	

		self.Site_2_Button.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_middle_01.sub")
		self.Site_2_Button.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_middle_02.sub")
		self.Site_2_Button.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")	

		self.Site_3_Button.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")
		self.Site_3_Button.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")
		self.Site_3_Button.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")	

		self.Site_1_Button.SetPosition(10, 260)
		self.Site_2_Button.SetPosition(73, 260)
		self.Site_3_Button.SetPosition(135, 260)
		
		self.Site_HorizontalBar.SetPosition(10, 240)
		
		self.Board.SetSize(200, 295)

	### 1 ###
	
		self.Auto_Attack_Button.Hide()
		self.Mobber_Button.Hide()
		self.Pick_Up_Button.Hide()
		self.Poty_Button.Hide()
		self.Restart_Button.Hide()
		self.Use_Item_Button.Hide()		
		
	### 2 ###		
		
		self.Mobber_Slot.Hide()	
		self.Item_Mobber_Slot.Hide()	
		self.Poty_1_Slot.Hide()	
		self.Item_Poty_1_Slot.Hide()	
		self.Poty_2_Slot.Hide()	
		self.Item_Poty_2_Slot.Hide()	

		self.Mobber_HorizontalBar.Hide()	
		self.Poty_HorizontalBar.Hide()	

		self.Mobber_Info_Text.Hide()	
		self.Mobber_Mode_Text.Hide()	
		self.Mobber_Delay_Text.Hide()	
		self.slotbar_Mobber_Delay.Hide()
		self.Poty_1_Text.Hide()
		self.Poty_2_Text.Hide()		

		self.Mobber_Mode_ComboBox.Hide()
	
	### 3 ###		
		
		self.Use_Item_HorizontalBar.Show()	
		
		self.Use_Item_Delay_Text.Show()
		self.slotbar_Use_Item_Delay.Show()
		self.Use_Item_Delay_Mode_ComboBox.Show()		
		
		self.Item_1_Slot.Show()	
		self.Item_1_Icon.Show()	
		self.Item_2_Slot.Show()	
		self.Item_2_Icon.Show()	
		self.Item_3_Slot.Show()	
		self.Item_3_Icon.Show()
		self.Item_4_Slot.Show()			
		self.Item_4_Icon.Show()	
		self.Item_5_Slot.Show()	
		self.Item_5_Icon.Show()	
		self.Item_6_Slot.Show()	
		self.Item_6_Icon.Show()	
		self.Item_7_Slot.Show()	
		self.Item_7_Icon.Show()	
		self.Item_8_Slot.Show()	
		self.Item_8_Icon.Show()
		self.Item_9_Slot.Show()	
		self.Item_9_Icon.Show()	
		self.Item_10_Slot.Show()	
		self.Item_10_Icon.Show()	
		self.Item_11_Slot.Show()	
		self.Item_11_Icon.Show()
		self.Item_12_Slot.Show()	
		self.Item_12_Icon.Show()
		self.Item_13_Slot.Show()	
		self.Item_13_Icon.Show()
		self.Item_14_Slot.Show()	
		self.Item_14_Icon.Show()
		self.Item_15_Slot.Show()	
		self.Item_15_Icon.Show()
		self.Item_16_Slot.Show()	
		self.Item_16_Icon.Show()
		self.Item_17_Slot.Show()	
		self.Item_17_Icon.Show()
		self.Item_18_Slot.Show()	
		self.Item_18_Icon.Show()
		self.Item_19_Slot.Show()	
		self.Item_19_Icon.Show()
		self.Item_20_Slot.Show()	
		self.Item_20_Icon.Show()
		self.Item_21_Slot.Show()	
		self.Item_21_Icon.Show()
		self.Item_22_Slot.Show()	
		self.Item_22_Icon.Show()
		self.Item_23_Slot.Show()	
		self.Item_23_Icon.Show()	
		self.Item_24_Slot.Show()	
		self.Item_24_Icon.Show()
		self.Item_25_Slot.Show()	
		self.Item_25_Icon.Show()	
	
		
	def OnUpdate(self):	
	
	### Mobber ###	
	
		global Mobber_Mode
		
		Mobber_Mode_Index = self.Mobber_Mode_ComboBox.GetCurrentText()
		if Mobber_Mode_Index == "Pelerynki":	
			Mobber_Mode = 1
			
		if Mobber_Mode_Index == "1 Slot":	
			Mobber_Mode = 2
			
	
		global Mobber_Delay
		Mobber_Delay = self.Mobber_Delay_EditLine.GetText()			
	
	
		global Mobber_ID

		if Mobber_ID == 0:
			self.Item_Mobber_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	
			
	### Poty ###	

		global Poty_1_ID
		global Poty_2_ID

		if Poty_1_ID == 0:
			self.Item_Poty_1_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	
			self.Poty_1_Text.SetText("0")
			self.Poty_1_Text.SetPosition(74, 204)			
			
		if Poty_2_ID == 0:
			self.Item_Poty_2_Slot.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	
			self.Poty_2_Text.SetText("0")
			self.Poty_2_Text.SetPosition(106, 204)	
			
	### Use Item ###
	
		Delay = self.Use_Item_Delay_Mode_ComboBox.GetCurrentText()			
		
		if Delay == "Minut":
			Use_Item_Delay_ok = int(Use_Item_Delay * 60)
			# chat.AppendChat(chat.CHAT_TYPE_INFO, str(Use_Item_Delay_ok))
		else:
			Use_Item_Delay_ok = int(Use_Item_Delay)
			# chat.AppendChat(chat.CHAT_TYPE_INFO, str(Use_Item_Delay_ok))	
	
		global Item_1_ID
		global Item_2_ID
		global Item_3_ID
		global Item_4_ID
		global Item_5_ID
		global Item_6_ID
		global Item_7_ID
		global Item_8_ID
		global Item_9_ID
		global Item_10_ID
		global Item_11_ID
		global Item_12_ID
		global Item_13_ID
		global Item_14_ID
		global Item_15_ID
		global Item_16_ID
		global Item_17_ID
		global Item_18_ID
		global Item_19_ID
		global Item_20_ID
		global Item_21_ID
		global Item_22_ID
		global Item_23_ID
		global Item_24_ID
		global Item_25_ID
		global Item_26_ID
		global Item_27_ID
		global Item_28_ID
		global Item_29_ID
		global Item_30_ID
				
		if Item_1_ID == 0:
			self.Item_1_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		

		if Item_2_ID == 0:
			self.Item_2_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_3_ID == 0:
			self.Item_3_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

		if Item_4_ID == 0:
			self.Item_4_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

		if Item_5_ID == 0:
			self.Item_5_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

		if Item_6_ID == 0:
			self.Item_6_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

		if Item_7_ID == 0:
			self.Item_7_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_8_ID == 0:
			self.Item_8_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_9_ID == 0:
			self.Item_9_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

		if Item_10_ID == 0:
			self.Item_10_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")		

		if Item_11_ID == 0:
			self.Item_11_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_12_ID == 0:
			self.Item_12_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_13_ID == 0:
			self.Item_13_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

		if Item_14_ID == 0:
			self.Item_14_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_15_ID == 0:
			self.Item_15_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_16_ID == 0:
			self.Item_16_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_17_ID == 0:
			self.Item_17_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_18_ID == 0:
			self.Item_18_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_19_ID == 0:
			self.Item_19_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

		if Item_20_ID == 0:
			self.Item_20_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_21_ID == 0:
			self.Item_21_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_22_ID == 0:
			self.Item_22_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_23_ID == 0:
			self.Item_23_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	

		if Item_24_ID == 0:
			self.Item_24_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")

		if Item_25_ID == 0:
			self.Item_25_Icon.LoadImage("d:/ymir work/ui/public/Slot_Base.sub")	
			
	################################### Save func #########################################	
	
	def Save_func(self):	
	
		global Item_1_ID
		global Item_2_ID
		global Item_3_ID
		global Item_4_ID
		global Item_5_ID
		global Item_6_ID
		global Item_7_ID
		global Item_8_ID
		global Item_9_ID
		global Item_10_ID
		global Item_11_ID
		global Item_12_ID
		global Item_13_ID
		global Item_14_ID
		global Item_15_ID
		global Item_16_ID
		global Item_17_ID
		global Item_18_ID
		global Item_19_ID
		global Item_20_ID
		global Item_21_ID
		global Item_22_ID
		global Item_23_ID
		global Item_24_ID
		global Item_25_ID
		
		global Item_1_Icon
		global Item_2_Icon
		global Item_3_Icon
		global Item_4_Icon
		global Item_5_Icon
		global Item_6_Icon
		global Item_7_Icon
		global Item_8_Icon
		global Item_9_Icon
		global Item_10_Icon
		global Item_11_Icon
		global Item_12_Icon
		global Item_13_Icon
		global Item_14_Icon
		global Item_15_Icon
		global Item_16_Icon
		global Item_17_Icon
		global Item_18_Icon
		global Item_19_Icon
		global Item_20_Icon
		global Item_21_Icon
		global Item_22_Icon
		global Item_23_Icon
		global Item_24_Icon
		global Item_25_Icon
		
		global Use_Item_Delay_ok
		
		global Mobber_ID
		global Mobber_Icon
		global Mobber_Mode
		global Mobber_Delay
		
		global Poty_1_ID
		global Poty_1_Icon
		global Poty_2_ID
		global Poty_2_Icon
				
		open('Config.cfg', 'w').write('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s' % (Use_Item_Delay_ok, Item_1_ID, Item_1_Icon, Item_2_ID, Item_2_Icon, Item_3_ID, Item_3_Icon, Item_4_ID, Item_4_Icon, Item_5_ID, Item_5_Icon, Item_6_ID, Item_6_Icon, Item_7_ID, Item_7_Icon, Item_8_ID, Item_8_Icon, Item_9_ID, Item_9_Icon, Item_10_ID, Item_10_Icon, Item_11_ID, Item_11_Icon, Item_12_ID, Item_12_Icon, Item_13_ID, Item_13_Icon, Item_14_ID, Item_14_Icon, Item_15_ID, Item_15_Icon, Item_16_ID, Item_16_Icon, Item_17_ID, Item_17_Icon, Item_18_ID, Item_18_Icon, Item_19_ID, Item_19_Icon, Item_20_ID, Item_20_Icon, Item_21_ID, Item_21_Icon, Item_22_ID, Item_22_Icon, Item_23_ID, Item_23_Icon, Item_24_ID, Item_24_Icon, Item_25_ID, Item_25_Icon, Mobber_ID, Mobber_Icon, Mobber_Mode, Mobber_Delay, Poty_1_ID, Poty_1_Icon, Poty_2_ID, Poty_2_Icon))
		
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "Pomyœlnie zapisano ustawienia!")
		
	################################### Load func #########################################
		
	def Load_func(self):
	
		global Item_1_ID
		global Item_2_ID
		global Item_3_ID
		global Item_4_ID
		global Item_5_ID
		global Item_6_ID
		global Item_7_ID
		global Item_8_ID
		global Item_9_ID
		global Item_10_ID
		global Item_11_ID
		global Item_12_ID
		global Item_13_ID
		global Item_14_ID
		global Item_15_ID
		global Item_16_ID
		global Item_17_ID
		global Item_18_ID
		global Item_19_ID
		global Item_20_ID
		global Item_21_ID
		global Item_22_ID
		global Item_23_ID
		global Item_24_ID
		global Item_25_ID
		
		global Item_1_Icon
		global Item_2_Icon
		global Item_3_Icon
		global Item_4_Icon
		global Item_5_Icon
		global Item_6_Icon
		global Item_7_Icon
		global Item_8_Icon
		global Item_9_Icon
		global Item_10_Icon
		global Item_11_Icon
		global Item_12_Icon
		global Item_13_Icon
		global Item_14_Icon
		global Item_15_Icon
		global Item_16_Icon
		global Item_17_Icon
		global Item_18_Icon
		global Item_19_Icon
		global Item_20_Icon
		global Item_21_Icon
		global Item_22_Icon
		global Item_23_Icon
		global Item_24_Icon
		global Item_25_Icon	
		
		global Use_Item_Delay_ok	
		
		global Mobber_ID
		global Mobber_Icon
		global Mobber_Mode
		global Mobber_Delay	

		global Poty_1_ID
		global Poty_1_Icon
		global Poty_2_ID
		global Poty_2_Icon		
	
		if os.path.exists("Config.cfg"):
			Options_Load = open("Config.cfg", "r").read().split()
							
			Use_Item_Delay_ok = Options_Load[0]
			
			Item_1_ID = Options_Load[1]	
			Item_1_Icon = Options_Load[2]	
			self.Item_1_Icon.LoadImage(str(Options_Load[2]))	
				
			chat.AppendChat(chat.CHAT_TYPE_INFO, str(Options_Load[2]))					
				
			Item_2_ID = Options_Load[3]		
			Item_2_Icon = Options_Load[4]			
			self.Item_2_Icon.LoadImage(Options_Load[4])	

			Item_3_ID = Options_Load[5]	
			Item_3_Icon = Options_Load[6]			
			self.Item_3_Icon.LoadImage(Options_Load[6])

			Item_4_ID = Options_Load[7]	
			Item_4_Icon = Options_Load[8]			
			self.Item_4_Icon.LoadImage(Options_Load[8])	

			Item_5_ID = Options_Load[9]	
			Item_5_Icon = Options_Load[10]			
			self.Item_5_Icon.LoadImage(Options_Load[10])

			Item_6_ID = Options_Load[11]
			Item_6_Icon = Options_Load[12]			
			self.Item_6_Icon.LoadImage(Options_Load[12])

			Item_7_ID = Options_Load[13]
			Item_7_Icon = Options_Load[14]			
			self.Item_7_Icon.LoadImage(Options_Load[14])

			Item_8_ID = Options_Load[15]
			Item_8_Icon = Options_Load[16]			
			self.Item_8_Icon.LoadImage(Options_Load[16])

			Item_9_ID = Options_Load[17]
			Item_9_Icon = Options_Load[18]			
			self.Item_9_Icon.LoadImage(Options_Load[18])

			Item_10_ID = Options_Load[19]
			Item_10_Icon = Options_Load[20]			
			self.Item_10_Icon.LoadImage(Options_Load[20])	

			Item_11_ID = Options_Load[21]
			Item_11_Icon = Options_Load[22]			
			self.Item_11_Icon.LoadImage(Options_Load[22])

			Item_12_ID = Options_Load[23]	
			Item_12_Icon = Options_Load[24]			
			self.Item_12_Icon.LoadImage(Options_Load[24])

			Item_13_ID = Options_Load[25]
			Item_13_Icon = Options_Load[26]			
			self.Item_13_Icon.LoadImage(Options_Load[26])

			Item_14_ID = Options_Load[27]
			Item_14_Icon = Options_Load[28]			
			self.Item_14_Icon.LoadImage(Options_Load[28])

			Item_15_ID = Options_Load[29]
			Item_15_Icon = Options_Load[30]			
			self.Item_15_Icon.LoadImage(Options_Load[30])

			Item_16_ID = Options_Load[31]
			Item_16_Icon = Options_Load[32]			
			self.Item_16_Icon.LoadImage(Options_Load[32])

			Item_17_ID = Options_Load[33]
			Item_17_Icon = Options_Load[34]			
			self.Item_17_Icon.LoadImage(Options_Load[34])

			Item_18_ID = Options_Load[35]
			Item_18_Icon = Options_Load[36]			
			self.Item_18_Icon.LoadImage(Options_Load[36])

			Item_19_ID = Options_Load[37]
			Item_19_Icon = Options_Load[38]			
			self.Item_19_Icon.LoadImage(Options_Load[38])

			Item_20_ID = Options_Load[39]
			Item_20_Icon = Options_Load[40]			
			self.Item_20_Icon.LoadImage(Options_Load[40])

			Item_21_ID = Options_Load[41]	
			Item_21_Icon = Options_Load[42]				
			self.Item_21_Icon.LoadImage(Options_Load[42])

			Item_22_ID = Options_Load[43]
			Item_22_Icon = Options_Load[44]				
			self.Item_22_Icon.LoadImage(Options_Load[44])

			Item_23_ID = Options_Load[45]
			Item_23_Icon = Options_Load[46]				
			self.Item_23_Icon.LoadImage(Options_Load[46])

			Item_24_ID = Options_Load[47]
			Item_24_Icon = Options_Load[48]				
			self.Item_24_Icon.LoadImage(Options_Load[48])	

			Item_25_ID = Options_Load[49]
			Item_25_Icon = Options_Load[50]				
			self.Item_25_Icon.LoadImage(Options_Load[50])
			
		### Mobber ###	
			
			Mobber_ID = Options_Load[51]	
			Mobber_Icon = Options_Load[52]	
			self.Item_Mobber_Slot.LoadImage(str(Options_Load[52]))	
			self.Mobber_HorizontalBar_Text.SetText("Mobber, ID - " + str(Options_Load[51]))		
			
			Mobber_Mode = Options_Load[53]
			
			# if Options_Load[53] == 1:
				# self.Mobber_Mode_ComboBox.InsertItem("Pelerynki") 
			# else:
				# self.Mobber_Mode_ComboBox.InsertItem("1_Slot") 				
			
			Mobber_Delay = Options_Load[54]	
			self.Mobber_Delay_EditLine.SetText(str(Options_Load[54]))	

		### Poty ###

			Poty_1_ID = Options_Load[55]
			self.Poty_1_Text.SetText(str(Options_Load[55]))	
			self.Poty_1_Text.SetPosition(64, 204)
			
			Poty_1_Icon = Options_Load[56]	
			self.Item_Poty_1_Slot.LoadImage(str(Options_Load[56]))	
			
			Poty_2_ID = Options_Load[57]
			self.Poty_2_Text.SetText(str(Options_Load[57]))
			self.Poty_2_Text.SetPosition(96, 204)				
			
			Poty_2_Icon = Options_Load[58]	
			self.Item_Poty_2_Slot.LoadImage(str(Options_Load[58]))	
		

			
									
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Mini MultiHack by ZAHON")						
	
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
	
	def Close(self):
		self.Save_func()
		self.Board.Hide()
		
	def About_Close(self):
		self.About.Hide()

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
		


Mini_MH().Show()
