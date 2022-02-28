# (a)
class TreasureChest:
    ### Python does not have private attribute
    # question: String(str)
    # answer: String(str)
    # points: String(str)

    def __init__(self, question, answer, points):
        self.question = question
        self.answer = answer
        self.points = points
    
    # (c)
    #   (i)
    def getQuestion(self):
        return self.question
    
    #   (ii)
    def checkAnswer(self, answer):
        return answer == self.answer

    #   (iii)
    def getPoints(self, num_attempts):
        if num_attempts == 1:
            return self.points
        elif num_attempts == 2:
            return self.points // 2
        elif num_attempts == 3 or num_attempts == 4:
            return self.num_attempts // 4
        else:
            return 0

# (b)
def readData():
    file = None
    try:
        file = open("TreasureChestData.txt", "r")
    except Exception as e:
        print("[-] Error: {e}")
        return
    arrayTreasure = []
    count = 0
    # data = []

    question = ""
    answer = ""
    points = ""
    
    fileData = file.readline()
    while fileData:
        
        ### Alternate implementation

        # data.append(file.readline().split(" ")[0])
        # if count == 3:
        #     count = 0
        # arrayTreasure.append(TreasureChest(data[0], data[1], data[2]))
        # count = count + 1        



        
        dataClass = fileData.split(" ")
        if dataClass[1] == "question":
            question = dataClass[0]
        elif dataClass[1] == "answer":
            answer = dataClass[0]
        elif dataClass[1] == "points":
            points = dataClass[0]

        if count == 3:
            count = 0
            arrayTreasure.append(TreasureChest(question, answer, points))
        count = count + 1

    else:
        print("EOF")



# if __name__ == "__main__":
