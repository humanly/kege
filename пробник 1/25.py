for a in range(0, 10):
    for b in range(0, 10):
        s = int(f'12345{a}6{b}8')
        if s % 17 == 0:
            print(s, s // 17)