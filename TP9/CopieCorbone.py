

def cc(data):
    correct = 0
    for i in range(2, len(data)):
        prix_1 = data[i - 2][1]
        prix_2 = data[i - 1][1]
        if ((prix_1 > prix_2) and (prix_2 > data[i][1])) or ((prix_1 < prix_2) and (prix_2 < data[i][1])):
            correct += 1
    rate = correct / (len(data) - 2)
    print(rate)
