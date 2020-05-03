# Problem
#
# Each letter represents a different digit,
# and no number is written with a leading zero.⁠
# ⁠
# What could the letter “O” represent?
# (choose one or more)⁠
#
# ☐ 7⁠
# ☐ 8⁠
# ☐ 9⁠
# ☐ 10⁠

LOL_dict = {}
MAX_B = 0
MAX_A = 0
MAX_D = 0
MAX_L = 0
MIN_B = 10
MIN_A = 10
MIN_D = 10
MIN_L = 10
i = 1
O_vals = set()

for B in range(1, 4):
    for A in range(1, 5):
        for D in range(B + 1, 7):  # interchangeable with B
            for L in range(8):
                if B != D and B != A and B != L and D != A and D != L and A != L:
                    if B + A + D > 9:  # causes carry, will cause 4 digits result
                        # print("BAD ignored %d" % (B * 100 + A * 10 + D))
                        continue
                    if A + L + A > 9:  # causes carry => Ls in LOL won't be same
                        # print("ALA ignored %d" % (A * 100 + L * 10 + A))
                        continue

                    BAD = B * 100 + A * 10 + D
                    ALA = A * 100 + L * 10 + A
                    DAB = D * 100 + A * 10 + B

                    # Max analysis for no carry
                    if MAX_A < A:
                        MAX_A = A  # 6
                    if MAX_B < B:
                        MAX_B = B  # 3
                    if MAX_D < D:
                        MAX_D = D  # 6
                    if MAX_L < L:
                        MAX_L = L  # 6

                    LOL = BAD + ALA + DAB
                    L_CALC_1 = LOL // 100
                    L_CALC_2 = (LOL % 100) % 10
                    O_CALC = (LOL % 100) // 10

                    # Not needed as A + L + A  < 10 accounts for this
                    #
                    # if L_CALC_1 != L_CALC_2:
                    #     continue

                    if L_CALC_1 != L:  # 57 Cases without this Would have to brute force this
                        continue

                    # Not needed as doest happen in 2 cases
                    # but no logical proof/reason to avoid it

                    if O_CALC != A and O_CALC != B and O_CALC != D and O_CALC != L:
                        O_vals.add(O_CALC)
                    else:
                        continue

                    # Not Needed as B A D min of 1 and B + A + D < 10 accounts for this
                    # if 99 < L <1000:

                    if str(LOL) in LOL_dict:
                        LOL_dict[str(LOL)].append([BAD, ALA, DAB])
                    else:
                        LOL_dict[str(LOL)] = [[BAD, ALA, DAB]]

                    print("%d BAD : %d, ALA : %d, DAB : %d | LOL : %d" % (i, BAD, ALA, DAB, LOL))
                    i = i + 1

# print("Max B: %d, Max A: %d, Max D: %d, Max L: %d" % (MAX_B, MAX_A, MAX_D, MAX_L))
print(f"O Values : {O_vals}")
