import app
import chat
import chr
import locale
import net
import player
import time
import ui
import skill
	
SCAN_START = 10000
SCAN_END = 5000000
mobVid = 0
AutoSkillUse1 = ""
AutoSkillUse2 = ""
AutoSkillUse2 = ""
AutoSkillUse3 = ""
AutoSkillUse4 = ""
AutoSkillUse5 = ""
AutoSkillUse6 = ""
AutoPottRed = ""
AutoPottBlue = ""
Levelbot = ""
AutoRevive = ""
x0 = ""
y0 = ""
z0 = ""
x1 = ""
y1 = ""
x2 = ""
y2 = ""
radius = ""
SetBase = ""
TapferkeitsUmhange = ""
LevelbotConfig = ""
TransferMobs = ""
AutoPickUp = ""
AttackSpeedHack = ""
MoveSpeedHack = ""
telestep = 0
teleport_mode = 0
last_teleport_time = 0
DoublePrevent = "inaktiv"
RestartBot = ""

class LevelBotDialog(ui.ThinBoard):
	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.__Load_LevelBotDialog()
		
	def __del__(self):
		ui.ThinBoard.__del__(self)

	def Destroy(self):
		global SetBase
		SetBase = ""
		self.Hide()
		return TRUE
		
	def __Load_LevelBotDialog(self):
		self.SetPosition(5, 350)
		self.SetSize(390, 550)
		self.Show()
		self.AddFlag("movable")
		self.AddFlag("float")
		
		self.LoadTextLines()
		self.LoadButtons()
		self.LoadEditLines()
		
		self.CheckState()

	def LoadEditLines(self):
		self.AutoPottBlueButtonPercentSlotBar = ui.SlotBar()
		self.AutoPottBlueButtonPercentSlotBar.SetParent(self)
		self.AutoPottBlueButtonPercentSlotBar.SetSize(30, 18)
		self.AutoPottBlueButtonPercentSlotBar.SetPosition(0 - (30 + 37 + 40), 164 + 9 - 2)
		self.AutoPottBlueButtonPercentSlotBar.SetWindowHorizontalAlignCenter()
		self.AutoPottBlueButtonPercentSlotBar.Show()
		
		self.AutoPottBlueButtonPercentEditline = ui.EditLine()
		self.AutoPottBlueButtonPercentEditline.SetParent(self.AutoPottBlueButtonPercentSlotBar)
		self.AutoPottBlueButtonPercentEditline.SetSize(30, 17)
		self.AutoPottBlueButtonPercentEditline.SetPosition(10, 2)
		self.AutoPottBlueButtonPercentEditline.SetMax(2)
		self.AutoPottBlueButtonPercentEditline.SetNumberMode()
		self.AutoPottBlueButtonPercentEditline.SetFocus()
		self.AutoPottBlueButtonPercentEditline.SetText("0")
		#self.AutoPottBlueButtonPercentEditline.SetTabEvent(ui.__mem_func__(self.AutoPottRedButtonPercentEditline.SetFocus))
		#self.AutoPottBlueButtonPercentEditline.SetReturnEvent(ui.__mem_func__(self.AutoPottRedButtonPercentEditline.SetFocus))
		self.AutoPottBlueButtonPercentEditline.Show()

		self.AutoPottRedButtonPercentSlotBar = ui.SlotBar()
		self.AutoPottRedButtonPercentSlotBar.SetParent(self)
		self.AutoPottRedButtonPercentSlotBar.SetSize(30, 18)
		self.AutoPottRedButtonPercentSlotBar.SetPosition(0 - (30 + 37 + 40), 124 + 9 - 2)
		self.AutoPottRedButtonPercentSlotBar.SetWindowHorizontalAlignCenter()
		self.AutoPottRedButtonPercentSlotBar.Show()
		
		self.AutoPottRedButtonPercentEditline = ui.EditLine()
		self.AutoPottRedButtonPercentEditline.SetParent(self.AutoPottRedButtonPercentSlotBar)
		self.AutoPottRedButtonPercentEditline.SetSize(30, 17)
		self.AutoPottRedButtonPercentEditline.SetPosition(10, 2)
		self.AutoPottRedButtonPercentEditline.SetMax(2)
		self.AutoPottRedButtonPercentEditline.SetNumberMode()
		self.AutoPottRedButtonPercentEditline.SetFocus()
		self.AutoPottRedButtonPercentEditline.SetText("0")
		self.AutoPottRedButtonPercentEditline.SetTabEvent(ui.__mem_func__(self.AutoPottBlueButtonPercentEditline.SetFocus))
		self.AutoPottRedButtonPercentEditline.SetReturnEvent(ui.__mem_func__(self.AutoPottBlueButtonPercentEditline.SetFocus))
		self.AutoPottRedButtonPercentEditline.Show()

		self.MoveSpeedStatsSlotbar = ui.SlotBar()
		self.MoveSpeedStatsSlotbar.SetParent(self)
		self.MoveSpeedStatsSlotbar.SetSize(30, 18)
		self.MoveSpeedStatsSlotbar.SetPosition(30, 164 + 9 - 2)
		self.MoveSpeedStatsSlotbar.SetWindowHorizontalAlignCenter()
		self.MoveSpeedStatsSlotbar.Show()
		
		self.MoveSpeedStats = ui.EditLine()
		self.MoveSpeedStats.SetParent(self.MoveSpeedStatsSlotbar)
		self.MoveSpeedStats.SetSize(30, 17)
		self.MoveSpeedStats.SetPosition(10, 2)
		self.MoveSpeedStats.SetMax(4)
		self.MoveSpeedStats.SetNumberMode()
		self.MoveSpeedStats.SetFocus()
		self.MoveSpeedStats.SetText("0")
		#self.MoveSpeedStats.SetTabEvent(ui.__mem_func__(self.AttackSpeedStats.SetFocus))
		#self.MoveSpeedStats.SetReturnEvent(ui.__mem_func__(self.AttackSpeedStats.SetFocus))
		self.MoveSpeedStats.Show()

		self.AttackSpeedStatsSlotbar = ui.SlotBar()
		self.AttackSpeedStatsSlotbar.SetParent(self)
		self.AttackSpeedStatsSlotbar.SetSize(30, 18)
		self.AttackSpeedStatsSlotbar.SetPosition(30, 124 + 9 - 2)
		self.AttackSpeedStatsSlotbar.SetWindowHorizontalAlignCenter()
		self.AttackSpeedStatsSlotbar.Show()
		
		self.AttackSpeedStats = ui.EditLine()
		self.AttackSpeedStats.SetParent(self.AttackSpeedStatsSlotbar)
		self.AttackSpeedStats.SetSize(30, 17)
		self.AttackSpeedStats.SetPosition(10, 2)
		self.AttackSpeedStats.SetMax(4)
		self.AttackSpeedStats.SetNumberMode()
		self.AttackSpeedStats.SetFocus()
		self.AttackSpeedStats.SetText("0")
		self.AttackSpeedStats.SetTabEvent(ui.__mem_func__(self.MoveSpeedStats.SetFocus))
		self.AttackSpeedStats.SetReturnEvent(ui.__mem_func__(self.MoveSpeedStats.SetFocus))
		self.AttackSpeedStats.Show()

		self.SetBaseRadiusSlotbar = ui.SlotBar()
		self.SetBaseRadiusSlotbar.SetParent(self)
		self.SetBaseRadiusSlotbar.SetSize(30, 18)
		self.SetBaseRadiusSlotbar.SetPosition(0 - (20 + 40), 294)
		self.SetBaseRadiusSlotbar.SetWindowHorizontalAlignCenter()
		self.SetBaseRadiusSlotbar.Show()
		
		self.SetBaseRadiusEditline = ui.EditLine()
		self.SetBaseRadiusEditline.SetParent(self.SetBaseRadiusSlotbar)
		self.SetBaseRadiusEditline.SetSize(30, 17)
		self.SetBaseRadiusEditline.SetPosition(10, 2)
		self.SetBaseRadiusEditline.SetMax(3)
		self.SetBaseRadiusEditline.SetNumberMode()
		self.SetBaseRadiusEditline.SetFocus()
		self.SetBaseRadiusEditline.SetText("0")
		#self.SetBaseRadiusEditline.SetTabEvent(ui.__mem_func__(self.MoveSpeedStats.SetFocus))
		#self.SetBaseRadiusEditline.SetReturnEvent(ui.__mem_func__(self.MoveSpeedStats.SetFocus))
		self.SetBaseRadiusEditline.Show()

		self.TapferkeitsUmhangeDelaySlotbar = ui.SlotBar()
		self.TapferkeitsUmhangeDelaySlotbar.SetParent(self)
		self.TapferkeitsUmhangeDelaySlotbar.SetSize(30, 18)
		self.TapferkeitsUmhangeDelaySlotbar.SetPosition(0 - (67 + 40), 294 + 40*2 + 9 - 2)
		self.TapferkeitsUmhangeDelaySlotbar.SetWindowHorizontalAlignCenter()
		self.TapferkeitsUmhangeDelaySlotbar.Show()
		
		self.TapferkeitsUmhangeDelay = ui.EditLine()
		self.TapferkeitsUmhangeDelay.SetParent(self.TapferkeitsUmhangeDelaySlotbar)
		self.TapferkeitsUmhangeDelay.SetSize(30, 17)
		self.TapferkeitsUmhangeDelay.SetPosition(8, 2)
		self.TapferkeitsUmhangeDelay.SetMax(3)
		self.TapferkeitsUmhangeDelay.SetNumberMode()
		self.TapferkeitsUmhangeDelay.SetFocus()
		self.TapferkeitsUmhangeDelay.SetText("0")
		#self.TapferkeitsUmhangeDelay.SetTabEvent(ui.__mem_func__(self.DelayChatSpamEditLine.SetFocus))
		#self.TapferkeitsUmhangeDelay.SetReturnEvent(ui.__mem_func__(self.DelayChatSpamEditLine.SetFocus))
		self.TapferkeitsUmhangeDelay.Show()

		self.TeleportZEditLineSlotBar = ui.SlotBar()
		self.TeleportZEditLineSlotBar.SetParent(self)
		self.TeleportZEditLineSlotBar.SetSize(43, 18)
		self.TeleportZEditLineSlotBar.SetPosition(-180 + 40 + 120, 294 + 40*3 + 1)
		self.TeleportZEditLineSlotBar.SetWindowHorizontalAlignCenter()
		self.TeleportZEditLineSlotBar.Show()
		
		self.TeleportZEditLine = ui.EditLine()
		self.TeleportZEditLine.SetParent(self.TeleportZEditLineSlotBar)
		self.TeleportZEditLine.SetSize(43, 17)
		self.TeleportZEditLine.SetPosition(16, 2)
		self.TeleportZEditLine.SetMax(4)
		self.TeleportZEditLine.SetNumberMode()
		self.TeleportZEditLine.SetFocus()
		self.TeleportZEditLine.SetText("0")
		#self.TeleportZEditLine.SetTabEvent(ui.__mem_func__(self.DelayChatSpamEditLine.SetFocus))
		#self.TeleportZEditLine.SetReturnEvent(ui.__mem_func__(self.DelayChatSpamEditLine.SetFocus))
		self.TeleportZEditLine.Show()

		self.TeleportYEditLineSlotBar = ui.SlotBar()
		self.TeleportYEditLineSlotBar.SetParent(self)
		self.TeleportYEditLineSlotBar.SetSize(43, 18)
		self.TeleportYEditLineSlotBar.SetPosition(-180 + 40 + 60, 294 + 40*3 + 1)
		self.TeleportYEditLineSlotBar.SetWindowHorizontalAlignCenter()
		self.TeleportYEditLineSlotBar.Show()
		
		self.TeleportYEditLine = ui.EditLine()
		self.TeleportYEditLine.SetParent(self.TeleportYEditLineSlotBar)
		self.TeleportYEditLine.SetSize(43, 17)
		self.TeleportYEditLine.SetPosition(16, 2)
		self.TeleportYEditLine.SetMax(4)
		self.TeleportYEditLine.SetNumberMode()
		self.TeleportYEditLine.SetFocus()
		self.TeleportYEditLine.SetText("0")
		self.TeleportYEditLine.SetTabEvent(ui.__mem_func__(self.TeleportZEditLine.SetFocus))
		self.TeleportYEditLine.SetReturnEvent(ui.__mem_func__(self.TeleportZEditLine.SetFocus))
		self.TeleportYEditLine.Show()

		self.TeleportXEditLineSlotBar = ui.SlotBar()
		self.TeleportXEditLineSlotBar.SetParent(self)
		self.TeleportXEditLineSlotBar.SetSize(43, 18)
		self.TeleportXEditLineSlotBar.SetPosition(-180 + 40, 294 + 40*3 + 1)
		self.TeleportXEditLineSlotBar.SetWindowHorizontalAlignCenter()
		self.TeleportXEditLineSlotBar.Show()
		
		self.TeleportXEditLine = ui.EditLine()
		self.TeleportXEditLine.SetParent(self.TeleportXEditLineSlotBar)
		self.TeleportXEditLine.SetSize(43, 17)
		self.TeleportXEditLine.SetPosition(16, 2)
		self.TeleportXEditLine.SetMax(4)
		self.TeleportXEditLine.SetNumberMode()
		self.TeleportXEditLine.SetFocus()
		self.TeleportXEditLine.SetText("0")
		self.TeleportXEditLine.SetTabEvent(ui.__mem_func__(self.TeleportYEditLine.SetFocus))
		self.TeleportXEditLine.SetReturnEvent(ui.__mem_func__(self.TeleportYEditLine.SetFocus))
		self.TeleportXEditLine.Show()
		
	def LoadButtons(self):
		self.CloseButton = ui.Button()
		self.CloseButton.SetParent(self)
		self.CloseButton.SetPosition(320, 39)
		self.CloseButton.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		self.CloseButton.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		self.CloseButton.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		self.CloseButton.SetToolTipText(locale.UI_CLOSE, 0, - 23)
		self.CloseButton.SetEvent(ui.__mem_func__(self.Close))
		self.CloseButton.Show()

		self.AutoSkillUse1 = ui.Button()
		self.AutoSkillUse1.SetParent(self)
		self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoSkillUse1.SetText("")
		self.AutoSkillUse1.SetPosition(30, 84)
		self.AutoSkillUse1.SetEvent(ui.__mem_func__(self.AutoSkillUseActivate1))
		self.AutoSkillUse1.Show()

		self.AutoSkillUse2 = ui.Button()
		self.AutoSkillUse2.SetParent(self)
		self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoSkillUse2.SetText("")
		self.AutoSkillUse2.SetPosition(30 + 3*1 + 32*1, 84)
		self.AutoSkillUse2.SetEvent(ui.__mem_func__(self.AutoSkillUseActivate2))
		self.AutoSkillUse2.Show()

		self.AutoSkillUse3 = ui.Button()
		self.AutoSkillUse3.SetParent(self)
		self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoSkillUse3.SetText("")
		self.AutoSkillUse3.SetPosition(30 + 3*2 + 32*2, 84)
		self.AutoSkillUse3.SetEvent(ui.__mem_func__(self.AutoSkillUseActivate3))
		self.AutoSkillUse3.Show()

		self.AutoSkillUse4 = ui.Button()
		self.AutoSkillUse4.SetParent(self)
		self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoSkillUse4.SetText("")
		self.AutoSkillUse4.SetPosition(30 + 3*3 + 32*3, 84)
		self.AutoSkillUse4.SetEvent(ui.__mem_func__(self.AutoSkillUseActivate4))
		self.AutoSkillUse4.Show()

		self.AutoSkillUse5 = ui.Button()
		self.AutoSkillUse5.SetParent(self)
		self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoSkillUse5.SetText("")
		self.AutoSkillUse5.SetPosition(30 + 3*4 + 32*4, 84)
		self.AutoSkillUse5.SetEvent(ui.__mem_func__(self.AutoSkillUseActivate5))
		self.AutoSkillUse5.Show()

		self.AutoSkillUse6 = ui.Button()
		self.AutoSkillUse6.SetParent(self)
		self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoSkillUse6.SetText("")
		self.AutoSkillUse6.SetPosition(30 + 3*5 + 32*5, 84)
		self.AutoSkillUse6.SetEvent(ui.__mem_func__(self.AutoSkillUseActivate6))
		self.AutoSkillUse6.Show()
		
		self.AutoSkillUse1Activated = ui.Button()
		self.AutoSkillUse1Activated.SetParent(self)
		self.AutoSkillUse1Activated.SetUpVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse1Activated.SetOverVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse1Activated.SetDownVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse1Activated.SetText("")
		self.AutoSkillUse1Activated.SetPosition(30, 84)
		self.AutoSkillUse1Activated.SetEvent(ui.__mem_func__(self.AutoSkillUseActivate1))
		self.AutoSkillUse1Activated.Show()

		self.AutoSkillUse2Activated = ui.Button()
		self.AutoSkillUse2Activated.SetParent(self)
		self.AutoSkillUse2Activated.SetUpVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse2Activated.SetOverVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse2Activated.SetDownVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse2Activated.SetText("")
		self.AutoSkillUse2Activated.SetPosition(30 + 3*1 + 32*1, 84)
		self.AutoSkillUse2Activated.SetEvent(ui.__mem_func__(self.AutoSkillUseActivate2))
		self.AutoSkillUse2Activated.Show()

		self.AutoSkillUse3Activated = ui.Button()
		self.AutoSkillUse3Activated.SetParent(self)
		self.AutoSkillUse3Activated.SetUpVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse3Activated.SetOverVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse3Activated.SetDownVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse3Activated.SetText("")
		self.AutoSkillUse3Activated.SetPosition(30 + 3*2 + 32*2, 84)
		self.AutoSkillUse3Activated.SetEvent(ui.__mem_func__(self.AutoSkillUseActivate3))
		self.AutoSkillUse3Activated.Show()

		self.AutoSkillUse4Activated = ui.Button()
		self.AutoSkillUse4Activated.SetParent(self)
		self.AutoSkillUse4Activated.SetUpVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse4Activated.SetOverVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse4Activated.SetDownVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse4Activated.SetText("")
		self.AutoSkillUse4Activated.SetPosition(30 + 3*3 + 32*3, 84)
		self.AutoSkillUse4Activated.SetEvent(ui.__mem_func__(self.AutoSkillUseActivate4))
		self.AutoSkillUse4Activated.Show()

		self.AutoSkillUse5Activated = ui.Button()
		self.AutoSkillUse5Activated.SetParent(self)
		self.AutoSkillUse5Activated.SetUpVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse5Activated.SetOverVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse5Activated.SetDownVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse5Activated.SetText("")
		self.AutoSkillUse5Activated.SetPosition(30 + 3*4 + 32*4, 84)
		self.AutoSkillUse5Activated.SetEvent(ui.__mem_func__(self.AutoSkillUseActivate5))
		self.AutoSkillUse5Activated.Show()

		self.AutoSkillUse6Activated = ui.Button()
		self.AutoSkillUse6Activated.SetParent(self)
		self.AutoSkillUse6Activated.SetUpVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse6Activated.SetOverVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse6Activated.SetDownVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
		self.AutoSkillUse6Activated.SetText("")
		self.AutoSkillUse6Activated.SetPosition(30 + 3*5 + 32*5, 84)
		self.AutoSkillUse6Activated.SetEvent(ui.__mem_func__(self.AutoSkillUseActivate6))
		self.AutoSkillUse6Activated.Show()

		self.AutoPottRedImage = ui.ExpandedImageBox()
		self.AutoPottRedImage.SetParent(self)
		self.AutoPottRedImage.SetPosition(30, 124)
		self.AutoPottRedImage.LoadImage(str("icon/item/27003.tga"))
		self.AutoPottRedImage.Show()
		
		self.AutoPottRedButton = ui.Button()
		self.AutoPottRedButton.SetParent(self.AutoPottRedImage)
		self.AutoPottRedButton.SetPosition(20, 10)
		self.AutoPottRedButton.SetSize(70, 40)
		self.AutoPottRedButton.SetEvent(ui.__mem_func__(self.AutoPottRedActivate))
		self.AutoPottRedButton.Show()

		self.AutoPottRedImageActivated = ui.ExpandedImageBox()
		self.AutoPottRedImageActivated.SetParent(self)
		self.AutoPottRedImageActivated.SetPosition(35, 124)
		self.AutoPottRedImageActivated.LoadImage(str("icon/item/30040.tga"))
		
		self.AutoPottRedButtonActivated = ui.Button()
		self.AutoPottRedButtonActivated.SetParent(self.AutoPottRedImageActivated)
		self.AutoPottRedButtonActivated.SetPosition(20, 10)
		self.AutoPottRedButtonActivated.SetSize(70, 40)
		self.AutoPottRedButtonActivated.SetEvent(ui.__mem_func__(self.AutoPottRedActivate))
		
		self.AutoPottBlueImage = ui.ExpandedImageBox()
		self.AutoPottBlueImage.SetParent(self)
		self.AutoPottBlueImage.SetPosition(30, 164)
		self.AutoPottBlueImage.LoadImage(str("icon/item/27006.tga"))
		self.AutoPottBlueImage.Show()
		
		self.AutoPottBlueButton = ui.Button()
		self.AutoPottBlueButton.SetParent(self.b)
		self.AutoPottBlueButton.SetPosition(20, 10)
		self.AutoPottBlueButton.SetSize(70, 40)
		self.AutoPottBlueButton.SetEvent(ui.__mem_func__(self.AutoPottBlueActivate))
		self.AutoPottBlueButton.Show()

		self.AutoPottBlueImageActivated = ui.ExpandedImageBox()
		self.AutoPottBlueImageActivated.SetParent(self)
		self.AutoPottBlueImageActivated.SetPosition(35, 164)
		self.AutoPottBlueImageActivated.LoadImage(str("icon/item/30040.tga"))
		
		self.AutoPottBlueButtonActivated = ui.Button()
		self.AutoPottBlueButtonActivated.SetParent(self.AutoPottBlueImageActivated)
		self.AutoPottBlueButtonActivated.SetPosition(20, 10)
		self.AutoPottBlueButtonActivated.SetSize(70, 40)
		self.AutoPottBlueButtonActivated.SetEvent(ui.__mem_func__(self.AutoPottBlueActivate))
		
		self.AttackSpeedStatusButton = ui.Button()
		self.AttackSpeedStatusButton.SetParent(self)
		self.AttackSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AttackSpeedStatusButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AttackSpeedStatusButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AttackSpeedStatusButton.SetText("Deaktiviert")
		self.AttackSpeedStatusButton.SetPosition(159 + 50 + 39, 124 + 9 - 2)
		self.AttackSpeedStatusButton.SetEvent(ui.__mem_func__(self.AttackSpeedStatus))
		self.AttackSpeedStatusButton.Show()

		self.MoveSpeedStatusButton = ui.Button()
		self.MoveSpeedStatusButton.SetParent(self)
		self.MoveSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.MoveSpeedStatusButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.MoveSpeedStatusButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.MoveSpeedStatusButton.SetText("Deaktiviert")
		self.MoveSpeedStatusButton.SetPosition(159 + 50 + 39, 164 + 9 - 2)
		self.MoveSpeedStatusButton.SetEvent(ui.__mem_func__(self.MoveSpeedStatus))
		self.MoveSpeedStatusButton.Show()

		self.AutoReviveButton = ui.Button()
		self.AutoReviveButton.SetParent(self)
		self.AutoReviveButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
		self.AutoReviveButton.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")
		self.AutoReviveButton.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		self.AutoReviveButton.SetText("Automatischer Neustart")
		self.AutoReviveButton.SetPosition(30, 214)
		self.AutoReviveButton.SetEvent(ui.__mem_func__(self.AutoReviveActivate))
		self.AutoReviveButton.Show()
	
		self.GetTargetVidButton = ui.Button()
		self.GetTargetVidButton.SetParent(self)
		self.GetTargetVidButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.GetTargetVidButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.GetTargetVidButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.GetTargetVidButton.SetText("Get Target Vid")
		self.GetTargetVidButton.SetPosition(30, 254)
		self.GetTargetVidButton.SetEvent(ui.__mem_func__(self.GetTargetVID))
		self.GetTargetVidButton.Show()

		self.SetVIDRangeButton = ui.Button()
		self.SetVIDRangeButton.SetParent(self)
		self.SetVIDRangeButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.SetVIDRangeButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.SetVIDRangeButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.SetVIDRangeButton.SetText("Set VID Range")
		self.SetVIDRangeButton.SetPosition(30 + 88 + 4, 254)
		self.SetVIDRangeButton.SetEvent(ui.__mem_func__(self.SetVIDRange))
		self.SetVIDRangeButton.Show()

		self.SetBasePositionButton = ui.Button()
		self.SetBasePositionButton.SetParent(self)
		self.SetBasePositionButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.SetBasePositionButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.SetBasePositionButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.SetBasePositionButton.SetText("Setze Base")
		self.SetBasePositionButton.SetPosition(30, 294)
		self.SetBasePositionButton.SetEvent(ui.__mem_func__(self.SetBasePosition))
		self.SetBasePositionButton.Show()

		self.TransferBasePositionButton = ui.Button()
		self.TransferBasePositionButton.SetParent(self)
		self.TransferBasePositionButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.TransferBasePositionButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.TransferBasePositionButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.TransferBasePositionButton.SetText("Transfer to Base")
		self.TransferBasePositionButton.SetPosition(30, 294 + 40)
		self.TransferBasePositionButton.SetEvent(ui.__mem_func__(self.TransferBasePosition))
		self.TransferBasePositionButton.Show()

		self.DeactivateBaseButton = ui.Button()
		self.DeactivateBaseButton.SetParent(self)
		self.DeactivateBaseButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.DeactivateBaseButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.DeactivateBaseButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.DeactivateBaseButton.SetText("Deaktiviere Range")
		self.DeactivateBaseButton.SetPosition(30 + 88 + 4, 294 + 40)
		self.DeactivateBaseButton.SetEvent(ui.__mem_func__(self.DeactivateBasePosition))
		self.DeactivateBaseButton.Show()

		self.TapferkeitsUmhangeImage = ui.ExpandedImageBox()
		self.TapferkeitsUmhangeImage.SetParent(self)
		self.TapferkeitsUmhangeImage.SetPosition(30, 294 + 40*2)
		self.TapferkeitsUmhangeImage.LoadImage(str("icon/item/70038.tga"))
		self.TapferkeitsUmhangeImage.Show()
		
		self.TapferkeitsUmhangeButton = ui.Button()
		self.TapferkeitsUmhangeButton.SetParent(self.TapferkeitsUmhangeImage)
		self.TapferkeitsUmhangeButton.SetPosition(20, 10)
		self.TapferkeitsUmhangeButton.SetSize(70, 40)
		self.TapferkeitsUmhangeButton.SetEvent(ui.__mem_func__(self.SetTapferkeitsUmhange))
		self.TapferkeitsUmhangeButton.Show()
		
		self.TapferkeitsUmhangeImageActivated = ui.ExpandedImageBox()
		self.TapferkeitsUmhangeImageActivated.SetParent(self)
		self.TapferkeitsUmhangeImageActivated.SetPosition(35, 294 + 40*2 + 5)
		self.TapferkeitsUmhangeImageActivated.LoadImage(str("icon/item/30040.tga"))
		
		self.TapferkeitsUmhangeButtonActivated = ui.Button()
		self.TapferkeitsUmhangeButtonActivated.SetParent(self.TapferkeitsUmhangeImageActivated)
		self.TapferkeitsUmhangeButtonActivated.SetPosition(20, 10)
		self.TapferkeitsUmhangeButtonActivated.SetSize(70, 40)
		self.TapferkeitsUmhangeButtonActivated.SetEvent(ui.__mem_func__(self.SetTapferkeitsUmhange))

		self.AutoPickUpButton = ui.Button()
		self.AutoPickUpButton.SetParent(self)
		self.AutoPickUpButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.AutoPickUpButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.AutoPickUpButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.AutoPickUpButton.SetText("Auto PickUp")
		self.AutoPickUpButton.SetPosition(30 + 88 + 4, 294 + 40*2)
		self.AutoPickUpButton.SetEvent(ui.__mem_func__(self.SelectAutoPickUp))
		self.AutoPickUpButton.Show()

		self.TeleportButton = ui.Button()
		self.TeleportButton.SetParent(self)
		self.TeleportButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.TeleportButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.TeleportButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.TeleportButton.SetText("Teleport")
		self.TeleportButton.SetPosition(30 + 88*2 + 4*2, 294 + 40*3)
		self.TeleportButton.SetEvent(ui.__mem_func__(self.TeleportToCoordinates))
		self.TeleportButton.Show()

		self.TeleportToMobsManyButton = ui.Button()
		self.TeleportToMobsManyButton.SetParent(self)
		self.TeleportToMobsManyButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.TeleportToMobsManyButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.TeleportToMobsManyButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.TeleportToMobsManyButton.SetText("Teleport to Mobs")
		self.TeleportToMobsManyButton.SetPosition(30, 454)
		self.TeleportToMobsManyButton.SetEvent(ui.__mem_func__(self.SelectTeleportToMobsMany))
		self.TeleportToMobsManyButton.Show()

		self.TransferMobsButton = ui.Button()
		self.TransferMobsButton.SetParent(self)
		self.TransferMobsButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.TransferMobsButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.TransferMobsButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.TransferMobsButton.SetText("Transfer Mobs")
		self.TransferMobsButton.SetPosition(30 + 92, 454)
		self.TransferMobsButton.SetEvent(ui.__mem_func__(self.SelectTransferMobs))
		self.TransferMobsButton.Show()

		self.AttackAndStandButton = ui.Button()
		self.AttackAndStandButton.SetParent(self)
		self.AttackAndStandButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.AttackAndStandButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.AttackAndStandButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.AttackAndStandButton.SetText("Stand & Attack")
		self.AttackAndStandButton.SetPosition(30 + 92*2, 454)
		self.AttackAndStandButton.SetEvent(ui.__mem_func__(self.SelectAttackAndStand))
		self.AttackAndStandButton.Show()

		self.StartLevelBotButton = ui.Button()
		self.StartLevelBotButton.SetParent(self)
		self.StartLevelBotButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
		self.StartLevelBotButton.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")
		self.StartLevelBotButton.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		self.StartLevelBotButton.SetText("Levelbot Start")
		self.StartLevelBotButton.SetPosition(13, 494)
		self.StartLevelBotButton.SetEvent(ui.__mem_func__(self.StartLevelBot))
		self.StartLevelBotButton.Show()

		self.StopLevelBotButton = ui.Button()
		self.StopLevelBotButton.SetParent(self)
		self.StopLevelBotButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
		self.StopLevelBotButton.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")
		self.StopLevelBotButton.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		self.StopLevelBotButton.SetText("Levelbot Stopp")
		self.StopLevelBotButton.SetPosition(197, 494)
		self.StopLevelBotButton.SetEvent(ui.__mem_func__(self.StopLevelBot))
		self.StopLevelBotButton.Show()
		
	def CreateImageButtons(self, UpVisual, OverVisual, DownVisual, Image, XPosition, YPosition, event, name):
		self.SpecialImageBox = ui.ExpandedImageBox()
		self.SpecialImageBox.SetParent(self)
		self.SpecialImageBox.SetPosition(int(XPosition), int(YPosition))
		if str(Image) != "":
			self.SpecialImageBox + str(name).LoadImage(str(Image))
		self.SpecialImageBox + str(name).Show()
		
		self.ImageBoxButton = ui.Button()
		if str(UpVisual) != "":
			self.ImageBoxButton.SetUpVisual(str(UpVisual))
		if str(OverVisual) != "":
			self.ImageBoxButton.SetOverVisual(str(OverVisual))
		if str(DownVisual) != "":
			self.ImageBoxButton.SetDownVisual(str(DownVisual))
		self.ImageBoxButton.SetText("Abbrechen")
		self.ImageBoxButton.SetParent(self.SpecialImageBox)
		self.ImageBoxButton.SetPosition(20, 10)
		self.ImageBoxButton.SetSize(70, 40)
		self.ImageBoxButton.SetEvent(ui.__mem_func__(event))
		self.ImageBoxButton.Show()

	def LoadTextLines(self):
		self.Headline = ui.TextLine()
		self.Headline.SetParent(self)
		self.Headline.SetDefaultFontName()
		self.Headline.SetPosition(30, 39)
		self.Headline.SetFeather()
		self.Headline.SetText("Levelbot 1.2 Konfiguration")
		self.Headline.SetFontColor(1.0, 0.5, 0.5)
		self.Headline.SetOutline()
		self.Headline.Show()
		
		self.AttackSpeedHackHeadline = ui.TextLine()
		self.AttackSpeedHackHeadline.SetParent(self)
		self.AttackSpeedHackHeadline.SetDefaultFontName()
		self.AttackSpeedHackHeadline.SetPosition(30 + 88 + 3, 124 + 10)
		self.AttackSpeedHackHeadline.SetFeather()
		self.AttackSpeedHackHeadline.SetText("Attack Speed Hack")
		self.AttackSpeedHackHeadline.SetFontColor(1.0, 1.0, 1.0)
		self.AttackSpeedHackHeadline.SetOutline()
		self.AttackSpeedHackHeadline.Show()

		self.MoveSpeedHackHeadline = ui.TextLine()
		self.MoveSpeedHackHeadline.SetParent(self)
		self.MoveSpeedHackHeadline.SetDefaultFontName()
		self.MoveSpeedHackHeadline.SetPosition(30 + 88 + 3, 164 + 10)
		self.MoveSpeedHackHeadline.SetFeather()
		self.MoveSpeedHackHeadline.SetText("Move Speed Hack")
		self.MoveSpeedHackHeadline.SetFontColor(1.0, 1.0, 1.0)
		self.MoveSpeedHackHeadline.SetOutline()
		self.MoveSpeedHackHeadline.Show()

		self.SetBaseRadiusText = ui.TextLine()
		self.SetBaseRadiusText.SetParent(self)
		self.SetBaseRadiusText.SetDefaultFontName()
		self.SetBaseRadiusText.SetPosition(30  + 88 + 9 + 30, 295)
		self.SetBaseRadiusText.SetFeather()
		self.SetBaseRadiusText.SetText("Base Radius")
		self.SetBaseRadiusText.SetFontColor(1.0, 1.0, 1.0)
		self.SetBaseRadiusText.SetOutline()
		self.SetBaseRadiusText.Show()
		
	def AutoReviveActivate(self):
		global AutoRevive
		if AutoRevive == "":
			AutoRevive = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Auto-Revive aktiviert!")
			self.AutoReviveButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		else:
			AutoRevive = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Auto-Revive deaktiviert!")
			self.AutoReviveButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")

	def AutoPottRedActivate(self):
		global AutoPottRed
		if AutoPottRed == "":
			AutoPottRed = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Roter Auto-Pott aktiviert!")
			self.AutoPottRedImageActivated.Show()
			self.AutoPottRedButtonActivated.Show()
		else:
			AutoPottRed = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Roter Auto-Pott deaktiviert!")
			self.AutoPottRedImageActivated.Hide()
			self.AutoPottRedButtonActivated.Hide()

	def AutoPottBlueActivate(self):
		global AutoPottBlue
		if AutoPottBlue == "":
			AutoPottBlue = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Blauer Auto-Pott aktiviert!")
			self.AutoPottBlueImageActivated.Show()
			self.AutoPottBlueButtonActivated.Show()
		else:
			AutoPottBlue = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Blauer Auto-Pott deaktiviert!")
			self.AutoPottBlueImageActivated.Hide()
			self.AutoPottBlueButtonActivated.Hide()

	def SelectAutoPickUp(self):
		global AutoPickUp
		if AutoPickUp == "":
			AutoPickUp = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Auto PickUp aktiviert!")
			self.AutoPickUpButton.SetUpVisual("d:/ymir work/ui/public/large_button_03.sub")
		else:
			AutoPickUp = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Auto PickUp deaktiviert!")
			self.AutoPickUpButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			
	def AutoSkillUseActivate1(self):
		global AutoSkillUse1
		if AutoSkillUse1 == "":
			AutoSkillUse1 = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Autoskill 1 aktiviert!")
			self.AutoSkillUse1Activated.Show()
		else:
			AutoSkillUse1 = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Autoskill 1 deaktiviert!")
			self.AutoSkillUse1Activated.Hide()

	def AutoSkillUseActivate2(self):
		global AutoSkillUse2
		if AutoSkillUse2 == "":
			AutoSkillUse2 = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Autoskill 2 aktiviert!")
			self.AutoSkillUse2Activated.Show()
		else:
			AutoSkillUse2 = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Autoskill 2 deaktiviert!")
			self.AutoSkillUse2Activated.Hide()

	def AutoSkillUseActivate3(self):
		global AutoSkillUse3
		if AutoSkillUse3 == "":
			AutoSkillUse3 = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Autoskill 3 aktiviert!")
			self.AutoSkillUse3Activated.Show()
		else:
			AutoSkillUse3 = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Autoskill 3 deaktiviert!")
			self.AutoSkillUse3Activated.Hide()

	def AutoSkillUseActivate4(self):
		global AutoSkillUse4
		if AutoSkillUse4 == "":
			AutoSkillUse4 = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Autoskill 4 aktiviert!")
			self.AutoSkillUse4Activated.Show()
		else:
			AutoSkillUse4 = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Autoskill 4 deaktiviert!")
			self.AutoSkillUse4Activated.Hide()

	def AutoSkillUseActivate5(self):
		global AutoSkillUse5
		if AutoSkillUse5 == "":
			AutoSkillUse5 = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Autoskill 5 aktiviert!")
			self.AutoSkillUse5Activated.Show()
		else:
			AutoSkillUse5 = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Autoskill 5 deaktiviert!")
			self.AutoSkillUse5Activated.Hide()

	def AutoSkillUseActivate6(self):
		global AutoSkillUse6
		if AutoSkillUse6 == "":
			AutoSkillUse6 = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Autoskill 6 aktiviert!")
			self.AutoSkillUse6Activated.Show()
		else:
			AutoSkillUse6 = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Autoskill 6 deaktiviert!")
			self.AutoSkillUse6Activated.Hide()
		
	def TeleportToCoordinates(self):
		global telestep
		global teleport_mode
		x_coordinate = self.TeleportXEditLine.GetText()
		y_coordinate = self.TeleportYEditLine.GetText()
		z_coordinate = self.TeleportZEditLine.GetText()
		x_coordinate = int(x_coordinate)*100
		y_coordinate = int(y_coordinate)*100
		z_coordinate = int(z_coordinate)*100
		(ax, ay, az) = player.GetMainCharacterPosition()
		teleport_mode = 1
		
