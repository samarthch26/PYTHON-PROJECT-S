li=[1,2,3,4,5,6,7,8,9]
player='X'
flag=0
wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
count=0
while True:
    print ("\n\t\t\t\t TIC-TAC-TOE")
    print(f"\n\t\t\t\t {li[0]} | {li[1]} | {li[2]}")
    print("\t\t\t\t-----------")
    print(f"\t\t\t\t {li[3]} | {li[4]} | {li[5]}")
    print("\t\t\t\t-----------")
    print(f"\t\t\t\t {li[6]} | {li[7]} | {li[8]}")
    if flag==1:
        break
    if count==9:
        print("\n\t\t\t\tMATCH TIE!")
        break
    print(f"\n\t\t\t\tPLAYER {player} TURN's:",end='')
    ch=int(input())
    if ch in li:
        li[ch-1]=player
        count=count+1
        for a,b,c in wins:
            if li[a]==li[b] and li[b]==li[c]:
                print (f"\n\t\t\t\t-----PLAYER {player} WIN'S-----")
                flag=1
        if player=='X':
            player='0'
        else:
            player='X'
    else:
        print("\n\t\t\t\tWrong Entered! \n\t\t\t\tTry Again!")
