CHARACTER_ALIAS = {
    'akuma': ['aku', 'gouki', 'akumer'],
    'alisa': ['ali', 'als'],
    'anna': [],
    'armor_king': ['armorking', 'amk', 'ak'],
    'asuka': ['asu'],
    'bob': [],
    'bryan': ['bry'],
    'claudio': ['cld', 'cla'],
    'devil_jin': ['dj', 'deviljin', 'dvj'],
    'dragunov': ['drag', 'sergei', 'dragu'],
    'eddy': ['edd', 'ed'],
    'eliza': ['elz'],
    'feng': ['fen'],
    'geese': ['goose'],
    'gigas': ['ggs', 'gig', 'gigass'],
    'heihachi': ['hashi', 'hei', 'hessu'],
    'hwoarang': ['hwo'],
    'jack7': ['j7', 'jack-7', 'jack'],
    'jin': ['jim'],
    'josie': ['jos'],
    'julia': ['jul'],
    'katarina': ['kat'],
    'kazumi': ['kzm', 'zumi'],
    'kazuya': ['kaz', 'kazze', 'masku'],
    'king': ['kin'],
    'kuma': ['panda', 'karhu', 'bear'],
    'lars': ['lar'],
    'law': ['marshall'],
    'lee': ['violet'],
    'lei': [],
    'leo': [],
    'lili': ['lil'],
    'lidia': ['lid', 'lidl'],
    'lucky_chloe': ['lucky', 'luckychloe', 'lck', 'lc', 'chloe'],
    'marduk': ['mdk', 'mar', 'duk'],
    'master_raven': ['masterraven', 'mraven', 'maven', 'mrv', 'raven', 'mr'],
    'miguel': ['mig'],
    'negan': ['ngn', 'neg'],
    'nina': ['nin'],
    'noctis': ['noctu', 'noct', 'noc'],
    'paul': [],
    'shaheen': ['sha'],
    'steve': ['stv', 'ste', 'fox'],
    'yoshimitsu': ['yoshi', 'manji', 'yos'],
    'xiaoyu': ['xiao', 'ling'],
    'zafina': ['zaffy', 'zaf'],
    "fahkumram": ['fah', 'fahkum', 'fahk', 'fak'],
    "leroy": ['ler'],
    "ganryu": ['gan', 'ganny'],
    "kunimitsu": ['kun', 'kuni'],
    "generic": []
}

MOVE_TYPES = {
    "Rage Art": ["ra", "rage_art", "rageart", "rage art"],
    "Rage Drive": ["rd", "ragedrive", "rage_drive", "rage drive"],
    "Wall Bounce": ["wb", "wall_bounce", "wallbounce", "wall bounce"],
    "Screw": ["ts", "tail_spin", "tailspin", "screw", "s!", "s", "screws"],
    "Homing": ["homing", "homari"],
    "Power Crush": ["armor", "armori", "pc", "power", "power_crush", "powercrush", "power crush"],
    "Throw": ["throw", "grab", "throws", "grabs"]
}

SORT_ORDER = {"Rage Art": 0, "Rage Drive": 1, "Wall Bounce": 2, "Screw": 3, "Homing": 4, "Power Crush": 5,
              "Throw": 6}

REPLACE = {
    ' ': '',
    ',': '',
    '/': '',
    'd+': 'd',
    'f+': 'f',
    'u+': 'u',
    'b+': 'b',
    'n+': 'n',
    'ws+': 'ws',
    'fc+': 'fc',
    'cd+': 'cd',
    'wr+': 'wr',
    'ra+': 'ra',
    'rd+': 'rd',
    'ss+': 'ss',
    '(': '',
    ')': '',
    '*+': '*'
}


BLACKLIST = [""]

EMOJI_LIST = ['1\ufe0f\u20e3', '2\ufe0f\u20e3', '3\ufe0f\u20e3', '4\ufe0f\u20e3', '5\ufe0f\u20e3']