###Teleportsteps by musicinstructor		
		if int(x_coordinate) < int(ax):
			while int(x_coordinate) < int(ax):
				if telestep > 10:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Um einen Packet-Flood Kick zu vermeiden wird erst in 5 Sekunden weiterteleportiert.")
					return
				chr.SetPixelPosition(int(ax) - 2000, int(ay))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				(ax, ay, az) = player.GetMainCharacterPosition()
				telestep = telestep + 1
				
			chr.SetPixelPosition(int(x_coordinate), int(ay))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
			
		if int(x_coordinate) > int(ax):
			while int(x_coordinate) > int(ax):
				if telestep > 10:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Um einen Packet-Flood Kick zu vermeiden wird erst in 5 Sekunden weiterteleportiert.")
					return
				chr.SetPixelPosition(int(ax) + 2000, int(ay))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				(ax, ay, az) = player.GetMainCharacterPosition()
				telestep = telestep + 1
				
			chr.SetPixelPosition(int(x_coordinate), int(ay))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
			
		if int(y_coordinate) < int(ay):
			while int(y_coordinate) < int(ay):
				if telestep > 10:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Um einen Packet-Flood Kick zu vermeiden wird erst in 5 Sekunden weiterteleportiert.")
					return
				chr.SetPixelPosition(int(ax), int(ay) - 2000)
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				(ax, ay, az) = player.GetMainCharacterPosition()
				telestep = telestep + 1
			
			chr.SetPixelPosition(int(ax), int(y_coordinate))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
			
		if int(y_coordinate) > int(ay):
			while int(y_coordinate) > int(ay):
				if telestep > 10:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Um einen Packet-Flood Kick zu vermeiden wird erst in 5 Sekunden weiterteleportiert.")
					return
				chr.SetPixelPosition(int(ax), int(ay) + 2000)
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				(ax, ay, az) = player.GetMainCharacterPosition()
				telestep = telestep + 1

			chr.SetPixelPosition(int(ax), int(y_coordinate))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

		if int(z_coordinate) < int(az) and int(z_coordinate) != 0:
			while int(z_coordinate) < int(az):
				if telestep > 7:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Um einen Packet-Flood Kick zu vermeiden wird erst in 5 Sekunden weiterteleportiert.")
					return
				chr.SetPixelPosition(int(ax), int(ay), int(az) - 2000)
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				(ax, ay, az) = player.GetMainCharacterPosition()
				telestep = telestep + 1

			chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
			
		if int(z_coordinate) > int(az) and int(z_coordinate) != 0:
			while int(z_coordinate) > int(az):
				if telestep > 7:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Um einen Packet-Flood Kick zu vermeiden wird erst in 5 Sekunden weiterteleportiert.")
					return
				chr.SetPixelPosition(int(ax), int(ay), int(az) + 2000)
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				(ax, ay, az) = player.GetMainCharacterPosition()
				telestep = telestep + 1

			chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
		
		teleport_mode = 0

	def SelectTeleportToMobsMany(self):
		global LevelbotConfig
		if LevelbotConfig == "" or LevelbotConfig == 1:
			LevelbotConfig = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot Konfiguration: Teleport to mobs!")
			self.TeleportToMobsManyButton.SetUpVisual("d:/ymir work/ui/public/large_button_03.sub")
			self.AttackAndStandButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			self.TransferMobsButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		else:
			LevelbotConfig = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot Konfiguration: Teleport to mobs deactivated!")
			self.TeleportToMobsManyButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
	
	def SelectAttackAndStand(self):
		global LevelbotConfig
		global TransferMobs
		if (LevelbotConfig == "" or LevelbotConfig == 0) and TransferMobs == "":
			LevelbotConfig = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot Konfiguration: Stand and attack!")
			self.AttackAndStandButton.SetUpVisual("d:/ymir work/ui/public/large_button_03.sub")
			self.TeleportToMobsManyButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		elif (LevelbotConfig == "" or LevelbotConfig == 0) and TransferMobs == 1:
			LevelbotConfig = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot Konfiguration: Transfer the mobs and stand and attack!")
			self.AttackAndStandButton.SetUpVisual("d:/ymir work/ui/public/large_button_03.sub")
		else:
			LevelbotConfig = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot Konfiguration: Stand and attack deactivated!")
			self.AttackAndStandButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		
	def SelectTransferMobs(self):
		global TransferMobs
		global LevelbotConfig
		if LevelbotConfig == 1 and TransferMobs == "":
			TransferMobs = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot Konfiguration: Transfer the mobs and stand and attack!")
			self.TransferMobsButton.SetUpVisual("d:/ymir work/ui/public/large_button_03.sub")
		elif TransferMobs == "" and (LevelbotConfig == "" or LevelbotConfig == 0):
			TransferMobs = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot Konfiguration: Transfer the mobs!")
			self.TransferMobsButton.SetUpVisual("d:/ymir work/ui/public/large_button_03.sub")
		else:
			TransferMobs = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot Konfiguration: Transfer the mobs deactivated!")
			self.TransferMobsButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			
	def AttackSpeedStatus(self):
		global AttackSpeedHack
		CurrentAttackSpeedHack = self.AttackSpeedStats.GetText()
		if AttackSpeedHack == "":
			AttackSpeedHack = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Attack Speed auf "+ str(CurrentAttackSpeedHack) + " gesetzt!")
			chr.SetAttackSpeed(int(CurrentAttackSpeedHack))
			self.AttackSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_03.sub")
			self.AttackSpeedStatusButton.SetText("Aktiviert")
		elif int(CurrentAttackSpeedHack) < 0.01:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Ungültiger Operator für den Attack Speed.")		
		else:
			if int(CurrentAttackSpeedHack) > 0.01:
				AttackSpeedHack = ""
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Attack Speed Hack deaktiviert!")
				chr.SetAttackSpeed(int(player.GetStatus(player.ATT_SPEED)))
				self.AttackSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
				self.AttackSpeedStatusButton.SetText("Deaktiviert")
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Ungültiger Operator für den Attack Speed.")		
			
	
	def MoveSpeedStatus(self):
		global MoveSpeedHack
		CurrentMoveSpeedHack = self.MoveSpeedStats.GetText()
		if MoveSpeedHack == "":
			MoveSpeedHack = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Move Speed auf "+ str(CurrentMoveSpeedHack) + " gesetzt!")
			chr.SetMoveSpeed(int(CurrentMoveSpeedHack))
			if int(CurrentMoveSpeedHack) > 200:
				self.MoveSpeedFix = WaitingDialog()
				self.MoveSpeedFix.Open(0.5)
				self.MoveSpeedFix.SAFE_SetTimeOverEvent(self.MoveSpeedHackFixLoop1)
			self.MoveSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_03.sub")
			self.MoveSpeedStatusButton.SetText("Aktiviert")
		elif int(CurrentMoveSpeedHack) < 0.01:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Ungültiger Operator für den Move Speed.")		
		else:
			if int(CurrentMoveSpeedHack) > 0.01:
				MoveSpeedHack = ""
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Move Speed Hack deaktiviert!")
				chr.SetMoveSpeed(int(player.GetStatus(player.MOVING_SPEED)))
				self.MoveSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
				self.MoveSpeedStatusButton.SetText("Deaktiviert")
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Ungültiger Operator für den Move Speed.")
				
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

	def PotionCheck(self):
		PositiveCount = 0
		for i in xrange(player.INVENTORY_PAGE_SIZE*2):
			ItemValue = player.GetItemIndex(i)
			if ItemValue == 27001 or ItemValue == 27002 or ItemValue == 27003:
				PositiveCount += 1
		return PositiveCount
		
	def StartLevelBot(self):
		global LevelbotConfig
		global TransferMobs
		global Levelbot
		if Levelbot == "":
			if LevelbotConfig == 0:
				Levelbot = 1
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot aktiviert!")
				self.StartLevelBotButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
				self.TeleportToMobs()
			elif (LevelbotConfig == 1 and TransferMobs == "") or LevelbotConfig == 1:
				Levelbot = 1
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot aktiviert!")
				self.StartLevelBotButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
				self.AttackAndStand()
			elif LevelbotConfig == 1 and TransferMobs != "":
				Levelbot = 1
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot aktiviert!")
				self.StartLevelBotButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
				self.AttackAndStand()
				self.TransferMobs()
			elif TransferMobs != "":
				Levelbot = 1
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Moblock aktiviert!")
				self.StartLevelBotButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
				self.TransferMobs()
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Bitte wähle eine Levelmethode!")			
		elif Levelbot != "":
			if LevelbotConfig == "" or TransferMobs == "":
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Bitte wähle eine Levelmethode!")
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot ist bereits aktiviert!")
		
	def TransferMobs(self):
		global SCAN_START
		global SCAN_END
		global Levelbot
		myVid = player.GetMainCharacterIndex()
		x, y, z = player.GetMainCharacterPosition()
		for i in xrange(SCAN_START, SCAN_END):
			if chr.INSTANCE_TYPE_ENEMY == chr.GetInstanceType(i) and Levelbot != "":
				chr.SelectInstance(i)
				chr.SetPixelPosition(int(x), int(y), int(z))
		if Levelbot != "":
			self.TeleportDelay = WaitingDialog()
			self.TeleportDelay.Open(5.0)
			self.TeleportDelay.SAFE_SetTimeOverEvent(self.TransferMobs)
			
		chr.SelectInstance(myVid)
		
	def StopLevelBot(self):
		global Levelbot
		global SetBase
		if Levelbot == "":
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot ist bereits deaktiviert!")
		elif Levelbot != "":
			Levelbot = ""
			SetBase = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Levelbot deaktiviert!")
			self.OnBreakLevelBot()
			self.SetBasePositionButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")	
			self.StartLevelBotButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
			
	def SetTapferkeitsUmhange(self):
		global TapferkeitsUmhange
		if TapferkeitsUmhange == "":	
			TapferkeitsUmhange = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Tapferkeitsumhänge wurden aktiviert.")
			self.TapferkeitsUmhangeButtonActivated.Show()
			self.TapferkeitsUmhangeImageActivated.Show()
			self.UseTapferkeitsUmhange()
		else:
			TapferkeitsUmhange = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Tapferkeitsumhänge wurden deaktiviert.")
			self.TapferkeitsUmhangeButtonActivated.Hide()
			self.TapferkeitsUmhangeImageActivated.Hide()
			
	def UseTapferkeitsUmhange(self):
		if TapferkeitsUmhange != "":
			for i in xrange(player.INVENTORY_PAGE_SIZE*3):
				ItemValue = player.GetItemIndex(i)
				if ItemValue == 70038:
					TapferkeitsUmhangeWaitingDelay = self.TapferkeitsUmhangeDelay.GetText()
					net.SendItemUsePacket(i)
					self.TapferkeitsUmhangDelay = WaitingDialog()
					self.TapferkeitsUmhangDelay.Open(int(TapferkeitsUmhangeWaitingDelay))
					self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.UseTapferkeitsUmhange)
					break
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Tapferkeitsumhänge wurden deaktiviert.")			
		
	def SetBasePosition(self):
		global x0
		global y0
		global z0
		global x1
		global y1
		global x2
		global y2
		global SetBase
		radius = self.SetBaseRadiusEditline.GetText()
		(x, y, z) = player.GetMainCharacterPosition()
		x = float(x)
		y = float(y)
		z = float(z)
		radius = float(radius)
		if int(radius) < 10:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Bitte wähle einen größeren Radius.")
		else:
			x1 = int(x-radius*100)
			y1 = int(y-radius*100)
			x2 = int(x+radius*100)
			y2 = int(y+radius*100)
			x0 = int(x)
			y0 = int(y)
			z0 = int(z)
