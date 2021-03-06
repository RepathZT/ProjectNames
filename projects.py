import random, sys

words1 = ["LOUD",
	    "RED",
	    "BLUE",
	    "GREEN",
	    "YELLOW",
	    "IRATE",
	    "ANGRY",
	    "PEEVED",
	    "HAPPY",
	    "SLIMY",
	    "SLEEPY",
	    "JUNIOR",
	    "SLICKER",
	    "UNITED",
	    "SOMBER",
	    "BIZARRE",
	    "ODD",
	    "WEIRD",
	    "WRONG",
	    "LATENT",
	    "CHILLY",
	    "STRANGE",
	    "SILENT",
	    "HOPPING",
	    "ORANGE",
	    "VIOLET",
	    "VIOLENT",
	    "BOUNDLESS",
	    "COBALT",
	    "BEACH",
	    "AQUA",
	    "KILLING",
	    "BULL",
	    "BYE",
	    "CONTRA",
	    "DEW",
	    "DROP",
	    "DRT",
	    "EGOTISTICAL",
	    "ERRONEOUS",
	    "EVENING",
	    "EVIL",
	    "FAIR",
	    "FOX",
	    "HIGH",
	    "JUMP",
	    "MADCAP",
	    "MONKEY",
	    "MOONLIGHT",
	    "OAK",
	    "PATH",
	    "PIN",
	    "SHELL",
	    "SHIFTING",
	    "SILK",
	    "STELLAR",
	    "STORM",
	    "SILVER",
	    "THIN",
	    "TRAFFIC",
	    "TRAIL",
	    "XKEY",
	    "YACHT",
	    "AGILE",
	    "AIR",
	    "AUTO",
	    "BELL",
	    "BLACK",
	    "BULLS",
	    "CENTER",
	    "CHALK",
	    "CHASE",
	    "CHEW",
	    "CIMBRI",
	    "COAST",
	    "COURIER",
	    "CRISS",
	    "DANCING",
	    "DANGER",
	    "DARK",
	    "DECK",
	    "DISH",
	    "DRAGON",
	    "FACE",
	    "FALL",
	    "FISH",
	    "GLOBAL",
	    "HIDE",
	    "HOME",
	    "INTEL",
	    "IVY",
	    "LIFE",
	    "LONG",
	    "MAGIC",
	    "MAIL",
	    "MAIN",
	    "OIL",
	    "OCT",
	    "ONE",
	    "PUZZLE",
	    "SHARK",
	    "SKY",
	    "SPOT",
	    "STEEL",
	    "STUMP",
	    "TALENT",
	    "TAPER",
	    "TAROT",
	    "TREASURE",
	    "TUNING",
	    "TUSK",
	    "WEALTHY",
	    "WEB",
	    "WHITE",
	    "DEITY",
	    "ARK",
	    "IRON",
	    "WAGON",
	    "FEED",
	    "ZESTY",
	    "BANANA",
	    "GOURMET",
	    "HALLUX",
	    "TURBO",
	    "JET",
	    "SOUFFLE",
	    "HEAD",
	    "HAMMER",
	    "SCHOOL",
	    "SIERRA",
	    "STUCCO",
	    "NIGHT",
	    "VIEW",
	    "PHOTO",
	    "BLIND",
	    "TAWDRY",
	    "RAGE",
	    "HOWLER",
	    "STRIKE",
	    "UNITE",
	    "STRAIT",
	    "TWISTED",
	    "WISTFUL",
	    "SURLY",
	    "DROPOUT",
	    "CHIMNEY",
	    "FREE",
	    "GOPHER",
	    "TOTE",
	    "CANDY",
	    "CROSS",
	    "ROCKY",
	    "LAND",
	    "HOLLOW",
	    "WATER",
	    "COTTON",
	    "FIRE",
	    "MOONLIGHT",
	    "WHISTLING",
	    "DANDER"]

