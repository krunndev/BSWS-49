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
class LogicStarRoadClaimCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields['BrawlerID'] = calling_instance.readDataReference()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        cost = 0
        if fields['BrawlerID'][1] == 1: # Colt
            cost = 160
        elif fields['BrawlerID'][1] == 2: # Bull
            cost = 160
        elif fields['BrawlerID'][1] == 3: # Brock
            cost = 160
        elif fields['BrawlerID'][1] == 6: # Barley
            cost = 160
        elif fields['BrawlerID'][1] == 8: # Nita
            cost = 160
        elif fields['BrawlerID'][1] == 10: # El Primo
            cost = 160
        elif fields['BrawlerID'][1] == 13: # Poco
            cost = 160
        elif fields['BrawlerID'][1] == 24: # Rosa
            cost = 160
        elif fields['BrawlerID'][1] == 4: # Rico
            cost = 430
        elif fields['BrawlerID'][1] == 7: # jessie
            cost = 430
        elif fields['BrawlerID'][1] == 9: # DynaMike
            cost = 430
        elif fields['BrawlerID'][1] == 18: # Darryl
            cost = 430
        elif fields['BrawlerID'][1] == 19: # Penny
            cost = 430
        elif fields['BrawlerID'][1] == 25: # Carl
            cost = 430
        elif fields['BrawlerID'][1] == 22: # Tick
            cost = 430
        elif fields['BrawlerID'][1] == 27: # 8-Bit
            cost = 430
        elif fields['BrawlerID'][1] == 34:  # Jacky
            cost = 430
        elif fields['BrawlerID'][1] == 61:  # Gus
            cost = 430
        brawler_id = fields["BrawlerID"][1]
        card_id = OwnedBrawlersLatest.get(brawler_id, {}).get('CardID', 0)
        player_data["OwnedBrawlers"][fields["BrawlerID"][1]] = {'CardID': card_id, 'Skins': [0], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}
        player_data['RareTokens'] = player_data['RareTokens'] - cost

        # DataBase.ReplaceValue
        db_instance.updatePlayerData(player_data, calling_instance)
        # DataBase.ReplaceValue End

        fields["Socket"] = calling_instance.client
        fields["Command"] = {"ID": 225}
        fields["PlayerID"] = calling_instance.player.ID
        Messaging.sendMessage(24111, fields, cryptoInit)

    def getCommandType(self):
        return 562