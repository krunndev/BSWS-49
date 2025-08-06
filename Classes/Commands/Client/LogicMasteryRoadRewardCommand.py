import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler
BrawlerMasteryThumbnail = {
    0: 91,    # Shelly → player_icon_shelly1
    1: 96,    # Colt → player_icon_colt1
    2: 97,    # Bull → player_icon_bull1
    3: 98,    # Brock → player_icon_brock1
    4: 123,   # Rico → player_icon_rico1
    5: 206,   # Spike → player_icon_spike1
    6: 117,   # Barley → player_icon_barley1
    7: 93,    # Jessie → player_icon_jessie1
    8: 92,    # Nita → player_icon_nita1
    9: 95,    # Dynamike → player_icon_dynamike1
    10: 116,  # El Primo → player_icon_primo1
    11: 207,  # Mortis → player_icon_mortis1
    12: 205,  # Crow → player_icon_crow1
    13: 119,  # Poco → player_icon_poco1
    14: 99,   # Bo → player_icon_bo1
    15: 196,  # Piper → player_icon_piper1
    16: 195,  # Pam → player_icon_pam1
    17: 200,  # Tara → player_icon_tara1
    18: 120,  # Darryl → player_icon_darryl1
    19: 121,  # Penny → player_icon_penny1
    20: 191,  # Frank → player_icon_frank1
    21: 198,  # Gene → player_icon_gene1
    22: 89,   # Tick → player_icon_tick1
    23: 203,  # Leon → player_icon_leon1
    24: 118,  # Rosa → player_icon_rosa1
    25: 122,  # Carl → player_icon_carl1
    26: 189,  # Bibi → player_icon_bibi1
    27: 100,  # 8-Bit → player_icon_8bit1
    28: 212,  # Sandy → player_icon_sandy1
    29: 188,  # Bea → player_icon_bea1
    30: 94,   # EMZ → player_icon_emz1
    31: 199,  # Mr. P → player_icon_mrp1
    32: 202,  # Max → player_icon_max1
    34: 124,  # Jacky → player_icon_jacky1
    35: 209,  # Gale → player_icon_gale1
    36: 194,  # Nani → player_icon_nani1
    37: 213,  # Sprout → player_icon_sprout1
    38: 211,  # Surge → player_icon_surge1
    39: 210,  # Colette → player_icon_colette1
    40: 208,  # Amber → player_icon_amber1
    41: 241,  # Lou → player_icon_lou1
    42: 197,  # Byron → player_icon_byron1
    43: 187,  # Edgar → player_icon_edgar1
    44: 214,  # Ruffs → player_icon_ruffs1
    45: 90,   # Stu → player_icon_stu1
    46: 215,  # Belle → player_icon_belle1
    47: 201,  # Squeak → player_icon_squeak1
    48: 193,  # Grom → player_icon_grom1
    49: 231,  # Buzz → player_icon_buzz1
    50: 192,  # Griff → player_icon_griff1
    51: 232,  # Ash → player_icon_ash1
    52: 204,  # Meg → player_icon_meg1
    53: 239,  # Lola → player_icon_lola1
    54: 233,  # Fang → player_icon_fang1
    56: 238,  # Eve → player_icon_eve1
    57: 217,  # Janet → player_icon_janet1
    58: 190,  # Bonnie → player_icon_bonnie1
    59: 216,  # Otis → player_icon_otis1
    60: 240,  # Sam → player_icon_sam1
    61: 234,  # Gus → player_icon_gus1
    62: 243,  # Buster → player_icon_buster1
    63: 237,  # Chester → player_icon_chester1
    64: 230,  # Gray → player_icon_gray1
    65: 244,  # Mandy → player_icon_mandy1
    66: 245,  # Artie → player_icon_artie
    67: 246,  # Willow → player_icon_willow
    68: 265   # Maisie → player_icon_maisie
}

