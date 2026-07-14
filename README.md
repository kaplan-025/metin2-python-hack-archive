# Metin2 Python Hack Archive

> A curated archive of **Python-based hacks, bots, mods, and animation overrides** for Metin2, gathered across various communities.

Collected over the years from Dreamfancy.org, M2kmod releases, and other Metin2 modding sources. Contains injection tools, in-game automation scripts, full mod frameworks with custom GUI, and 7x damage animation packs for all classes.

---

## 📁 Full Directory Tree

```
Python Arşivi/
│
├── 7x Damage/                          # Animation damage multiplier mods
│   ├── dmg/                             #   Damage animation overrides (MSA/MSK)
│   │   ├── pc/                          #     Original animations per class
│   │   │   ├── assassin/                #       + bow, dualhand_sword, onehand_sword
│   │   │   │   ├── action/              #         (dance, kiss, clap, etc.)
│   │   │   │   ├── bow/                 #         combo/damage/run/walk sequences
│   │   │   │   ├── dualhand_sword/      #         combo_01~08 + rampage
│   │   │   │   ├── fishing/             #         fishing animations
│   │   │   │   ├── general/             #         damage/dead/run/walk
│   │   │   │   ├── horse/               #         mounted animations
│   │   │   │   ├── horse_bow/           #         mounted bow
│   │   │   │   ├── horse_dualhand_sword/#         mounted dual sword
│   │   │   │   ├── horse_onehand_sword/ #         mounted onehand
│   │   │   │   ├── intro/               #         character select screen
│   │   │   │   ├── onehand_sword/       #         combo_01~07 + rampage
│   │   │   │   ├── skill/               #         20+ skill animations (amseup,
│   │   │   │   │                        #           charyun, dokgigung, eunhyeong,
│   │   │   │   │                        #           gungsin, gwangyeok, hwajo, etc.)
│   │   │   │   └── wedding/             #         wedding attire
│   │   │   ├── shaman/                  #       bell, fan, 30+ skills
│   │   │   │   ├── action/              #         (same social actions)
│   │   │   │   ├── bell/                #         combo_01~07
│   │   │   │   ├── fan/                 #         combo_01~07
│   │   │   │   ├── fishing/             #
│   │   │   │   ├── general/             #
│   │   │   │   ├── horse/               #         mounted bell+fan
│   │   │   │   ├── horse_bell/          #
│   │   │   │   ├── horse_fan/           #
│   │   │   │   ├── intro/               #
│   │   │   │   ├── skill/               #         35+ skills (bipabu, boho, budong,
│   │   │   │   │                        #           byeorak, daejeongeop, gicheon,
│   │   │   │   │                        #           hosin, jeungeop, jeungryeok,
│   │   │   │   │                        #           kwaesok, noejeon, paeryong, etc.)
│   │   │   │   └── wedding/             #
│   │   │   ├── sura/                    #       onehand_sword, 25+ skills
│   │   │   │   ├── action/              #
│   │   │   │   ├── fishing/             #
│   │   │   │   ├── general/             #
│   │   │   │   ├── horse/               #
│   │   │   │   ├── horse_onehand_sword/ #
│   │   │   │   ├── intro/               #
│   │   │   │   ├── onehand_sword/       #         combo_01~07
│   │   │   │   ├── skill/               #         30+ skills (geomhwan, gongpo,
│   │   │   │   │                        #           gwigeom, heuksin, hwayeom,
│   │   │   │   │                        #           jumagap, maryeong, pabeop, etc.)
│   │   │   │   └── wedding/             #
│   │   │   └── warrior/                 #       onehand + twohand sword, 25+ skills
│   │   │       ├── action/              #
│   │   │       ├── fishing/             #
│   │   │       ├── general/             #
│   │   │       ├── horse/               #
│   │   │       ├── horse_onehand_sword/ #
│   │   │       ├── horse_twohand_sword/ #
│   │   │       ├── intro/               #
│   │   │       ├── onehand_sword/       #         combo_01~07 + attack seq
│   │   │       ├── skill/               #         30+ skills (cheongeun, daejin,
│   │   │       │                        #           geomgyeong, gigongcham, gihyeol,
│   │   │       │                        #           gyeoksan, noegeom, palbang, etc.)
│   │   │       ├── twohand_sword/       #         combo_01~07 + damage seq
│   │   │       ├── twohand_sword - Kopia/ #       backup copy
│   │   │       └── wedding/             #
│   │   └── pc2/                          #     PvP-specific animation set
│   │       ├── assassin/                 #       (same structure as pc/ mirror)
│   │       ├── shaman/                   #
│   │       ├── sura/                     #
│   │       └── warrior/                  #
│   └── lib/                              #   Python loader script for 7x dmg
│       ├── dmg/                          #     mirrored animation structure
│       │   ├── pc/                       #
│       │   └── pc2/                      #
│       └── otodamage.py                  #     Auto-damage injector script
│
├── Karışık/                              # Standalone hack scripts (40+ files)
│   │
│   │   ### Bots ###
│   ├── farmbot.py                        #   Auto farming bot
│   ├── fishbot1.0.py                     #   Fishing bot v1.0
│   ├── fishbot1.1.py                     #   Fishing bot v1.1
│   ├── fishbot-darealfreak.py            #   Fishing bot by DaRealFreak
│   ├── 123klo-fishbot.py                 #   Fishing bot by 123klo
│   ├── levelbot.py                       #   Leveling bot
│   ├── craplevelbot.py                   #   Crap level bot
│   ├── pasha37-levelbot.py               #   Level bot by Pasha37
│   ├── buffbot.py                        #   Auto buff bot
│   ├── spambot.py                        #   Chat spam bot
│   ├── energybot.py                      #   Auto energy recharge bot
│   ├── efsunbotu.py                      #   Enchantment bot
│   ├── efsunbotu2.py                     #   Enchantment bot v2
│   ├── alchemistbot.py                   #   Alchemy bot
│   ├── darealfreakbot.py                 #   Multi-purpose bot by DaRealFreak
│   ├── mesajbot.py                       #   Auto messenger bot
│   │
│   │   ### Multi-Hacks ###
│   ├── multihack.py                      #   Multi-hack (collection of toggles)
│   ├── multihack2.py                     #   Multi-hack v2
│   ├── multihack3.py                     #   Multi-hack v3
│   ├── multihack4.py                     #   Multi-hack v4
│   ├── kagb-multihack.py                 #   Multi-hack by KAGB
│   ├── rajmultihack.py                   #   Multi-hack by Raj
│   ├── vbmultihack.py                    #   VB multi-hack
│   ├── 123klo-multihack.py              #   Multi-hack by 123klo
│   │
│   │   ### Teleport Hacks ###
│   ├── teleport1.py                      #   Teleport hack v1
│   ├── teleport2.py                      #   Teleport hack v2
│   ├── teleport3.py                      #   Teleport hack v3
│   ├── teleport4.py                      #   Teleport hack v4
│   │
│   │   ### Damage / Combat ###
│   ├── 7x damage.py                      #   7x damage script
│   ├── skillhack.py                      #   Skill hack
│   ├── modhack.py                        #   Attack speed / mod hack
│   ├── kickhack.py                       #   Kick / stagger hack
│   ├── zoomhack.py                       #   Zoom distance hack
│   ├── padmak.py                         #   PvP auto-dodge
│   ├── edithack.py                       #   Edit / memory hack
│   ├── okcuhack.py                       #   OKCU hack
│   ├── yangbug.py                        #   Yang dupe bug
│   │
│   │   ### Item & Utility ###
│   ├── itemcreator.py                    #   Item creator tool
│   ├── shopcreator.py                    #   Shop creator tool
│   ├── pickupstealer.py                  #   Auto pickup / steal
│   ├── itembasma.py                      #   Item duplication
│   ├── moblock.py                        #   Mob lock-on
│   ├── vidscanner.py                     #   Video scanner
│   ├── metinbulucu.py                    #   Metin stone finder
│   └── antifly(sekmeme).py              #   Anti-fly / no knockback
│
├── M2kmod/                                # Full-featured Metin2 modification framework
│   ├── 1.3 version/                       #   Legacy release (Python 2.2 + 2.7)
│   │   ├── python22/                      #     Python 2.2 build
│   │   │   ├── launch_m2k.py              #       Launcher script
│   │   │   └── m2kmod/                    #       Mod root
│   │   │       ├── __init__.py
│   │   │       ├── hackbar.py             #       Main hack GUI bar
│   │   │       ├── Saves/                 #       Config saves (.m2k)
│   │   │       ├── Images/                #       GUI texture library (.tga)
│   │   │       │   ├── General/           #         icons: chat, combo, exp, ghost,
│   │   │       │   │                      #           horse, moon, nofog, pickup, etc.
│   │   │       │   ├── Hackbar/           #         module icons: buff, energy, eqchanger,
│   │   │       │   │                      #           fish, ghost, info, inventory, etc.
│   │   │       │   └── Shortcuts/         #         arrow & action buttons
│   │   │       │       └── Arrow/         #           teleport direction arrows
│   │   │       └── Modules/               #     (only 1.4+ has modules)
│   │   └── python27/                      #     Python 2.7 build (mirror structure)
│   │
│   ├── 1.4 version/                       #   Stable release (Python 2.7)
│   │   ├── hackbar.py                     #     Main hack GUI bar
│   │   ├── __init__.py
│   │   ├── Saves/                         #     Config: config.m2k, priceconfig.m2k, texts.m2k
│   │   ├── Images/                        #     GUI textures (+Hackbar, General, Shortcuts)
│   │   └── Modules/                       #     Feature modules:
│   │       ├── __init__.py
│   │       ├── Bookreader.py              #       Auto book reader (Exp, Skill)
│   │       ├── Buffbot.py                 #       Auto party buffing
│   │       ├── EQChanger.py               #       Equipment switcher
│   │       ├── Info.py                    #       Server/player info display
│   │       ├── Inventorymanager.py        #       Auto inventory management
│   │       ├── Itemcreator.py             #       Item spawning tool
│   │       ├── Itemstealer.py             #       Auto loot / steal
│   │       ├── Levelbot.py                #       Auto leveling
│   │       ├── Settings.py                #       Mod configuration
│   │       ├── Shopcreator.py             #       Auto shop creation
│   │       ├── Soulstonereader.py         #       Soulstone stat reader
│   │       ├── Spambot.py                 #       Chat spam automation
│   │       ├── Taubuyer.py                #       Auto buy from NPC
│   │       ├── Telehack.py                #       Teleport hack module
│   │       ├── m2k_hook.py                #       Game hook interface
│   │       ├── m2k_lib.py                 #       Core library
│   │       ├── pyDetour.py                #       Python detour engine
│   │       ├── swich.py                   #       Feature switch/toggle
│   │       └── tp.py                      #       Teleport coordinates
│   │
│   └── 2.0 version (final)/               #   Final release
│       ├── m2kmod_run.py                  #     Runner script
│       ├── m2kmod_script.py               #     Alternative launcher
│       └── m2kmod/                        #     Mod root (same structure as 1.4)
│           ├── __init__.py
│           ├── hackbar.py
│           ├── Saves/
│           ├── Images/
│           └── Modules/                   #     (same module set as 1.4)
│
├── Python Loader/                         # DLL injectors for running .py in-game
│   ├── Loader 1/                          #   Generic Python loaders
│   │   ├── Python_Loader_2.2.dll          #     For Python 2.2
│   │   ├── Python_Loader_2.7.dll          #     For Python 2.7
│   │   └── msvcr100d.dll                  #     VC++ runtime dependency
│   └── Loader 2/                          #   KAGB branded loaders
│       ├── kagb22.dll                     #     KAGB loader (Python 2.2)
│       ├── kagb27.dll                     #     KAGB loader (Python 2.7)
│       └── msvcr100d.dll                  #     VC++ runtime dependency
│
├── Zahon Mod/                             # Advanced GUI mod with detector systems
│   ├── ZAHON_MOD/                         #   Main mod directory
│   │   ├── Buttons/                       #   GUI button textures (.tga / .xcf)
│   │   │   ├── ETC/                       #     Off, On, Question Mark, Restart
│   │   │   ├── Function/                  #     Auto Attack, Auto Pot, Detector,
│   │   │   │                              #       GM Detector, Mobber, Pick Up,
│   │   │   │                              #       Teleport, Use Item
│   │   │   ├── Gui/                       #     Show/Hide buttons
│   │   │   ├── Other/                     #     Book Reader (Buy, Egzo, Rada)
│   │   │   ├── Other_Gui/                 #     BS, Buff Bot, Exp Donator, FB,
│   │   │   │                              #       Inventory Manager, Item Clicker,
│   │   │   │                              #       Python Loader, Spam Bot
│   │   │   └── Teleport/                  #     Direction arrows
│   │   ├── Config/                        #   Detection configuration
│   │   │   ├── Detector/                  #     All_List, Boss_List, Metin_List,
│   │   │   │                              #       Ore_List, Player_List
│   │   │   ├── GM_Detector/               #     GM detection name lists
│   │   │   ├── Another/                   #     Extra configs
│   │   │   ├── Teleport/                  #     Teleport coordinates
│   │   │   └── Save/                      #     Save data
│   │   ├── Icons/                         #   Icon textures
│   │   │   ├── Auto_Pot/                  #     Blue/Red pot indicators
│   │   │   ├── Detector/                  #     Boss, Metin, Ore, Player icons
│   │   │   ├── ETC/                       #     Bar, Empty Slot
│   │   │   ├── GM_Detector/               #     GM warning icon
│   │   │   ├── Info/                      #     Logo, Facebook, YouTube, MPC
│   │   │   └── Info_Screen/               #     Splash screen images
│   │   └── Python/                        #   Python scripts
│   │       ├── BS.pyc                     #     Compiled BS module
│   │       └── Fake_Info.py               #     Fake info display
│   └── lib/                               #   Library version (same structure)
│       └── ZAHON_MOD.py                   #     Main library entry point
│           └── ZAHON_MOD/                 #     (mirrors ZAHON_MOD/ contents)
│
├── .gitignore                             # Ignores .pyc, __pycache__, .DS_Store
├── LICENSE                                 # License file
└── README.md                              # This file
```

