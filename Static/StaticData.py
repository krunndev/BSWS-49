import json

class StaticData:
    ShopData = json.loads(open("Static/Shop.json", 'r').read())
    EventsData = None

    def Preload():
        StaticData.ShopData = json.loads(open("Static/Shop.json", 'r').read())
        StaticData.EventsData = json.loads(open("Static/Events.json", 'r').read())