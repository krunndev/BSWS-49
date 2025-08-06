import json
from Classes.Commands.LogicCommand import LogicCommand
from Database.DatabaseHandler import DatabaseHandler
from Classes.Files.Classes.Cards import Cards
from Classes.Messaging import Messaging

class LogicStarrRoadNextUnlockCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        calling_instance.readVInt()
        fields["UnlockedBrawler"] = calling_instance.readVInt()
        print(fields["UnlockedBrawler"])
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        
        #player_data["UnlockingCardID"].append(Cards().get_unlock_by_brawler_id(fields["UnlockedBrawler"]))
        #print("New Cards ID: ", player_data["UnlockingCardID"])
        
        
        if fields["UnlockedBrawler"] == 1:
           # player_data["UnlockingCardID"].append(4)
            player_data["UnlockingCardID"] = 4
            player_data["UnlockingBrawler"] = 2
            player_data["Brawlers"].remove(2)
        if fields["UnlockedBrawler"] == 2:
            player_data["UnlockingCardID"] = 8
            player_data["UnlockingBrawler"] = 3
            player_data["Brawlers"].remove(3)
        if fields["UnlockedBrawler"] == 3:
            player_data["UnlockingCardID"] = 12
            player_data["UnlockingBrawler"] = 4
            player_data["Brawlers"].remove(4)
        if fields["UnlockedBrawler"] == 4:
            player_data["UnlockingCardID"] = 16
            player_data["UnlockingBrawler"] = 5
            player_data["Brawlers"].remove(5)
        if fields["UnlockedBrawler"] == 5:
            player_data["UnlockingCardID"] = 20
            player_data["UnlockingBrawler"] = 6
            player_data["Brawlers"].remove(6)
        if fields["UnlockedBrawler"] == 6:
            player_data["UnlockingCardID"] = 24
            player_data["UnlockingBrawler"] = 7
            player_data["Brawlers"].remove(7)
        if fields["UnlockedBrawler"] == 7:
            player_data["UnlockingCardID"] = 28
            player_data["UnlockingBrawler"] = 8
            player_data["Brawlers"].remove(8)
        if fields["UnlockedBrawler"] == 8:
            player_data["UnlockingCardID"] = 32
            player_data["UnlockingBrawler"] = 9
            player_data["Brawlers"].remove(9)
        if fields["UnlockedBrawler"] == 9:
            player_data["UnlockingCardID"] = 36
            player_data["UnlockingBrawler"] = 10
            player_data["Brawlers"].remove(10)
        if fields["UnlockedBrawler"] == 10:
            player_data["UnlockingCardID"] = 40
            player_data["UnlockingBrawler"] = 11
            player_data["Brawlers"].remove(11)
        if fields["UnlockedBrawler"] == 11:
            player_data["UnlockingCardID"] = 44
            player_data["UnlockingBrawler"] = 12
            player_data["Brawlers"].remove(12)
        if fields["UnlockedBrawler"] == 12:
            player_data["UnlockingCardID"] = 48
            player_data["UnlockingBrawler"] = 13
            player_data["Brawlers"].remove(13)
        if fields["UnlockedBrawler"] == 13:
            player_data["UnlockingCardID"] = 52
            player_data["UnlockingBrawler"] = 14
            player_data["Brawlers"].remove(14)
        if fields["UnlockedBrawler"] == 14:
            player_data["UnlockingCardID"] = 56
            player_data["UnlockingBrawler"] = 15
            player_data["Brawlers"].remove(15)
        if fields["UnlockedBrawler"] == 15:
            player_data["UnlockingCardID"] = 60
            player_data["UnlockingBrawler"] = 16
            player_data["Brawlers"].remove(16)
        if fields["UnlockedBrawler"] == 16:
            player_data["UnlockingCardID"] = 64
            player_data["UnlockingBrawler"] = 17
            player_data["Brawlers"].remove(17)
        if fields["UnlockedBrawler"] == 17:
            player_data["UnlockingCardID"] = 68
            player_data["UnlockingBrawler"] = 18
            player_data["Brawlers"].remove(18)
        if fields["UnlockedBrawler"] == 18:
            player_data["UnlockingCardID"] = 72
            player_data["UnlockingBrawler"] = 19
            player_data["Brawlers"].remove(19)
        if fields["UnlockedBrawler"] == 19:
            player_data["UnlockingCardID"] = 95
            player_data["UnlockingBrawler"] = 20
            player_data["Brawlers"].remove(20)
        if fields["UnlockedBrawler"] == 20:
            player_data["UnlockingCardID"] = 100
            player_data["UnlockingBrawler"] = 21
            player_data["Brawlers"].remove(21)
        if fields["UnlockedBrawler"] == 21:
            player_data["UnlockingCardID"] = 105
            player_data["UnlockingBrawler"] = 22
            player_data["Brawlers"].remove(22)
        if fields["UnlockedBrawler"] == 22:
            player_data["UnlockingCardID"] = 110
            player_data["UnlockingBrawler"] = 23
            player_data["Brawlers"].remove(23)
        if fields["UnlockedBrawler"] == 23:
            player_data["UnlockingCardID"] = 115
            player_data["UnlockingBrawler"] = 24
            player_data["Brawlers"].remove(24)
        if fields["UnlockedBrawler"] == 24:
            player_data["UnlockingCardID"] = 120
            player_data["UnlockingBrawler"] = 25
            player_data["Brawlers"].remove(25)
        if fields["UnlockedBrawler"] == 25:
            player_data["UnlockingCardID"] = 125
            player_data["UnlockingBrawler"] = 26
            player_data["Brawlers"].remove(26)
        if fields["UnlockedBrawler"] == 26:
            player_data["UnlockingCardID"] = 130
            player_data["UnlockingBrawler"] = 27
            player_data["Brawlers"].remove(27)
        if fields["UnlockedBrawler"] == 27:
            player_data["UnlockingCardID"] = 177
            player_data["UnlockingBrawler"] = 28
            player_data["Brawlers"].remove(28)
        if fields["UnlockedBrawler"] == 28:
            player_data["UnlockingCardID"] = 182
            player_data["UnlockingBrawler"] = 29
            player_data["Brawlers"].remove(29)
        if fields["UnlockedBrawler"] == 29:
            player_data["UnlockingCardID"] = 188
            player_data["UnlockingBrawler"] = 30
            player_data["Brawlers"].remove(30)
        if fields["UnlockedBrawler"] == 30:
            player_data["UnlockingCardID"] = 194
            player_data["UnlockingBrawler"] = 31
            player_data["Brawlers"].remove(31)
        if fields["UnlockedBrawler"] == 31:
            player_data["UnlockingCardID"] = 200
            player_data["UnlockingBrawler"] = 32
            player_data["Brawlers"].remove(32)
        if fields["UnlockedBrawler"] == 32:
            player_data["UnlockingCardID"] = 206
            player_data["UnlockingBrawler"] = 34
            player_data["Brawlers"].remove(34)
        if fields["UnlockedBrawler"] == 34:
            player_data["UnlockingCardID"] = 218
            player_data["UnlockingBrawler"] = 36
            player_data["Brawlers"].remove(36)
        if fields["UnlockedBrawler"] == 36:
            player_data["UnlockingCardID"] = 230
            player_data["UnlockingBrawler"] = 37
            player_data["Brawlers"].remove(37)
        if fields["UnlockedBrawler"] == 37:
            player_data["UnlockingCardID"] = 236
            player_data["UnlockingBrawler"] = 40
            player_data["Brawlers"].remove(40)
        if fields["UnlockedBrawler"] == 40:
            player_data["UnlockingCardID"] = 303
            player_data["UnlockingBrawler"] = 42
            player_data["Brawlers"].remove(42)
        if fields["UnlockedBrawler"] == 42:
            player_data["UnlockingCardID"] = 327
            player_data["UnlockingBrawler"] = 43
            player_data["Brawlers"].remove(43)
        if fields["UnlockedBrawler"] == 43:
            player_data["UnlockingCardID"] = 334
            player_data["UnlockingBrawler"] = 45
            player_data["Brawlers"].remove(45)
        if fields["UnlockedBrawler"] == 45:
            player_data["UnlockingCardID"] = 358
            player_data["UnlockingBrawler"] = 47
            player_data["Brawlers"].remove(47)
        if fields["UnlockedBrawler"] == 47:
            player_data["UnlockingCardID"] = 372
            player_data["UnlockingBrawler"] = 48
            player_data["Brawlers"].remove(48)
        if fields["UnlockedBrawler"] == 48:
            player_data["UnlockingCardID"] = 379
            player_data["UnlockingBrawler"] = 50
            player_data["Brawlers"].remove(50)
        if fields["UnlockedBrawler"] == 50:
            player_data["UnlockingCardID"] = 393
            player_data["UnlockingBrawler"] = 52
            player_data["Brawlers"].remove(52)
        if fields["UnlockedBrawler"] == 52:
            player_data["UnlockingCardID"] = 417
            player_data["UnlockingBrawler"] = 58
            player_data["Brawlers"].remove(58)
        if fields["UnlockedBrawler"] == 58:
            player_data["UnlockingCardID"] = 474
            player_data["UnlockingBrawler"] = 61
            player_data["Brawlers"].remove(61)
        if fields["UnlockedBrawler"] == 61:
            player_data["UnlockingCardID"] = 605
            player_data["UnlockingBrawler"] = 63
            player_data["Brawlers"].remove(63)
        if fields["UnlockedBrawler"] == 63:
            player_data["UnlockingCardID"] = 523
            player_data["UnlockingBrawler"] = 64
            player_data["Brawlers"].remove(64)
        if fields["UnlockedBrawler"] == 64:
            player_data["UnlockingCardID"] = 531
            player_data["UnlockingBrawler"] = 67
            player_data["Brawlers"].remove(67)
        if fields["UnlockedBrawler"] == 67:
            player_data["UnlockingCardID"] = 557
            player_data["UnlockingBrawler"] = 69
            player_data["Brawlers"].remove(69)
        if fields["UnlockedBrawler"] == 69:
            player_data["UnlockingCardID"] = 573
            player_data["UnlockingBrawler"] = 71
            player_data["Brawlers"].remove(71)
        if fields["UnlockedBrawler"] == 71:
            player_data["UnlockingCardID"] = 589
            player_data["UnlockingBrawler"] = 73
            player_data["Brawlers"].remove(73)
        if fields["UnlockedBrawler"] == 73:
            player_data["UnlockingCardID"] = 605
            player_data["CompleteStarr"] = 1
        cardID = player_data["UnlockingCardID"]
            
        rare = [1, 2, 3, 6, 8, 10, 13, 24]
        super_rare = [4, 7, 9, 18, 19, 22, 25, 27, 34, 61]
        epic = [14, 15, 16, 20, 26, 29, 30, 36, 43, 45, 48, 50, 58, 69]
        mythic = [11, 17, 21, 35, 31, 32, 37, 42, 47, 64, 67, 71]
        legendary = [5, 12, 23, 28, 40, 52, 63]
        
        ja = fields["UnlockedBrawler"]
        
        if ja in rare:
            player_data["CollectedCredits"] = player_data["CollectedCredits"] - 160
        if ja in super_rare:
            player_data["CollectedCredits"] = player_data["CollectedCredits"] - 430
        if ja in epic:
            player_data["CollectedCredits"] = player_data["CollectedCredits"] - 925
        if ja in mythic:
            player_data["CollectedCredits"] = player_data["CollectedCredits"] - 1900
        if ja in legendary:
            player_data["CollectedCredits"] = player_data["CollectedCredits"] - 3800
        player_data["OwnedBrawlers"][ja] = {'CardID': cardID, 'Skins': [0], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}
            
        
        
        db_instance.updatePlayerData(player_data, calling_instance)
        fields["Socket"] = calling_instance.client
        fields["Command"] = {"ID": 227}
        fields["PlayerID"] = calling_instance.player.ID
        Messaging.sendMessage(24111, fields, cryptoInit)

    def getCommandType(self):
        return 562