from Classes.Logic.LogicCommandManager import LogicCommandManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class SetSupportedCreatorResponseMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(1)
        self.writeString(fields["Code"])

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 28686

    def getMessageVersion(self):
        return self.messageVersion