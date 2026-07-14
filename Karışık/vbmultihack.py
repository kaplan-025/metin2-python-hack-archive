# Metin2Bot [Dreamfancy]
import chat
import chr
import locale
import ui
import background
import time
import player

		
class Hackdialog(ui.ThinBoard):

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.LoadBoard()
		
	def LoadBoard(self):
		self.SetCenterPosition()
		self.SetSize(390, 160)
		self.Show()
		self.AddFlag("movable")
		
		self.LoadText()
		self.LoadButton()
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Hile basariyla calistirildi.")
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Metin2Bot hilesinde sorun olustu.")
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Lutfen dreamfancy ile iletisim kurun.")
		
	def LoadText(self):
		self.Titel = ui.TextLine()
		self.Titel.SetParent(self)
		self.Titel.SetDefaultFontName()
		self.Titel.SetPosition(-80, 4)
		self.Titel.SetFeather()
		self.Titel.SetWindowHorizontalAlignCenter()
		self.Titel.SetText("Metin2 Multihack")
		self.Titel.SetFontColor(8.0, 0.5, 0)
		self.Titel.SetOutline()
		self.Titel.Show()			
		
		self.Mtitel = ui.TextLine()
		self.Mtitel.SetParent(self)
		self.Mtitel.SetDefaultFontName()
		self.Mtitel.SetPosition(-69, 30)
		self.Mtitel.SetFeather()
		self.Mtitel.SetWindowHorizontalAlignCenter()
		self.Mtitel.SetText("Metin2Bot Multihack")
		self.Mtitel.SetFontColor(8.0, 0.1, 0)
		self.Mtitel.SetOutline()
		self.Mtitel.Show()
		
		self.Atttitel = ui.TextLine()
		self.Atttitel.SetParent(self)
		self.Atttitel.SetDefaultFontName()
		self.Atttitel.SetPosition(-180, 90)
		self.Atttitel.SetFeather()
		self.Atttitel.SetWindowHorizontalAlignCenter()
		self.Atttitel.SetText("Saldiri hizi")
		self.Atttitel.SetFontColor(8.0, 0.1, 0)
		self.Atttitel.SetOutline()
		self.Atttitel.Show()	
		
		self.SlotwahlSlotBar = ui.SlotBar()
		self.SlotwahlSlotBar.SetParent(self)
		self.SlotwahlSlotBar.SetSize(80, 18)
		self.SlotwahlSlotBar.SetPosition(-55, 90)
		self.SlotwahlSlotBar.SetWindowHorizontalAlignCenter()
		self.SlotwahlSlotBar.Show()
		
		self.ChatEditLine = ui.EditLine()
		self.ChatEditLine.SetParent(self.SlotwahlSlotBar)
		self.ChatEditLine.SetSize(130, 25)
		self.ChatEditLine.SetPosition(2, 2)
		self.ChatEditLine.SetMax(3)
		self.ChatEditLine.SetText("")
		self.ChatEditLine.SetFocus()
		self.ChatEditLine.Show()
		
		self.Movetitel = ui.TextLine()
		self.Movetitel.SetParent(self)
		self.Movetitel.SetDefaultFontName()
		self.Movetitel.SetPosition(-180, 120)
		self.Movetitel.SetFeather()
		self.Movetitel.SetWindowHorizontalAlignCenter()
		self.Movetitel.SetText("Hareket hizi")
		self.Movetitel.SetFontColor(8.0, 0.1, 0)
		self.Movetitel.SetOutline()
		self.Movetitel.Show()
		
		self.SlotwahlSlotBar2 = ui.SlotBar() 
		self.SlotwahlSlotBar2.SetParent(self)
		self.SlotwahlSlotBar2.SetSize(80, 18)
		self.SlotwahlSlotBar2.SetPosition(-55, 120)
		self.SlotwahlSlotBar2.SetWindowHorizontalAlignCenter()
		self.SlotwahlSlotBar2.Show()
		
		self.ChatEditLine2 = ui.EditLine()
		self.ChatEditLine2.SetParent(self.SlotwahlSlotBar2)
		self.ChatEditLine2.SetSize(130, 25)
		self.ChatEditLine2.SetPosition(2, 2)
		self.ChatEditLine2.SetMax(3)
		self.ChatEditLine2.SetText("")
		self.ChatEditLine2.SetFocus()
		self.ChatEditLine2.Show()
				
	def LoadButton(self):

		self.AttButton = ui.Button()
		self.AttButton.SetParent(self)
		self.AttButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.AttButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.AttButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.AttButton.SetText("Aktiflestir")
		self.AttButton.SetPosition(190, 90)
		self.AttButton.SetEvent(ui.__mem_func__(self.MakeAtt))
		self.AttButton.Show()
		
		self.AttOffButton = ui.Button()
		self.AttOffButton.SetParent(self)
		self.AttOffButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.AttOffButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.AttOffButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.AttOffButton.SetText("Kapat")
		self.AttOffButton.SetPosition(280, 90)
		self.AttOffButton.SetEvent(ui.__mem_func__(self.MakeAttOff))
		self.AttOffButton.Show()

		self.MovButton = ui.Button()
		self.MovButton.SetParent(self)
		self.MovButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.MovButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.MovButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.MovButton.SetText("Aktiflestir")
		self.MovButton.SetPosition(190, 120)
		self.MovButton.SetEvent(ui.__mem_func__(self.MakeMov))
		self.MovButton.Show()
		
		self.MovOffButton = ui.Button()
		self.MovOffButton.SetParent(self)
		self.MovOffButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.MovOffButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.MovOffButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.MovOffButton.SetText("Kapat")
		self.MovOffButton.SetPosition(280, 120)
		self.MovOffButton.SetEvent(ui.__mem_func__(self.MakeMovOff))
		self.MovOffButton.Show()
	
	def __del__(self):
		ui.ThinBoard.__del__(self)

	def Show(self):
		ui.ThinBoard.Show(self)

	def Close(self):
		self.Hide()
		
	def MakeAtt(self):
		Angriffspeed = self.ChatEditLine.GetText()
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Saldiri hiziniz: " + Angriffspeed)
		chr.SetAttackSpeed(int(Angriffspeed))
		
	def MakeAttOff(self):
		chr.SetAttackSpeed(int(player.GetStatus(player.ATT_SPEED)))
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Saldiri hizi kapatildi.")
			
	def MakeMov(self):
		Bewegspeed = self.ChatEditLine2.GetText()
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Hareket hiziniz: " + Bewegspeed)
		chr.SetMoveSpeed(int(Bewegspeed))
		
	def MakeMovOff(self):
		chr.SetMoveSpeed(int(player.GetStatus(player.MOVING_SPEED)))
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Hareket hizi kapatildi.")
		

		
StartDialog = Hackdialog()
StartDialog.Show()