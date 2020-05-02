# Problem
#
# If the same letter is used twice,
# it’s the same digit in both places,
# and if different letters are used,
# the digits are also different.⁠
# No number is written with a leading zero. ⁠
# ⁠
# What is the value of T?⁠
# ⁠
# A. 2⁠
# B. 4⁠
# C. 6⁠
# D. 7⁠

sol = []

for e in range(2, 10):
    for s in range(e + 1, 10):
        es = 10 * e + s
        se = 10 * s + e
        test = es * se
        if es * se > 999:
            t_1 = test // 1000
            e_1 = (test - (t_1 * 1000)) // 100
            s_1 = (test - (t_1 * 1000) - (e_1 * 100)) // 10
            t_2 = (test - (t_1 * 1000) - (e_1 * 100) - (s_1 * 10))
            if e_1 == e and s_1 == s and t_1 == t_2:
                sol.append([t_1, e_1, s_1, t_2])
                print("ES = %d, SE = %d, ES * SE = %d" % (es, se, es * se))
                print("T = %d, E = %d, S = %d, T = %d" % (t_1, e_1, s_1, t_2))

print(sol)
