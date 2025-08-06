from Classes.Packets.PiranhaMessage import PiranhaMessage

from Database.DatabaseHandler import DatabaseHandler

class TeamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(player.ID)

        self.writeVInt(fields['roomType'])
        self.writeBoolean(False)
        self.writeVInt(3)

        self.writeLong(0, player.roomID[1])
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
       
        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeDataReference(15,281)

        self.writeBoolean(False)

        self.writeVInt(2) # Players count
        
        self.writeBoolean(True) # king the room

        self.writeLong(player.ID[0], player.ID[1])

        self.writeDataReference(16, player.SelectedBrawlers[0])

        try:
            self.writeDataReference(29, playerData['SelectedSkins'][f'{player.SelectedBrawlers[0]}'])
        except:
            self.writeDataReference(29, 0)

        self.writeVInt(playerData["OwnedBrawlers"][f"{player.SelectedBrawlers[0]}"]["Trophies"]) # Brawler Trophies

        self.writeVInt(playerData["OwnedBrawlers"][f"{player.SelectedBrawlers[0]}"]["HighestTrophies"])

        self.writeVInt(playerData["OwnedBrawlers"][f"{player.SelectedBrawlers[0]}"]["PowerLevel"])

        self.writeVInt(0)

        self.writeVInt(3) # Player Status

        self.writeBoolean(False)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)


        # PlayerDisplayData::encode
        self.writeString(player.Name)
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(-1)  

        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeDataReference(0)

        self.writeVInt(0)

        self.writeBoolean(True) # king the room

        self.writeLong(0, 1)

        self.writeDataReference(16, player.SelectedBrawlers[0])

        try:
            self.writeDataReference(29, playerData['SelectedSkins'][f'{player.SelectedBrawlers[0]}'])
        except:
            self.writeDataReference(29, 0)

        self.writeVInt(playerData["OwnedBrawlers"][f"{player.SelectedBrawlers[0]}"]["Trophies"]) # Brawler Trophies

        self.writeVInt(playerData["OwnedBrawlers"][f"{player.SelectedBrawlers[0]}"]["HighestTrophies"])

        self.writeVInt(playerData["OwnedBrawlers"][f"{player.SelectedBrawlers[0]}"]["PowerLevel"])

        self.writeVInt(0)

        self.writeVInt(3) # Player Status

        self.writeBoolean(False)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)


        # PlayerDisplayData::encode
        self.writeString('БОТ')
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(-1)  

        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeDataReference(0)

        self.writeVInt(0)
        # PlayerDisplayData::encode


        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(1)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeBoolean(True)

        self.writeBoolean(False)

        self.writeBoolean(False)

        self.writeBoolean(False)

        self.writeVInt(1)

        self.writeVInt(1)

        self.writeVInt(1)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

    def decode(self):
        pass
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24124

    def getMessageVersion(self):
        return self.messageVersion
