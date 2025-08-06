from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage

from Database.DatabaseHandler import DatabaseHandler
import json
import Configuration

class SetSupportedCreatorMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Code"] = self.readString()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        fields["Socket"] = calling_instance.client
        if fields["Code"] in Configuration.settings["WillowCreators"]:
        	fields["Socket"] = calling_instance.client
        	fields["Command"] = {"ID": 215}
        	fields["PlayerID"] = calling_instance.player.ID
        	calling_instance.player.ContentCreator = fields["Code"]
        	player_data["ContentCreator"] = fields["Code"]
        	db_instance.updatePlayerData(player_data, calling_instance)
        	Messaging.sendMessage(24111, fields, cryptoInit)
        	print("Code Using!")
        else:
        	Messaging.sendMessage(28686, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 18686

    def getMessageVersion(self):
        return self.messageVersion