#			chat.AppendChat(chat.CHAT_TYPE_INFO, "Base Position gesetzt auf: (" + str(x1/100) + ", " + str(y1/100) + ", " + str(z/100) + ")")
#			chat.AppendChat(chat.CHAT_TYPE_INFO, "Base Position gesetzt auf: (" + str(x2/100) + ", " + str(y2/100) + ", " + str(z/100) + ")")
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Aktuelle Position : (" + str(x0/100) + ", " + str(y0/100) + ", " + str(z0/100) + ")")
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Deine Base Range beträgt " + str(int(radius)) + " Koordinaten.")
			self.SetBasePositionButton.SetUpVisual("d:/ymir work/ui/public/large_button_03.sub")
			SetBase = 1

	def AttackAndStand(self):
		global x0
		global y0
		global z0
		global SetBase
		(x, y, z) = player.GetMainCharacterPosition()
		x0 = int(x)
		y0 = int(y)
		z0 = int(z)
		self.AttackAndStandDuration()
		
	def AttackAndStandDuration(self):
		global Levelbot
		if Levelbot != "":
			RandomRotation = app.GetRandom(0,7)
			chr.SetDirection(RandomRotation)
			player.SetAttackKeyState(TRUE)	
			self.SetBaseAgain = WaitingDialog()
			self.SetBaseAgain.Open(2.5)
			self.SetBaseAgain.SAFE_SetTimeOverEvent(self.WarpBaseAgain)
			
	def WarpBaseAgain(self):
		global x0
		global y0
		global z0
		chr.SetPixelPosition(int(x0), int(y0), int(z0))
		self.AttackAndStandDuration()
			
	def TransferBasePosition(self):
		global x0
		global y0
		global z0
		global x1
		global y1
		global x2
		global y2
		if x0 == "" or y0 == "":
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Du hast keine Base gesetzt.")
		else:
