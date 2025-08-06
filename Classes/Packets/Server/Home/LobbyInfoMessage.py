import datetime
import time
import random
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage

class LobbyInfoMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.startTime = datetime.datetime.now()

    def getPing(self):
        # Calculate the ping here (replace with your own logic)
        start_time = time.time()
        # Simulate some processing time
        time.sleep(0.1)
        end_time = time.time()
        ping = random.randint(50,90)  # Convert to milliseconds
        return ping

    def encode(self, fields, player):
        self.writeVInt(ClientsManager.GetCount())
        self.writeString(f"Willow Brawl\nPlayers online: {ClientsManager.GetCount()}\nServer Ping: {self.getPing()}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nKL Brawl Stage\n"f"Version: {player.ClientVersion}\nPing: {self.getPing()}")
        self.writeVInt(0)

    def decode(self):
        fields = {}
        fields["PlayerCount"] = self.readVInt()
        fields["Text"] = self.readString()
        fields["Unk1"] = self.readVInt()
        super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 23457

    def getMessageVersion(self):
        return self.messageVersion
