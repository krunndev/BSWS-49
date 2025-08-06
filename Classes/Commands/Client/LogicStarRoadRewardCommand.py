import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

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

class LogicStarRoadRewardCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["BrawleIndex"] = calling_instance.readDataReference()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        fields["Socket"] = calling_instance.client
        
        # cardID for brawlerID and cost for brawlerID
        cardID = 0
        cost = 0
        gemscost = 0

        ### Редкие (Rare) - 29 gems
        if fields["BrawleIndex"][1] == 1:    # Colt
            cardID = 4
            cost = 160
            gemscost = 29
        elif fields["BrawleIndex"][1] == 2:  # Bull
            cardID = 8
            cost = 160
            gemscost = 29
        elif fields["BrawleIndex"][1] == 3:  # Brock
            cardID = 12
            cost = 160
            gemscost = 29
        elif fields["BrawleIndex"][1] == 6:  # Barley
            cardID = 24
            cost = 160
            gemscost = 29
        elif fields["BrawleIndex"][1] == 8:  # Nita
            cardID = 32
            cost = 160
            gemscost = 29
        elif fields["BrawleIndex"][1] == 10: # El Primo
            cardID = 40
            cost = 160
            gemscost = 29
        elif fields["BrawleIndex"][1] == 13: # Poco
            cardID = 52
            cost = 160
            gemscost = 29
        elif fields["BrawleIndex"][1] == 24: # Rosa
            cardID = 120
            cost = 160
            gemscost = 29

        ### Супер-редкие (Super Rare) - 79 gems
        elif fields["BrawleIndex"][1] == 4:  # Rico
            cardID = 16
            cost = 430
            gemscost = 79
        elif fields["BrawleIndex"][1] == 7:  # Jessie
            cardID = 28
            cost = 430
            gemscost = 79
        elif fields["BrawleIndex"][1] == 9:  # Dynamike
            cardID = 36
            cost = 430
            gemscost = 79
        elif fields["BrawleIndex"][1] == 18: # Darryl
            cardID = 72
            cost = 430
            gemscost = 79
        elif fields["BrawleIndex"][1] == 19: # Penny
            cardID = 95
            cost = 430
            gemscost = 79
        elif fields["BrawleIndex"][1] == 20: # Frank
            cardID = 100
            cost = 430
            gemscost = 79
        elif fields["BrawleIndex"][1] == 22: # Tick
            cardID = 110
            cost = 430
            gemscost = 79
        elif fields["BrawleIndex"][1] == 25: # Carl
            cardID = 125
            cost = 430
            gemscost = 79
        elif fields["BrawleIndex"][1] == 27: # 8-Bit
            cardID = 177
            cost = 430
            gemscost = 79
        elif fields["BrawleIndex"][1] == 34: # Jacky
            cardID = 218
            cost = 430
            gemscost = 79
        elif fields["BrawleIndex"][1] == 61: # Gus
            cardID = 507
            cost = 430
            gemscost = 79

        ### Эпические (Epic) - 169 gems
        elif fields["BrawleIndex"][1] == 14: # Bo
            cardID = 56
            cost = 800
            gemscost = 169
        elif fields["BrawleIndex"][1] == 15: # Piper
            cardID = 60
            cost = 800
            gemscost = 169
        elif fields["BrawleIndex"][1] == 16: # Pam
            cardID = 64
            cost = 800
            gemscost = 169
        elif fields["BrawleIndex"][1] == 26: # Bibi
            cardID = 130
            cost = 800
            gemscost = 169
        elif fields["BrawleIndex"][1] == 29: # Bea
            cardID = 188
            cost = 800
            gemscost = 169
        elif fields["BrawleIndex"][1] == 30: # Emz
            cardID = 194
            cost = 800
            gemscost = 169
        elif fields["BrawleIndex"][1] == 36: # Nani
            cardID = 230
            cost = 800
            gemscost = 169
        elif fields["BrawleIndex"][1] == 43: # Edgar
            cardID = 334
            cost = 800
            gemscost = 169
        elif fields["BrawleIndex"][1] == 45: # Stu
            cardID = 358
            cost = 800
            gemscost = 169
        elif fields["BrawleIndex"][1] == 48: # Grom
            cardID = 379
            cost = 800
            gemscost = 169
        elif fields["BrawleIndex"][1] == 50: # Griff
            cardID = 393
            cost = 800
            gemscost = 169
        elif fields["BrawleIndex"][1] == 58: # Bonnie
            cardID = 474
            cost = 800
            gemscost = 169

        ### Мифические (Mythic) - 349 gems
        elif fields["BrawleIndex"][1] == 11: # Mortis
            cardID = 44
            cost = 1250
            gemscost = 349
        elif fields["BrawleIndex"][1] == 17: # Tara
            cardID = 68
            cost = 1250
            gemscost = 349
        elif fields["BrawleIndex"][1] == 21: # Gene
            cardID = 105
            cost = 1250
            gemscost = 349
        elif fields["BrawleIndex"][1] == 31: # Mr.P
            cardID = 200
            cost = 1250
            gemscost = 349
        elif fields["BrawleIndex"][1] == 32: # Max
            cardID = 206
            cost = 1250
            gemscost = 349
        elif fields["BrawleIndex"][1] == 37: # Sprout
            cardID = 236
            cost = 1250
            gemscost = 349
        elif fields["BrawleIndex"][1] == 42: # Byron
            cardID = 327
            cost = 1250
            gemscost = 349
        elif fields["BrawleIndex"][1] == 47: # Squeak
            cardID = 372
            cost = 1250
            gemscost = 349
        elif fields["BrawleIndex"][1] == 64: # Gray
            cardID = 531
            cost = 1250
            gemscost = 349
        elif fields["BrawleIndex"][1] == 67: # Willow
            cardID = 557
            cost = 1250
            gemscost = 349

        ### Легендарные (Legendary) - 699 gems
        elif fields["BrawleIndex"][1] == 5:  # Spike
            cardID = 20
            cost = 2500
            gemscost = 699
        elif fields["BrawleIndex"][1] == 12: # Crow
            cardID = 48
            cost = 2500
            gemscost = 699
        elif fields["BrawleIndex"][1] == 23: # Leon
            cardID = 115
            cost = 2500
            gemscost = 699
        elif fields["BrawleIndex"][1] == 28: # Sandy
            cardID = 182
            cost = 2500
            gemscost = 699
        elif fields["BrawleIndex"][1] == 40: # Amber
            cardID = 303
            cost = 2500
            gemscost = 699
        elif fields["BrawleIndex"][1] == 52: # Meg
            cardID = 417
            cost = 2500
            gemscost = 699
        elif fields["BrawleIndex"][1] == 63: # Chester
            cardID = 523
            cost = 2500
            gemscost = 699
     # # # Хроматические (Chromatic) - 169 gems
        elif fields["BrawleIndex"][1] == 35:
        	cardID = 224 # Gale
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 38:
        	cardID = 279 # Surge
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 39:
        	cardID = 296 # Colette
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 41:
        	cardID = 320 # Lou
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 44:
        	cardID = 341 # Ruffs
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 46:
        	cardID = 365 # Belle
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 49:
        	cardID = 386 # Buzz
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 51:
        	cardID = 410 # Ash
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 53:
        	cardID = 427 # Lolla
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 54:
        	cardID = 434 # Fang
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 56:
        	cardID = 448 # Eve
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 57:
        	cardID = 466 # Janet
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 59:
        	cardID = 491 # Otis
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 60:
        	cardID = 499 # Sam
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 62:
        	cardID = 515 # Buster
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 65:
        	cardID = 539 # Mandy
        	gemscost = 169
        elif fields["BrawleIndex"][1] == 66:
        	cardID = 547 # RT
        	gemscost = 349

        # cardID for brawlerID and cost for brawlerID End
        player_data["OwnedBrawlers"][fields["BrawleIndex"][1]] = {'CardID': cardID, 'Skins': [0], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 25000, 'MasteryClaimed': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}
        player_data["Gems"] = player_data["Gems"] - gemscost
        player_data["delivery_items"] = {
        'Boxes': []
         }
        box = {
        'Type': 0,
        'Items': []
        }
        item = {'Amount': 1, 'DataRef': [16, fields["BrawleIndex"][1]], 'RewardID': 1}
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
        return 560