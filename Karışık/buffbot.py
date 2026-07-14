# Metin2Bot [Dreamfancy]
import app
import chat
import chr
import locale
import net
import time
import ui
import player
import skill
import chrmgr
import item

IsOnScreen = "0"
buffbotstatus = ""
timing = "0"
cooltimedelay = "0"
delayslide = 0
buff1 = "0"
buff2 = "0"
buff3 = "0"
pothp = "0"
potsp = "0"

class Botdialog(ui.ThinBoard):

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.LoadBoard()
		self.skillname()
		
	def LoadBoard(self):
		self.SetCenterPosition()
		self.SetSize(340, 170)
		self.Show()
		self.AddFlag("movable")
		self.LoadText()
		self.LoadButton()
		
	def LoadText(self):
		self.Title = ui.TextLine()
		self.Title.SetParent(self)
		self.Title.SetDefaultFontName()
		self.Title.SetPosition(-90, 4)
		self.Title.SetFeather()
		self.Title.SetWindowHorizontalAlignCenter()
		self.Title.SetText("Dreamfancy - Buffbot 0.1")
		self.Title.SetFontColor(1.0, 0.8, 0)
		self.Title.SetOutline()
		self.Title.Show()
		
		self.TargetName = ui.TextLine()
		self.TargetName.SetParent(self)
		self.TargetName.SetDefaultFontName()
		self.TargetName.SetPosition(-70, 33)
		self.TargetName.SetFeather()
		self.TargetName.SetWindowHorizontalAlignCenter()
		self.TargetName.SetText("Secili birsey yok.")
		self.TargetName.SetOutline()
		self.TargetName.Show()

		self.Info = ui.TextLine()
		self.Info.SetParent(self)
		self.Info.SetDefaultFontName()
		self.Info.SetPosition(-125, 33)
		self.Info.SetFeather()
		self.Info.SetWindowHorizontalAlignCenter()
		self.Info.SetFontColor(1.0, 0.8, 0)
		self.Info.SetText("Hedef: ")
		self.Info.SetOutline()
		self.Info.Show()

		self.Info2 = ui.TextLine()
		self.Info2.SetParent(self)
		self.Info2.SetDefaultFontName()
		self.Info2.SetPosition(-125, 55)
		self.Info2.SetFeather()
		self.Info2.SetWindowHorizontalAlignCenter()
		self.Info2.SetFontColor(1.0, 0.8, 0)
		self.Info2.SetText("ID:")
		self.Info2.SetOutline()
		self.Info2.Show()	

		self.ChatEditLine = ui.TextLine()
		self.ChatEditLine.SetParent(self)
		self.ChatEditLine.SetDefaultFontName()
		self.ChatEditLine.SetPosition(100, 55)
		self.ChatEditLine.SetFeather()
		self.ChatEditLine.SetText("0")
		self.ChatEditLine.SetOutline()
		self.ChatEditLine.Show()
		
		self.hpper = ui.TextLine()
		self.hpper.SetParent(self)
		self.hpper.SetFontColor(1.0, 0.8, 0)
		self.hpper.SetPosition(20, 100)
		self.hpper.SetText("HP - Kapali")
		self.hpper.Show()
		self.spper = ui.TextLine()
		self.spper.SetParent(self)
		self.spper.SetFontColor(1.0, 0.8, 0)
		self.spper.SetPosition(20, 120)
		self.spper.SetText("SP - Kapali")
		self.spper.Show()		
		self.delayper = ui.TextLine()
		self.delayper.SetParent(self)
		self.delayper.SetFontColor(1.0, 0.8, 0)
		self.delayper.SetPosition(20, 140)
		self.delayper.SetText("Sure-0saniye")
		self.delayper.Show()	
		
	def LoadButton(self):
		self.CloseButton = ui.Button()
		self.CloseButton.SetParent(self)
		self.CloseButton.SetPosition(320, 4)
		self.CloseButton.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		self.CloseButton.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		self.CloseButton.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		self.CloseButton.SetToolTipText(locale.UI_CLOSE, 0, - 23)
		self.CloseButton.SetEvent(ui.__mem_func__(self.Close))
		self.CloseButton.Show()
		
		self.BuffBotStartButton = ui.Button()
		self.BuffBotStartButton.SetParent(self)
		self.BuffBotStartButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.BuffBotStartButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.BuffBotStartButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.BuffBotStartButton.SetText("Baslat")
		self.BuffBotStartButton.SetPosition(130, 75)
		self.BuffBotStartButton.SetEvent(ui.__mem_func__(self.StartBuffbot))
		self.BuffBotStartButton.Show()	

		self.GetVIDButton = ui.Button()
		self.GetVIDButton.SetParent(self)
		self.GetVIDButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.GetVIDButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.GetVIDButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.GetVIDButton.SetText("Hedefi sec")
		self.GetVIDButton.SetPosition(245, 30)
		self.GetVIDButton.SetEvent(ui.__mem_func__(self.GetVID))
		self.GetVIDButton.Show()	

		self.buf1 = ui.Button()
		self.buf1.SetParent(self)
		self.buf1.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
		self.buf1.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
		self.buf1.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
		self.buf1.SetText("1-Kapali")
		self.buf1.SetPosition(290, 60)
		self.buf1.SetEvent(ui.__mem_func__(self.stat1))
		self.buf1.Show()	

		self.buf2 = ui.Button()
		self.buf2.SetParent(self)
		self.buf2.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
		self.buf2.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
		self.buf2.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
		self.buf2.SetText("2-Kapali")
		self.buf2.SetPosition(290, 90)
		self.buf2.SetEvent(ui.__mem_func__(self.stat2))
		self.buf2.Show()

		self.buf3 = ui.Button()
		self.buf3.SetParent(self)
		self.buf3.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
		self.buf3.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
		self.buf3.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
		self.buf3.SetText("3-Kapali")
		self.buf3.SetPosition(290, 120)
		self.buf3.SetEvent(ui.__mem_func__(self.stat3))
		self.buf3.Show()
		
		self.slidebar1 = ui.SliderBar()
		self.slidebar1.SetParent(self)
		self.slidebar1.SetPosition(100, 105)
		self.slidebar1.SetEvent(ui.__mem_func__(self .slideHP))
		self.slidebar1.Show()

		self.slidebar2 = ui.SliderBar()
		self.slidebar2.SetParent(self)
		self.slidebar2.SetPosition(100, 125)
		self.slidebar2.SetEvent(ui.__mem_func__(self .slideSP))
		self.slidebar2.Show()

		self.slidebar3 = ui.SliderBar()
		self.slidebar3.SetParent(self)
		self.slidebar3.SetPosition(100, 145)
		self.slidebar3.SetEvent(ui.__mem_func__(self .slidedelay))
		self.slidebar3.Show()
	
	def skillname(self):
		##0razb
		##2sura
		##3saman
		##5ninja
		te1=int(net.GetMainActorRace())
		te2=int(net.GetMainActorSkillGroup())
		SkillIndex=1
		if te1==3:
			SkillIndex = 91
			if te2==2:
				SkillIndex==106
		elif te1==2:
			SkillIndex = 61
			if te2==2:
				SkillIndex==76
		elif te1==5:
			SkillIndex = 31
			if te2==2:
				SkillIndex==46
		elif te1==0:
			SkillIndex = 1
			if te2==2:
				SkillIndex==16
		ski1=skill.GetSkillName(SkillIndex + 3)
		ski2=skill.GetSkillName(SkillIndex + 4)
		ski3=skill.GetSkillName(SkillIndex + 5)
		self.buf1.SetToolTipText(ski1, 75, 2)
		self.buf2.SetToolTipText(ski2, 75, 2)
		self.buf3.SetToolTipText(ski3, 75, 2)
		
	def __del__(self):
		ui.ThinBoard.__del__(self)

	def Show(self):
		ui.ThinBoard.Show(self)

	def Close(self):
		player.ClearTarget()
		global buffbotstatus, timing, cooltimedelay, delayslide, buff1, buff2, buff3, pothp, potsp, IsOnScreen
		buffbotstatus = ""
		IsOnScreen = "0"
		timing = "0"
		cooltimedelay = "0"
		delayslide = 0
		buff1 = "0"
		buff2 = "0"
		buff3 = "0"
		pothp = "0"
		potsp = "0"
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
		
	def slidedelay(self):
		global delayslide
		delayslide=int(self.slidebar3.GetSliderPos()*100)
		self.delayper.SetText('Sure-' + str(delayslide) + 'saniye')

	def slideHP(self):
		global pothp
		temp = int(self.slidebar1.GetSliderPos()*100)
		if temp > 0:
			self.hpper.SetText('HP - ' + str(temp) + '%')
			pothp = temp
		else:
			self.hpper.SetText("HP - Kapali")
			pothp = "0"

	def slideSP(self):
		global potsp
		temp = int(self.slidebar2.GetSliderPos()*100)
		if temp > 0:
			self.spper.SetText('SP - ' + str(temp) + '%')
			potsp = temp
		else:
			self.spper.SetText("SP - Kapali")
			potsp = "0"

	def delaydef(self):
		global timing
		if timing=="0":
			timing = time.clock()
		else:
			curtiming = time.clock()
			timetowait=timing + 5
			if timetowait<curtiming:
				timing="0"
				net.SendChatPacket("/restart")

	def AutoPot(self):
		global pothp, potsp
		hp = int(player.GetStatus(player.HP))
		hpsize = int(player.GetStatus(player.MAX_HP))
		sp = int(player.GetStatus(player.SP))
		spsize = int(player.GetStatus(player.MAX_SP))
		if hp<=0:
			self.delaydef()
		if potsp != "0":
			if sp<spsize/100 * potsp:
				for i in xrange(player.INVENTORY_PAGE_SIZE*3):
					ItemValue = player.GetItemIndex(i)
					if ItemValue == 27004 or ItemValue == 27005 or ItemValue == 27006:
						net.SendItemUsePacket(i)
		if pothp != "0":
			if hp<hpsize/100 * pothp:
				for i in xrange(player.INVENTORY_PAGE_SIZE*3):
					ItemValue = player.GetItemIndex(i)
					if ItemValue == 27001 or ItemValue == 27002 or ItemValue == 27003:
						net.SendItemUsePacket(i)

	def StartBuffbot(self):
		global buffbotstatus,buff1,buff2,buff3,cooltimedelay
		vid = int(self.ChatEditLine.GetText())
		if buff1=="1" or buff2=="1" or buff3=="1":
			if vid != 0:
				if buffbotstatus != "":
					buffbotstatus = ""
					self.BuffBotStartButton.SetText("Baslat")
				else:
					buffbotstatus = "1"
					cooltimedelay="-1"
					self.BuffBotStartButton.SetText("Durdur")
					name = chr.GetNameByVID(vid)
					self.TargetName.SetText(name)
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Metin2Bot - Once hedef secin!")
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Metin2Bot - Herhangi bir skill acin.")
		
	def GetVID(self):
		global buffbotstatus
		if buffbotstatus=="":
			if self.TargetName.GetText() != "Hicbirsey":
				vid = player.GetTargetVID()
				self.ChatEditLine.SetText(str(vid))
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Metin2Bot - Once bir hedef secin.")
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Metin2Bot - Once botu durdurun!")
	
	def stat1(self):
		global buff1,buffbotstatus
		if buffbotstatus=="":
			if buff1 != "1":
				self.buf1.SetText("1-Acik")
				buff1 = "1"
			else:
				self.buf1.SetText("1-Kapali")
				buff1 = "0"
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Metin2Bot - Once botu durdurun!")

	def stat2(self):
		global buff2,buffbotstatus
		if buffbotstatus == "":
			if buff2 != "1":
				self.buf2.SetText("2-Acik")
				buff2 = "1"
			else:
				self.buf2.SetText("2-Kapali")
				buff2 = "0"
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Metin2Bot - Once botu durdurun!")


	def stat3(self):
		global buff3,buffbotstatus
		if buffbotstatus=="":
			if buff3 != "1":
				self.buf3.SetText("3-Acik")
				buff3 = "1"
			else:
				self.buf3.SetText("3-Kapali")
				buff3 = "0"
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Metin2Bot - Once botu durdurun!")

	def OnUpdate(self):
		targetVID = self.ChatEditLine.GetText()
		global buffbotstatus, buff1, buff2, buff3, cooltimedelay, delayslide
		if buffbotstatus != "" :
			self.AutoPot()
			player.SetTarget(int(targetVID))
			if cooltimedelay=="0":
				cooltimedelay = time.clock()
			else:
				curtiming = time.clock()
				if cooltimedelay=="-1":
					timetowait=0
				else:
					timetowait=cooltimedelay + delayslide
				if timetowait<curtiming:
					if buff1=="1":
						statskill= player.IsSkillCoolTime(4)
						if statskill==0:
							player.ClickSkillSlot(4)
						else:
							sk1=1
					if buff2=="1":
						statskill= player.IsSkillCoolTime(5)
						if statskill==0:
							player.ClickSkillSlot(5)
						else:
							sk2=1
					if buff3=="1":
						statskill= player.IsSkillCoolTime(6)
						if statskill==0:
							player.ClickSkillSlot(6)
						else:
							sk3=1
					if buff1=="0":
						sk1=1
					if buff2=="0":
						sk2=1
					if buff3=="0":
						sk3=1
					if sk1==1 and sk2==1 and sk3==1:
						cooltimedelay="0"
						sk1=0
						sk2=0
						sk3=0
		else:
			vid = player.GetTargetVID()
			name = chr.GetNameByVID(vid)
			self.TargetName.SetText(name)
			return			
		
class BotStarter(ui.ThinBoard):

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.LoadBoard2()

	def LoadBoard2(self):
		self.SetCenterPosition()
		self.SetSize(42 ,24)
		self.Show()
		self.AddFlag("movable")
		self.load = ui.Button()
		self.load.SetParent(self)
		self.load.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
		self.load.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
		self.load.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
		self.load.SetText("Hileyi Goster")
		self.load.SetPosition(0, 0)
		self.load.SetEvent(ui.__mem_func__(self.shower))
		self.load.Show()

	def shower(self):
		global IsOnScreen
		if IsOnScreen=="0":
			self.dialstarter=Botdialog()
			self.dialstarter.Show()
			IsOnScreen="1"
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Metin2Bot - Hile zaten acilmis bir durumda!")

StartDialog = BotStarter()
StartDialog.Show()