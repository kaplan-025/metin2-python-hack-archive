import chrmgr
import dbg
ww=chrmgr.SetPathName
dd=chrmgr.RegisterCacheMotionData
def oo(bb):
    c=''
    d=''
    f=''
    reczna=''
    dzwonek=''
    wahlaz=''
    onehand=''
    dzwonekbut=''
    wahlazbut=''
    lenonehand=len(bb)-15
    lenreczna=len(bb)-21
    lendzwonek=len(bb)-12
    lenwahlaz=len(bb)-11
    lendzwonekbut=len(bb)-6
    lenwahlazbut=len(bb)-5
    g=len(bb)-22
    a=len(bb)-5
    b=len(bb)-16
    for i in range(15):
        onehand=onehand+bb[lenonehand+i]
    for i in range(21):
        reczna=reczna+bb[lenreczna+i]
    for i in range(12):
        dzwonek=dzwonek+bb[lendzwonek+i]
    for i in range(6):
        dzwonekbut=dzwonekbut+bb[lendzwonekbut+i]
    for i in range(11):
        wahlaz=wahlaz+bb[lenwahlaz+i]
    for i in range(5):
        wahlazbut=wahlazbut+bb[lenwahlazbut+i]
    for i in range(5):
        c=c+bb[a+i]
    for i in range(16):
        d=d+bb[b+i]
    for i in range(22):
        f=f+bb[g+i]
    if c=='/bow/':
        ww(bb)
    elif d=='/dualhand_sword/':
        ww('d:/ymir work/pc/assassin/dualhand_sword/')
    elif f=='/horse_dualhand_sword/':
        ww('d:/ymir work/pc/assassin/dualhand_sword/')
    elif reczna=='/horse_onehand_sword/':
        ww('d:/ymir work/pc/assassin/dualhand_sword/')
    elif reczna=='/horse_twohand_sword/':
        ww('d:/ymir work/pc/assassin/dualhand_sword/')
    elif dzwonek=='/horse_bell/':
        ww('d:/ymir work/pc/assassin/dualhand_sword/')
    elif dzwonekbut=='/Bell/':
        ww('d:/ymir work/pc/assassin/dualhand_sword/')
    elif wahlaz=='/horse_fan/':
        ww('d:/ymir work/pc/assassin/dualhand_sword/')
    elif wahlazbut=='/fan/':
        ww('d:/ymir work/pc/assassin/dualhand_sword/')
    elif onehand=='/onehand_sword/':
        ww('d:/ymir work/pc/assassin/dualhand_sword/')
    else:
        ww(bb)
def jaja(x,y,z,p=999):
    if z == 'combo_03.msa':
        dd(x,y, 'combo_01.msa')
    elif z == 'combo_04.msa':
        dd(x,y ,'combo_02.msa')
    elif p == 999:
        dd(x,y,z)
    else:
        dd(x,y,z,p)
        
    
chrmgr.SetPathName=oo
chrmgr.RegisterCacheMotionData=jaja
dbg.LogBox('dmg')


