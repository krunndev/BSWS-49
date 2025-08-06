from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage

from Database.DatabaseHandler import DatabaseHandler
import json

class TeamChangeMemberSettingsMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields['csvID'] = self.readVInt()
        if fields['csvID'] == 23:
            fields['starpowerID'] = self.readVInt()
        else:
            fields['brawlerSkinID'] = self.readDataReference()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])

        fields["Socket"] = calling_instance.client
        fields['roomType'] = calling_instance.player.roomType
        calling_instance.player.SelectedSkins[0] = fields['brawlerSkinID'][1]
        calling_instance.player.SelectedBrawlers[0] = player_data["SelectedBrawlers"][0]
        for i in range(2):
            Messaging.sendMessage(24124, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 14350

    def getMessageVersion(self):
        return self.messageVersion
