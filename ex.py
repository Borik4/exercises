def funk_1(p):
    minimum = float('inf')
    for i in p:
        if i % 2 == 1:
            minimum = min(minimum, i)
    return minimum

print(funk_1([13, 22, 4, 65, 2, 7, 98, 19]), '  ==   7')

def funk_2(p):
    minimum = float('inf')
    second_minimum = float('inf')
    for i in p:
        if i < minimum:
            minimum, second_minimum = i, minimum
        elif i < second_minimum:
            second_minimum = i
    return second_minimum

print(funk_2([1, 23, 55, 6, 78, 2, 9, 90]), '  ==   2')
print(funk_2([54, 31, 5, 98, 83, 77]), '  ==   31')

def funk_3(p):
    c = ''.join([str(i) for i in p])
    count = 0
    for i in c:
        if i == '0':
            count+=1
    return count

def funk_3_1(p):
    return len([i for i in ''.join([str(i) for i in p]) if i == '0'])

print(funk_3([100, 456405, 878121002255, 540140, 5230254, 10]), '  ==   9')
print(funk_3_1([100, 456405, 878121002255, 540140, 5230254, 10]), '  ==   9')


def funk_4(p):
    p = [str(i) for i in p]
    max_count = -float('inf')
    # max_num =
    count = -float('inf')
    # num =
    for i in p:
        num = i[0]
        count = 1
        for o in range(1, len(i)):
            if i[o] == num:
                count += 1
            else:
                if max_count < count:
                    max_num = num
                    max_count = count
                    num = i[o]
                    count = 1
                else:
                    num = i[o]
                    count = 1

    return max_count, max_num

print('count:', funk_4([14444452, 65523336555555598, 1444441125445588555, 11122555565445])[0], 'digit:', funk_4([14444452, 65523336555555598, 1444441125445588555, 11122555565445])[1], '  ==   count: 7 digit: 5')