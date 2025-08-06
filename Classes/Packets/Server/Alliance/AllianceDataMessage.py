from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.AllianceHeaderEntry import AllianceHeaderEntry
from Database.DatabaseHandler import ClubDatabaseHandler, DatabaseHandler
from Classes.ClientsManager import ClientsManager
import json

class AllianceDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        clubdb_instance = ClubDatabaseHandler()
        db_instance = DatabaseHandler()
        clubData = json.loads(clubdb_instance.getClubWithLowID(fields["AllianceID"][1])[0][1])
        db_instance.loadAccount(player, player.ID)
        allSockets = ClientsManager.GetAll()

        self.writeBoolean(False)
        
        AllianceHeaderEntry.encode(self, clubdb_instance, clubData)

        self.writeString(clubData["Description"])

        self.writeVInt(len(clubData["Members"]))

        for i in clubdb_instance.getMembersSorted(clubData):
            memberData = i[1]
            playerData = json.loads(db_instance.getPlayerEntry([memberData['HighID'], memberData['LowID']])[2])
            self.writeLong(memberData['HighID'], memberData['LowID'])
            self.writeVInt(memberData['Role']) # Role
            self.writeVInt(playerData['Trophies']) # Trophie
            
            if playerData["ID"][1] in allSockets:
                self.writeVInt(2) # Player State TODO: Members state
            else:
                self.writeVInt(0)
            self.writeVInt(6974) # State Timer

            self.writeVInt(0)

            self.writeBoolean(False) # DoNotDisturb TODO: Do not disturb sync

            self.writeString(playerData['Name']) # Player Name
            self.writeVInt(100)
            self.writeVInt(28000000 + playerData['Thumbnail']) # Player Thumbnail
            self.writeVInt(43000000 + playerData['Namecolor']) # Player Name Color
            self.writeVInt(46000000) # Color Gradients

            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeVInt(0)

            self.writeVInt(0)

        for i in range(0): # club league week number?
            self.writeVInt(0)
            self.writeVInt(3) # day
            self.writeVInt(18) # total club trophies earned
            self.writeVInt(0) # event day club trophies earned
            self.writeVInt(8) # total tickets used
            self.writeVInt(0) # event day tickets used
            self.writeVInt(6) # event day max tickets
            self.writeVInt(6) # event day tickets left
            self.writeVInt(0) # event day player ranking
            self.writeBoolean(True) # everyone have it to true

        self.writeVInt(0) # player experience lvl but why tf it doesn't show for some people

    def decode(self):
        fields = {}
        super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24301

    def getMessageVersion(self):
        return self.messageVersion