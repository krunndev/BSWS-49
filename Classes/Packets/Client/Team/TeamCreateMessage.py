from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage

import random

class TeamCreateMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields['mapSlot'] = self.readVInt()
        fields['mapID'] = self.readVInt()
        fields['roomType'] = self.readVInt()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        calling_instance.player.roomID[1] = random.randint(0,1000)
        Messaging.sendMessage(24124, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 14350

    def getMessageVersion(self):
        return self.messageVersion