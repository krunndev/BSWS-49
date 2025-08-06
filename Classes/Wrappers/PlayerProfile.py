from Classes.Wrappers.PlayerDisplayData import PlayerDisplayData

class PlayerProfile:
    def encode(calling_instance, fields, playerData):
        #calling_instance.encodeLogicLong(LogicLong(fields["PlayerID"][0], fields["PlayerID"][1]))
        calling_instance.writeDataReference(16, playerData['favoriteBrawler'])

        sortedBrawlers = sorted(playerData["OwnedBrawlers"], key=lambda x: (playerData["OwnedBrawlers"][x]['Trophies']), reverse=True)

        calling_instance.writeVInt(len(sortedBrawlers))
        for brawlerID in sortedBrawlers:
            brawlerData = playerData["OwnedBrawlers"][brawlerID]
            calling_instance.writeDataReference(16, brawlerID)
            if brawlerData["Skins"] != []:
                calling_instance.writeDataReference(29, brawlerData["Skins"][0]) # TODO: Sync with current skin
            else:
                calling_instance.writeDataReference(0)
            calling_instance.writeVInt(brawlerData["Trophies"])
            calling_instance.writeVInt(brawlerData["HighestTrophies"])
            calling_instance.writeVInt(brawlerData["PowerLevel"])

        calling_instance.writeVInt(16)

        calling_instance.writeVInt(1)
        calling_instance.writeVInt(playerData["threeXthreeWins"])        
        
        calling_instance.writeVInt(2)
        calling_instance.writeVInt(playerData["Experience"])

        calling_instance.writeVInt(3)
        calling_instance.writeVInt(playerData["Trophies"])

        calling_instance.writeVInt(4)
        calling_instance.writeVInt(playerData["HighestTrophies"])

        calling_instance.writeVInt(5)
        calling_instance.writeVInt(len(sortedBrawlers))

        calling_instance.writeVInt(8)
        calling_instance.writeVInt(playerData["soloWins"])

        calling_instance.writeVInt(11)
        calling_instance.writeVInt(playerData["duoWins"])

        calling_instance.writeVInt(9)
        calling_instance.writeVInt(0)

        calling_instance.writeVInt(12)
        calling_instance.writeVInt(0)

        calling_instance.writeVInt(13)
        calling_instance.writeVInt(0)

        calling_instance.writeVInt(14)
        calling_instance.writeVInt(0)

        calling_instance.writeVInt(15)
        calling_instance.writeVInt(0)

        calling_instance.writeVInt(16)
        calling_instance.writeVInt(0)

        calling_instance.writeVInt(18)
        calling_instance.writeVInt(17) # Power League Solo Rank

        calling_instance.writeVInt(17)
        calling_instance.writeVInt(19) # Power League Team Rank

        calling_instance.writeVInt(19)
        calling_instance.writeVInt(19) # Club League Rank

        PlayerDisplayData.encode(calling_instance, playerData)

        calling_instance.writeBoolean(True)
        calling_instance.writeVInt(0)

        calling_instance.writeString("hello world")
        calling_instance.writeVInt(0)
        calling_instance.writeVInt(0)

        try:
            calling_instance.writeDataReference(29, playerData["SelectedSkins"][f'{playerData["favoriteBrawler"]}'])
        except:
            calling_instance.writeDataReference(0)
        if playerData['battleIcon'] == 0:
            calling_instance.writeDataReference(0) # icon
        else:
            calling_instance.writeDataReference(28, playerData['battleIcon']) # icon
        
        if playerData['battleIcon1'] == 0:
            calling_instance.writeDataReference(0) # icon 2
        else:
            calling_instance.writeDataReference(28, playerData['battleIcon1']) # icon 2
        
        if playerData['battlePin'] == 0:
            calling_instance.writeDataReference(0) # pin
        else:
            calling_instance.writeDataReference(52, playerData['battlePin']) # pin

        if playerData['battleTitle'] == 0:
            calling_instance.writeDataReference(0) # titles
        else:
            calling_instance.writeDataReference(76, playerData['battleTitle']) # titles

    def decode(calling_instance, fields):
        pass