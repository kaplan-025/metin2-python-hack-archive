# Metin2Bot [Dreamfancy]
import ui
import dbg
import app
import snd
import net
import chat
import locale
import constInfo
import chrmgr
import player
import chr
import game
import background
import uiPhaseCurtain
import chat
import playerSettingModule
import uiRestart
import os
import imp
import time
import pack
import uiCommon
import uiTip
import skill
import item
import shop
import grp
import wndMgr
import textTail
import effect
import fly
import systemSetting
import quest
import guild
import messenger
import constInfo
import exchange
import interfacemodule
import shop

AttackSpeedHack = "150"
MoveSpeedHack = "150"

chat.AppendChat(chat.CHAT_TYPE_NOTICE, "|cFF00FF00|H|h[Metin2Bot]: " + "|cFFFFCC00|H|h " + "Metin2Bot Tools")
chat.AppendChat(chat.CHAT_TYPE_NOTICE, "|cFF00FF00|H|h[Metin2Bot]: " + "|cFFFFCC00|H|h " + "Pickup hack - Teleport hack - Multihack - Hayalet modu")

class Dialog1(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(235, 194)
		self.Board.SetCenterPosition()
		self.Board.AddFlag('movable')
		self.Board.AddFlag('float')
		self.Board.SetTitleName('Metin2Bot Tools')
		self.Board.SetCloseEvent(self.Close)
		self.Board.Show()
		self.__BuildKeyDict()
		self.comp = Component()

		self.image497 = self.comp.ExpandedImage(self.Board , 6, 30, 'lib/banner.jpg')
		self.movespbutt = self.comp.Button(self.Board, 'Aktif / Kapat ', '', 129, 132, self.movespbutt_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.attacksbutt = self.comp.Button(self.Board, 'Aktif / Kapat ', '', 131, 161, self.attacksbutt_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.tele = self.comp.Button(self.Board, 'Teleport', '', 87, 95, self.tele_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.ghost = self.comp.Button(self.Board, 'Hayalet', '', 160, 95, self.ghost_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.Pickup = self.comp.Button(self.Board, 'Esya calma', '', 13, 95, self.Pickup_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.slotbar_slotbar_movesp, self.movesp = self.comp.EditLine(self.Board, '250', 81, 135, 35, 15, 3)
		self.slotbar_slotbar_attacksp, self.attacksp = self.comp.EditLine(self.Board, '250', 81, 163, 35, 15, 3)
		self.attacks = self.comp.TextLine(self.Board, 'Hizli vurma', 15, 134, self.comp.RGB(255, 255, 0))
		self.moves = self.comp.TextLine(self.Board, 'Hizli kosma', 14, 163, self.comp.RGB(255, 255, 0))
	
	def movespbutt_func(self):
		global MoveSpeedHack
		CurrentMoveSpeedHack = self.movesp.GetText()
		if MoveSpeedHack == "":
			MoveSpeedHack = 1
			chat.AppendChat(chat.CHAT_TYPE_NOTICE, "|cFF00FF00|H|h[Metin2Bot]: " + "|cFFFFCC00|H|h " + "Hizli kosma aktif edildi.")
			chr.SetMoveSpeed(int(CurrentMoveSpeedHack))
			self.movespbutt.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			self.movespbutt.SetText("Aktif")
			if int(CurrentMoveSpeedHack) > 200:
				self.MoveSpeedFix = WaitingDialog()
				self.MoveSpeedFix.Open(0.5)
				self.MoveSpeedFix.SAFE_SetTimeOverEvent(self.MoveSpeedHackFixLoop1)
		elif int(CurrentMoveSpeedHack) < 0.01:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "")		
		else:
			if int(CurrentMoveSpeedHack) > 0.01:
				MoveSpeedHack = ""
				chat.AppendChat(chat.CHAT_TYPE_NOTICE, "|cFF00FF00|H|h[Metin2Bot]: " + "|cFFFFCC00|H|h " + "Hizli kosma kapatildi.")
				chr.SetMoveSpeed(int(player.GetStatus(player.MOVING_SPEED)))
				self.movespbutt.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
				self.movespbutt.SetText("Kapali")
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "")
				
	def MoveSpeedHackFixLoop1(self):
		chr.SetMoveSpeed(int(player.GetStatus(player.MOVING_SPEED)))
		self.MoveSpeedHackFixLoop2()

	def MoveSpeedHackFixLoop2(self):
		global MoveSpeedHack
		if MoveSpeedHack != "":
			CurrentMoveSpeedHack = self.MoveSpeedStats.GetText()
			chr.SetMoveSpeed(int(CurrentMoveSpeedHack))
			self.MoveSpeedFix = WaitingDialog()
			self.MoveSpeedFix.Open(0.5)
			self.MoveSpeedFix.SAFE_SetTimeOverEvent(self.MoveSpeedHackFixLoop1)	
	
	def attacksbutt_func(self):
		global AttackSpeedHack
		CurrentAttackSpeedHack = self.attacksp.GetText()
		if AttackSpeedHack == "":
			AttackSpeedHack = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "")
			chr.SetAttackSpeed(int(CurrentAttackSpeedHack))
			self.attacksbutt.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			self.attacksbutt.SetText("Aktif")
			chat.AppendChat(chat.CHAT_TYPE_NOTICE, "|cFF00FF00|H|h[Metin2Bot]: " + "|cFFFFCC00|H|h " + "Hizli vurma aktif edildi.")
		elif int(CurrentAttackSpeedHack) < 0.01:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "")		
		else:
			if int(CurrentAttackSpeedHack) > 0.01:
				AttackSpeedHack = ""
				chat.AppendChat(chat.CHAT_TYPE_INFO, "")
				chr.SetAttackSpeed(int(player.GetStatus(player.ATT_SPEED)))
				self.attacksbutt.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
				self.attacksbutt.SetText("Kapali")
				chat.AppendChat(chat.CHAT_TYPE_NOTICE, "|cFF00FF00|H|h[Metin2Bot]: " + "|cFFFFCC00|H|h " + "Hizli vurma kapatildi.")
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "")
	
	def tele_func(self):
		import Rest.pyc
	
	def ghost_func(self):
		chr.Revive()
		
	def Pickup_func(self):
		import Restdrp.dll
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
		scroll = ui.ScrollBar()
		scroll.SetParent(ListBox)
		scroll.SetPosition(width-15, 0)
		scroll.SetScrollBarSize(heigh)
		scroll.Show()
		ListBox.SetScrollBar(scroll)
		return bar, ListBox

class WaitingDialog(ui.Window):

	def __init__(self):
		ui.Windows.__init__(self)
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.Window.__del__(self)

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
			
Dialog1().Show()
