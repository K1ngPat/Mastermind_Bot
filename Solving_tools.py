import random
import time

start = time.time()

def check_row(attempt: list, key: list):
    """Checks the current attempt and returns, for example, 3 whites and 1 red as int(31). 
    \nReturn Type: int \nParameters: attempt = attempted answer; key = correct answer"""
    att = [0 for _ in range(5)]
    ky = [0 for _ in range(5)]

    red = 0
    white = 0

    # Following for loop makes sure the lists are copied without being referenced to same memory location
    for ind in range(5):
        att[ind] = attempt[ind]
        ky[ind] = key[ind]

    for jj in range(5):
        if ky[jj] == att[jj]:
            att[jj] = -1
            ky[jj] = -2
            red += 1

    for k_ind in range(5):
        for a_ind in range(5):
            if ky[k_ind] == att[a_ind] and k_ind != a_ind:
                ky[k_ind] = -2
                att[a_ind] = -1
                white += 1

    return int(((10*white) + red))


def play_game():
    actkey = [random.randint(1,8) for _ in range(5)]
    for tryno in range(12):
        print("Attempt number" + str(tryno+1) + "\nAttempt Please enter guess with space between all entries, for example, \"1 2 3 4 5\"")
        din = input()
        actatt = din.split()
        for i in range(5):
            actatt[i] = int(actatt[i])
        
        print(str(check_row(actatt, actkey)))
        if check_row(actatt, actkey) == 5:
            print("YOU WIN!!!!")
            print("CODE WAS " + str(actkey))
            return 0

    print("CODE WAS " + str(actkey))
    return 0

def make_data_table():
    print("Enter data table")
    y = input().split(' ')
    return y

def playing_ai(data_list):
    dunkey = [random.randint(1,8) for _ in range(5)]
    dl = data_list[:]
    hist = [[0, 0] for _ in range(12)]
    for k in range(12):
        att_scores = []
        if k != 0:
            for ind in range(int((len(dl)/6)-1), -1, -1):
                if check_row(hist[k-1][0], [int(dl[6*ind]), int(dl[6*ind + 1]), int(dl[6*ind + 2]), int(dl[6*ind + 3]), int(dl[6*ind + 4])]) != hist[k-1][1]:
                    for t in range(6):
                        del dl[6*ind]
    
        print("Move " + str(k+1) + ", Number of available options is: " + str(len(dl)/6))
        for pcnt in range(int(len(dl)/6)):
            att_scores.append(float(dl[pcnt*6 + 5]))
        ag = random.choices(range(int(len(dl)/6)), att_scores)[0]
        hist[k][0] = [int(dl[6*ag]), int(dl[6*ag + 1]), int(dl[6*ag + 2]), int(dl[6*ag + 3]), int(dl[6*ag + 4])]
        t = check_row(hist[k][0], dunkey)
        print(t)
        hist[k][1] = t
        if t == 5:
            print("AI won in " + str(k+1) + " moves")
            return 0

def get_datalist_startAI():
    f = open("datalist.txt", "rt")
    dtl = f.read().split(" ")
    del dtl[196608]
    playing_ai(dtl)

get_datalist_startAI()

end = time.time()

print(str(end-start))
