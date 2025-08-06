import csv


class Pins:

    def getPinsID():
        EmotesID = []
        with open('Classes/Files/assets/csv_logic/emotes.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[1].lower() != 'true':
                        EmotesID.append(line_count - 2)
                    if row[0] != "":
                        line_count += 1

            return EmotesID
        
    def getEmotesCost(name):
        with open('Classes/Files/assets/csv_logic/emotes.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[11] == name:
                        formatedRow = []
                        formatedRow.append(line_count - 2)
                        for i in row:
                            if i != '':
                                formatedRow.append(i)
                        print(formatedRow)
                        break
                    if row[0] != "":
                        line_count += 1


    def getEmotesInfoByName(name):
        with open('Classes/Files/assets/csv_logic/emotes.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[0] == name:
                        formatedRow = []
                        formatedRow.append(line_count - 2)
                        for i in row:
                            if i != '':
                                formatedRow.append(i)
                        print(formatedRow)
                        break
                    if row[0] != "":
                        line_count += 1