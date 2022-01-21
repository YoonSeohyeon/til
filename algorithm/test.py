#알고리즘 문제 1

def solution1(array, commands):
    answer = []
    for num in commands:
        i = num[0] - 1
        j = num[1]
        k = num[2] - 1
        if i == j:
            new_array = [array[i]]

        else:
            new_array = array[i:j]

        new_array.sort()

        answer.append(new_array[k])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


result = solution1(array,commands)

print(result)

# 두번째 문제

def solution2(numbers):
    answer = ''
    length = len(numbers)
    if length == 1:
        return [numbers]
    else:
        result = []
        for i in numbers:
            b = numbers.copy()
            b.remove(i)
            b.sort()
            for j in solution2(b):
                j.insert



    # return answer

numbers = [6, 10, 1]

solution2(numbers)


# 팀 알고리즘 1

def solution_team(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    same_num = []
    answer = []
    zero_num = 0
    for i in lottos:
        if i in win_nums:
            same_num.append(i)
        if i == 0:
            zero_num+=1
    total_correct_num = len(same_num)+zero_num
    answer.append(rank[total_correct_num])
    answer.append(rank[len(same_num)])

    return answer



lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
print(solution_team(lottos, win_nums))