---

## 🔧 Requirements

- **Metin2 client** (any version that supports Python loading)
- **Python Loader** DLL (included in `Python Loader/`)
  - Python 2.2 compatible → `Python_Loader_2.2.dll` or `kagb22.dll`
  - Python 2.7 compatible → `Python_Loader_2.7.dll` or `kagb27.dll`
- **VC++ runtime** (`msvcr100d.dll` included)

## 🚀 Quick Start

```bash
# 1. Choose your Python Loader (2.2 or 2.7)
# 2. Inject the DLL into your Metin2 process
# 3. Load your desired .py script
# 4. Use in-game hotkeys (varies per script)
```

### M2kmod Usage

1. Inject with the appropriate Python Loader
2. Run `hackbar.py` — the GUI appears in-game
3. Toggle modules via the button interface

### Zahon Mod Usage

1. Copy `ZAHON_MOD/` into your Metin2 `lib/` directory
2. Inject `ZAHON_MOD.py` via Python Loader
3. GUI with button-based module control appears in-game

### 7x Damage Mod

1. Run `otodamage.py` to enable auto-damage injection
2. Animation files (`.msa`/`.msk`) override default attack speeds
3. Covers all 4 classes with multiple weapon types

## ⚠️ Disclaimer

This archive is for **educational and research purposes only**. Using these scripts may result in a permanent game account ban. No warranty is provided for any of the scripts — use at your own risk.

---

*Sources: Dreamfancy.org, M2kmod, KAGB, Zahon Mod & various Metin2 modding communities*
