
#obtain number of boxes from file, return a list of number of boxes
def  getNum(filepath):
    num_list = []
    with open(filepath, 'r')as file:
        f = file.readlines()
        for line in f:
            l_list = []
            str = line.strip().split(',')
            l_list = list(map(int,str))
            num_list.append(l_list)
    return num_list
def computeBoxNum(list):
    sum_box = 0
    threeBox = [0,5,3,1]
    sum_box = list[5] + list[4] +list[3] + ((list[2]+3)//4)
    remTwoBox = 5*list[3] + threeBox[(list[2]%4)]
    if list[1] > remTwoBox:
        sum_box += ((list[1] - remTwoBox) + 8)//9
    remOneBox = 36*sum_box - 36*list[5] - 25*list[4] - 16*list[3] - 9*list[2] - 4*list[1]
    if list[0] > remOneBox:
        sum_box += ((list[0] - remOneBox)+35)//36
    return sum_box
if __name__ == '__main__':
    file_path = input()
    num_list = getNum(file_path)
    print(num_list)
    for n_list in num_list:
        sum = computeBoxNum(n_list)
        print(sum)
