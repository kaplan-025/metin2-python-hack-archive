# Metin2Bot [Dreamfancy]
import ui
import snd
import item
import net
import chat
import app
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
import dbg

class Dialog1(ui.ThinBoard):
	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.BuildWindow()

	def __del__(self):
		ui.ThinBoard.__del__(self)

	def BuildWindow(self):
		self.SetSize(172, 104)
		self.SetCenterPosition()
		self.AddFlag('movable')
		self.AddFlag('float')
		self.comp = Component()

		self.Zoom = self.comp.ToggleButton(self, 'Zoom kaldir', '', 12, 15, (lambda arg = 'off': self.Zoom_func(arg)), (lambda arg = 'on': self.Zoom_func(arg)), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.NoFog = self.comp.ToggleButton(self, 'Sisleri kaldir', '', 12, 45, (lambda arg = 'off': self.NoFog_func(arg)), (lambda arg = 'on': self.NoFog_func(arg)), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.CoolTime = self.comp.ToggleButton(self, 'Gece / Gunduz', '', 91, 14, (lambda arg = 'off': self.CoolTime_func(arg)), (lambda arg = 'on': self.CoolTime_func(arg)), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.Kar = self.comp.ToggleButton(self, 'Kar yagdir', '', 90, 44, (lambda arg = 'off': self.Kar_func(arg)), (lambda arg = 'on': self.Kar_func(arg)), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.Dropper = self.comp.ToggleButton(self, 'Kick hack', '', 38, 73, (lambda arg = 'off': self.Dropper_func(arg)), (lambda arg = 'on': self.Dropper_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
	
	def Zoom_func(self, arg):
		if arg=='on':
			app.SetCameraMaxDistance(999000)	
		elif arg=='off':
			app.SetCameraMaxDistance(2500)	
	
	def NoFog_func(self, arg):
		if arg=='on':
			app.SetMinFog(70000)
		elif arg=='off':
			app.SetMinFog(2500)
	
	def CoolTime_func(self, arg):
		if arg=='on':
			player.ToggleCoolTime()
		elif arg=='off':
			player.ToggleCoolTime()
	
	def Kar_func(self, arg):
		if arg=='on':
			background.EnableSnow(1)
		elif arg=='off':
			background.EnableSnow(0)
	
	def Dropper_func(self, arg):
		if arg=='on':
			net.SendGoldDropPacketNew(1)
			net.SendGoldDropPacketNew(1)
			net.SendGoldDropPacketNew(1)
		elif arg=='off':
			net.SendGoldDropPacketNew(1)
	
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
		return SlotBar, Value

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
		return (r*255, g*255, b*255)

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

Dialog1().Show()
