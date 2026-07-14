import os
import app
import dbg
import grp
import item
import background
import chr
import chrmgr
import player
import snd
import chat
import textTail
import snd
import net
import effect
import wndMgr
import fly
import systemSetting
import quest
import guild
import skill
import messenger
import locale
import constInfo
import exchange
import time
import ui

class PickUP(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadPick()
	
	def __del__(self):
		ui.ScriptWindow.__del__(self)
	def LoadPick(self):
	
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Auto Pickup")
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "By - ShieldSlayeR")
             
		
		self.LoadMainForm()
		self.FaceButton()
		
	def LoadMainForm(self):

		global OnOff
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(200, 150)
		self.Board.SetPosition(wndMgr.GetScreenWidth()-500, wndMgr.GetScreenHeight()-400)
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetTitleName("Auto Pickup - By ShieldSlayeR")
		self.Board.SetCloseEvent(self.Board.Hide)
		self.Board.Show()

		self.PickMessage = ui.TextLine()
		self.PickMessage.SetParent(self.Board)
		self.PickMessage.SetPosition(35, 95)
		self.PickMessage.SetText("Auto Pickup - By ShieldSlayeR")
		self.PickMessage.Show()


		self.PickOn = ui.Button()
		self.PickOn.SetParent(self.Board)
		self.PickOn.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.PickOn.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.PickOn.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.PickOn.SetText("Start")
		self.PickOn.SetPosition(10, 70)
		self.PickOn.SetEvent(self.PickUp)
		self.PickOn.Show()
		
		self.PickOff = ui.Button()
		self.PickOff.SetParent(self.Board)
		self.PickOff.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.PickOff.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.PickOff.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.PickOff.SetText("Stop")
		self.PickOff.SetPosition(100, 70)
		self.PickOff.SetEvent(self.PickUpStop)
		self.PickOff.Show()
		
		
	def FaceButton(self):
	
		global PickButton
		PickButton = ui.Button()
		PickButton.SetText("")
		PickButton.SetPosition(wndMgr.GetScreenWidth()-100,wndMgr.GetScreenHeight()-500)
		PickButton.SetSize(88, 21)
		PickButton.SetEvent(self.Board.Show)
		PickButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		PickButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		PickButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		PickButton.Show()
		
		global PickText
		PickText = ui.TextLine()
		PickText.SetParent(PickButton)
		PickText.SetVerticalAlignCenter()
		PickText.SetHorizontalAlignCenter()
		PickText.SetPosition(43,10)
		PickText.SetText("PickUpBot")
		PickText.Show()

	def SendGoldDown(self):
		net.SendGoldDropPacketNew(500)
	
	def OpenInv(self):
		ToggleInventoryWindow()
		
	def PickUp(self):
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Auto-Pickup is enable.")
		self.PickUpStart()
	def PickUpStart(self):
		player.PickCloseItem()
		player.SetAttackKeyState(TRUE)
		for a in range(90):
			if player.GetItemIndex(a) == 70038:
				net.SendItemUsePacket(a)
				return
		
		self.Delay = WaitingDialog()
		PickDelay = 0.1
			
		self.Delay.Open(int(PickDelay))
		self.Delay.SAFE_SetTimeOverEvent(self.PickUpStart)
			
	def PickUpStop(self):
		player.SetAttackKeyState(FALSE)
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Auto-Pickup is disable.")
		
		StopDelay = 999999
		self.Delay.Open(int(StopDelay))
			
	def Stealth(self):
		player.HidePlayer()
		
	
		
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
		
StartDialog = PickUP()
StartDialog.Board.Hide()
