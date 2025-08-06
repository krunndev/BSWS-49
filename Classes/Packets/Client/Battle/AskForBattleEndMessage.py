from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage

from Database.DatabaseHandler import ClubDatabaseHandler, DatabaseHandler
from Classes.ClientsManager import ClientsManager
import json


class AskForBattleEndMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Unk1"] = self.readVInt()
        fields["Result"] = self.readVInt()
        fields["Rank"] = self.readVInt()
        fields["MapID"] = self.readDataReference()
        fields["HeroesCount"] = self.readVInt()
        fields["Heroes"] = []
        for i in range(fields["HeroesCount"]): fields["Heroes"].append({"Brawler": {"ID": self.readDataReference(), "SkinID": self.readDataReference()}, "Team": self.readVInt(), "IsPlayer": self.readBoolean(), "PlayerName": self.readString()})
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        clubdb_instance = ClubDatabaseHandler()
        db_instance = DatabaseHandler()
        if calling_instance.player.AllianceID != [0, 0]:
            clubData = json.loads(clubdb_instance.getClubWithLowID(calling_instance.player.AllianceID[1])[0][1])
        else:
            print('Not Club')
        playerData = db_instance.getPlayer(calling_instance.player.ID)
        for i in range(1):
        	for brawlerID,brawlerInfo in calling_instance.player.OwnedBrawlers.items():
                    if 0 <= brawlerInfo["Trophies"] <= 49:
                        mastery_val = 5
                        win_val = 9
                        lose_val = 0
                    elif 50 <= brawlerInfo["Trophies"] <= 99:
                        mastery_val = 10
                        win_val = 8
                        lose_val = -1
                    elif 100 <= brawlerInfo["Trophies"] <= 199:
                        mastery_val = 15
                        win_val = 8
                        lose_val = -2
                    elif 200 <= brawlerInfo["Trophies"] <= 299:
                        mastery_val = 20
                        win_val = 8
                        lose_val = -3
                    elif 300 <= brawlerInfo["Trophies"] <= 399:
                        mastery_val = 30
                        win_val = 8
                        lose_val = -4
                    elif 400 <= brawlerInfo["Trophies"] <= 499:
                        mastery_val = 40
                        win_val = 8
                        lose_val = -5
                    elif 500 <= brawlerInfo["Trophies"] <= 599:
                        mastery_val = 45
                        win_val = 8
                        lose_val = -6
                    elif 600 <= brawlerInfo["Trophies"] <= 699:
                        mastery_val = 50
                        win_val = 8
                        lose_val = -7
                    elif 700 <= brawlerInfo["Trophies"] <= 799:
                        mastery_val = 60
                        win_val = 8
                        lose_val = -8
                    elif 800 <= brawlerInfo["Trophies"] <= 899:
                        mastery_val = 65
                        win_val = 7
                        lose_val = -9
                    elif 900 <= brawlerInfo["Trophies"] <= 999:
                        mastery_val = 70
                        win_val = 6
                        lose_val = -10
                    elif 1000 <= brawlerInfo["Trophies"] <= 1099:
                        mastery_val = 75
                        win_val = 5
                        lose_val = -11
                    elif 1100 <= brawlerInfo["Trophies"] <= 1199:
                        mastery_val = 80
                        win_val = 4
                        lose_val = -12
                    elif 1199 <= brawlerInfo["Trophies"] <= 1200:
                        mastery_val = 85
                        win_val = 3
                        lose_val = -12
                        

        if fields['Rank'] == 0:
            if calling_instance.player.AllianceID != [0, 0]:
                clubData['Trophies'] =  clubData['Trophies'] + win_val
                print(clubData['Trophies'])
                clubdb_instance.updateClubData(clubData, calling_instance.player.AllianceID[1])
            else:
                print('You Not Club')

            playerData["Trophies"] = playerData["Trophies"] + win_val
            playerData["HighestTrophies"] = playerData["HighestTrophies"] + win_val
            playerData["RareTokens"] = playerData["RareTokens"] + 40
            brawler = calling_instance.player.SelectedBrawlers[0]
            playerData["OwnedBrawlers"][f"{brawler}"]["Trophies"] = playerData["OwnedBrawlers"][f"{brawler}"]["Trophies"] + win_val
            playerData["OwnedBrawlers"][f"{brawler}"]["MasteryPoints"] = playerData["OwnedBrawlers"][f"{brawler}"]["MasteryPoints"] + mastery_val
            playerData["OwnedBrawlers"][f"{brawler}"]["HighestTrophies"] = playerData["OwnedBrawlers"][f"{brawler}"]["HighestTrophies"] + win_val
            db_instance.updatePlayerData(playerData, calling_instance)
        else:
            if calling_instance.player.AllianceID != [0, 0]:
                clubData['Trophies'] =  clubData['Trophies'] - lose_val
                print(clubData['Trophies'])
                clubdb_instance.updateClubData(clubData, calling_instance.player.AllianceID[1])
            else:
                print('You Not Club')
            playerData["Trophies"] = playerData["Trophies"] - lose_val
            playerData["HighestTrophies"] = playerData["HighestTrophies"] - lose_val
            brawler = calling_instance.player.SelectedBrawlers[0]
            playerData["OwnedBrawlers"][f"{brawler}"]["Trophies"] = playerData["OwnedBrawlers"][f"{brawler}"]["Trophies"] - lose_val
            playerData["OwnedBrawlers"][f"{brawler}"]["HighestTrophies"] = playerData["OwnedBrawlers"][f"{brawler}"]["HighestTrophies"] - lose_val
            db_instance.updatePlayerData(playerData, calling_instance)
        Messaging.sendMessage(23456, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 14110

    def getMessageVersion(self):
        return self.messageVersion
