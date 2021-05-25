a = int(input());

for i in range(a):
    b = int(input());
    lit = [0] * (b+1);
    lit[0] = 1;
    lit[1] = 1;
    if b > 1:
        lit[2] = 1;
    for i in range(len(lit)-3):
        lit[i+3] = lit[i] + lit[i+1]
    print(lit[b-1]);