###Teleportsteps by musicinstructor
			(ax, ay, az) = player.GetMainCharacterPosition()
			if int(x1) < int(ax): # links
				while int(x0) < int(ax):
					chr.SetPixelPosition(int(ax) - 2000, int(ay))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					(ax, ay, az) = player.GetMainCharacterPosition()

				chr.SetPixelPosition(int(x0), int(ay))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

			if int(x2) > int(ax): # rechts
				while int(x0) > int(ax):
					chr.SetPixelPosition(int(ax) + 2000, int(ay))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					(ax, ay, az) = player.GetMainCharacterPosition()

				chr.SetPixelPosition(int(x0), int(ay))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

			if int(y1) < int(ay): # unten
				while int(y0) < int(ay):
					chr.SetPixelPosition(int(ax), int(ay) - 2000)
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					(ax, ay, az) = player.GetMainCharacterPosition()

				chr.SetPixelPosition(int(ax), int(y0))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				
			if int(y2) > int(ay): # oben
				while int(y0) > int(ay):
					chr.SetPixelPosition(int(ax), int(ay) + 2000)
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					(ax, ay, az) = player.GetMainCharacterPosition()

				chr.SetPixelPosition(int(ax), int(y0))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Du wurdest auf deine Base Position zurückgesetzt(" + str(x0/100) + ", " + str(y0/100) + ", " + str(z0/100) + ")")
			import uiTarget
			global SCAN_START
			global SCAN_END
			for i in xrange(SCAN_START, SCAN_END):
				if chr.INSTANCE_TYPE_ENEMY == chr.GetInstanceType(i):
					uiTarget.BannVid = int(i)
				
	def DeactivateBasePosition(self):
		global SetBase
		if SetBase != "":	
			SetBase = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Die Base Position wurde deaktiviert.")
			self.SetBasePositionButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")	
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Die Base Position ist nicht aktiviert.")			
		
	def GetTargetVID(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "Target VID: " + str(player.GetTargetVID()))
		
	def SetVIDRange(self):
		global SCAN_START
		global SCAN_END
		for i in range(0, 6000000):
			if chr.INSTANCE_TYPE_ENEMY == chr.GetInstanceType(i):
				SCAN_START = int(i-500)
				SCAN_END = int(i+1000000)
				break	
		chat.AppendChat(chat.CHAT_TYPE_INFO, "VID Range: " + str(SCAN_START) + ", " + str(SCAN_END))
		
	def TeleportToMobs(self):
		global mobVid
		myVid = player.GetMainCharacterIndex()
		player.SetAttackKeyState(FALSE)
		for i in range(SCAN_START, SCAN_END):
			if chr.INSTANCE_TYPE_ENEMY == chr.GetInstanceType(i) and Levelbot != "":
				distance = player.GetCharacterDistance(i)
				if distance <= 2000:
					chr.SelectInstance(i)
					mobX, mobY, mobZ = chr.GetPixelPosition(i)
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(mobX), int(mobY), int(mobZ))
					mobVid = i
					RandomDirection = app.GetRandom(0,8)
					chr.SetDirection(RandomDirection)
					player.SetAttackKeyState(TRUE)
					break
				
		if Levelbot != "":
			self.TeleportDelay = WaitingDialog()
			self.TeleportDelay.Open(2.5)
			self.TeleportDelay.SAFE_SetTimeOverEvent(self.TeleportToMobs)
			
	def OnBreakLevelBot(self):
		player.SetAttackKeyState(FALSE)

	def AutoRevive(self):
		global Levelbot
		global DoublePrevent
		global RestartBot
		net.SendChatPacket("/restart_here")
		if Levelbot != "":
			RestartBot = "on"
		self.StopLevelBot()
		PotionCount = self.PotionCheck()
		if int(PotionCount) >= 1:
			self.RefillHP(0)
			chat.AppendChat(chat.CHAT_TYPE_INFO, str(PotionCount) + " Rote Potions dabei")
			if str(RestartBot) == "on":
				self.WaitingDialog.Open(7.0)
				self.WaitingDialog.SAFE_SetTimeOverEvent(self.StartLevelBot)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, str(PotionCount) + " Rote Potions dabei")	
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Der Levelbot wird automatisch gestoppt")	
			RestartBot = "off"
		DoublePrevent = "inaktiv"
		
	def RefillHP(self, count):
		if count == 0:
			Maximum_TP = player.GetStatus(player.MAX_HP)
			Actual_TP = player.GetStatus(player.HP)
			for i in xrange(player.INVENTORY_PAGE_SIZE*2):
				ItemValue = player.GetItemIndex(i)
				if ItemValue == 27001 or ItemValue == 27002 or ItemValue == 27003:
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					count = 1
					break
		
	def AutoReviveDelay(self):
		self.WaitingDialog = WaitingDialog()
		self.WaitingDialog.Open(10.5)
		self.WaitingDialog.SAFE_SetTimeOverEvent(self.AutoRevive)
		
	def AutoPottRed(self):
		Maximum_TP = player.GetStatus(player.MAX_HP)
		Actual_TP = player.GetStatus(player.HP)
		Percent = self.AutoPottRedButtonPercentEditline.GetText()
		if (float(Actual_TP) / (float(Maximum_TP)) * 100) < int(Percent):
			for i in xrange(player.INVENTORY_PAGE_SIZE*3):
				ItemValue = player.GetItemIndex(i)
				if ItemValue == 27001 or ItemValue == 27002 or ItemValue == 27003:
					net.SendItemUsePacket(i)
					self.WaitingDelay(0)
					break

	def AutoPottBlue(self):
		Maximum_MP = player.GetStatus(player.MAX_SP)
		Actual_MP = player.GetStatus(player.SP)
		Percent = self.AutoPottBlueButtonPercentEditline.GetText()
		if (float(Actual_MP) / (float(Maximum_MP)) * 100) < int(Percent):
			for i in xrange(player.INVENTORY_PAGE_SIZE*3):
				ItemValue = player.GetItemIndex(i)
				if ItemValue == 27004 or ItemValue == 27005 or ItemValue == 27006:
					net.SendItemUsePacket(i)
					self.WaitingDelay(1)
					break
					
	def WaitingDelay(self, flag):
		self.WarteSchleife = WaitingDialog()
		self.WarteSchleife.Open(0.2)
		if flag == 0:
			self.WarteSchleife.SAFE_SetTimeOverEvent(self.AutoPottRed)
		elif flag == 1:
			self.WarteSchleife.SAFE_SetTimeOverEvent(self.AutoPottBlue)
		
	def CheckState(self):	
		global AutoSkillUse1
		global AutoSkillUse2
		global AutoSkillUse2
		global AutoSkillUse3
		global AutoSkillUse4
		global AutoSkillUse5
		global AutoSkillUse6
		global AutoPottRed
		global AutoPottBlue
		global TapferkeitsUmhange
		global AutoRevive
		global TransferMobs
		global LevelbotConfig
		global AutoPickUp
		global AttackSpeedHack
		global MoveSpeedHack
		(x, y, z) = player.GetMainCharacterPosition()
		race = net.GetMainActorRace()
		group = net.GetMainActorSkillGroup()
		SkillGrade1 = player.GetSkillGrade(1)
		SkillGrade2 = player.GetSkillGrade(2)
		SkillGrade3 = player.GetSkillGrade(3)
		SkillGrade4 = player.GetSkillGrade(4)
		SkillGrade5 = player.GetSkillGrade(5)
		SkillGrade6 = player.GetSkillGrade(6)
		SkillLevel1 = player.GetSkillLevel(1)
		SkillLevel2 = player.GetSkillLevel(2)
		SkillLevel3 = player.GetSkillLevel(3)
		SkillLevel4 = player.GetSkillLevel(4)
		SkillLevel5 = player.GetSkillLevel(5)
		SkillLevel6 = player.GetSkillLevel(6)
		if 1 == SkillGrade1:
			SkillLevel1 += 19
		elif 2 == SkillGrade1:
			SkillLevel1 += 29
		elif 3 == SkillGrade1:
			SkillLevel1 = 40
		if 1 == SkillGrade2:
			SkillLevel2 += 19
		elif 2 == SkillGrade2:
			SkillLevel2 += 29
		elif 3 == SkillGrade2:
			SkillLevel2 = 40
		if 1 == SkillGrade3:
			SkillLevel3 += 19
		elif 2 == SkillGrade3:
			SkillLevel3 += 29
		elif 3 == SkillGrade3:
			SkillLevel3 = 40
		if 1 == SkillGrade4:
			SkillLevel4 += 19
		elif 2 == SkillGrade4:
			SkillLevel4 += 29
		elif 3 == SkillGrade4:
			SkillLevel4 = 40
		if 1 == SkillGrade5:
			SkillLevel5 += 19
		elif 2 == SkillGrade5:
			SkillLevel5 += 29
		elif 3 == SkillGrade5:
			SkillLevel5 = 40
		if 1 == SkillGrade6:
			SkillLevel6 += 19
		elif 2 == SkillGrade6:
			SkillLevel6 += 29
		elif 3 == SkillGrade6:
			SkillLevel6 = 40
			
		if SkillLevel1 < 20:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/warrior/samyeon_01.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/warrior/samyeon_01.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/warrior/samyeon_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/warrior/gigongcham_01.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/warrior/gigongcham_01.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/warrior/gigongcham_01.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/assassin/amseup_01.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/assassin/amseup_01.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/assassin/amseup_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/assassin/yeonsa_01.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/assassin/yeonsa_01.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/assassin/yeonsa_01.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/sura/swaeryeong_01.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/sura/swaeryeong_01.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/sura/swaeryeong_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/sura/maryeong_01.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/sura/maryeong_01.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/sura/maryeong_01.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/shaman/bipabu_01.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/shaman/bipabu_01.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/shaman/bipabu_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/shaman/noejeon_01.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/shaman/noejeon_01.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/shaman/noejeon_01.sub")
		elif SkillLevel1 < 30 and SkillLevel1 >= 20:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/warrior/samyeon_02.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/warrior/samyeon_02.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/warrior/samyeon_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/warrior/gigongcham_02.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/warrior/gigongcham_02.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/warrior/gigongcham_02.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/assassin/amseup_02.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/assassin/amseup_02.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/assassin/amseup_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/assassin/yeonsa_02.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/assassin/yeonsa_02.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/assassin/yeonsa_02.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/sura/swaeryeong_02.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/sura/swaeryeong_02.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/sura/swaeryeong_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/sura/maryeong_02.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/sura/maryeong_02.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/sura/maryeong_02.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/shaman/bipabu_02.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/shaman/bipabu_02.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/shaman/bipabu_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/shaman/noejeon_02.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/shaman/noejeon_02.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/shaman/noejeon_02.sub")
		elif SkillLevel1 >= 30:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/warrior/samyeon_03.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/warrior/samyeon_03.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/warrior/samyeon_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/warrior/gigongcham_03.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/warrior/gigongcham_03.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/warrior/gigongcham_03.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/assassin/amseup_03.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/assassin/amseup_03.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/assassin/amseup_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/assassin/yeonsa_03.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/assassin/yeonsa_03.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/assassin/yeonsa_03.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/sura/swaeryeong_03.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/sura/swaeryeong_03.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/sura/swaeryeong_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/sura/maryeong_03.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/sura/maryeong_03.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/sura/maryeong_03.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/shaman/bipabu_03.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/shaman/bipabu_03.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/shaman/bipabu_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse1.SetUpVisual("d:/ymir work/ui/skill/shaman/noejeon_03.sub")
					self.AutoSkillUse1.SetOverVisual("d:/ymir work/ui/skill/shaman/noejeon_03.sub")
					self.AutoSkillUse1.SetDownVisual("d:/ymir work/ui/skill/shaman/noejeon_03.sub")
		if SkillLevel2 < 20:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/warrior/palbang_01.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/warrior/palbang_01.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/warrior/palbang_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/warrior/gyeoksan_01.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/warrior/gyeoksan_01.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/warrior/gyeoksan_01.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/assassin/gungsin_01.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/assassin/gungsin_01.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/assassin/gungsin_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/assassin/gwangyeok_01.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/assassin/gwangyeok_01.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/assassin/gwangyeok_01.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/sura/yonggwon_01.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/sura/yonggwon_01.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/sura/yonggwon_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/sura/hwayeom_01.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/sura/hwayeom_01.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/sura/hwayeom_01.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/shaman/yongpa_01.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/shaman/yongpa_01.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/shaman/yongpa_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/shaman/byeorak_01.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/shaman/byeorak_01.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/shaman/byeorak_01.sub")
		elif SkillLevel2 < 30 and SkillLevel2 >= 20:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/warrior/palbang_02.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/warrior/palbang_02.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/warrior/palbang_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/warrior/gyeoksan_02.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/warrior/gyeoksan_02.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/warrior/gyeoksan_02.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/assassin/gungsin_02.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/assassin/gungsin_02.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/assassin/gungsin_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/assassin/gwangyeok_02.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/assassin/gwangyeok_02.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/assassin/gwangyeok_02.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/sura/yonggwon_02.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/sura/yonggwon_02.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/sura/yonggwon_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/sura/hwayeom_02.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/sura/hwayeom_02.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/sura/hwayeom_02.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/shaman/yongpa_02.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/shaman/yongpa_02.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/shaman/yongpa_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/shaman/byeorak_02.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/shaman/byeorak_02.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/shaman/byeorak_02.sub")
		elif SkillLevel2 >= 30:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/warrior/palbang_03.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/warrior/palbang_03.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/warrior/palbang_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/warrior/gyeoksan_03.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/warrior/gyeoksan_03.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/warrior/gyeoksan_03.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/assassin/gungsin_03.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/assassin/gungsin_03.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/assassin/gungsin_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/assassin/gwangyeok_03.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/assassin/gwangyeok_03.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/assassin/gwangyeok_03.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/sura/yonggwon_03.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/sura/yonggwon_03.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/sura/yonggwon_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/sura/hwayeom_03.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/sura/hwayeom_03.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/sura/hwayeom_03.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/shaman/yongpa_03.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/shaman/yongpa_03.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/shaman/yongpa_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse2.SetUpVisual("d:/ymir work/ui/skill/shaman/byeorak_03.sub")
					self.AutoSkillUse2.SetOverVisual("d:/ymir work/ui/skill/shaman/byeorak_03.sub")
					self.AutoSkillUse2.SetDownVisual("d:/ymir work/ui/skill/shaman/byeorak_03.sub")
		if SkillLevel3 < 20:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/warrior/jeongwi_01.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/warrior/jeongwi_01.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/warrior/jeongwi_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/warrior/daejin_01.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/warrior/daejin_01.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/warrior/daejin_01.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/assassin/charyun_01.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/assassin/charyun_01.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/assassin/charyun_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/assassin/hwajo_01.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/assassin/hwajo_01.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/assassin/hwajo_01.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/sura/gwigeom_01.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/sura/gwigeom_01.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/sura/gwigeom_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/sura/muyeong_01.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/sura/muyeong_01.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/sura/muyeong_01.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/shaman/paeryong_01.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/shaman/paeryong_01.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/shaman/paeryong_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/shaman/pokroe_01.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/shaman/pokroe_01.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/shaman/pokroe_01.sub")
		elif SkillLevel3 < 30 and SkillLevel3 >= 20:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/warrior/jeongwi_02.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/warrior/jeongwi_02.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/warrior/jeongwi_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/warrior/daejin_02.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/warrior/daejin_02.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/warrior/daejin_02.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/assassin/charyun_02.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/assassin/charyun_02.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/assassin/charyun_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/assassin/hwajo_02.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/assassin/hwajo_02.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/assassin/hwajo_02.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/sura/gwigeom_02.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/sura/gwigeom_02.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/sura/gwigeom_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/sura/muyeong_02.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/sura/muyeong_02.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/sura/muyeong_02.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/shaman/paeryong_02.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/shaman/paeryong_02.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/shaman/paeryong_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/shaman/pokroe_02.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/shaman/pokroe_02.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/shaman/pokroe_02.sub")
		elif SkillLevel3 >= 30:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/warrior/jeongwi_03.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/warrior/jeongwi_03.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/warrior/jeongwi_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/warrior/daejin_03.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/warrior/daejin_03.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/warrior/daejin_03.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/assassin/charyun_03.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/assassin/charyun_03.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/assassin/charyun_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/assassin/hwajo_03.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/assassin/hwajo_03.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/assassin/hwajo_03.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/sura/gwigeom_03.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/sura/gwigeom_03.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/sura/gwigeom_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/sura/muyeong_03.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/sura/muyeong_03.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/sura/muyeong_03.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/shaman/paeryong_03.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/shaman/paeryong_03.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/shaman/paeryong_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse3.SetUpVisual("d:/ymir work/ui/skill/shaman/pokroe_03.sub")
					self.AutoSkillUse3.SetOverVisual("d:/ymir work/ui/skill/shaman/pokroe_03.sub")
					self.AutoSkillUse3.SetDownVisual("d:/ymir work/ui/skill/shaman/pokroe_03.sub")
		if SkillLevel4 < 20:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/warrior/geomgyeong_01.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/warrior/geomgyeong_01.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/warrior/geomgyeong_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/warrior/cheongeun_01.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/warrior/cheongeun_01.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/warrior/cheongeun_01.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/assassin/eunhyeong_01.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/assassin/eunhyeong_01.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/assassin/eunhyeong_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/assassin/gyeonggong_01.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/assassin/gyeonggong_01.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/assassin/gyeonggong_01.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/sura/gongpo_01.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/sura/gongpo_01.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/sura/gongpo_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/sura/heuksin_01.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/sura/heuksin_01.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/sura/heuksin_01.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/shaman/hosin_01.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/shaman/hosin_01.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/shaman/hosin_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/shaman/jeongeop_01.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/shaman/jeongeop_01.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/shaman/jeongeop_01.sub")
		elif SkillLevel4 < 30 and SkillLevel4 >= 20:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/warrior/geomgyeong_02.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/warrior/geomgyeong_02.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/warrior/geomgyeong_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/warrior/cheongeun_02.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/warrior/cheongeun_02.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/warrior/cheongeun_02.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/assassin/eunhyeong_02.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/assassin/eunhyeong_02.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/assassin/eunhyeong_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/assassin/gyeonggong_02.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/assassin/gyeonggong_02.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/assassin/gyeonggong_02.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/sura/gongpo_02.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/sura/gongpo_02.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/sura/gongpo_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/sura/heuksin_02.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/sura/heuksin_02.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/sura/heuksin_02.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/shaman/hosin_02.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/shaman/hosin_02.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/shaman/hosin_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/shaman/jeongeop_02.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/shaman/jeongeop_02.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/shaman/jeongeop_02.sub")
		elif SkillLevel4 >= 30:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/warrior/geomgyeong_03.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/warrior/geomgyeong_03.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/warrior/geomgyeong_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/warrior/cheongeun_03.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/warrior/cheongeun_03.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/warrior/cheongeun_03.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/assassin/eunhyeong_03.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/assassin/eunhyeong_03.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/assassin/eunhyeong_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/assassin/gyeonggong_03.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/assassin/gyeonggong_03.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/assassin/gyeonggong_03.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/sura/gongpo_03.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/sura/gongpo_03.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/sura/gongpo_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/sura/heuksin_03.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/sura/heuksin_03.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/sura/heuksin_03.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/shaman/hosin_03.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/shaman/hosin_03.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/shaman/hosin_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse4.SetUpVisual("d:/ymir work/ui/skill/shaman/jeongeop_03.sub")
					self.AutoSkillUse4.SetOverVisual("d:/ymir work/ui/skill/shaman/jeongeop_03.sub")
					self.AutoSkillUse4.SetDownVisual("d:/ymir work/ui/skill/shaman/jeongeop_03.sub")
		if SkillLevel5 < 20:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/warrior/tanhwan_01.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/warrior/tanhwan_01.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/warrior/tanhwan_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/warrior/geompung_01.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/warrior/geompung_01.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/warrior/geompung_01.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/assassin/sangong_01.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/assassin/sangong_01.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/assassin/sangong_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/assassin/gigung_01.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/assassin/gigung_01.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/assassin/gigung_01.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/sura/jumagap_01.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/sura/jumagap_01.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/sura/jumagap_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/sura/tusok_01.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/sura/tusok_01.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/sura/tusok_01.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/shaman/boho_01.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/shaman/boho_01.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/shaman/boho_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/shaman/kwaesok_01.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/shaman/kwaesok_01.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/shaman/kwaesok_01.sub")
		elif SkillLevel5 < 30 and SkillLevel5 >= 20:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/warrior/tanhwan_02.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/warrior/tanhwan_02.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/warrior/tanhwan_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/warrior/geompung_02.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/warrior/geompung_02.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/warrior/geompung_02.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/assassin/sangong_02.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/assassin/sangong_02.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/assassin/sangong_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/assassin/gigung_02.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/assassin/gigung_02.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/assassin/gigung_02.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/sura/jumagap_02.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/sura/jumagap_02.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/sura/jumagap_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/sura/tusok_02.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/sura/tusok_02.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/sura/tusok_02.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/shaman/boho_02.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/shaman/boho_02.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/shaman/boho_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/shaman/kwaesok_02.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/shaman/kwaesok_02.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/shaman/kwaesok_02.sub")
		elif SkillLevel5 >= 30:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/warrior/tanhwan_03.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/warrior/tanhwan_03.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/warrior/tanhwan_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/warrior/geompung_03.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/warrior/geompung_03.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/warrior/geompung_03.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/assassin/sangong_03.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/assassin/sangong_03.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/assassin/sangong_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/assassin/gigung_03.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/assassin/gigung_03.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/assassin/gigung_03.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/sura/jumagap_03.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/sura/jumagap_03.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/sura/jumagap_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/sura/tusok_03.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/sura/tusok_03.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/sura/tusok_03.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/shaman/boho_03.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/shaman/boho_03.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/shaman/boho_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse5.SetUpVisual("d:/ymir work/ui/skill/shaman/kwaesok_03.sub")
					self.AutoSkillUse5.SetOverVisual("d:/ymir work/ui/skill/shaman/kwaesok_03.sub")
					self.AutoSkillUse5.SetDownVisual("d:/ymir work/ui/skill/shaman/kwaesok_03.sub")
		if SkillLevel6 < 20:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/warrior/gihyeol_01.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/warrior/gihyeol_01.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/warrior/gihyeol_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/warrior/noegeom_01.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/warrior/noegeom_01.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/warrior/noegeom_01.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/assassin/seomjeon_01.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/assassin/seomjeon_01.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/assassin/seomjeon_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/assassin/seomgwang_01.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/assassin/seomgwang_01.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/assassin/seomgwang_01.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/sura/pabeop_01.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/sura/pabeop_01.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/sura/pabeop_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/sura/geomhwan_01.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/sura/geomhwan_01.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/sura/geomhwan_01.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/shaman/gicheon_01.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/shaman/gicheon_01.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/shaman/gicheon_01.sub")
				elif int(group) == 2:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/shaman/jeungryeok_01.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/shaman/jeungryeok_01.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/shaman/jeungryeok_01.sub")
		elif SkillLevel6 < 30 and SkillLevel6 >= 20:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/warrior/gihyeol_02.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/warrior/gihyeol_02.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/warrior/gihyeol_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/warrior/noegeom_02.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/warrior/noegeom_02.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/warrior/noegeom_02.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/assassin/seomjeon_02.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/assassin/seomjeon_02.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/assassin/seomjeon_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/assassin/seomgwang_02.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/assassin/seomgwang_02.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/assassin/seomgwang_02.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/sura/pabeop_02.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/sura/pabeop_02.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/sura/pabeop_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/sura/geomhwan_02.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/sura/geomhwan_02.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/sura/geomhwan_02.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/shaman/gicheon_02.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/shaman/gicheon_02.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/shaman/gicheon_02.sub")
				elif int(group) == 2:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/shaman/jeungryeok_02.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/shaman/jeungryeok_02.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/shaman/jeungryeok_02.sub")
		elif SkillLevel6 >= 30:
			if ((int(race) == 0) or ((int(race) == 4))):
				if int(group) == 1:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/warrior/gihyeol_03.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/warrior/gihyeol_03.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/warrior/gihyeol_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/warrior/noegeom_03.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/warrior/noegeom_03.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/warrior/noegeom_03.sub")
			elif (int(race) == 1) or (int(race) == 5):
				if int(group) == 1:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/assassin/seomjeon_03.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/assassin/seomjeon_03.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/assassin/seomjeon_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/assassin/seomgwang_03.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/assassin/seomgwang_03.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/assassin/seomgwang_03.sub")
			elif (int(race) == 2) or (int(race) == 6):
				if int(group) == 1:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/sura/pabeop_03.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/sura/pabeop_03.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/sura/pabeop_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/sura/geomhwan_03.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/sura/geomhwan_03.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/sura/geomhwan_03.sub")
			elif (int(race) == 3) or (int(race) == 7):
				if int(group) == 1:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/shaman/gicheon_03.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/shaman/gicheon_03.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/shaman/gicheon_03.sub")
				elif int(group) == 2:
					self.AutoSkillUse6.SetUpVisual("d:/ymir work/ui/skill/shaman/jeungryeok_03.sub")
					self.AutoSkillUse6.SetOverVisual("d:/ymir work/ui/skill/shaman/jeungryeok_03.sub")
					self.AutoSkillUse6.SetDownVisual("d:/ymir work/ui/skill/shaman/jeungryeok_03.sub")

		if int(group) == 0:
			self.AutoSkillUse1.Hide()
			self.AutoSkillUse2.Hide()
			self.AutoSkillUse3.Hide()
			self.AutoSkillUse4.Hide()
			self.AutoSkillUse5.Hide()
			self.AutoSkillUse6.Hide()
			
			self.ErrorLog = ui.TextLine()
			self.ErrorLog.SetParent(self)
			self.ErrorLog.SetDefaultFontName()
			self.ErrorLog.SetPosition(30, 84)
			self.ErrorLog.SetFeather()
			self.ErrorLog.SetText("No skills learned yet!")
			self.ErrorLog.SetFontColor(0.2, 0.4, 1.0)
			self.ErrorLog.SetOutline()
			self.ErrorLog.Show()
			
		if AutoSkillUse1 != "":
			self.AutoSkillUse1Activated.Show()
		elif AutoSkillUse1 == "":
			self.AutoSkillUse1Activated.Hide()
		if AutoSkillUse2 != "":
			self.AutoSkillUse2Activated.Show()
		elif AutoSkillUse2 == "":
			self.AutoSkillUse2Activated.Hide()
		if AutoSkillUse3 != "":
			self.AutoSkillUse3Activated.Show()
		elif AutoSkillUse3 == "":
			self.AutoSkillUse3Activated.Hide()
		if AutoSkillUse4 != "":
			self.AutoSkillUse4Activated.Show()
		elif AutoSkillUse4 == "":
			self.AutoSkillUse4Activated.Hide()
		if AutoSkillUse5 != "":
			self.AutoSkillUse5Activated.Show()
		elif AutoSkillUse5 == "":
			self.AutoSkillUse5Activated.Hide()
		if AutoSkillUse6 != "":
			self.AutoSkillUse6Activated.Show()
		elif AutoSkillUse6 == "":
			self.AutoSkillUse6Activated.Hide()
		if AutoPottRed != "":
			self.AutoPottRedButtonActivated.Show()
			self.AutoPottRedImageActivated.Show()
		elif AutoPottRed == "":
			self.AutoPottRedButtonActivated.Hide()
			self.AutoPottRedImageActivated.Hide()
		if AutoPottBlue != "":
			self.AutoPottBlueButtonActivated.Show()
			self.AutoPottBlueImageActivated.Show()
		elif AutoPottBlue == "":
			self.AutoPottBlueButtonActivated.Hide()
			self.AutoPottBlueImageActivated.Hide()
		if TapferkeitsUmhange != "":
			self.TapferkeitsUmhangeButtonActivated.Show()
			self.TapferkeitsUmhangeImageActivated.Show()
		elif TapferkeitsUmhange == "":
			self.TapferkeitsUmhangeButtonActivated.Hide()
			self.TapferkeitsUmhangeImageActivated.Hide()
		if AutoRevive != "":
			self.AutoReviveButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		if TransferMobs != "":
			self.TransferMobsButton.SetUpVisual("d:/ymir work/ui/public/large_button_03.sub")
		if LevelbotConfig == 0:
			self.TeleportToMobsManyButton.SetUpVisual("d:/ymir work/ui/public/large_button_03.sub")
		elif LevelbotConfig == 1:
			self.AttackAndStandButton.SetUpVisual("d:/ymir work/ui/public/large_button_03.sub")
		if AutoPickUp != "":
			self.AutoPickUpButton.SetUpVisual("d:/ymir work/ui/public/large_button_03.sub")
		if AttackSpeedHack != "":
			self.AttackSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_03.sub")
			self.AttackSpeedStatusButton.SetText("Aktiviert")
		if MoveSpeedHack != "":
			self.MoveSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
			self.MoveSpeedStatusButton.SetText("Aktiviert")
			
		self.TeleportXEditLine.SetText(str(int(x/100)))			
		self.TeleportYEditLine.SetText(str(int(y/100)))			
		self.TeleportZEditLine.SetText("0")

		self.AttackSpeedStats.SetText((str(player.GetStatus(player.ATT_SPEED))))		
		self.MoveSpeedStats.SetText((str(player.GetStatus(player.MOVING_SPEED))))
