from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler



class AllianceLeagueDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        
    def encode(self, fields, player):
        self.writeBoolean(True) # League Enabled

        League = True
        self.writeBoolean(League) # League Array
        if League:
        	# League Season
        	self.writeVInt(1) # Unk
        	self.writeVInt(432000) # Begin Countdown
        	self.writeVInt(0) # Timer
        	self.writeVInt(120) # League Tokens
        	self.writeVInt(3) # Event Days Maps
        	
        	# League Events
        	self.writeVInt(1) # Day
        	self.writeVInt(4) # Tickets
        	self.writeDataReference(15, 7)
        	self.writeVInt(1) # Array
        	self.writeVInt(1) # Unk
        	self.writeBoolean(True) # Unk
        	
        	self.writeVInt(2) # Day
        	self.writeVInt(4) # Tickets
        	self.writeDataReference(15, 25)
        	self.writeVInt(1) # Array
        	self.writeVInt(1) # Unk
        	self.writeBoolean(True) # Unk
        	
        	self.writeVInt(3) # Day
        	self.writeVInt(6) # Tickets
        	self.writeDataReference(15, 5)
        	self.writeVInt(1) # Array
        	self.writeVInt(1) # Unk
        	self.writeBoolean(True)

        LeagueData = True
        self.writeBoolean(LeagueData) # League Data Boolean
        
        if LeagueData:
        	# League Data
        	self.writeVLong(0, 1) # LeagueID
        	self.writeVInt(18) # Rank
        	self.writeVInt(0)
        	self.writeVInt(0)
        	self.writeVInt(0)
        	self.writeVLong(player.AllianceID[0], player.AllianceID[1]) # ClubID
        	self.writeVInt(3) # Day number
        	self.writeVInt(317) # Trophies
        	self.writeVInt(1) # Season Leaderboard Place
        	self.writeBoolean(True) # New Event
        	self.writeVInt(300) # Season score
        	self.writeVInt(1) # Season Place
        	self.writeVInt(19) # New Rank

        LeaguePlayerData = True
        self.writeBoolean(LeaguePlayerData) # Player League Data

        if LeaguePlayerData:
        	# Player League Data
        	self.writeVLong(0, 1)
        	self.writeVInt(0) # Unk
        	self.writeVInt(6) # Used normal tickets
        	self.writeVInt(0) # Max Golden Tickets
        	self.writeVInt(14) # Season used normal tickets
        	self.writeVInt(0) # Golden tickets
        	self.writeVInt(0) # Used golden tickets

        # Upcoming League Week
        self.writeBoolean(True) # LeagueArrray
        self.writeVInt(0) # Unk
        self.writeVInt(432000) # Begin Countdown
        self.writeVInt(999999) # Timer
        self.writeVInt(0) # League Tokens
        self.writeVInt(3) # Event Days Maps
        
        # Upcoming League Events
        self.writeVInt(1) # Day
        self.writeVInt(4) # Tickets
        self.writeDataReference(15, 7)
        self.writeVInt(1) # Array
        self.writeVInt(1) # Unk
        self.writeBoolean(True) # Unk
        
        self.writeVInt(2) # Day
        self.writeVInt(4) # Tickets
        self.writeDataReference(15, 25)
        self.writeVInt(1) # Array
        self.writeVInt(1) # Unk
        self.writeBoolean(True) # Unk
        
        self.writeVInt(3) # Day
        self.writeVInt(6) # Tickets
        self.writeDataReference(15, 5)
        self.writeVInt(1) # Array
        self.writeVInt(1) # Unk
        self.writeBoolean(True) # Unk

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 22161

    def getMessageVersion(self):
        return self.messageVersion