from Classes.ByteStreamHelper import ByteStreamHelper
from Classes.Packets.PiranhaMessage import PiranhaMessage

import json
import Configuration
import datetime
from Database.DatabaseHandler import DatabaseHandler

from Static.StaticData import StaticData


class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(player.ID)[2])
        ownedBrawlersCount = len(player.OwnedBrawlers)
        ownedPinsCount = len(player.OwnedPins)
        ownedThumbnailCount = len(player.OwnedThumbnails)
        ownedTitlesCount = len(player.OwnedTitles)
        ownedSkins = []
        
        for brawlerInfo in player.OwnedBrawlers.values():
            try:
                ownedSkins.extend(brawlerInfo["Skins"])
            except KeyError:
                continue

        self.writeVInt(-1433793731) #timestamp
        self.writeVInt(2023064)#timestamp
        self.writeVInt(52685)#timestamp LogicDailyDataBegin
        self.writeVInt(52685) #timestamp

        self.writeVInt(player.Trophies) # Trophies

        self.writeVInt(player.HighestTrophies + 1000) # Highest Trophies
        self.writeVInt(player.HighestTrophies + 1000) # Highest Trophies

        self.writeVInt(player.TrophyRoadTier) # collected trophy road rewards

        self.writeVInt(503026) # exp points

        self.writeDataReference(28, player.Thumbnail)
        self.writeDataReference(43, player.Namecolor)

        self.writeVInt(26) # played Game Mode
        for x in range(26):
            self.writeVInt(x)

        self.writeVInt(len(player.SelectedSkins)) # Selected Skins
        for brawler_id in player.SelectedSkins:
            self.writeDataReference(29, player.SelectedSkins[brawler_id])

        self.writeVInt(0) # available ramdon skins

        self.writeVInt(0) # random skins

        self.writeVInt(len(ownedSkins))
        for skinID in ownedSkins:
            self.writeDataReference(29, skinID)

        self.writeVInt(0) # skin purchase option

        self.writeVInt(0) # unk skin array5

        self.writeVInt(0) # leaderboard region
        self.writeVInt(player.HighestTrophies) # highest trophies
        self.writeVInt(0) # tokens used in battle
        self.writeVInt(2) # control mode

        self.writeBoolean(True) # battle hints
        self.writeVInt(0) # token doubler left
        self.writeVInt(52684) # trophy league timer
        self.writeVInt(722284) # power play timer
        self.writeVInt(56284) # Brawl pass season timer

        self.writeVInt(0) # 
        self.writeVInt(0) # 
        self.writeVInt(0) # drop chance of characters in boxes
        # self.writeVInt(93)
        # self.writeVInt(206)
        # self.writeVInt(456)
        # self.writeVInt(1001)
        # self.writeVInt(2264)

        self.writeBoolean(True) # false, false, true
        self.writeVInt(2) # token doubler  new tag state
        self.writeVInt(2) # event tickets new tag state
        self.writeVInt(2) # coins pack new tag state
        self.writeVInt(0) # name change cost
        self.writeVInt(0) # timer for next name change

        # Shop Array Start
        ShopData = StaticData.ShopData
        
        self.writeVInt(1 + len(ShopData["Offers"]))  # Offers count
        
        self.writeVInt(2)  # RewardCount
        for i in range(1):
            self.writeVInt(1) # ItemType
            self.writeVInt(250)
            self.writeDataReference(16, 3) # CsvID
            self.writeVInt(1032)
        for i in range(1):
            self.writeVInt(45) # ItemType
            self.writeVInt(500)
            self.writeDataReference(16, 3) # CsvID
            self.writeVInt(1032)


        self.writeVInt(0)
        self.writeVInt(19) # Cost
        self.writeVInt(5184000) #Time
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) #Claim
        self.writeVInt(0) #???
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(49)
        self.writeInt(0)
        self.writeString("ОСОБАЯ АКЦИЯ") #Title
        self.writeBoolean(False)
        self.writeString("offer_mecha") #theme
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeDataReference(0)
        self.writeDataReference(1) #panel layout
        self.writeBoolean(False)
        self.writeBoolean(True)
        self.writeVInt(0)
        self.writeVInt(0) # new vint v49
        self.writeVInt(19) # new vint v49
        

        for i in ShopData["Offers"]:
            def checkAvailability():
                results = []
                result = False
                for reward in i["Rewards"]:
                    if reward["ItemType"] == 4:
                        if any(reward["Extra"] in b["Skins"] for b in player.OwnedBrawlers.values()):
                            if len(i["Rewards"]) > 1:
                                results.append(True)
                            else:
                                result = True
                        if str(reward["BrawlerID"][1]) not in list(player.OwnedBrawlers.keys()):
                            midresult = False
                            for x in i["Rewards"]:
                                if x["ItemType"] == 3:
                                    midresult = True
                            if midresult != True:
                                if len(i["Rewards"]) > 1:
                                    results.append(True)
                                else:
                                    result = True
                    if reward["ItemType"] == 3 or reward["ItemType"] == 30:
                        if str(reward["BrawlerID"][1]) in list(player.OwnedBrawlers.keys()):
                            if len(i["Rewards"]) > 1:
                                results.append(True)
                            else:
                                result = True
                    if reward["ItemType"] == 19:
                        if reward["Extra"] in player.OwnedPins:
                            if len(i["Rewards"]) > 1:
                                results.append(True)
                            else:
                                result = True
                    if reward["ItemType"] == 25:
                        if reward["Extra"] in player.OwnedThumbnails:
                            if len(i["Rewards"]) > 1:
                                results.append(True)
                            else:
                                result = True
                    if i["Rewards"].index(reward) == len(i["Rewards"]) - 1:
                        if True in results:
                            result = True
                return result

            self.writeVInt(len(i["Rewards"]))  # RewardCount
            for reward in i["Rewards"]:
                self.writeVInt(reward["ItemType"])  # ItemType
                self.writeVInt(reward["Amount"])
                if reward["BrawlerID"][0] != 0:
                    self.writeDataReference(reward["BrawlerID"][0], reward["BrawlerID"][1])  # CsvID
                else:
                    self.writeDataReference(0)
                self.writeVInt(reward["Extra"])

            self.writeVInt(i["Currency"])  # Currency(0-Gems, 1-Gold, 3-StarpoInts)
            self.writeVInt(i["Cost"]) # Cost
            self.writeVInt(i["Time"]) #Time
            self.writeVInt(0)
            self.writeVInt(0)
            if ShopData["Offers"].index(i) in player.PushasedOffers or checkAvailability() == True:
            	self.writeBoolean(True) # Claim
            else:
            	self.writeBoolean(i['Claim']) # Claim
            self.writeVInt(0)  # Offer Index
            self.writeVInt(0)
            self.writeBoolean(i["DailyOffer"])  # Daily Offer ne work pohodu
            self.writeVInt(i["OldPrice"])  # Old price
            self.writeInt(0)
            self.writeString(i["Text"]) #Title
            self.writeBoolean(False)
            self.writeString(i["Background"]) #theme
            self.writeVInt(-1)
            self.writeBoolean(i["Processed"])
            self.writeVInt(i["TypeBenefit"])  # Type Benefit
            self.writeVInt(i["Benefit"])  # Benefit
            self.writeString()
            self.writeBoolean(i["OneTimeOffer"])  # One time offer
            self.writeBoolean(False)  # Claimed
            if i["BigOffer"] == True:
                if i["ShopPanelLayouts"] != -1:
                    self.writeDataReference(69, i["ShopPanelLayouts"]) # For Big Offers
                else:
                    self.writeDataReference(0, 0) # For Big Offers
                if i["ShopStyleSets"] != -1:
                    self.writeDataReference(70, i["ShopStyleSets"]) # For Big Offers
                else:
                    self.writeDataReference(0, 0) # For Big Offers
            else:
                self.writeDataReference(0, 0) # For Big Offers
                self.writeDataReference(0, 0) # For Big Offers              
            self.writeBoolean(False)
            self.writeBoolean(True)
            self.writeVInt(0)
            self.writeVInt(0) # new vint v49
            self.writeVInt(i["Cost"]) # Cost
        
        self.writeVInt(200) # tokens for battle
        self.writeVInt(0) # timer until new token

        self.writeVInt(0) #count

        self.writeVInt(1) #unk
        self.writeVInt(30) #unk

        self.writeByte(1) # count brawlers selected
        self.writeDataReference(16, player.SelectedBrawlers[0]) # selected brawler

        self.writeString(player.Region) # location
        self.writeString(player.ContentCreator) # supported creator

        self.writeVInt(0) # resources gained
        self.writeVInt(0) # count 0

        
        BrawlPassLVLP = 0
        BrawlPassLVL = 0
        
        lvl = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        lvl2 = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]
        lvl3 = [62, 63, 64, 65, 66, 67, 68, 69, 70]

        for lvlID in player.BrawlPassLVL:
            print(lvlID)
            for lvlID in range(lvlID):
                byte = 4
                intByte = byte * 2
                byte += intByte
                print(byte)
                BrawlPassLVL += byte

        # BrawlPassSeasonData::encode
        self.writeVInt(1) # count brawl pass seasons
        for season in range(1):
            self.writeVInt(17) # season
            self.writeVInt(0) # season token collected
            self.writeVInt(player.Vip) # Brawl Pass (0 - not buy, 1 - buy)
            self.writeVInt(-1)
            self.writeBoolean(False) # 0x0

            # LogicBitList::encode
            self.writeBoolean(True) # Brawl Pass Premium
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(2)
            # LogicBitList:encode End

            # LogicBitList::encode
            self.writeBoolean(True) # Brawl Pass Default
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(2)
            # LogicBitList::encode End
        # BrawlPassSeasonData::encode End

        self.writeVInt(0)

        self.writeBoolean(True) # 0x1
        self.writeVInt(0)
        self.writeVInt(153826)
        self.writeVInt(2)
        self.writeVInt(0) # club league quest count

        self.writeBoolean(True)
        self.writeVInt(ownedPinsCount + ownedThumbnailCount + ownedTitlesCount)  # Vanity Count
        for i in player.OwnedPins:
            self.writeDataReference(52, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        for i in player.OwnedThumbnails:
            self.writeDataReference(28, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)
                
        for i in player.OwnedTitles:
            self.writeDataReference(76, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)


        self.writeBoolean(False) # Power league season data

        self.writeInt(0)
        self.writeVInt(502052)
        
        self.writeDataReference(16, player.favoriteBrawler) # Favorite Brawler

        self.writeBoolean(False) # Logic Daily Data end

        self.writeVInt(2023070) # Logic Conf Data begin

        self.writeVInt(33) # event slot id
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(3)
        self.writeVInt(4)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12)
        self.writeVInt(13)
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(18)
        self.writeVInt(19)
        self.writeVInt(20)
        self.writeVInt(21)
        self.writeVInt(22)
        self.writeVInt(23)
        self.writeVInt(24)
        self.writeVInt(25)
        self.writeVInt(26)
        self.writeVInt(27)
        self.writeVInt(28)
        self.writeVInt(29)
        self.writeVInt(30)
        self.writeVInt(31)
        self.writeVInt(32)
        self.writeVInt(33)

        self.writeVInt(3) # event count

        self.writeVInt(1) # Index
        self.writeVInt(1) # Index
        self.writeVInt(0)
        self.writeVInt(72292)
        self.writeVInt(0)
        self.writeDataReference(15, 7) # map id
        self.writeVInt(-1)
        self.writeVInt(2)
        self.writeString("")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # MapMaker map structure array
        self.writeVInt(0)
        self.writeBoolean(False) # Power League array entry
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        
        self.writeVInt(1) # Index
        self.writeVInt(2) # Index
        self.writeVInt(0)
        self.writeVInt(72292)
        self.writeVInt(0)
        self.writeDataReference(15, 59) # map id
        self.writeVInt(-1)
        self.writeVInt(2)
        self.writeString("")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # MapMaker map structure array
        self.writeVInt(0)
        self.writeBoolean(False) # Power League array entry
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        
        self.writeVInt(1) # Index
        self.writeVInt(3) # Index
        self.writeVInt(0)
        self.writeVInt(72292)
        self.writeVInt(0)
        self.writeDataReference(15, 40) # map id
        self.writeVInt(-1)
        self.writeVInt(2)
        self.writeString("")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # MapMaker map structure array
        self.writeVInt(0)
        self.writeBoolean(False) # Power League array entry
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)


        self.writeVInt(0) # upcoming event count
       
        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800]) # Brawler Upgrade Cost
        ByteStreamHelper.encodeIntList(self, [20, 50, 140, 280]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [150, 400, 1200, 2600]) # Shop Coins Amount

        self.writeVInt(1)  # Locked Brawler
        for i in range(1):
         self.writeDataReference(16, 69)
         self.writeInt(max(0, int((datetime.datetime(*Configuration.settings["HankTimer"]) - datetime.datetime.now()).total_seconds()))) #таймер
         self.writeInt(3500)
         self.writeInt(3400)
         self.writeBoolean(True)

        self.writeVInt(1)
        self.writeInt(1)
        self.writeInt(41000060) #themeid


        self.writeVInt(0) # Timed int entry count
        # self.writeVInt(31)
        # self.writeVInt(1)
        # self.writeVInt(499427)
        # self.writeVInt(758627)
        # self.writeVInt(29)
        # self.writeVInt(24)
        # self.writeVInt(0)
        # self.writeVInt(413027)
        self.writeVInt(0) # custom event

        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(-1)
        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(4)

        ByteStreamHelper.encodeIntList(self, [0, 29, 79, 169, 349, 699]) # brawler cost gems ?
        ByteStreamHelper.encodeIntList(self, [0, 160, 450, 500, 1500, 4500]) # what is that ? looks like chroma price of chromatic brawlers but it doesn't go under 500

        self.writeLong(player.ID[0], player.ID[1]) # Player ID

        self.writeVInt(2) # Notification factory
        
        self.writeVInt(81)
        self.writeInt(228) #Notification ID
        self.writeBoolean(False)
        self.writeInt(0)
        self.writeString("Добро пожаловать в Willow Brawl!\nПока что это только первый нотиф, в будущем доделаю логику и тут уже можно будет выдавать скины!")
        self.writeVInt(1)
        self.writeVInt(1)
        
        self.writeVInt(81)
        self.writeInt(228) #Notification ID
        self.writeBoolean(False)
        self.writeInt(0)
        self.writeString("Сохраните данные своей учетной записи! Например, сделайте скриншот\n"f"Ваше Имя: " + str(player.Name) + "\n"f"Ваш Account ID: " + str(player.ID) + "\n"f"Ваш регион: " + str(player.Region) + "\n"f"Эти данные нужны для переноса учетной записи на новое устройство, а также для приобретения внутриигровой валюты""\n"f"НИКОМУ кроме администрации не предоставляйте эти данные!!!")
        self.writeVInt(1)
        self.writeVInt(1)
        
        self.writeVInt(-1)
        self.writeBoolean(False) # 0x0
        self.writeVInt(0) # gatcha drop
        self.writeVInt(0) 
        self.writeVInt(0)

        # Calendar Array
        self.writeBoolean(False)
        for i in range(0):
            self.writeVInt(-1)
            self.writeVInt(2)
            self.writeVInt(0)
            self.writeVInt(1)
            self.writeVInt(4)
            self.writeVInt(1)
            self.writeDataReference(0)
            self.writeVInt(29)
            self.writeBoolean(False)     
            self.writeVInt(1)
            self.writeVInt(2)
            self.writeVInt(3)
            self.writeVInt(0)
            self.writeDataReference(16,18)
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeVInt(3)
            self.writeVInt(0)
            self.writeDataReference(16,19)
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeVInt(2)
            self.writeVInt(0)
            self.writeVInt(1)
            self.writeVInt(2)
            self.writeVInt(1)
            self.writeVInt(4)
            self.writeVInt(0)
            self.writeDataReference(16,18)
            self.writeVInt(52)
            self.writeBoolean(False)
            self.writeVInt(1)
            self.writeVInt(1)
            self.writeVInt(2)
            self.writeVInt(1)
            self.writeVInt(4)
            self.writeVInt(0)
            self.writeDataReference(16,18)
            self.writeVInt(52)
            self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(3600) # TIme
            self.writeVInt(0) 
            self.writeVInt(0)
            self.writeVInt(2)
        # Calendar Array End

        # new function v46
        self.writeVInt(0) # new function v46

        # StarRoad
        

        brawlerID = 0
        rareBrawlers = [8, 2, 1, 3, 6, 10, 13, 24]
        superRareBrawlers = [7, 9, 22, 27, 4, 18, 19, 20, 25, 34, 61]
        epicBrawlers = [14, 15, 16, 26, 29, 30, 36, 43, 45, 48, 50, 58]
        mythicBrawlers = [11, 17, 21, 31, 32, 37, 42, 47, 64, 67]
        legendaryBrawlers = [5, 12, 23, 28, 40, 52, 63]
        newRareBrawlers = []
        newSuperRareBrawlers = []
        newEpicBrawlers = []
        newMythicBrawlers = []
        newLegendaryBrawlers = []
        unlockingBrawlers = []
        newRareBrawlers = rareBrawlers.copy()
        newSuperRareBrawlers = superRareBrawlers.copy()
        newEpicBrawlers = epicBrawlers.copy()
        newMythicBrawlers = mythicBrawlers.copy()
        newLegendaryBrawlers = legendaryBrawlers.copy()
        
        for brawlerID in rareBrawlers:
             try:
                 if brawlerID not in player.OwnedBrawlers[str(brawlerID)]:
                     newRareBrawlers.remove(brawlerID)
             except:
                 if brawlerID not in player.OwnedBrawlers:
                     pass
                     

             #if brawlerID in rareBrawlers and player.OwnedBrawlers:
             #        newRareBrawlers.remove(brawlerID)
             #    else:
             #        print(f"Element {brawlerID} is not in newRareBrawlers")


        for brawlerID in superRareBrawlers:
             try:
                 if brawlerID not in player.OwnedBrawlers[str(brawlerID)]:
                     newSuperRareBrawlers.remove(brawlerID)
             except:
                 if brawlerID not in player.OwnedBrawlers:
                     pass
                     
        for brawlerID in epicBrawlers:
             try:
                 if brawlerID not in player.OwnedBrawlers[str(brawlerID)]:
                     newEpicBrawlers.remove(brawlerID)
             except:
                 if brawlerID not in player.OwnedBrawlers:
                     pass
                            
        for brawlerID in mythicBrawlers:
             try:
                 if brawlerID not in player.OwnedBrawlers[str(brawlerID)]:
                     newMythicBrawlers.remove(brawlerID)
             except:
                 if brawlerID not in player.OwnedBrawlers:
                     pass
                            
        for brawlerID in legendaryBrawlers:
             try:
                 if brawlerID not in player.OwnedBrawlers[str(brawlerID)]:
                     newLegendaryBrawlers.remove(brawlerID)
             except:
                 if brawlerID not in player.OwnedBrawlers:
                     pass

        allBrawlers = newRareBrawlers + newSuperRareBrawlers + newEpicBrawlers + newMythicBrawlers + newLegendaryBrawlers

        try:
        	if newRareBrawlers and newRareBrawlers != [0, 0]:
        		unlockingBrawlers.append(newRareBrawlers[0])
        		newRareBrawlers.remove(newRareBrawlers[0])
        		cost = 160
        		costGems = 29
        	elif newSuperRareBrawlers and newSuperRareBrawlers != [0, 0]:
        		unlockingBrawlers.append(newSuperRareBrawlers[0])
        		newSuperRareBrawlers.remove(newSuperRareBrawlers[0])
        		cost = 430
        		costGems = 79
        	elif newEpicBrawlers and newEpicBrawlers != [0, 0]:
        		unlockingBrawlers.append(newEpicBrawlers[0])
        		newEpicBrawlers.remove(newEpicBrawlers[0])
        		cost = 925
        		costGems = 169
        	elif newMythicBrawlers and newMythicBrawlers != [0, 0]:
        		unlockingBrawlers.append(newMythicBrawlers[0])
        		newMythicBrawlers.remove(newMythicBrawlers[0])
        		cost = 1900
        		costGems = 349
        	elif newLegendaryBrawlers and newLegendaryBrawlers != [0, 0]:
        		unlockingBrawlers.append(newLegendaryBrawlers[0])
        		newEpicBrawlers.remove(newLegendaryBrawlers[0])
        		cost = 3400
        		costGems = 699
        except Exception as e:
        	print(f"[StarRoad] Ошибка при выборе бравлера: {e}")

        self.writeBoolean(True) # Starr road array

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(len(unlockingBrawlers)) #бравлер который анлокается + бравлеры на выбор которые следующ
        
        if len(unlockingBrawlers) == 0:
            print('StarRoad is full claimed')
        else:
            self.writeDataReference(16, unlockingBrawlers[0]) #brawler
            self.writeVInt(cost)
            self.writeVInt(costGems)
            self.writeVInt(0)
            self.writeVInt(player.RareTokens) # Claimed Credits
            self.writeVInt(0)
            self.writeVInt(0)
        
        self.writeVInt(len(allBrawlers)) #бравлеры которые дальше уже стоят

        
        

        if len(allBrawlers) == 0:
            pass
        else:
            
            for brawlerID in allBrawlers:
                if brawlerID in newRareBrawlers:
                    cost = 160
                    costGems = 29
                elif brawlerID in newSuperRareBrawlers:
                    cost = 430
                    costGems = 79
                elif brawlerID in newEpicBrawlers:
                    cost = 925
                    costGems = 169
                elif brawlerID in newMythicBrawlers:
                    cost = 1900
                    costGems = 349
                elif brawlerID in newLegendaryBrawlers:
                    cost = 3400
                    costGems = 699
                self.writeDataReference(16, brawlerID) #brawler
                self.writeVInt(cost)
                self.writeVInt(costGems)
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeVInt(brawlerID)
                self.writeVInt(0)
  
        self.writeVInt(0)
        self.writeVInt(0)
        # StarRoad End


        # MasteryEntry::encode
        self.writeVInt(ownedBrawlersCount) # new function v48
        for brawlerID,brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID) # Brawler
            self.writeVInt(brawlerInfo["MasteryPoints"])
            self.writeVInt(brawlerInfo["MasteryClaimed"])
        # MasteryEntry::encode End

        self.writeVInt(0) # v48
        self.writeVInt(0) # v48
        self.writeVInt(0) # v48
        self.writeVInt(0) # v48
        self.writeVInt(0) # v48
        self.writeBoolean(False)  # v48
        self.writeBoolean(False)  # v48
        self.writeBoolean(False)  # v48
        self.writeBoolean(False)  # v48

        self.writeVInt(0) # end LogicClientHome

        self.writeVLong(player.ID[0], player.ID[1]) # player id
        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(player.ID[0], player.ID[1])

        self.writeStringReference(player.Name)
        self.writeBoolean(player.Registered) # name set

        self.writeInt(-1)

        self.writeVInt(17) # commodity count

        self.writeVInt(ownedBrawlersCount + 5)

        for brawlerInfo in player.OwnedBrawlers.values():
            self.writeDataReference(23, brawlerInfo["CardID"])
            self.writeVInt(-1)
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(-1)
        self.writeVInt(player.Coins) # Gold

        self.writeDataReference(5, 10)
        self.writeVInt(-1)
        self.writeVInt(player.StarPoints)

        self.writeDataReference(5, 13)
        self.writeVInt(-1)
        self.writeVInt(player.ClubCoins)
        
        self.writeDataReference(5, 20)
        self.writeVInt(-1)
        self.writeVInt(player.ChromaticTokens) # ChromaticTokens
        
        self.writeDataReference(5, 21)
        self.writeVInt(-1)
        self.writeVInt(0) # Fame

        self.writeVInt(ownedBrawlersCount)

        for brawlerID,brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["Trophies"])
        
        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["HighestTrophies"])

        self.writeVInt(1) # Array
        self.writeDataReference(16, 0)
        self.writeVInt(-1)
        self.writeVInt(1)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["PowerPoints"])
        
        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["PowerLevel"] - 1)

        self.writeVInt(0) # hero star power and gadget

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["State"])

        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array

        self.writeVInt(player.Gems) # Diamonds
        self.writeVInt(player.Gems) # Free Diamonds

        self.writeVInt(10) # Player Level
        self.writeVInt(100)
        self.writeVInt(0) # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(100) # Battle Count
        self.writeVInt(10) # WinCount
        self.writeVInt(80) # LoseCount
        self.writeVInt(50) # WinLooseStreak
        self.writeVInt(20) # NpcWinCount
        self.writeVInt(0) # NpcLoseCount
        self.writeVInt(2) # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(12)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)

    def decode(self):
        fields = {}
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion