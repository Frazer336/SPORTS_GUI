def duplicate_function(x):
  return list(dict.fromkeys(x))
  
#read data
file = open("formatted_scores.txt", "r")

GAME_ID = []
TEAM_ID = []
GAME_DATE_EST = []
TEAM_ABBREVIATION = []
TEAM_CITY_NAME = []
TEAM_WINS_LOSSES = []
PTS_QTR1 = []
PTS_QTR2 = []
PTS_QTR3 = []
PTS_QTR4 = []
PTS = []
FG_PCT = []
FT_PCT = []
FG3_PCT = []
AST = []
REB = []
TOV = []

for line in file:
    splitLine = line.split(",")
    GAME_ID.append(splitLine[0])
    TEAM_ID.append(splitLine[1])
    GAME_DATE_EST.append(splitLine[2])
    TEAM_ABBREVIATION.append(splitLine[3])
    TEAM_CITY_NAME.append(splitLine[4])
    TEAM_WINS_LOSSES.append(splitLine[5])
    PTS_QTR1.append(splitLine[6])
    PTS_QTR2.append(splitLine[7])
    PTS_QTR3.append(splitLine[8])
    PTS_QTR4.append(splitLine[9])
    PTS.append(splitLine[10])
    FG_PCT.append(splitLine[11])
    FT_PCT.append(splitLine[12])
    FG3_PCT.append(splitLine[13])
    AST.append(splitLine[14])
    REB.append(splitLine[15])
    TOV.append(splitLine[16])

    



print(TEAM_ABBREVIATION)

file.close()


