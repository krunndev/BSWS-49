import json
import random
import string
from Classes.Files.Classes.Cards import Cards
from Classes.Files.Classes.Characters import Characters

class Player:
    ClientVersion = "0.0.0"

    ID = [0, 1]
    AllianceID = [0, 0]
    Token = ""
    Name = "Игрок"
    Registered = False

    Vip = 0
    Thumbnail = 0
    Namecolor = 0
    Region = "RU"
    ContentCreator = ""
    Brawlers = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,36,37,40,42,43,45,47,48,50,52,58,61,63,64,67,69,71,73]
    UnlockingCardID = 4
    UsedPromoCodes = []

    Coins = 0
    CoinsGained = 0
    Gems = 0
    StarPoints = 0
    ChromaticTokens = 0
    RareTokens = 0
    ClubCoins = 0
    
    Trophies = 0
    HighestTrophies = 0
    TrophiesGained = 0

    TrophyRoadTier = 0
    BrawlPassLVL = [1]

    Experience = 0
    Level = 0
    Tokens = 0
    TokensGained = 0
    TokensDoubler = 0

    PushasedOffers = []
    
    delivery_items = {}
    
    BattleLogs = {}
    
    banned = False
    
    BPTokens = 0

    pl_rank = 1

    club_trophies = 0

    club_rank = 1

    club_tickets = 0

    vs = 0

    roomID = [0, 0]
    roomType = 0
    playerData = []

    brawlersID = Characters.getBrawlersID()

    favoriteBrawler = 0
    battleIcon = 0
    battleIcon1 = 0
    battlePin = 0
    battleTitle = 0

    threeXthreeWins = 0
    solowWins = 0
    duoWins = 0

    battleIconBrawler = {}
    for id in brawlersID:
        battleIconBrawler.update({f'{id}': 0})

    battleIcon1Brawler = {}
    for id in brawlersID:
        battleIcon1Brawler.update({f'{id}': 0})

    battlePinBrawler = {}
    for id in brawlersID:
        battlePinBrawler.update({f'{id}': 0})

    battleTitleBrawler = {}
    for id in brawlersID:
        battleTitleBrawler.update({f'{id}': 0})
    
    NotificationFactory = {}

    SelectedSkins = {}
    for id in brawlersID:
        SelectedSkins.update({f'{id}': 0})

    SelectedBrawlers = [0, 1, 8]
    RandomizerSelectedSkins = []
    OwnedPins = []
    OwnedThumbnails = []
    OwnedTitles = []
    SelectedBrawlersSkins = {
        0: 0,
	1: 0,
	8: 0,
    }
    OwnedBrawlers = {
        0: {'CardID': 0, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    }

    def __init__(self):
        pass

    def getDataTemplate(self, highid, lowid, token):
        if highid == 0 and lowid == 0:
            self.ID[0] = int(''.join([str(random.randint(0, 9)) for _ in range(1)]))
            self.ID[1] = int(''.join([str(random.randint(0, 9)) for _ in range(8)]))
            self.Token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40))
        else:
            self.ID[0] = highid
            self.ID[1] = lowid
            self.Token = token

        DBData = {
            'ID': self.ID,
            'Token': self.Token,
            'Name': self.Name,
            'AllianceID': self.AllianceID,
            'Registered': self.Registered,
            'Vip': self.Vip,
            'Thumbnail': self.Thumbnail,
            'Namecolor': self.Namecolor,
            'Region': self.Region,
            'ContentCreator': self.ContentCreator,
            'Brawlers': self.Brawlers,
            'UnlockingCardID': self.UnlockingCardID,
            'UsedPromoCodes': self.UsedPromoCodes,
            'Coins': self.Coins,
            'CoinsGained': self.CoinsGained,
            'Gems': self.Gems,
            'StarPoints': self.StarPoints,
            'ChromaticTokens': self.ChromaticTokens,
            'RareTokens': self.RareTokens,
            'ClubCoins': self.ClubCoins,
            'Trophies': self.Trophies,
            'HighestTrophies': self.HighestTrophies,
            'TrophiesGained': self.TrophiesGained,

            'TrophyRoadTier': self.TrophyRoadTier,
            'BrawlPassLVL': self.BrawlPassLVL,

            'Experience': self.Experience,
            'Level': self.Level,
            'Tokens': self.Tokens,
            'TokensGained': self.TokensGained,
            'TokensDoubler': self.TokensDoubler,
            'PushasedOffers': self.PushasedOffers,
            'delivery_items': self.delivery_items,
            'BattleLogs': self.BattleLogs,
            'banned': self.banned,
            'BPTokens': self.BPTokens,
            'pl_rank': self.pl_rank,
            'club_trophies': self.club_trophies,
            'club_rank': self.club_rank,
            'club_tickets': self.club_tickets,
            'favoriteBrawler': self.favoriteBrawler,
            'battleIcon': self.battleIcon,
            'battleIcon1': self.battleIcon1,
            'battlePin': self.battlePin,
            'battleTitle': self.battleTitle,
            'battleIconBrawler': self.battleIconBrawler,
            'battleIcon1Brawler': self.battleIcon1Brawler,
            'battlePinBrawler': self.battlePinBrawler,
            'battleTitleBrawler': self.battleTitleBrawler,
            'threeXthreeWins': self.threeXthreeWins,
            'soloWins': self.solowWins,
            'duoWins': self.duoWins,
            'roomID': self.roomID,
            'roomType': self.roomType,
            'playerData': self.playerData,
            'brawlersID': self.brawlersID,
            'vs': self.vs,
            'NotificationFactory': self.NotificationFactory,
            'SelectedSkins': self.SelectedSkins,
            'SelectedBrawlers': self.SelectedBrawlers,
            'OwnedPins': self.OwnedPins,
            'OwnedThumbnails': self.OwnedThumbnails,
            'OwnedTitles': self.OwnedTitles,
            'OwnedBrawlers': self.OwnedBrawlers
        }
        return DBData

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4))