BrawlerMasteryTitle = {
    0: 0,    # Shelly
    1: 1,     # Colt
    2: 2,     # Bull
    3: 3,     # Brock
    4: 4,    # Rico
    5: 5,    # Spike
    6: 6,     # Barley
    7: 7,    # Jessie
    8: 8,    # Nita
    9: 9,     # Dynamike
    10: 10,   # Elprimo
    11: 11,   # Mortis
    12: 12,    # Crow
    13: 13,   # Poco
    14: 14,    # Bo
    15: 15,   # Piper
    16: 16,   # Pam
    17: 17,   # Tara
    18: 18,    # Darryl
    19: 19,   # Penny
    20: 20,   # Frank
    21: 21,   # Gene
    22: 22,   # Tick
    23: 23,   # Leon
    24: 24,   # Rosa
    25: 25,    # Carl
    26: 26,    # Bibi
    27: 27,    # 8bit
    28: 28,   # Sandy
    29: 29,    # Bea
    30: 30,   # Emz
    31: 31,   # Mr.p
    32: 32,   # Max
    34: 33,  # Jacky
    35: 34,   # Gale
    36: 35,   # Nani
    37: 36,   # Sprout
    38: 37,   # Surge
    39: 38,    # Colette
    40: 39,    # Amber
    41: 40,   # Lou
    42: 41,    # Byron
    43: 42,    # Edgar
    44: 43,   # Ruffs
    45: 44,   # Stu
    46: 45,   # Belle
    47: 46,  # Squeak
    48: 47,  # Grom
    49: 48,    # Buzz
    50: 49,   # Griff
    51: 50,    # Ash
    52: 51,   # Meg
    53: 52,   # Lolla
    54: 53,   # Fang
    56: 54,   # Eve
    57: 55,   # Janet
    58: 56,    # Bonnie
    59: 57,   # Otis
    60: 58,    # Sam
    61: 59,   # Gus
    62: 60,   # Buster
    63: 61,    # Chester
    64: 62,   # Gray
    65: 63,   # Mandy
    66: 64,   # Artie
    67: 65,   # Willow
    68: 66,   # Maisie
    69: 67
}

BrawlerMasteryPin = {
    0: 1032,    # Shelly
    1: 994,     # Colt
    2: 987,     # Bull
    3: 985,     # Brock
    4: 1028,    # Rico
    5: 1033,    # Spike
    6: 979,     # Barley
    7: 1011,    # Jessie
    8: 1021,    # Nita
    9: 997,     # Dynamike
    10: 1027,   # Elprimo
    11: 1018,   # Mortis
    12: 995,    # Crow
    13: 1026,   # Poco
    14: 983,    # Bo
    15: 1025,   # Piper
    16: 1023,   # Pam
    17: 1038,   # Tara
    18: 996,    # Darryl
    19: 1024,   # Penny
    20: 1002,   # Frank
    21: 1004,   # Gene
    22: 1039,   # Tick
    23: 1012,   # Leon
    24: 1029,   # Rosa
    25: 991,    # Carl
    26: 982,    # Bibi
    27: 976,    # 8bit
    28: 1031,   # Sandy
    29: 980,    # Bea
    30: 999,   # Emz
    31: 1019,   # Mr.p
    32: 1016,   # Max
    34: 1009,  # Jacky
    35: 1003,   # Gale
    36: 1020,   # Nani
    37: 1034,   # Sprout
    38: 1037,   # Surge
    39: 993,    # Colette
    40: 977,    # Amber
    41: 1014,   # Lou
    42: 989,    # Byron
    43: 999,    # Edgar
    44: 1030,   # Ruffs
    45: 1036,   # Stu
    46: 981,   # Belle
    47: 1035,  # Squeak
    48: 1007,  # Grom
    49: 988,    # Buzz
    50: 1006,   # Griff
    51: 978,    # Ash
    52: 1017,   # Meg
    53: 1013,   # Lolla
    54: 1001,   # Fang
    56: 1000,   # Eve
    57: 1010,   # Janet
    58: 984,    # Bonnie
    59: 1022,   # Otis
    60: 986,    # Sam
    61: 1008,   # Gus
    62: 990,   # Buster
    63: 992,    # Chester
    64: 1005,   # Gray
    65: 1015,   # Mandy
    66: 1072,   # Artie
    67: 1082,   # Willow
    68: 1120   # Maisie
}

