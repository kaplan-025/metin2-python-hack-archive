import chatm2g as chat, playerm2g2 as player, m2netm2g as m2net
import ui,app,chr,item,skill,time,game,shop,os,background,constInfo,wndMgr,math,uiCommon,grp,dbg,m2k_lib,Global,thread

from CY_FIX import *

class SpamDialog(ui.ScriptWindow):
	
	def __init__(self):
		self.Board = ui.ThinBoard()
		self.Board.SetSize(198, 288)
		self.Board.SetPosition(52, int(m2k_lib.ReadConfig("HackbarCoordHeight")))
		self.Board.Hide()
		
		self.LibWrapper = m2k_lib.m2libWrapper()
		self.comp = m2k_lib.Component()
		self.Header = self.comp.TextLine(self.Board, 'Spambot', 73, 7, self.comp.RGB(255, 255, 0))
		self.DelayLabel = self.comp.TextLine(self.Board, 'Delay: 15 Sec.', 70, 223, self.comp.RGB(255, 255, 255))
		self.SavedTextsLabel = self.comp.TextLine(self.Board, 'Saved Texts:', 20, 145, self.comp.RGB(255, 255, 255))
		self.SpamTypeLabel = self.comp.TextLine(self.Board, 'Spam-Mode:', 20, 170, self.comp.RGB(255, 255, 255))
		
		self.DelaySlide = self.comp.SliderBar(self.Board, 0.15, self.SlideFunc, 13, 208)
		self.Close = self.comp.Button(self.Board, '', 'Close', 178, 7, self.Hide_UI, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
		self.SaveNewButton = self.comp.Button(self.Board, 'Save New', '', 68, 113, self.SaveNewText, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub','d:/ymir work/ui/public/middle_button_03.sub')
		self.SaveButton = self.comp.Button(self.Board, 'Save', '', 17, 113, self.SaveText, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub','d:/ymir work/ui/public/small_button_03.sub')
		self.RemoveButton = self.comp.Button(self.Board, 'Remove', '', 139, 113, self.RemoveText, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub','d:/ymir work/ui/public/small_button_03.sub')
		self.ClearButton = self.comp.Button(self.Board, '', 'Clear', 178, 60, self.ClearTextBox, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
		self.SpamOn = self.comp.Button(self.Board, '', '', 80, 240, self.SetSpamStatus, 'm2kmod\Images\start_0.tga', 'm2kmod\Images\start_1.tga', 'm2kmod\Images\start_2.tga')
		self.SpamOff = self.comp.HideButton(self.Board, '', '', 75, 240, self.SetSpamStatus, 'm2kmod\Images\stop_0.tga', 'm2kmod\Images\stop_1.tga', 'm2kmod\Images\stop_2.tga')
		self.Slotbar, self.SpamText = self.comp.EditLine(self.Board, '', 23, 29, 150, 75, 150)
		self.SpamModeCombo = self.comp.ComboBoxFunc(self.Board, '', 100, 170, 70, self.SetSpamMode)
		self.SpamCombo = self.comp.ComboBoxFunc(self.Board, '', 100, 145, 70, self.GetTextContent)
		
		self.SpamModeCombo.InsertItem(1,"Normal-Chat")
		self.SpamModeCombo.InsertItem(2,"Global-Chat")
		self.SpamModeCombo.InsertItem(3,"PM-Spammer")
		

		self.Delay = int(m2k_lib.ReadConfig("SpamDelay"))
		self.CurrentNum = int(m2k_lib.ReadConfig("CurrentText"))
		self.Type = m2k_lib.ReadConfig("Type")
	
		self.LoadTexts()
		
		self.SpamCombo.SetCurrentItem("Text "+ str(self.CurrentNum))		
		self.SpamModeCombo.SetCurrentItem(self.Type)
	
		self.DelaySlide.SetSliderPos(float(self.Delay*0.01))
		self.SlideFunc()
		
	def switch_state(self):
		if self.Board.IsShow():
			self.Hide_UI()
		else:
			self.Board.Show()
			self.Board.SetPosition(52, int(m2k_lib.ReadConfig("HackbarCoordHeight")))
	def Hide_UI(self):
		self.Board.Hide()
		m2k_lib.SaveConfig("SpamDelay", str(self.Delay))
		m2k_lib.SaveConfig("Type", self.Type)
		m2k_lib.SaveConfig("CurrentText", str(self.CurrentNum))
	
	def SlideFunc(self):
		self.Delay = int((self.DelaySlide.GetSliderPos()*100)+0.001)
		self.DelayLabel.SetText("Delay: "+str(self.Delay)+ " Sec.")
	
	def SetSpamStatus(self):
		if Global.Spambot:
			Global.Spambot = 0
			chat.AppendChat(7, '[m2k-Mod] Spam-Bot stoped')	
			self.SpamOn.Show()
			self.SpamOff.Hide()	
		else: 
			Global.Spambot = 1
			chat.AppendChat(7, '[m2k-Mod] Spam-Bot started')	
			self.SpamOff.Show()
			self.SpamOn.Hide()
			thread.start_new_thread(self.SpamBotThread,())
	
	
	def SpamBotThread(self):
		while Global.Spambot:
			if self.Type == "Normal-Chat":
				m2net.SendChatPacket(self.SpamText.GetText(), chat.CHAT_TYPE_TALKING)
			elif self.Type == "Global-Chat":
				m2net.SendChatPacket(self.SpamText.GetText(), chat.CHAT_TYPE_SHOUT)
			elif self.Type == "PM-Spammer":
				self.LibWrapper.SendPrivateMessages(self.SpamText.GetText())
			time.sleep(self.Delay)
		
		
	def SetSpamMode(self):
		self.Type = self.SpamModeCombo.GetCurrentText()
		if self.Type == "PM-Spammer":
			if not m2k_lib.IsPremium() or self.LibWrapper.m2botlib == None:
				self.Type = "Normal-Chat"
				self.SpamModeCombo.SetCurrentItem(self.Type)
				chat.AppendChat(7,"[m2k-Mod] No Premium or m2botlib could no be loaded")
				return
				
	
	def LoadTexts(self):
		self.SpamCombo.ClearItem()
		i = 1
		for text in open("m2kmod/Saves/texts.m2k", "r+").readlines():
			self.SpamCombo.InsertItem(i,"Text " + str(i))
			if i == self.CurrentNum:
				self.SpamText.SetText(text)
			i += 1
			
	def GetTextContent(self):	
		lines = open("m2kmod/Saves/texts.m2k", "r+").readlines()
		self.SpamText.SetText(lines[self.SpamCombo.GetSelectedIndex()-1])
		self.CurrentNum = self.SpamCombo.GetSelectedIndex()
	
	def SaveNewText(self):
		with open("m2kmod/Saves/texts.m2k", "a") as file:
			file.write(self.SpamText.GetText().replace("\n", "") + "\n")
		self.LoadTexts()
	
	def SaveText(self):
		textList = []
		with open('m2kmod/Saves/texts.m2k', 'r') as file:
			lines = file.readlines()
			i=0
			for line in lines:
				if i == self.CurrentNum - 1:
					textList.append(self.SpamText.GetText().replace("\n", "") + "\n")
				else:
					textList.append(line)
				i += 1

		with open('m2kmod/Saves/texts.m2k', 'w') as file:
			file.writelines(textList)
		self.LoadTexts()
		
	def RemoveText(self):
		textList = []
		with open('m2kmod/Saves/texts.m2k', 'r') as file:
			lines = file.readlines()
			i=0
			for line in lines:
				if not i == self.CurrentNum - 1:
					textList.append(line)
				i += 1

		with open('m2kmod/Saves/texts.m2k', 'w') as file:
			file.writelines(textList)
		self.LoadTexts()
		
	def ClearTextBox(self):
		self.SpamText.SetText("")
		
	
	

