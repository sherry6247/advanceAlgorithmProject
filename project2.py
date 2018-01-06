def combine_num(str):
    dp = [1,1]
    for i in range(len(str)):
        temp = 0
        if int(str[i]) != 0:
            temp = dp[1]
        if i > 0:
            if validTwo(int(str[i-1]+str[i])):
                temp = temp + dp[0]
        dp[0] = dp[1]
        dp[1] = temp
    return dp[1]
def validTwo(s):
    if s >= 10 and s <= 26:
        return True
    else:
        return False

if __name__ == '__main__':
    print("please enter a string:")
    str = input()
    com_num = combine_num(str)
    print(com_num)