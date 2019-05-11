class SoccerPlayer(object):
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number
        print("----------------------")

    def GetData(self):
        return "Name: " + self.name, "Position: " + self.position, "Number: " + str(self.number)

    def ChangeNumber(self, number):
        print("----------------------")
        print("Change Number " + str(self.number) + " to " + str(number))
        print("----------------------")
        self.number = number

    def __str__(self):
        return "데헷"

player = SoccerPlayer("팡무", "깍두기", 7)

for item in player.GetData():
    print(item)

player.ChangeNumber(777)

