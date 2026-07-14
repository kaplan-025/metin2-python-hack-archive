import ui
import m2net
import chr
import player
SCAN_START = 10000
SCAN_END = 5000000

class TestMe(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.AddFlag("movable")
		self.AddFlag("float")
		self.SetPosition(10,10)
		self.SetSize(100,70)
		self.SetTitleName("MobLock")
		
		
		
		
		TestBtn = ui.Button()
		TestBtn.SetParent(self)
		TestBtn.SetPosition(20,35)
		TestBtn.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		TestBtn.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		TestBtn.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		TestBtn.SetText("MobLock")
		TestBtn.SetEvent(lambda:self.OnStart())
		TestBtn.Show()
		
		self.TestBtn = TestBtn
		
		self.Show()
		
	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)
		
				

	def OnStart(self):
	        global SCAN_START
		global SCAN_END
		myVid = player.GetMainCharacterIndex()
		x, y, z = player.GetMainCharacterPosition()
		for i in xrange(SCAN_START, SCAN_END):
			if chr.INSTANCE_TYPE_ENEMY == chr.GetInstanceType(i):
				chr.SelectInstance(i)
				chr.SetPixelPosition(int(x), int(y), int(z))
			
			
	
		
TestMe()