import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler


class LogicSetPlayerBattleCardCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["battleBrawler"] = calling_instance.readDataReference()
        fields["battleIcon"] = calling_instance.readDataReference()
        fields["battleIcon1"] = calling_instance.readVInt()
        fields["battleIconIndex"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])

        if fields['battleIcon'][0] == 52 and fields['battleBrawler'] == None:
            player_data['battlePin'] = fields['battleIcon'][1]
            db_instance.updatePlayerData(player_data, calling_instance)

        elif fields['battleIcon'][0] == 52 and fields['battleBrawler'][0] == 16:
            player_data['battlePinBrawler'] = fields['battleIcon'][1]
            db_instance.updatePlayerData(player_data, calling_instance)

        elif fields['battleIcon'][0] == 28 and fields['battleBrawler'] == None and fields["battleIconIndex"] == 0:
            player_data['battleIcon'] = fields['battleIcon'][1]
            db_instance.updatePlayerData(player_data, calling_instance)

        elif fields['battleIcon'][0] == 28 and fields['battleBrawler'] == None and fields["battleIconIndex"] == 1:
            player_data['battleIcon1'] = fields['battleIcon'][1]
            db_instance.updatePlayerData(player_data, calling_instance)

        elif fields['battleIcon'][0] == 28 and fields['battleBrawler'][0] == 16 and fields["battleIconIndex"] == 0:
            player_data['battleIconBrawler'] = fields['battleIcon'][1]
            db_instance.updatePlayerData(player_data, calling_instance)

        elif fields['battleIcon'][0] == 28 and fields['battleBrawler'][0] == 16 and fields["battleIconIndex"] == 1:
            player_data['battleIcon1Brawler'] = fields['battleIcon'][1]
            db_instance.updatePlayerData(player_data, calling_instance)

        elif fields['battleIcon'][0] == 76 and fields['battleBrawler'] == None:
            player_data['battleTitle'] = fields['battleIcon'][1]
            db_instance.updatePlayerData(player_data, calling_instance)

        elif fields['battleIcon'][0] == 76 and fields['battleBrawler'][0] == 16:
            player_data['battleTitleBrawler'] = {
                "brawlerID": fields['battleBrawler'][0],
                "titleID": fields['battleIcon'][1]
            }
            db_instance.updatePlayerData(player_data, calling_instance)

    def getCommandType(self):
        return 568