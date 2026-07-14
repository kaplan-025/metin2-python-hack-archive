import ui
import dbg
import app
import os
import locale
import chat
import time
import player
import chrmgr
import shop
import item
import net
import grp
import wndMgr
import mouseModule
import chr
import skill
import math
import miniMap
import background
import nonplayer
import snd
import exception
import uiCommon
import shop
import ServerInfo
import game
import thread
import uiToolTip
import textTail

class Fake_Info(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Fake_Info = ui.BoardWithTitleBar()
		self.Fake_Info.SetSize(205, 200)
		self.Fake_Info.SetCenterPosition()
		self.Fake_Info.AddFlag('movable')
		self.Fake_Info.AddFlag('float')
		self.Fake_Info.SetTitleName('Fake Info')
		self.Fake_Info.SetCloseEvent(self.Fake_Info_Close)
		self.Fake_Info.Show()
		self.__BuildKeyDict()
		self.comp = Component()
	
	################################### HorizontalBars #######################		

		self.Fake_Info_HorizontalBar = self.comp.HorizontalBar(self.Fake_Info , 10, 35, 185)
		self.Fake_Info_HorizontalBar_Text = self.comp.TextLine_SetPackedFontColor(self.Fake_Info_HorizontalBar, 'Zmiana tylko wizualna!', 5, 0, 0xFFFFE3AD)			
	
	################################## Text ###################################	
			
		self.Fake_Info_Set_Nick_Text = self.comp.TextLine(self.Fake_Info, 'Nick Postaci', 15, 56, self.comp.RGB(255, 255, 255))		
		self.Fake_Info_Set_Level_Text = self.comp.TextLine(self.Fake_Info, 'Level Postaci', 15, 76, self.comp.RGB(255, 255, 255))		
		self.Fake_Info_Set_Weapon_Text = self.comp.TextLine(self.Fake_Info, 'Wygl¹d Broni', 15, 96, self.comp.RGB(255, 255, 255))		
		self.Fake_Info_Set_Armor_Text = self.comp.TextLine(self.Fake_Info, 'Wygl¹d Zbroi', 15, 116, self.comp.RGB(255, 255, 255))		
		self.Fake_Info_Set_Visual_Text = self.comp.TextLine(self.Fake_Info, 'Wygl¹d', 15, 136, self.comp.RGB(255, 255, 255))		

	################################## EditLine ###################################		
		
		self.slotbar_Fake_Info_Set_Nick, self.Fake_Info_Set_Nick_EditLine = self.comp.EditLine(self.Fake_Info, '', 80, 55, 60, 15, 100)
		self.slotbar_Fake_Info_Set_Level, self.Fake_Info_Set_Level_EditLine = self.comp.EditLine(self.Fake_Info, '', 80, 75, 60, 15, 100)
		self.slotbar_Fake_Info_Set_Weapon, self.Fake_Info_Set_Weapon_EditLine = self.comp.EditLine(self.Fake_Info, '', 80, 95, 60, 15, 100)
		self.slotbar_Fake_Info_Set_Armor, self.Fake_Info_Set_Armor_EditLine = self.comp.EditLine(self.Fake_Info, '', 80, 115, 60, 15, 100)
		self.slotbar_Fake_Info_Set_Visual, self.Fake_Info_Set_Visual_EditLine = self.comp.EditLine(self.Fake_Info, '', 80, 135, 60, 15, 100)
			
	################################## Buttons #########################################		
	
		self.Fake_Info_Set_Nick_Button = self.comp.Button(self.Fake_Info, 'Ustaw', '', 150, 55, self.Fake_Info_Set_Nick_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Fake_Info_Set_Level_Button = self.comp.Button(self.Fake_Info, 'Ustaw', '', 150, 75, self.Fake_Info_Set_Level_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Fake_Info_Set_Weapon_Button = self.comp.Button(self.Fake_Info, 'Ustaw', '', 150, 95, self.Fake_Info_Set_Weapon_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Fake_Info_Set_Armor_Button = self.comp.Button(self.Fake_Info, 'Ustaw', '', 150, 115, self.Fake_Info_Set_Armor_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Fake_Info_Set_Visual_Button = self.comp.Button(self.Fake_Info, 'Ustaw', '', 150, 135, self.Fake_Info_Set_Visual_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
			
	################################## Fake Info Func #########################################			
			
	def Fake_Info_Set_Nick_func(self):
		chr.SetNameString(str(self.Fake_Info_Set_Nick_EditLine.GetText()))
		chat.AppendChat(2, "Aby zatwierdziæ zmianê wykonaj akcjê na koncie - u¿yj dopalacza, zdejmij item itp.")
		
	def Fake_Info_Set_Level_func(self):
		player.SetStatus(player.LEVEL, int(self.Fake_Info_Set_Level_EditLine.GetText()))			
	
	def Fake_Info_Set_Weapon_func(self):
		chr.SetWeapon(int(self.Fake_Info_Set_Weapon_EditLine.GetText()))
		
	def Fake_Info_Set_Armor_func(self):
		chr.SetArmor(int(self.Fake_Info_Set_Armor_EditLine.GetText()))
	
	def Fake_Info_Set_Visual_func(self):
		chr.SetRace(7)
	
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
		
	def SliderBarHide(self, parent, sliderPos, func, x, y):
		Slider = ui.SliderBar()
		if parent != None:
			Slider.SetParent(parent)
		Slider.SetPosition(x, y)
		Slider.SetSliderPos(sliderPos / 100)
		Slider.Hide()
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
		bar.SetColor(0x77000000)
		bar.Show()
		ListBox=ui.ListBoxEx()
		ListBox.SetParent(bar)
		ListBox.SetPosition(0, 0)
		ListBox.SetSize(width, heigh)
		ListBox.Show()
		# scroll = ui.ScrollBar()
		# scroll.SetParent(ListBox)
		# scroll.SetPosition(width-15, 0)
		# scroll.SetScrollBarSize(heigh)
		# scroll.Show()
		# ListBox.SetScrollBar(scroll)
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

Fake_Info().Show()
