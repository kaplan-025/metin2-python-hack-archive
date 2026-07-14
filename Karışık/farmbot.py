import player,ui,wndMgr,game,app,nonplayer,chat,chr

OldHPTargetBoard = game.GameWindow.SetHPTargetBoard
LastCheck = 0
MatchCount = 0
HookedVid = [0, 0]

class MobDialog(ui.ThinBoard):

	startscan = 100
	endscan = 400000
	MobList = []

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.LoadGui()
		self.SetVIDRange()
		HookSetHPTargetBoard()
	def __del__(self):
		ui.ThinBoard.__del__(self)
		
	def LoadGui(self):
	
		self.Button1 = ui.Button()
		self.Button1.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.Button1.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.Button1.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.Button1.SetText("Scan")
		self.Button1.SetEvent(self.AddMobData)
		self.Button1.SetPosition(wndMgr.GetScreenWidth()-90,157)
		self.Button1.Show()	
		
	def Show(self):
		ui.ThinBoard.Show(self)
		
	def SetVIDRange(self):
		Found = 0
		Start = 0
		End = 1000000
		for loop in xrange(1, 7):
			for i in xrange(Start, End):
				if chr.INSTANCE_TYPE_ENEMY == chr.GetInstanceType(i):
					self.startscan = int(i) - 500
					self.endscan = int(i) + 50000
					Found = 1
					break
			if Found == 0:
				Start = End
				End = End + 1000000
		chat.AppendChat(chat.CHAT_TYPE_INFO, "VID Range: " + str(self.startscan) + " - " + str(self.endscan))	
	
	def AddMobData(self):
		Count = 0
		self.SetVIDRange()
		for i in xrange(int(self.startscan), int(self.endscan)): 
			if chr.INSTANCE_TYPE_ENEMY == chr.GetInstanceType(i): 
				chr.SelectInstance(i) 
				vid = int(i) 
				level = nonplayer.GetLevelByVID(i) 
				vnum = chr.GetRace(i) 
				mobX, mobY, mobZ = chr.GetPixelPosition(i) 
				Distance = player.GetCharacterDistance(i) 
				MobData = {"VNUM":vnum,"LEVEL":level,"X":mobX,"Y":mobY,"Z":mobZ,"VID":vid,"COUNT":Count,"DISTANCE":Distance} 
				Count += 1 
				if IsMobAlive(i): 
					self.MobList.append(MobData) 
				else: 
					chat.AppendChat(1, "Mob is Dead!") 
					while self.MobList.count(MobData) > 0: 
						self.MobList.remove(MobData)  
		if len(self.MobList) != 0:
			NearestMob = 0
			for data in self.MobList:
				vnum = str(data["VNUM"])
				level = str(data["LEVEL"])
				Distance = float(data["DISTANCE"])
				id = str(data["VID"])
				Count = str(data["COUNT"])
				if float(Distance) < float(self.MobList[NearestMob]["DISTANCE"]):
					NearestMob = int(Count)

			x = float(self.MobList[int(NearestMob)]["X"])
			y = float(self.MobList[int(NearestMob)]["Y"])
			z = float(self.MobList[int(NearestMob)]["Z"])
			vid = int(self.MobList[int(NearestMob)]["VID"])
			self.WalkToMob(x, y, z, vid)
		
	def WalkToMob(self, x, y, z, vid):
		self.vid = vid
		myVid = player.GetMainCharacterIndex()
		chr.SelectInstance(myVid)
		chr.MoveToDestPosition(int(myVid), int(x), int(y))
		self.MobList = []

		
def IsMobAlive(vid):
	global LastCheck
	global MatchCount
	global HookedVid
	chr.SelectInstance(vid)
	BoundBox = chr.GetBoundBoxOnlyXY(vid)
	Distance = player.GetCharacterDistance(vid)
	if chr.GetInstanceType(vid) == chr.INSTANCE_TYPE_ENEMY:
		if HookedVid[0] == vid and HookedVid[1] <= 0 and Distance <= 200:
			return 0
		if LastCheck == str(BoundBox):
			MatchCount += 1
		else:
			MatchCount = 0
		LastCheck = str(BoundBox)
		
		if Distance >= 975:
			return 1
			
		if MatchCount >= 9:
			MatchCount = 0
			return 0
		else:
			return 1
	else:
		if BoundBox[3] >= 175:
			return 0
		else:
			return 1	
		
def HookedSetHPTargetBoard(self, vid, hpPercentage):
	global OldHPTargetBoard
	global HookedVid
	OldHPTargetBoard(self, vid, hpPercentage)
	HookedVid = [vid, hpPercentage]

def HookSetHPTargetBoard():
	game.GameWindow.SetHPTargetBoard = HookedSetHPTargetBoard
	chat.AppendChat(1, "SetHPTargetBoard wurde erfolgreich gehooked.")		

def UnHookSetHPTargetBoard():
	global OldHPTargetBoard
	game.GameWindow.SetHPTargetBoard = OldHPTargetBoard
	chat.AppendChat(1, "SetHPTargetBoard Hook wurde erfolgreich entfernt.")				
		
MobDialog().Show()

