
def pw_criteria(pw):
    same_adj = False
    cur_streak = 0
    digit_cur = 10
    while pw > 0:
        digit_next = pw % 10
        if digit_cur == digit_next:
            cur_streak += 1
        else:
            if cur_streak == 1:
                same_adj = True
            cur_streak = 0
        if digit_next > digit_cur:
            return False
        pw = pw // 10
        digit_cur = digit_next
    if cur_streak == 1:
                same_adj = True
    return same_adj

valid_pw = 0
for i in range(272091, 815432+1):
    if i % 100 == 0:
        print(i, valid_pw)
    if pw_criteria(i):
        valid_pw += 1

print(valid_pw)