words2 = ["WHISPER",
	    "CUTTLEFISH",
	    "MAZE",
	    "MOONLIGHT",
	    "LEGION",
	    "FISH",
	    "CADE",
	    "ANCHOR",
	    "ZEPHYR",
	    "INFORMANT",
	    "SPECTRE"
	    "FIELD",
	    "RUN",
	    "MAN",
	    "FALCON",
	    "OCTAVE",
	    "SWEEPER",
	    "MIRE",
	    "BOX",
	    "GIRAFFE",
	    "GOAT",
	    "INGENUITY",
	    "EASEL",
	    "OLIVE",
	    "ACID",
	    "LANDS",
	    "SEAT",
	    "OCELOT",
	    "ROCKET",
	    "STAR",
	    "BLOSSOM",
	    "CRUSH",
	    "FINDER",
	    "WALE",
	    "TRUMPET",
	    "SHADOW",
	    "WORTH",
	    "WIND",
	    "BREW",
	    "TREAD",
	    "THIEF",
	    "BLAZER",
	    "SCORE",
	    "SHOP",
	    "GAP",
	    "STEED",
	    "DOR",
	    "SOURCE",
	    "TOPPER",
	    "FOOT",
	    "HEART",
	    "PEARL",
	    "WATCH",
	    "EYE",
	    "MASS",
	    "FUN",
	    "STICK",
	    "CINEPLEX",
	    "LINE",
	    "SKILL",
	    "OASIS",
	    "MOUSE",
	    "THUNDER",
	    "FLY",
	    "LIFT",
	    "OUT",
	    "BOWL",
	    "BROKER",
	    "TIDE",
	    "BASE",
	    "INK",
	    "BELLS",
	    "SAVER",
	    "HAUL",
	    "LANTERN",
	    "ORDER",
	    "CORE",
	    "STOCK",
	    "SKYWARD",
	    "ROOF",
	    "CUBE",
	    "FIN",
	    "WRITER",
	    "BEAM",
	    "KNIGHT",
	    "CURSOR",
	    "KEYHOLE",
	    "LAY",
	    "CARD",
	    "MAP",
	    "FORK",
	    "ATTIRE",
	    "CLUSTER",
	    "CANDID",
	    "BOUNCE",
	    "STREAM",
	    "CHEF",
	    "BED",
	    "TROUGH",
	    "LEAK",
	    "GLEE",
	    "PANDA",
	    "PLOW",
	    "MILL",
	    "MONTANA",
	    "NEIGHBOR",
	    "STAND",
	    "PLATE",
	    "ANGLO",
	    "DATE",
	    "YARD",
	    "ZONE",
	    "MONK",
	    "DRAKE",
	    "BAZZARE",
	    "VICAR",
	    "MINT",
	    "KNAVE",
	    "KILT",
	    "TOLL",
	    "SPAWN",
	    "JEEP",
	    "POOL",
	    "FLOW",
	    "SET",
	    "CALENDAR",
	    "CHASER",
	    "GHOSTLY",
	    "GRAM",
	    "KNOB",
	    "POINT",
	    "WITCH",
	    "MOUTH",
	    "WALK",
	    "SPRITZ",
	    "FELONY",
	    "MOON",
	    "SUCKER",
	    "PENGUIN",
	    "WAFFLE",
	    "MAESTRO",
	    "TRINITY",
	    "SQUIRREL",
	    "FARM",
	    "NET",
	    "TRAWL",
	    "SPORK",
	    "ROUTE",
	    "BAGEL",
	    "ANALYST",
	    "SEAGULL",
	    "CHIPMUNK",
	    "ARTIST",
	    "SCAN",
	    "ENTOURAGE",
	    "GENESIS",
	    "SPATULA",
	    "MASTER"]

try:
	newwords1 = [x for x in words1 if x.startswith(str(sys.argv[1]))]
	print(random.choice(newwords1).upper()+random.choice(words2).upper())
except:
	print(random.choice(words1).upper()+random.choice(words2).upper())