#		self.TeleportZEditLine.SetText(str(int(z/100)))		
	
	def OnRender(self):
		global telestep
		global teleport_mode
		global last_teleport_time
		telestep = 0
		if teleport_mode == 1 and app.GetTime() > last_teleport_time + 5:
			last_teleport_time = app.GetTime()
			self.TeleportToCoordinates()		

	def OnUpdate(self):
		global x1
		global y1
		global x2
		global y2
		global SetBase
		global AutoSkillUse1
		global AutoSkillUse2
		global AutoSkillUse3
		global AutoSkillUse4
		global AutoSkillUse5
		global AutoSkillUse6
		global AutoPottRed
		global AutoPottBlue
		global AutoPickUp
		global AttackSpeedHack
		global DoublePrevent
		global Levelbot
		if int(player.GetStatus(player.HP)) <= 0 and str(DoublePrevent) == "inaktiv":
			self.AutoReviveDelay()
			DoublePrevent = "aktiv"
		CurrentAttackSpeedHack = self.AttackSpeedStats.GetText()
		(x, y, z) = player.GetMainCharacterPosition()
		if Levelbot != "":
			if AutoSkillUse1 != "":
				if skill.CanUseSkill(1):
					player.ClickSkillSlot(1)
			if AutoSkillUse2 != "":
				if skill.CanUseSkill(2):
					player.ClickSkillSlot(2)
			if AutoSkillUse3 != "":
				if skill.CanUseSkill(3):
					player.ClickSkillSlot(3)
			if AutoSkillUse4 != "":
				if skill.CanUseSkill(4):
					player.ClickSkillSlot(4)
			if AutoSkillUse5 != "":
				if skill.CanUseSkill(5):
					player.ClickSkillSlot(5)
			if AutoSkillUse6 != "":
				if skill.CanUseSkill(6):
					player.ClickSkillSlot(6)
		if AutoPottRed != "":
			self.AutoPottRed()
		if AutoPottBlue != "":
			self.AutoPottBlue()
		if ((x1 > x) or (x2 < x) or (y2 < y) or (y1 > y)) and SetBase != "":
			self.TransferBasePosition()
		if AutoPickUp != "":
			player.PickCloseItem()
		if AttackSpeedHack != "":
			chr.SetAttackSpeed(int(CurrentAttackSpeedHack))
	
	def Show(self):
		ui.ThinBoard.Show(self)
		
	def Close(self):
		global SetBase
		SetBase = ""
		self.Hide()
		return TRUE
		
	def OnPressEscapeKey(self):
		self.Hide()
		return TRUE
		
class SelectModDialog(ui.ThinBoard):
	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.Levelbot = LevelBotDialog()
		self.Levelbot.Show()	
		
	def __del__(self):
		ui.ThinBoard.__del__(self)
		
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
		
SelectMod = SelectModDialog()
SelectMod.Show()