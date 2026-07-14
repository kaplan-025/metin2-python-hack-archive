import ui,app,chat,chr,net,player,item,skill,time,game,shop,chrmgr
import background,constInfo,wndMgr,math,uiCommon,grp,dbg,m2k_lib

class SpamDialog(ui.ScriptWindow):
	
	def __init__(self):
		self.Board = ui.ThinBoard()
		self.Board.SetSize(198, 245)
		self.Board.SetPosition(52, 40)
	#	self.Board.AddFlag('movable')
		self.Board.Hide()
		
		self.comp = m2k_lib.Component()
		self.Header = self.comp.TextLine(self.Board, 'Spambot', 73, 7, self.comp.RGB(255, 255, 0))
		self.DelayLabel = self.comp.TextLine(self.Board, 'Delay: 15 Sec.', 70, 163, self.comp.RGB(255, 255, 255))
		
		self.DelaySlide = self.comp.SliderBar(self.Board, 0.15, self.SlideFunc, 13, 148)
		self.Close = self.comp.Button(self.Board, '', 'Close', 175, 7, self.Hide_UI, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
		self.ChatTypeButton = self.comp.Button(self.Board, 'Global', 'Chattype', 17, 113, self.SetType, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub','d:/ymir work/ui/public/small_button_03.sub')
		self.SaveTextButton = self.comp.Button(self.Board, 'Save', '', 139, 113, self.SaveTextContent, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub','d:/ymir work/ui/public/small_button_03.sub')
		self.SpamOn = self.comp.HideButton(self.Board, '', '', 80, 190, self.SetSpamStatus, 'm2kmod\Images\start_0.tga', 'm2kmod\Images\start_1.tga', 'm2kmod\Images\start_2.tga')
		self.SpamOff = self.comp.HideButton(self.Board, '', '', 75, 190, self.SetSpamStatus, 'm2kmod\Images\stop_0.tga', 'm2kmod\Images\stop_1.tga', 'm2kmod\Images\stop_2.tga')
		self.Slotbar, self.SpamText = self.comp.EditLine(self.Board, '', 23, 29, 150, 75, 150)
		self.SpamCombo = self.comp.ComboBoxFunc(self.Board, '<choose>', 69, 115, 60, self.GetTextContent)
		
		self.SpamStatus = int(m2k_lib.ReadConfig("SpamStatus"))
		self.Delay = int(m2k_lib.ReadConfig("SpamDelay"))
		self.CurrentNum = m2k_lib.ReadConfig("CurrentText")
		self.Type = m2k_lib.ReadConfig("Type")
	
		if self.SpamStatus == 1:
			self.SpamOff.Show()
			self.StartSpam()
		else:
			self.SpamOn.Show()
			self.StopSpam()
			
		if self.Type == "Normal":
			self.ChatTypeButton.SetText("Normal")
		else:
			self.ChatTypeButton.SetText("Global")
		
		list = ("Text1", "Text2", "Text3", "Text4", "Text5", "Text6", "Text7", "Text8") 
		for Account in list:
			self.SpamCombo.InsertItem(1,Account)
		self.SpamCombo.SetCurrentItem(self.CurrentNum)	
		self.GetTextContent()
		
		self.DelaySlide.SetSliderPos(float(self.Delay*0.01))
		self.SlideFunc()
		
	def switch_state(self):
		if self.Board.IsShow():
			self.Hide_UI()
		else:
			self.Board.Show()
	def Hide_UI(self):
		self.Board.Hide()
		m2k_lib.SaveConfig("SpamStatus", str(self.SpamStatus))
		m2k_lib.SaveConfig("SpamDelay", str(self.Delay))
		m2k_lib.SaveConfig("Type", str(self.Type))
		m2k_lib.SaveConfig("CurrentText", str(self.CurrentNum))
		
	
	def SlideFunc(self):
		self.Delay = int((self.DelaySlide.GetSliderPos()*100)+0.001)
		self.DelayLabel.SetText("Delay: "+str(self.Delay)+ " Sec.")
	
	def SetSpamStatus(self):
		if self.SpamStatus == 0:
			self.SpamStatus = 1
			chat.AppendChat(7, '[m2k-Mod] Spam-Bot started')	
			self.SpamOff.Show()
			self.SpamOn.Hide()
			self.StartSpam()
		else: 
			self.SpamStatus = 0
			chat.AppendChat(7, '[m2k-Mod] Spam-Bot stoped')	
			self.SpamOn.Show()
			self.SpamOff.Hide()	
			self.StopSpam()
	
	def SetType(self):
		if self.Type == "Normal":
			self.Type = "Global"
			chat.AppendChat(7, '[m2k-Mod] Spam-Mode changed to Globalchat-Spamming')
		else: 
			self.Type = "Normal"
			chat.AppendChat(7, '[m2k-Mod] Spam-Mode changed to Normalchat-Spamming')		
		self.ChatTypeButton.SetText(self.Type)

	def StartSpam(self):
		if self.Type == "Normal":
			net.SendChatPacket(str(self.SpamText.GetText()), chat.CHAT_TYPE_TALKING)
		else: 
			net.SendChatPacket(str(self.SpamText.GetText()), chat.CHAT_TYPE_SHOUT)
		
		self.UpdateSpam = m2k_lib.WaitingDialog()
		self.UpdateSpam.Open(self.Delay)
		self.UpdateSpam.SAFE_SetTimeOverEvent(self.StartSpam)
		
	def StopSpam(self):
		self.UpdateSpam = m2k_lib.WaitingDialog()
		self.UpdateSpam.Close()
		
	def GetTextContent(self):	
		self.SpamText.SetText(m2k_lib.ReadConfig(self.SpamCombo.GetCurrentText()))
		self.CurrentNum = self.SpamCombo.GetCurrentText()
	
	def SaveTextContent(self):
		m2k_lib.SaveConfig("Text"+str(num), self.SpamText.GetText())
