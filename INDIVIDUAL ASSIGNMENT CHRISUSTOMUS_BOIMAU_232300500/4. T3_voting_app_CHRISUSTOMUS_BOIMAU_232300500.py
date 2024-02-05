"""
T3 - VOTING APP

NAMA = CHRISUSTOMUS BOIMAU
NIM  = 232300500
"""

vote_box = {}
vote_box["1"] = 0
vote_box["2"] = 0
vote_box["3"] = 0

while True:
    print("""\n0. done
1. chris
2. Tomus
3. Boimau        
""")
    vote = input("\ninput = ")
    if vote == "0":
        break
    elif vote == "1":
        vote_box["1"] += 1
    elif vote == "2":
        vote_box["2"] += 1
    elif vote == "3":
        vote_box["3"] += 1
    else:
        print("\nPLEASE CHOSE A NUMBER BETWEN 0,1,2,AND 3\n")

print("---result---")
for i in vote_box:
    print(f"number {i} have {vote_box[i]} sound")
    

