############### MobScanner by !Beni! ###############
####################################################
############### Modul by Kamer1337   ###############
####################################################
import player,chat,ui,chr,app,time,dbg,kamer,chrmgr
from thread import start_new_thread as st
from chr import SelectInstance as sel,SetPixelPosition as easytp,GetInstanceType as gettyp,INSTANCE_TYPE_OBJECT,INSTANCE_TYPE_BUILDING,INSTANCE_TYPE_ENEMY,INSTANCE_TYPE_NPC,INSTANCE_TYPE_PLAYER,GetPixelPosition
chat.post=lambda msg: chat.AppendChat(1,msg)
chr.isDead=lambda vid: int(chrmgr.GetVIDInfo(vid).split("isDead=")[1][0])
class MobScannerDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.Phase=0
		self.Step=4250#4000
		self.runned=0
		self.NearestMob=0
		self.SortedList=[]
		self.distance_dict={}
		self.vids={INSTANCE_TYPE_OBJECT:[],INSTANCE_TYPE_BUILDING:[],INSTANCE_TYPE_ENEMY:[],INSTANCE_TYPE_NPC:[],INSTANCE_TYPE_PLAYER:[]}
	def Start(self):
		self.Show()
	def __del__(self):
		self.Hide()
		chat.post("DEL")
		ui.ScriptWindow.__del__(self)
	def Distance(self,vid):
		return player.GetCharacterDistance(vid)
	def scannerthread(self,brange,range):
		IsExistingVid=chr.HasInstance
		getTypVid=gettyp
		vids=self.vids
		for vid in xrange(brange,range):
			#self.backup=vid
			instance=getTypVid(vid)
			if (instance not in vids) or (not IsExistingVid(vid)):
				continue
			if len(vids[instance])<500:#150
				vids[instance].append(vid)
			else:
				black=[]
				for i in vids[instance]:
					if i in black:
						vids[instance].remove(i)
					else:
						black.append(i)
				del black
		self.UpdateMobNear()
	def ExistVid(self,vid):
		vids=self.vids
		for i in vids:
			if vid in vids[i]:
				return TRUE
		return FALSE
	def OnUpdate(self):
		range=self.Phase
		endrange=self.Step+range
		self.scannerthread(range,endrange)
		if self.Phase>4000000:
			self.runned=1
			self.Phase=0
		else:
			self.Phase=endrange
		#return
	def UpdateMobNear(self):
		distance_dict={}
		SortedList=[]
		black=[]
		distance=0
		Attackable=player.CanAttackInstance
		HasDied=chr.isDead
		VIDs=self.vids
		for vid in VIDs[INSTANCE_TYPE_ENEMY]:
			if not Attackable(vid) or vid in black or HasDied(vid):
				VIDs[INSTANCE_TYPE_ENEMY].remove(vid)
				continue
			black.append(vid)
			distance = self.Distance(vid)
			if not distance in distance_dict:
				distance_dict[distance] = []
				SortedList.append(distance)
			distance_dict[distance].append(vid)
		del black
		del distance
		SortedList.sort()
		self.SortedList=SortedList
		self.distance_dict=distance_dict
	def FirstMob(self):
		if len(self.vids[INSTANCE_TYPE_ENEMY]):
			x=self.distance_dict[self.SortedList[0]][0]
		else:
			return 0
		return x
	def RemoveFirstMob(self):
		try:
			self.vids.remove(self.distance_dict[self.SortedList[0]][0])
		except:
			pass
		del self.distance_dict[self.SortedList[0]][0]
		if len(self.distance_dict[self.SortedList[0]]) == 0:
			del self.SortedList[0]
	def RemoveMob(self,vid):
		dis=self.distance_dict
		for i in dis:
			if vid in dis[i]:
				dis[i].remove(vid)
				break
		if vid in self.vids[INSTANCE_TYPE_ENEMY]:
			self.vids[INSTANCE_TYPE_ENEMY].remove(vid)
	def GetNearestMobs(self):
		#buggy "list index out of range"
		return self.distance_dict[self.SortedList[0]]
	
	
	def PullEveryMob(self):
		for vid in self.vids[INSTANCE_TYPE_ENEMY]:
			kamer.SendBattlePacket(vid)
	def isGMNear(self):
		IsGM=chr.IsGameMaster
		GetName=chr.GetNameByVID
		exists=chr.HasInstance
		mainVid=player.GetMainCharacterIndex()
		for vid in self.vids[INSTANCE_TYPE_PLAYER]:
			if exists(vid) and (IsGM(vid) or GetName(vid)[0]=='['):
				chr.SelectInstance(vid)
				chr.Show()
				GM_Name = chr.GetNameByVID(vid)
				chat.AppendChat(7, 'Attention ! %s is near !!' % GM_Name)
				break
	def SpamAll(self):
		message="HeyHo"
		exists=chr.HasInstance
		IsGM=chr.IsGameMaster
		for vid in self.vids[INSTANCE_TYPE_PLAYER]:
			if exists(vid) and not IsGM(vid):
				net.SendWhisperPacket(chr.GetNameByVID(vid), message)
				break
				
	def PullRandMobs(self,counter):
		for i in xrange(counter):
			kamer.SendBattlePacket(self.vids[INSTANCE_TYPE_ENEMY][app.GetRandom(0, len(self.vids[INSTANCE_TYPE_ENEMY])-1)])
	def PullMobs(self,counter):
		retnArray=[]
		x=0
		distance_dict=self.distance_dict
		SortedList=self.SortedList
		for dis in SortedList:
			for vid in distance_dict[dis]:
				kamer.SendBattlePacket(vid)
				retnArray.append(vid)
				x+=1
				if x>=counter:
					return retnArray
		return retnArray
	def Stop(self):
		self.Hide()
