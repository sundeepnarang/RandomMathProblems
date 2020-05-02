# Problem
#
# The robot starts on the center dot of the grid,
# makes four moves of one unit with each move in a
# randomly selected direction (up, down, left, or right),
# and then stops. The robot does not move diagonally. ⁠
# ⁠
# Which region is most likely to contain the dot the robot stops on?⁠
# ⁠
# A. The inner green square⁠
# B. The blue V region⁠
# C. The outer orange region⁠
# ⁠


from matplotlib import pyplot as plt

c_l_map = {
    "green": "lightgreen",
    "blue": "royalblue",
    "orange": "gold",
}


def get_color(x_1, y_1):
    if (x_1 == 0 and 0 <= y_1 <= 2) or (y_1 == 1 and (x_1 == -1 or x_1 == 1)):
        return 'green'
    elif (y_1 == 0 and (-2 <= x_1 < 0 or 0 < x_1 <= 2)) or \
            (y_1 == -1 and -1 <= x_1 <= 1) or \
            (x_1 == 0 and y_1 == -2):
        return 'blue'
    else:
        return 'orange'


def init_m_dict(m_dict={}):
    for x_i in range(-4, 5):
        for y_i in range(-4, 5):
            if abs(x_i) + abs(y_i) < 5:
                coord = "%d, %d" % (x_i, y_i)
                m_dict[coord] = [0, get_color(x_i, y_i)]
    return m_dict


def apply_move(x_1, y_1, m):
    if m == 0:
        x_1 = x_1 + 1
    if m == 1:
        y_1 = y_1 + 1
    if m == 2:
        x_1 = x_1 - 1
    if m == 3:
        y_1 = y_1 - 1
    return x_1, y_1


def move(x=0, y=0):
    m_dict = init_m_dict()
    for m1 in range(4):
        for m2 in range(4):
            for m3 in range(4):
                for m4 in range(4):
                    x, y = apply_move(x, y, m1)
                    x, y = apply_move(x, y, m2)
                    x, y = apply_move(x, y, m3)
                    x, y = apply_move(x, y, m4)
                    coord = "%d, %d" % (x, y)
                    m_dict[coord][0] = m_dict[coord][0] + 1
                    x = 0
                    y = 0

    # m_dict = {k: v for k, v in sorted(m_dict.items(), key=lambda item: item[1], reverse=True)}

    return m_dict


def plot(m_dict):
    r_probs = {k: [0, 0] for k in c_l_map}
    x_val = []
    y_val = []
    t_val = []
    c_val = []
    m_val = []
    for key in m_dict:
        x_str, y_str = key.split(", ")
        x_val.append(int(x_str))
        y_val.append(int(y_str))
        t = m_dict[key][0]
        p = t / 256
        c = m_dict[key][1]
        p_str = ("%.5f" % p).rstrip('0').rstrip('.')
        t_val.append("%d\n[%s]" % (t, p_str))

        r_probs[c][0] = r_probs[c][0] + t
        r_probs[c][1] = r_probs[c][1] + p

        if p_str == "0":
            m_val.append('x')
            c_val.append(c_l_map[c])
        else:
            m_val.append('o')
            c_val.append(c)
    #
    plt.figure(figsize=(10.24, 7.68))
    # print(plt.rcParams.get('figure.figsize'))
    # print(plt.rcParams.get('figure.dpi'))
    for xp, yp, cp, m in zip(x_val, y_val, c_val, m_val):
        plt.scatter([xp], [yp], color=[cp], marker=m)

    plt.ylim(-6, 6)

    for i, txt in enumerate(t_val):
        plt.annotate(txt, (x_val[i], y_val[i]), xytext=(0, -30), textcoords='offset points', ha="center")

    plt.show()

    t_moves = 0
    t_prob = 0

    for color in r_probs:
        t_moves = t_moves + r_probs[color][0]
        t_prob = t_prob + r_probs[color][1]
        print("For (%s) region total moves are [%d] and "
              "probability is [%.5f]" %
              (color, r_probs[color][0], r_probs[color][1]))

    print("\nTotal moves are [%d] with probability [%d]" % (t_moves, t_prob))


if __name__ == '__main__':
    plot(move())