OwnedBrawlersLatest = {
        0: {'CardID': 0, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        1: {'CardID': 4, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        2: {'CardID': 8, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        3: {'CardID': 12, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        4: {'CardID': 16, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        5: {'CardID': 20, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        6: {'CardID': 24, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        7: {'CardID': 28, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        8: {'CardID': 32, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        9: {'CardID': 36, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        10: {'CardID': 40, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        11: {'CardID': 44, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        12: {'CardID': 48, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        13: {'CardID': 52, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        14: {'CardID': 56, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        15: {'CardID': 60, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        16: {'CardID': 64, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        17: {'CardID': 68, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        18: {'CardID': 72, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        19: {'CardID': 95, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        20: {'CardID': 100, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        21: {'CardID': 105, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        22: {'CardID': 110, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        23: {'CardID': 115, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        24: {'CardID': 120, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        25: {'CardID': 125, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        26: {'CardID': 130, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        27: {'CardID': 177, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        28: {'CardID': 182, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        29: {'CardID': 188, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        30: {'CardID': 194, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        31: {'CardID': 200, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        32: {'CardID': 206, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        34: {'CardID': 218, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        35: {'CardID': 224, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        36: {'CardID': 230, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        37: {'CardID': 236, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        38: {'CardID': 279, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        39: {'CardID': 296, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        40: {'CardID': 303, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        41: {'CardID': 320, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        42: {'CardID': 327, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        43: {'CardID': 334, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        44: {'CardID': 341, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        45: {'CardID': 358, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        46: {'CardID': 365, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        47: {'CardID': 372, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        48: {'CardID': 379, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        49: {'CardID': 386, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        50: {'CardID': 393, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        51: {'CardID': 410, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        52: {'CardID': 417, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        53: {'CardID': 427, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        54: {'CardID': 434, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        56: {'CardID': 448, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        57: {'CardID': 466, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        58: {'CardID': 474, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        59: {'CardID': 491, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        60: {'CardID': 499, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        61: {'CardID': 507, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        62: {'CardID': 515, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        63: {'CardID': 523, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        64: {'CardID': 531, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        65: {'CardID': 539, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        
        66: {'CardID': 547, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        67: {'CardID': 557, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
}

class LogicMasteryRoadRewardCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["BrawleIndex"] = calling_instance.readDataReference()
        fields["MasteryIndex"] = calling_instance.readVInt()
        fields["unk3"] = calling_instance.readDataReference()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        fields["Socket"] = calling_instance.client
        
        # cardID for brawlerID and cost for brawlerID
        cardID = 0
        cost = 0
        # cardID for brawlerID and cost for brawlerID End
        
        brawler = fields["BrawleIndex"][1]
        player_data["OwnedBrawlers"][f"{brawler}"]["MasteryClaimed"] = player_data["OwnedBrawlers"][f"{brawler}"]["MasteryClaimed"] + 1
        player_data["delivery_items"] = {
            'Boxes': []
        }
        box = {
            'Type': 0,
            'Items': []
        }
        # редкие, сверхредкие, эпики
        if fields["BrawleIndex"][1] in [8, 2, 1, 3, 6, 10, 13, 24, 7, 9, 22, 27, 4, 18, 19, 20, 25, 34, 61, 14, 15, 16, 26, 29, 30, 36, 43, 45, 48, 50, 58]:
            if fields["MasteryIndex"] == 2: # 750 coins
                item = {'Amount': 750, 'DataRef': [0, 0], 'RewardID': 7}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
                player_data['Coins'] = player_data['Coins'] + 750
            
            elif fields["MasteryIndex"] == 3: # 100 power points
                item = {'Amount': 100, 'DataRef': [16, 0], 'RewardID': 24}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
            
            elif fields["MasteryIndex"] == 4: # Credits
                item = {'Amount': 75, 'DataRef': [16, 0], 'RewardID': 22}
                box['Items'].append(item)
                box['Type'] = 100
                player_data['RareTokens'] += player_data['RareTokens'] + 75
                player_data["delivery_items"]['Boxes'].append(box)
            
            elif fields["MasteryIndex"] == 5: # 200 power points
                item = {'Amount': 200, 'DataRef': [16, fields["BrawleIndex"][1]], 'RewardID': 24}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
            
            elif fields["MasteryIndex"] == 6: # 1250 coins
                item = {'Amount': 1250, 'DataRef': [0, 0], 'RewardID': 7}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
                player_data['Coins'] = player_data['Coins'] + 1250
            
            elif fields["MasteryIndex"] == 7: # Credits
                item = {'Amount': 150, 'DataRef': [16, fields["BrawleIndex"][1]], 'RewardID': 22}
                box['Items'].append(item)
                box['Type'] = 100
                player_data['RareTokens'] += player_data['RareTokens'] + 150
                player_data["delivery_items"]['Boxes'].append(box)
                
            elif fields["MasteryIndex"] == 8: #Pin
                brawler_id = fields["BrawleIndex"][1]
                pin_id = BrawlerMasteryPin.get(brawler_id)
                item = {'Amount': 1, 'DataRef': [52, pin_id],  'RewardID': 11}
                player_data["OwnedPins"].append(pin_id)
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
                
            elif fields["MasteryIndex"] == 9: #Thumbnail
                brawler_id = fields["BrawleIndex"][1]
                thumb_id = BrawlerMasteryThumbnail.get(brawler_id)
                player_data["OwnedThumbnails"].append(thumb_id)
                item = {'Amount': 1, 'DataRef': [28, thumb_id], 'RewardID': 11}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
                
            elif fields["MasteryIndex"] == 10: #Title
                brawler_id = fields["BrawleIndex"][1]
                title_id = BrawlerMasteryTitle.get(brawler_id)
                item = {'Amount': 1, 'DataRef': [71, title_id], 'RewardID': 10}
                player_data["OwnedTitles"].append(title_id)
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
                
                # мифики и леги
        elif fields['BrawleIndex'][1] in [5, 12, 23, 28, 40, 52, 63, 11, 17, 21, 31, 32, 37, 42, 47, 64, 67]:
            if fields["MasteryIndex"] == 2: # 1000 coins
                item = {'Amount': 1000, 'DataRef': [0, 0], 'RewardID': 7}
                player_data['Coins'] += player_data['Coins'] + 100
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
            
            elif fields["MasteryIndex"] == 3: # 100 power points
                item = {'Amount': 150, 'DataRef': [16, fields["BrawleIndex"][1]], 'RewardID': 24}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
            
            elif fields["MasteryIndex"] == 4: # Credits
                item = {'Amount': 100, 'DataRef': [16, 0], 'RewardID': 7}
                box['Items'].append(item)
                box['Type'] = 100
                player_data['Coins'] += player_data['Coins'] + 100
                player_data["delivery_items"]['Boxes'].append(box)
            
            elif fields["MasteryIndex"] == 5: # 300 power points
                item = {'Amount': 300, 'DataRef': [16, 0], 'RewardID': 24}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)

            elif fields["MasteryIndex"] == 6: # 2000 coins
                item = {'Amount': 2000, 'DataRef': [0, 0], 'RewardID': 7}
                box['Items'].append(item)
                box['Type'] = 100
                player_data['Coins'] += player_data['Coins'] + 2000
                player_data["delivery_items"]['Boxes'].append(box)
                
            elif fields["MasteryIndex"] == 7: # 100 credits
                item = {'Amount': 100, 'DataRef': [0, 0], 'RewardID': 7}
                box['Items'].append(item)
                box['Type'] = 100
                player_data['Coins'] += player_data['Coins'] + 2000
                player_data["delivery_items"]['Boxes'].append(box)
                
            elif fields["MasteryIndex"] == 8: #Pin
                brawler_id = fields["BrawleIndex"][1]
                pin_id = BrawlerMasteryPin.get(brawler_id)
                item = {'Amount': 1, 'DataRef': [52, pin_id],  'RewardID': 11}
                player_data["OwnedPins"].append(pin_id)
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
                
            elif fields["MasteryIndex"] == 9: #Thumbnail
                brawler_id = fields["BrawleIndex"][1]
                thumb_id = BrawlerMasteryThumbnail.get(brawler_id)
                player_data["OwnedThumbnails"].append(thumb_id)
                item = {'Amount': 1, 'DataRef': [28, thumb_id], 'RewardID': 11}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
                
            elif fields["MasteryIndex"] == 10: #Title
                brawler_id = fields["BrawleIndex"][1]
                title_id = BrawlerMasteryTitle.get(brawler_id)
                item = {'Amount': 1, 'DataRef': [71, title_id], 'RewardID': 10}
                player_data["OwnedTitles"].append(title_id)
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)

        # хромики
        elif fields['BrawleIndex'][1] in [35, 38, 39, 41, 44, 46, 49, 51, 53, 54, 56, 57, 59, 60, 62, 65, 66, 68]:
            if fields["MasteryIndex"] == 2: # 1000 coins
                item = {'Amount': 1000, 'DataRef': [0, 0], 'RewardID': 7}
                player_data['Coins'] += player_data['Coins'] + 100
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
            
            elif fields["MasteryIndex"] == 3: # 100 power points
                item = {'Amount': 150, 'DataRef': [16, fields["BrawleIndex"][1]], 'RewardID': 24}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
            
            elif fields["MasteryIndex"] == 4: # Credits
                item = {'Amount': 100, 'DataRef': [16, 0], 'RewardID': 7}
                box['Items'].append(item)
                box['Type'] = 100
                player_data['Coins'] += player_data['Coins'] + 100
                player_data["delivery_items"]['Boxes'].append(box)
            
            elif fields["MasteryIndex"] == 5: # 300 power points
                item = {'Amount': 300, 'DataRef': [16, 0], 'RewardID': 24}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)

            elif fields["MasteryIndex"] == 6: # 2000 coins
                item = {'Amount': 2000, 'DataRef': [0, 0], 'RewardID': 7}
                box['Items'].append(item)
                box['Type'] = 100
                player_data['Coins'] += player_data['Coins'] + 2000
                player_data["delivery_items"]['Boxes'].append(box)
                
            elif fields["MasteryIndex"] == 7: # 100 credits
                item = {'Amount': 100, 'DataRef': [0, 0], 'RewardID': 7}
                box['Items'].append(item)
                box['Type'] = 100
                player_data['Coins'] += player_data['Coins'] + 2000
                player_data["delivery_items"]['Boxes'].append(box)
                
            elif fields["MasteryIndex"] == 8: #Pin
                brawler_id = fields["BrawleIndex"][1]
                pin_id = BrawlerMasteryPin.get(brawler_id)
                item = {'Amount': 1, 'DataRef': [52, pin_id],  'RewardID': 11}
                player_data["OwnedPins"].append(pin_id)
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
                
            elif fields["MasteryIndex"] == 9: #Thumbnail
                brawler_id = fields["BrawleIndex"][1]
                thumb_id = BrawlerMasteryThumbnail.get(brawler_id)
                player_data["OwnedThumbnails"].append(thumb_id)
                item = {'Amount': 1, 'DataRef': [28, thumb_id], 'RewardID': 11}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
                
            elif fields["MasteryIndex"] == 10: #Title
                brawler_id = fields["BrawleIndex"][1]
                title_id = BrawlerMasteryTitle.get(brawler_id)
                item = {'Amount': 1, 'DataRef': [71, title_id], 'RewardID': 10}
                player_data["OwnedTitles"].append(title_id)
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)

        # DataBase.ReplaceValue
        db_instance.updatePlayerData(player_data, calling_instance)
        # DataBase.ReplaceValue End
        
        # Delivery Send
        fields["Command"] = {"ID": 203}
        fields["PlayerID"] = calling_instance.player.ID
        Messaging.sendMessage(24111, fields, cryptoInit)
        # Delivery Send End

    def getCommandType(self):
        return 569