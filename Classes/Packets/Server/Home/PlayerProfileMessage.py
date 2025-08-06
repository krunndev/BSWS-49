from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.PlayerProfile import PlayerProfile
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
from Classes.Wrappers.AllianceHeaderEntry import AllianceHeaderEntry
import json

class PlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        db_instance = DatabaseHandler()
        clubdb_instance = ClubDatabaseHandler()
        playerData = db_instance.getPlayer(fields["PlayerID"])
        if playerData["AllianceID"] != [0, 0]:
             clubData = json.loads(clubdb_instance.getClubWithLowID(playerData["AllianceID"][1])[0][1])
        else:
             print('Not Club')
            
        self.writeVLong(fields['PlayerID'][0], fields['PlayerID'][1])
        PlayerProfile.encode(self, fields, playerData)
        if playerData["AllianceID"] != [0, 0]:
        	self.writeBoolean(True) # TODO: Club
        	AllianceHeaderEntry.encode(self, clubdb_instance, clubData)
        	self.writeDataReference(25, clubData["Members"][str(fields["PlayerID"][1])]["Role"])
        else:
        	self.writeBoolean(False) # TODO: Club
        	self.writeDataReference(0)


    def decode(self):
        pass
        # fields = {}
        # fields["PlayerCount"] = self.readVInt()
        # fields["Text"] = self.readString()
        # fields["Unk1"] = self.readVInt()
        # super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24113

    def getMessageVersion(self):
        return self.messageVersion