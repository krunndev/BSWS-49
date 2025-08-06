import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

class LogicClaimRankUpRewardCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeVInt(0)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["RewardID"] = calling_instance.readVInt()
        fields['RewardType'] = calling_instance.readVInt()
        fields['BrawlPassSeason'] = calling_instance.readVInt()
        fields['LVL'] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        if fields['RewardID'] == 6: # Trophy Road
            if fields['LVL'] == 0:
                player_data["delivery_items"] = {
                'Boxes': []
                }
                box = {
                'Type': 0,
                'Items': []
                }
                item = {'Amount': 25, 'DataRef': [0, 0], 'RewardID': 24}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)

                db_instance.updatePlayerData(player_data, calling_instance)
            if fields['LVL'] == 1:
                player_data["delivery_items"] = {
                'Boxes': []
                }
                box = {
                'Type': 0,
                'Items': []
                }
                item = {'Amount': 160, 'DataRef': [0, 0], 'RewardID': 22}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)
                player_data['RareTokens'] = player_data['RareTokens'] + 160

                db_instance.updatePlayerData(player_data, calling_instance)
        if fields['RewardID'] == 9:
            if fields['LVL'] == 0:
                player_data["delivery_items"] = {
                'Boxes': []
                }
                box = {
                'Type': 0,
                'Items': []
                }
                item = {'Amount': 2750, 'DataRef': [0, 0], 'RewardID': 25}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)

                db_instance.updatePlayerData(player_data, calling_instance)

            if fields['LVL'] == 1:
                player_data["delivery_items"] = {
                'Boxes': []
                }
                box = {
                'Type': 0,
                'Items': []
                }
                item = {'Amount': 160, 'DataRef': [0, 0], 'RewardID': 25}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)

            if fields['LVL'] == 2:
                player_data["delivery_items"] = {
                'Boxes': []
                }
                box = {
                'Type': 0,
                'Items': []
                }
                item = {'Amount': 45, 'DataRef': [0, 0], 'RewardID': 22}
                box['Items'].append(item)
                box['Type'] = 100
                player_data["delivery_items"]['Boxes'].append(box)

        fields["Socket"] = calling_instance.client
        fields["Command"] = {"ID": 203}
        fields["PlayerID"] = calling_instance.player.ID
        Messaging.sendMessage(24111, fields, cryptoInit)

    def getCommandType(self):
        return 517
