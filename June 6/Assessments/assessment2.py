#Task 1
import csv

with open("players.csv","r") as file:
    reader=csv.reader(file)

    for row in reader:
        print(row)

#Task 2
import csv

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        print(row)

#Task 3
import csv

count=0

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        count+=1

print(count)

#Task 4
import csv

highest_runs=0
top_player=""

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        runs=int(row[4])

        if runs>highest_runs:
            highest_runs=runs
            top_player=row[1]

print(top_player,highest_runs)

#Task 5
import csv

lowest_runs=999999
low_player=""

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        runs=int(row[4])

        if runs<lowest_runs:
            lowest_runs=runs
            low_player=row[1]

print(low_player,lowest_runs)

#Task 6
import csv

total=0
count=0

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        total+=int(row[4])
        count+=1

print(total/count)

#Task 7
import csv

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        if int(row[4])>600:
            print(row)

#Task 8
import csv

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        if int(row[4])<500:
            print(row)

#Task 9
import csv

team_count={}

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        team=row[2]

        if team in team_count:
            team_count[team]+=1
        else:
            team_count[team]=1

print(team_count)

#Task 10
import csv

team_runs={}

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        team=row[2]
        runs=int(row[4])

        if team in team_runs:
            team_runs[team]+=runs
        else:
            team_runs[team]=runs

print(team_runs)

#Task 11
import csv

team_runs={}

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        team=row[2]
        runs=int(row[4])

        if team in team_runs:
            team_runs[team]+=runs
        else:
            team_runs[team]=runs

top_team=max(team_runs,key=team_runs.get)

print(top_team)

#Task 12
import csv

team_runs={}

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        team=row[2]
        runs=int(row[4])

        if team in team_runs:
            team_runs[team]+=runs
        else:
            team_runs[team]=runs

low_team=min(team_runs,key=team_runs.get)

print(low_team)

#Task 13
import csv

highest_fours=0
top_player=""

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        fours=int(row[5])

        if fours>highest_fours:
            highest_fours=fours
            top_player=row[1]

print(top_player,highest_fours)

#Task 14
import csv

highest_sixes=0
top_player=""

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        sixes=int(row[6])

        if sixes>highest_sixes:
            highest_sixes=sixes
            top_player=row[1]

print(top_player,highest_sixes)

#Task 15
import csv

total_fours=0

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        total_fours+=int(row[5])

print(total_fours)

#Task 16
import csv

total_sixes=0

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        total_sixes+=int(row[6])

print(total_sixes)

#Task 17
import csv

players=[]

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        players.append(row[1])

players.sort()

print(players)

#Task 18
import csv

teams=set()

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        teams.add(row[2])

print(teams)

#Task 19
import csv

team_runs={}

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        team=row[2]
        runs=int(row[4])

        if team in team_runs:
            team_runs[team]+=runs
        else:
            team_runs[team]=runs

print(team_runs)

#Task 20
import csv

player_runs={}

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        player=row[1]
        runs=int(row[4])

#Task 21
def find_top_scorer():

    import csv

    highest_runs=0
    top_player=""

    with open("players.csv","r") as file:
        reader=csv.reader(file)
        next(reader)

        for row in reader:
            runs=int(row[4])

            if runs>highest_runs:
                highest_runs=runs
                top_player=row[1]

    print(top_player,highest_runs)

find_top_scorer()

#Task 22
def calculate_average_runs():

    import csv

    total=0
    count=0

    with open("players.csv","r") as file:
        reader=csv.reader(file)
        next(reader)

        for row in reader:
            total+=int(row[4])
            count+=1

    print(total/count)

calculate_average_runs()

#Task 23
def find_best_team():

    import csv

    team_runs={}

    with open("players.csv","r") as file:
        reader=csv.reader(file)
        next(reader)

        for row in reader:
            team=row[2]
            runs=int(row[4])

            if team in team_runs:
                team_runs[team]+=runs
            else:
                team_runs[team]=runs

    top_team=max(team_runs,key=team_runs.get)

    print(top_team)

find_best_team()

#Task 24
def find_total_boundaries():

    import csv

    total_fours=0
    total_sixes=0

    with open("players.csv","r") as file:
        reader=csv.reader(file)
        next(reader)

        for row in reader:
            total_fours+=int(row[5])
            total_sixes+=int(row[6])

    print(total_fours+total_sixes)

find_total_boundaries()

#Task 25
try:

    import csv

    with open("players.csv","r") as file:
        reader=csv.reader(file)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("File not found")

#Task 26
import csv

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:

        try:
            runs=int(row[4])
            print(runs)

        except ValueError:
            print("Invalid run value")

#Task 27
import csv

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:

        try:
            matches=int(row[3])
            print(matches)

        except ValueError:
            print("Invalid match count")

#Task 28
import numpy as np
import csv

runs_list=[]

with open("players.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        runs_list.append(int(row[4]))

arr=np.array(runs_list)

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))
print(np.median(arr))

#Task 29
import pandas as pd

df=pd.read_csv("players.csv")

print(df)

#Task 30
import pandas as pd

df=pd.read_csv("players.csv")

print(df.sort_values(by="runs",ascending=False).head(5))

#Task 31
import pandas as pd

df=pd.read_csv("players.csv")

print(df.sort_values(by="runs",ascending=False))

#Task 32
import pandas as pd

df=pd.read_csv("players.csv")

print(df.groupby("team")["runs"].sum())

#Task 33
import pandas as pd

df=pd.read_csv("players.csv")

print(df.groupby("team")["runs"].mean())

#Task 34
import pandas as pd

df=pd.read_csv("players.csv")

print(df[df["runs"]>600])

#Task 35
import pandas as pd

df=pd.read_csv("players.csv")

team_runs=df.groupby("team")["runs"].sum()

print(team_runs.idxmax())

#Task 36
import pandas as pd

df=pd.read_csv("players.csv")

top_players=df[df["runs"]>600]

top_players.to_csv("top_players.csv",index=False)

print("File created")

#Task 37
import pandas as pd

df=pd.read_csv("players.csv")

summary=df.groupby("team").agg({
"runs":"sum",
"player_name":"count"
})

summary["average_runs"]=df.groupby("team")["runs"].mean()

summary.to_csv("team_summary.csv")

print("File created")

#Task 38
while True:

    print("1.Player Analysis")
    print("2.Team Analysis")
    print("3.Boundary Analysis")
    print("4.Export Reports")
    print("5.Exit")

    choice=int(input("Enter choice:"))

    if choice==1:
        print("Player Analysis")

    elif choice==2:
        print("Team Analysis")

    elif choice==3:
        print("Boundary Analysis")

    elif choice==4:
        print("Export Reports")

    elif choice==5:
        print("Exited")
        break

    else:
        print("Invalid choice")

        player_runs[player]=runs

print(player_runs)
