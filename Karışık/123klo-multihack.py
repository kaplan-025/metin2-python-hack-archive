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

UpButton = ui.Button()
UpLine = ui.TextLine()
GhostModeButton = ui.Button()
GhostModeLine = ui.TextLine()
OpenSettingsButton = ui.Button()
OpenSettingsLine = ui.TextLine()

UpLabel = ui.TextLine()
UpgradeLabel = ui.TextLine()
GhostModLabel = ui.TextLine()

Refine = 0
MoveSpeed = 0
Combo = 0	
ZoomHack = 0
NoFog = 0
DayNight = 0
EnableSnow = 0

AutoRedPot = 0
AutoBluePot = 0
AutoAttack = 0
AutoPickup = 0
AutoRestart = 0

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
		
		chat.AppendChat(chat.CHAT_TYPE_INFO, "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Multihack by 123klo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		chat.AppendChat(chat.CHAT_TYPE_INFO, "~~~~~~~~~~~~~~~~~~~~~~~~~~Credits: Slait, DaRealFreak, Kamarun~~~~~~~~~~~~~~~~~~~~~~~~~")
		chat.AppendChat(chat.CHAT_TYPE_INFO, "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Have Fun ;)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
											 
		self.LoadText()
		self.LoadButton()
		self.LoadEditLines()
		
	def Show(self):
		ui.ThinBoard.Show(self)
		
	def Close(self):
		self.Hide()
		return TRUE
		
	def OnPressEscapeKey(self):
		self.Hide()
		return TRUE
		
		
		
		
	def LoadText(self):
	
		self.MainLabel = ui.TextLine()
		self.MainLabel.SetParent(self)
		self.MainLabel.SetDefaultFontName()
		self.MainLabel.SetPosition(-50, 10)
		self.MainLabel.SetFeather()
		self.MainLabel.SetWindowHorizontalAlignCenter()
		self.MainLabel.SetText("Multihack by 123klo")
		self.MainLabel.SetFontColor(1.0, 0.8, 0)
		self.MainLabel.SetOutline()
		self.MainLabel.Show()
		
		self.RefineLabel = ui.TextLine()
		self.RefineLabel.SetParent(self)
		self.RefineLabel.SetDefaultFontName()
		self.RefineLabel.SetPosition(-110, 40)
		self.RefineLabel.SetFeather()
		self.RefineLabel.SetWindowHorizontalAlignCenter()
		self.RefineLabel.SetText("Upgrade")
	#	self.RefineLabel.SetFontColor(1.0, 0.8, 0)
		self.RefineLabel.SetOutline()
		self.RefineLabel.Show()	
		
		self.MoveSpeedLabel = ui.TextLine()
		self.MoveSpeedLabel.SetParent(self)
		self.MoveSpeedLabel.SetDefaultFontName()
		self.MoveSpeedLabel.SetPosition(-110, 70)
		self.MoveSpeedLabel.SetFeather()
		self.MoveSpeedLabel.SetWindowHorizontalAlignCenter()
		self.MoveSpeedLabel.SetText("MoveSpeed:")
	#	self.MoveSpeedLabel.SetFontColor(1.0, 0.8, 0)
		self.MoveSpeedLabel.SetOutline()
		self.MoveSpeedLabel.Show()	
		
		self.MoveSpeedPerncentLabel = ui.TextLine()
		self.MoveSpeedPerncentLabel.SetParent(self)
		self.MoveSpeedPerncentLabel.SetDefaultFontName()
		self.MoveSpeedPerncentLabel.SetPosition(-10, 70)
		self.MoveSpeedPerncentLabel.SetFeather()
		self.MoveSpeedPerncentLabel.SetWindowHorizontalAlignCenter()
		self.MoveSpeedPerncentLabel.SetText("%")
		self.MoveSpeedPerncentLabel.SetFontColor(1.0, 0.8, 0)
		self.MoveSpeedPerncentLabel.SetOutline()
		self.MoveSpeedPerncentLabel.Show()	
		
		self.ComboLabel = ui.TextLine()
		self.ComboLabel.SetParent(self)
		self.ComboLabel.SetDefaultFontName()
		self.ComboLabel.SetPosition(-110, 100)
		self.ComboLabel.SetFeather()
		self.ComboLabel.SetWindowHorizontalAlignCenter()
		self.ComboLabel.SetText("Combo:")
	#	self.ComboLabel.SetFontColor(1.0, 0.8, 0)
		self.ComboLabel.SetOutline()
		self.ComboLabel.Show()	
		
		self.ZoomHackLabel = ui.TextLine()
		self.ZoomHackLabel.SetParent(self)
		self.ZoomHackLabel.SetDefaultFontName()
		self.ZoomHackLabel.SetPosition(-110, 130)
		self.ZoomHackLabel.SetFeather()
		self.ZoomHackLabel.SetWindowHorizontalAlignCenter()
		self.ZoomHackLabel.SetText("ZoomHack:")
	#	self.ZoomHackLabel.SetFontColor(1.0, 0.8, 0)
		self.ZoomHackLabel.SetOutline()
		self.ZoomHackLabel.Show()	
		
		self.NoFogLabel = ui.TextLine()
		self.NoFogLabel.SetParent(self)
		self.NoFogLabel.SetDefaultFontName()
		self.NoFogLabel.SetPosition(-110, 160)
		self.NoFogLabel.SetFeather()
		self.NoFogLabel.SetWindowHorizontalAlignCenter()
		self.NoFogLabel.SetText("NoFog:")
	#	self.NoFogLabel.SetFontColor(1.0, 0.8, 0)
		self.NoFogLabel.SetOutline()
		self.NoFogLabel.Show()	
		
		self.DayNightLabel = ui.TextLine()
		self.DayNightLabel.SetParent(self)
		self.DayNightLabel.SetDefaultFontName()
		self.DayNightLabel.SetPosition(-110, 190)
		self.DayNightLabel.SetFeather()
		self.DayNightLabel.SetWindowHorizontalAlignCenter()
		self.DayNightLabel.SetText("Day/Night:")
	#	self.DayNightLabel.SetFontColor(1.0, 0.8, 0)
		self.DayNightLabel.SetOutline()
		self.DayNightLabel.Show()	
		
		self.SnowLabel = ui.TextLine()
		self.SnowLabel.SetParent(self)
		self.SnowLabel.SetDefaultFontName()
		self.SnowLabel.SetPosition(-110, 220)
		self.SnowLabel.SetFeather()
		self.SnowLabel.SetWindowHorizontalAlignCenter()
		self.SnowLabel.SetText("Snow:")
	#	self.SnowLabel.SetFontColor(1.0, 0.8, 0)
		self.SnowLabel.SetOutline()
		self.SnowLabel.Show()	
		
		self.LineLabel = ui.TextLine()	
		self.LineLabel.SetParent(self)
		self.LineLabel.SetDefaultFontName()
		self.LineLabel.SetPosition(-110, 240)
		self.LineLabel.SetFeather()
		self.LineLabel.SetWindowHorizontalAlignCenter()
		self.LineLabel.SetText("____________________________________________")
		self.LineLabel.SetFontColor(1.0, 0.8, 0)
		self.LineLabel.SetOutline()
		self.LineLabel.Show()	
		
		self.AutoRedPotLabel = ui.TextLine()	
		self.AutoRedPotLabel.SetParent(self)
		self.AutoRedPotLabel.SetDefaultFontName()
		self.AutoRedPotLabel.SetPosition(-110, 270)
		self.AutoRedPotLabel.SetFeather()
		self.AutoRedPotLabel.SetWindowHorizontalAlignCenter()
		self.AutoRedPotLabel.SetText("RedPotting:")
		self.AutoRedPotLabel.SetFontColor(35.0, 0.0, 0.0)
		self.AutoRedPotLabel.SetOutline()
		self.AutoRedPotLabel.Show()	
		
		self.RedPotPercentLabel = ui.TextLine()	
		self.RedPotPercentLabel.SetParent(self)
		self.RedPotPercentLabel.SetDefaultFontName()
		self.RedPotPercentLabel.SetPosition(-12, 269)
		self.RedPotPercentLabel.SetFeather()
		self.RedPotPercentLabel.SetWindowHorizontalAlignCenter()
		self.RedPotPercentLabel.SetText("%")
		self.RedPotPercentLabel.SetFontColor(35.0, 0.0, 0.0)
		self.RedPotPercentLabel.SetOutline()
		self.RedPotPercentLabel.Show()	
		
		self.AutoBluePotLabel = ui.TextLine()	
		self.AutoBluePotLabel.SetParent(self)
		self.AutoBluePotLabel.SetDefaultFontName()
		self.AutoBluePotLabel.SetPosition(-110, 300)
		self.AutoBluePotLabel.SetFeather()
		self.AutoBluePotLabel.SetWindowHorizontalAlignCenter()
		self.AutoBluePotLabel.SetText("BluePotting:")
		self.AutoBluePotLabel.SetFontColor(0.0, 0.0, 1.0)
		self.AutoBluePotLabel.SetOutline()
		self.AutoBluePotLabel.Show()	
		
		self.BluePotPercentLabel = ui.TextLine()	
		self.BluePotPercentLabel.SetParent(self)
		self.BluePotPercentLabel.SetDefaultFontName()
		self.BluePotPercentLabel.SetPosition(-12, 300)
		self.BluePotPercentLabel.SetFeather()
		self.BluePotPercentLabel.SetWindowHorizontalAlignCenter()
		self.BluePotPercentLabel.SetText("%")
		self.BluePotPercentLabel.SetFontColor(0.0, 0.0, 1.0)
		self.BluePotPercentLabel.SetOutline()
		self.BluePotPercentLabel.Show()	
		
		self.AutoAttackLabel = ui.TextLine()	
		self.AutoAttackLabel.SetParent(self)
		self.AutoAttackLabel.SetDefaultFontName()
		self.AutoAttackLabel.SetPosition(-110, 330)
		self.AutoAttackLabel.SetFeather()
		self.AutoAttackLabel.SetWindowHorizontalAlignCenter()
		self.AutoAttackLabel.SetText("AutoAttack:")
	#	self.AutoAttackLabel.SetFontColor(1.0, 0.8, 0)
		self.AutoAttackLabel.SetOutline()
		self.AutoAttackLabel.Show()
		
		self.AutoPickLabel = ui.TextLine()	
		self.AutoPickLabel.SetParent(self)
		self.AutoPickLabel.SetDefaultFontName()
		self.AutoPickLabel.SetPosition(-110, 360)
		self.AutoPickLabel.SetFeather()
		self.AutoPickLabel.SetWindowHorizontalAlignCenter()
		self.AutoPickLabel.SetText("AutoPickup:")
	#	self.AutoPickLabel.SetFontColor(1.0, 0.8, 0)
		self.AutoPickLabel.SetOutline()
		self.AutoPickLabel.Show()
		
		self.AutoRestartLabel = ui.TextLine()	
		self.AutoRestartLabel.SetParent(self)
		self.AutoRestartLabel.SetDefaultFontName()
		self.AutoRestartLabel.SetPosition(-110, 390)
		self.AutoRestartLabel.SetFeather()
		self.AutoRestartLabel.SetWindowHorizontalAlignCenter()
		self.AutoRestartLabel.SetText("AutoRestart:")
	#	self.AutoRestartLabel.SetFontColor(1.0, 0.8, 0)
		self.AutoRestartLabel.SetOutline()
		self.AutoRestartLabel.Show()
		
		
		global GhostModLabel
		GhostModLabel = ui.TextLine()	
		GhostModLabel.SetDefaultFontName()
		GhostModLabel.SetPosition(-490, 45)						
		GhostModLabel.SetFeather()
		GhostModLabel.SetWindowHorizontalAlignCenter()
		GhostModLabel.SetText("GhostMod")
		GhostModLabel.SetFontColor(1.0, 0.8, 0)
		GhostModLabel.SetOutline()
		GhostModLabel.Show()
		
		global UpgradeLabel
		UpgradeLabel = ui.TextLine()	
		UpgradeLabel.SetDefaultFontName()
		UpgradeLabel.SetPosition(-490, 65)
		UpgradeLabel.SetFeather()
		UpgradeLabel.SetWindowHorizontalAlignCenter()
		UpgradeLabel.SetText("Upgrade 1x")
		UpgradeLabel.SetFontColor(1.0, 0.8, 0)
		UpgradeLabel.SetOutline()
		UpgradeLabel.Show()
		
		global OpenSettingsLabel
		OpenSettingsLabel = ui.TextLine()	
		OpenSettingsLabel.SetDefaultFontName()
		OpenSettingsLabel.SetPosition(-490, 85)
		OpenSettingsLabel.SetFeather()
		OpenSettingsLabel.SetWindowHorizontalAlignCenter()
		OpenSettingsLabel.SetText("OpenSettings")
		OpenSettingsLabel.SetFontColor(1.0, 0.8, 0)
		OpenSettingsLabel.SetOutline()
		OpenSettingsLabel.Show()
		
	def LoadButton(self):
		
		self.CloseButton = ui.Button()
		self.CloseButton.SetParent(self)
		self.CloseButton.SetPosition(220, 10)
		self.CloseButton.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		self.CloseButton.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		self.CloseButton.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		self.CloseButton.SetToolTipText(locale.UI_CLOSE, 0, - 23)
		self.CloseButton.SetEvent(ui.__mem_func__(self.Hide))
		self.CloseButton.Show()
		
		
		self.SetRefineModeButton = ui.Button()
		self.SetRefineModeButton.SetParent(self)
		self.SetRefineModeButton.SetPosition(75, 37)
		self.SetRefineModeButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.SetRefineModeButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.SetRefineModeButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.SetRefineModeButton.SetEvent(ui.__mem_func__(self.RefineMode))
		self.SetRefineModeButton.SetText("DT")
		self.SetRefineModeButton.SetToolTipText("Swich between DT and normal Upgrading")
		self.SetRefineModeButton.Show()
		
		self.MoveSpeedButton = ui.Button()
		self.MoveSpeedButton.SetParent(self)
		self.MoveSpeedButton.SetPosition(140, 69)
		self.MoveSpeedButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.MoveSpeedButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.MoveSpeedButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.MoveSpeedButton.SetEvent(ui.__mem_func__(self.MoveSpeed))
		self.MoveSpeedButton.SetText("Of")
		self.MoveSpeedButton.Show()
		
		self.ComboTypeButton = ui.Button()
		self.ComboTypeButton.SetParent(self)
		self.ComboTypeButton.SetPosition(75, 97)
		self.ComboTypeButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.ComboTypeButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.ComboTypeButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.ComboTypeButton.SetEvent(ui.__mem_func__(self.Combo))
		self.ComboTypeButton.SetText("Off")
		self.ComboTypeButton.Show()
		
		self.ZoomHackButton = ui.Button()
		self.ZoomHackButton.SetParent(self)
		self.ZoomHackButton.SetPosition(75, 127)
		self.ZoomHackButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.ZoomHackButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.ZoomHackButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.ZoomHackButton.SetEvent(ui.__mem_func__(self.ZoomHack))
		self.ZoomHackButton.SetText("Off")
		self.ZoomHackButton.Show()
		
		self.NoFogButton = ui.Button()
		self.NoFogButton.SetParent(self)
		self.NoFogButton.SetPosition(75, 157)
		self.NoFogButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.NoFogButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.NoFogButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.NoFogButton.SetEvent(ui.__mem_func__(self.NoFog))
		self.NoFogButton.SetText("Off")
		self.NoFogButton.Show()
		
		self.DayNightButton = ui.Button()
		self.DayNightButton.SetParent(self)
		self.DayNightButton.SetPosition(75, 187)
		self.DayNightButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.DayNightButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.DayNightButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.DayNightButton.SetEvent(ui.__mem_func__(self.DayNight))
		self.DayNightButton.SetText("Day")
		self.DayNightButton.Show()
		
		self.SnowButton = ui.Button()
		self.SnowButton.SetParent(self)
		self.SnowButton.SetPosition(75, 217)
		self.SnowButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.SnowButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.SnowButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.SnowButton.SetEvent(ui.__mem_func__(self.EnableSnow))
		self.SnowButton.SetText("Off")
		self.SnowButton.Show()
		
		self.AutoRedPotButton = ui.Button()
		self.AutoRedPotButton.SetParent(self)
		self.AutoRedPotButton.SetPosition(140, 267)
		self.AutoRedPotButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoRedPotButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoRedPotButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoRedPotButton.SetEvent(ui.__mem_func__(self.AutoRedPot))
		self.AutoRedPotButton.SetText("Off")
		self.AutoRedPotButton.Show()
		
		self.AutoBluePotButton = ui.Button()
		self.AutoBluePotButton.SetParent(self)
		self.AutoBluePotButton.SetPosition(140, 297)
		self.AutoBluePotButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoBluePotButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoBluePotButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoBluePotButton.SetEvent(ui.__mem_func__(self.AutoBluePot))
		self.AutoBluePotButton.SetText("Off")
		self.AutoBluePotButton.Show()
		
		self.AutoAttackButton = ui.Button()
		self.AutoAttackButton.SetParent(self)
		self.AutoAttackButton.SetPosition(75, 327)
		self.AutoAttackButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoAttackButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoAttackButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoAttackButton.SetEvent(ui.__mem_func__(self.AutoAttack))
		self.AutoAttackButton.SetText("Off")
		self.AutoAttackButton.Show()
		
		self.AutoPickupButton = ui.Button()
		self.AutoPickupButton.SetParent(self)
		self.AutoPickupButton.SetPosition(75, 357)
		self.AutoPickupButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoPickupButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoPickupButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoPickupButton.SetEvent(ui.__mem_func__(self.AutoPickup))
		self.AutoPickupButton.SetText("Off")
		self.AutoPickupButton.Show()
		
		self.AutoRestartButton = ui.Button()
		self.AutoRestartButton.SetParent(self)
		self.AutoRestartButton.SetPosition(75, 387)
		self.AutoRestartButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoRestartButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoRestartButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoRestartButton.SetEvent(ui.__mem_func__(self.AutoRestart))
		self.AutoRestartButton.SetText("Off")
		self.AutoRestartButton.Show()
		
		self.InstructionButton = ui.Button()
		self.InstructionButton.SetParent(self)
		self.InstructionButton.SetPosition(10, 427)
		self.InstructionButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.InstructionButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.InstructionButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.InstructionButton.SetEvent(ui.__mem_func__(self.Instruction))
		self.InstructionButton.SetText("Run Instructions")
		self.InstructionButton.SetToolTipText("Open the Thread for an instructions")
		self.InstructionButton.Show()
		
		self.CopyrightButton = ui.Button()
		self.CopyrightButton.SetParent(self)
		self.CopyrightButton.SetPosition(150, 427)
		self.CopyrightButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.CopyrightButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.CopyrightButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.CopyrightButton.SetEvent(ui.__mem_func__(self.MyEpvpProfile))
		self.CopyrightButton.SetText("©123klo E*PvP")
		self.CopyrightButton.SetToolTipText("Open my E*PvP Profile")
		self.CopyrightButton.Show()
		
		
		global GhostModeButton
		GhostModeButton.SetText("")
		GhostModeButton.SetPosition(2, 45)
		GhostModeButton.SetSize(88,21)
		GhostModeButton.SetEvent(self.GhostMod)
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
		UpButton.SetEvent(self.RefineOneTime)
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
		
	def LoadEditLines(self):
	
		self.SlotBarRedPotting = ui.SlotBar()
		self.SlotBarRedPotting.SetParent(self)
		self.SlotBarRedPotting.SetSize(30, 18)
		self.SlotBarRedPotting.SetPosition(-32, 268)
		self.SlotBarRedPotting.SetWindowHorizontalAlignCenter()
		self.SlotBarRedPotting.Show()
		
		self.EditLineRedPotting = ui.EditLine()
		self.EditLineRedPotting.SetParent(self.SlotBarRedPotting)
		self.EditLineRedPotting.SetSize(30, 17)
		self.EditLineRedPotting.SetPosition(8, 2)
		self.EditLineRedPotting.SetMax(2)
		self.EditLineRedPotting.SetNumberMode()
		self.EditLineRedPotting.SetText("90")
		self.EditLineRedPotting.SetFocus()
		self.EditLineRedPotting.Show()
		
		
		self.SlotBarBluePotting = ui.SlotBar()
		self.SlotBarBluePotting.SetParent(self)
		self.SlotBarBluePotting.SetSize(30, 18)
		self.SlotBarBluePotting.SetPosition(-32, 298)
		self.SlotBarBluePotting.SetWindowHorizontalAlignCenter()
		self.SlotBarBluePotting.Show()
		
		self.EditLineBluePotting = ui.EditLine()
		self.EditLineBluePotting.SetParent(self.SlotBarBluePotting)
		self.EditLineBluePotting.SetSize(30, 17)
		self.EditLineBluePotting.SetPosition(8, 2)
		self.EditLineBluePotting.SetMax(2)
		self.EditLineBluePotting.SetNumberMode()
		self.EditLineBluePotting.SetText("40")
		self.EditLineBluePotting.SetFocus()
		self.EditLineBluePotting.Show()
		
		
		self.SlotBarMoveSpeed = ui.SlotBar()
		self.SlotBarMoveSpeed.SetParent(self)
		self.SlotBarMoveSpeed.SetSize(30, 18)
		self.SlotBarMoveSpeed.SetPosition(-30, 70)
		self.SlotBarMoveSpeed.SetWindowHorizontalAlignCenter()
		self.SlotBarMoveSpeed.Show()
		
		self.EditLineMoveSpeed = ui.EditLine()
		self.EditLineMoveSpeed.SetParent(self.SlotBarMoveSpeed)
		self.EditLineMoveSpeed.SetSize(30, 17)
		self.EditLineMoveSpeed.SetPosition(8, 2)
		self.EditLineMoveSpeed.SetMax(3)
		self.EditLineMoveSpeed.SetNumberMode()
		self.EditLineMoveSpeed.SetText("200")
		self.EditLineMoveSpeed.SetFocus()
		self.EditLineMoveSpeed.Show()
	
	
	def MyEpvpProfile(self):
	
		os.system("start http://www.elitepvpers.com/forum/members/2581363-123klo.html")
		
	def Instruction(self):
	
		os.system("start http://www.elitepvpers.com/forum/newthread.php?do=postthread&f=405")
		
		
		
			
	def RefineMode(self):
		
		global Refine
		
		if Refine == 0:
			Refine = 1
			self.SetRefineModeButton.SetText("Normal")
		else:	
			Refine = 0
			self.SetRefineModeButton.SetText("DT")
			
	def RefineOneTime(self):
	
		global Refine
	
		if Refine == 0:
			Refine = 1
			net.SendRefinePacket(int(0), int(4))    
		else:	
			Refine = 0
			net.SendRefinePacket(int(0), int(0dddddddddddd))
		
	def MoveSpeed(self):	
	
		global MoveSpeed
		
		if MoveSpeed == 0:
			MoveSpeed = 1
			self.MoveSpeedButton.SetText("On")
			self.EnableMoveSpeed()
		else:	
			MoveSpeed = 0
			self.MoveSpeedButton.SetText("Off")
			self.DisableMoveSpeed()
		
	def EnableMoveSpeed(self):

		MoveSpeed = self.EditLineMoveSpeed.GetText()
		NormalMoveSpeed = player.GetStatus(player.MOVING_SPEED)

		chr.SetMoveSpeed(int(NormalMoveSpeed))
		chr.SetMoveSpeed(int(MoveSpeed))
		
		self.delay = WaitingDialog()
		self.delay.Open(int(1.0))
		self.delay.SAFE_SetTimeOverEvent(self.EnableMoveSpeed)
		
	def DisableMoveSpeed(self):
	
		NormalMoveSpeed2 = player.GetStatus(player.MOVING_SPEED)
		chr.SetMoveSpeed(int(NormalMoveSpeed2))
		
		self.delay = WaitingDialog()
		self.delay.Open(int(99999999999999999))
		self.delay.SAFE_SetTimeOverEvent(self.DisableMoveSpeed)
		
	def GhostMod(self):
		
		chr.Revive()
		
	def Combo(self):
		
		global Combo
		
		if Combo == 0:
			Combo = 1
			self.ComboTypeButton.SetText("An")
			chr.testSetComboType(2)
		else:	
			Combo = 0
			self.ComboTypeButton.SetText("Aus")
			chr.testSetComboType(0)
	
	def ZoomHack(self):
		
		global ZoomHack
		
		if ZoomHack == 0:
			ZoomHack = 1
			self.ZoomHackButton.SetText("An")
			app.SetCameraMaxDistance(12000)	
		else:	
			ZoomHack = 0
			self.ZoomHackButton.SetText("Aus")
			app.SetCameraMaxDistance(2500)	
	
	def NoFog(self):
	
		global NoFog
		
		if NoFog == 0:
			NoFog = 1
			self.NoFogButton.SetText("An")
			app.SetMinFog(70000)
		else:	
			NoFog = 0
			self.NoFogButton.SetText("Aus")
			app.SetMinFog(2500)

	def DayNight(self):
	
		global DayNight
		
		if DayNight == 0:
			DayNight = 1
			self.DayNightButton.SetText("Night")
			background.SetEnvironmentData(1)
			background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
			
		else:	
			DayNight = 0
			self.DayNightButton.SetText("Day")
			background.SetEnvironmentData(0)
			
	def EnableSnow(self):
		
		global EnableSnow
		
		if EnableSnow == 0:
			EnableSnow = 1
			self.SnowButton.SetText("Snow")
			background.EnableSnow(1)
		else:	
			EnableSnow = 0
			self.SnowButton.SetText("Off")
			background.EnableSnow(0)
			
			
			
			
######### Auto Potting Red #########	
			
	def AutoRedPot(self):

		global AutoRedPot
		
		if AutoRedPot == 0:
			AutoRedPot = 1
			self.AutoRedPotButton.SetText("On")
			self.EnableRedAutoPotting()
			
		else:	
			AutoRedPot = 0
			self.AutoRedPotButton.SetText("Off")
			self.DisableRedAutoPotting()
			
	def EnableRedAutoPotting(self):
		
		MaxTP = player.GetStatus(player.MAX_HP)
		ActualTP = player.GetStatus(player.HP)
		RedPercentValue = self.EditLineRedPotting.GetText()
		
		if (float(ActualTP) / (float(MaxTP)) * 100) < int(RedPercentValue):
			for i in xrange(player.INVENTORY_PAGE_SIZE*3):
				RedPott = player.GetItemIndex(i)
				if RedPott == 27001 or RedPott == 27002 or RedPott == 27003:
					net.SendItemUsePacket(i)
					break
					
		self.delay = WaitingDialog()
		self.delay.Open(int(0.5))
		self.delay.SAFE_SetTimeOverEvent(self.EnableRedAutoPotting)
			
	def DisableRedAutoPotting(self):
		
		for i in xrange(player.INVENTORY_PAGE_SIZE*3):
				RedPott = player.GetItemIndex(i)
				if RedPott == 27001 or RedPott == 27002 or RedPott == 27003:
					net.SendItemUsePacket(i)
					break
					
		self.delay = WaitingDialog()
		self.delay.Open(int(999999999999999999999))
		self.delay.SAFE_SetTimeOverEvent(self.DisableRedAutoPotting)
		
	
######### Auto Potting Blue #########

	def AutoBluePot(self):

		global AutoBluePot
		
		if AutoBluePot == 0:
			AutoBluePot = 1
			self.AutoBluePotButton.SetText("On")
			self.EnableBlueAutoPotting()
			
		else:	
			AutoBluePot = 0
			self.AutoBluePotButton.SetText("Off")
			self.DisableBlueAutoPotting()
			
	def EnableBlueAutoPotting(self):

		MaxSP = player.GetStatus(player.MAX_SP)
		ActualSP = player.GetStatus(player.SP)
		BluePercentValue = self.EditLineBluePotting.GetText()
		
		if (float(ActualSP) / (float(MaxSP)) * 100) < int(BluePercentValue):
			for i in xrange(player.INVENTORY_PAGE_SIZE*3):
				BluePott = player.GetItemIndex(i)
				if BluePott == 27004 or BluePott == 27005 or BluePott == 27006:
					net.SendItemUsePacket(i)
					break
					
		self.delay = WaitingDialog()
		self.delay.Open(int(0.5))
		self.delay.SAFE_SetTimeOverEvent(self.EnableBlueAutoPotting)
			
	def DisableBlueAutoPotting(self):
		
		for i in xrange(player.INVENTORY_PAGE_SIZE*3):
				BluePott = player.GetItemIndex(i)
				if BluePott == 27004 or BluePott == 27005 or BluePott == 27006:
				#	net.SendItemUsePacket(i)
					break
					
		self.delay = WaitingDialog()
		self.delay.Open(int(999999999999999999999))
		self.delay.SAFE_SetTimeOverEvent(self.DisableBlueAutoPotting)	
		
		
		
		
	def AutoAttack(self):
		
		global AutoAttack
		
		if AutoAttack == 0:
			AutoAttack = 1
			self.AutoAttackButton.SetText("On")	
			self.EnableAutoAttack()
		else:	
			AutoAttack = 0
			self.AutoAttackButton.SetText("Off")
			self.DisableAutoAttack()
		
	def EnableAutoAttack(self):
	
		Direction = app.GetRandom(0,7)
		player.SetAttackKeyState(TRUE)
		chr.SetDirection(Direction)
		
		
		
		self.delay = WaitingDialog()
		self.delay.Open(int(1.0))
		self.delay.SAFE_SetTimeOverEvent(self.EnableAutoAttack)
			
	def DisableAutoAttack(self):
	
		player.SetAttackKeyState(FALSE)
		
		self.delay = WaitingDialog()
		self.delay.Open(int(99999999999999999))
		self.delay.SAFE_SetTimeOverEvent(self.DisableAutoAttack)

		
	def AutoPickup(self):

		global AutoPickup
		
		if AutoPickup == 0:
			AutoPickup = 1
			self.AutoPickupButton.SetText("On")	
			self.EnableAutoPickup()
		else:	
			AutoPickup = 0
			self.AutoPickupButton.SetText("Off")
			self.DisableAutoPickup()
		
	def EnableAutoPickup(self):
		
		
		
		player.PickCloseItem() 
		
		self.delay = WaitingDialog()
		self.delay.Open(int(0.5))
		self.delay.SAFE_SetTimeOverEvent(self.EnableAutoPickup)
			
	def DisableAutoPickup(self):
		
		player.PickCloseItem()
		
		self.delay = WaitingDialog()
		self.delay.Open(int(999999999999999999999999999999))
		self.delay.SAFE_SetTimeOverEvent(self.DisableAutoPickup)
		

		
	
	def AutoRestart(self):

		global AutoRestart
		
		if AutoRestart == 0:
			AutoRestart = 1
			self.AutoRestartButton.SetText("On")	
			self.EnableRestart()
		else:	
			AutoRestart = 0
			self.AutoRestartButton.SetText("Off")
			self.DisableRestart()
		
	def EnableRestart(self):
		
		net.SendChatPacket("/restart_here")
	
		self.delay = WaitingDialog()
		self.delay.Open(int(2.5))
		self.delay.SAFE_SetTimeOverEvent(self.EnableRestart)
		

	
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
		
	def OnPressExitKey(self):

		self.Close()
		return TRUE
		
Multi = MultihackDialog()
Multi.Close()