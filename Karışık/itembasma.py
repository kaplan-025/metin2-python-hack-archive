import app
import chat
import chr
import locale
import net
import player
import time
import ui
import interfacemodule
import background
import os
import thread
import time

UpButton = ui.Button()
UpLine = ui.TextLine()
GhostModeButton = ui.Button()
GhostModeLine = ui.TextLine()

UpLabel = ui.TextLine()
UpgradeLabel = ui.TextLine()
GhostModLabel = ui.TextLine()

class MultihackDialog(ui.ThinBoard):
	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.__Load_MessagebotDialog()
		
	def __del__(self):
		ui.ThinBoard.__del__(self)

	def Destroy(self):
		global SetBase
		SetBase = ""
		self.Hide()
		return TRUE
		
	def __Load_MessagebotDialog(self):
	
		self.SetPosition(100, 45)
		self.SetSize(250, 470)
		self.AddFlag("movable")
		self.AddFlag("float")
		self.Close()
		
		self.Elements()
		
		
	def Show(self):
		ui.ThinBoard.Show(self)
		
	def Close(self):
		self.Hide()
		return TRUE
		
	def OnPressEscapeKey(self):
		self.Hide()
		return TRUE
		
	def Elements(self):

		global GhostModLabel
		GhostModLabel = ui.TextLine()	
		GhostModLabel.SetDefaultFontName()
		GhostModLabel.SetPosition(-375, 45)						
		GhostModLabel.SetFeather()
		GhostModLabel.SetWindowHorizontalAlignCenter()
		GhostModLabel.SetText("Normal")
		GhostModLabel.SetFontColor(1.0, 0.8, 0)
		GhostModLabel.SetOutline()
		GhostModLabel.Show()
		
		global UpgradeLabel
		UpgradeLabel = ui.TextLine()	
		UpgradeLabel.SetDefaultFontName()
		UpgradeLabel.SetPosition(-375, 65)
		UpgradeLabel.SetFeather()
		UpgradeLabel.SetWindowHorizontalAlignCenter()
		UpgradeLabel.SetText("DT")
		UpgradeLabel.SetFontColor(1.0, 0.8, 0)
		UpgradeLabel.SetOutline()
		UpgradeLabel.Show()
		
	
	
		global GhostModeButton
		GhostModeButton.SetText("")
		GhostModeButton.SetPosition(2, 45)
		GhostModeButton.SetSize(88,21)
		GhostModeButton.SetEvent(self.Normal)
		GhostModeButton.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		GhostModeButton.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		GhostModeButton.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		GhostModeButton.Show()
		global GhostModeLine
		GhostModeLine.SetParent(GhostModeButton)
		GhostModeLine.SetPosition(23,10)
		GhostModeLine.SetVerticalAlignCenter()
		GhostModeLine.SetHorizontalAlignCenter()
		GhostModeLine.Show()
		
		global UpButton
		UpButton.SetText("")
		UpButton.SetPosition(2, 65)
		UpButton.SetSize(88,21)
		UpButton.SetEvent(self.DT)
		UpButton.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		UpButton.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		UpButton.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		UpButton.Show()
		global UpLine
		UpLine.SetParent(UpButton)
		UpLine.SetPosition(23,10)
		UpLine.SetVerticalAlignCenter()
		UpLine.SetHorizontalAlignCenter()
		UpLine.Show()
		
		global OpenSettingsButton
		OpenSettingsButton.SetText("")
		OpenSettingsButton.SetPosition(2, 85)
		OpenSettingsButton.SetSize(88,21)
		OpenSettingsButton.SetEvent(self.Show)
		OpenSettingsButton.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		OpenSettingsButton.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		OpenSettingsButton.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		OpenSettingsButton.Show()
		global OpenSettingsLine
		OpenSettingsLine.SetParent(OpenSettingsButton)
		OpenSettingsLine.SetPosition(23,10)
		OpenSettingsLine.SetVerticalAlignCenter()
		OpenSettingsLine.SetHorizontalAlignCenter()
		OpenSettingsLine.Show()
		
			
	def Normal(self):
	
		net.SendRefinePacket(int(0), int(0)) 
		
	def DT(self):

		net.SendRefinePacket(int(0), int(4))
	
		
Multi = MultihackDialog()
Multi.Show()