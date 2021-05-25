a = int(input());
count = 0;

lit = [0] * 1000001;

lit[1] = 0;
lit[2] = 1;
lit[3] = 1;


def divid(n):
    if lit[n] != 0:
        return lit[n];
    if n % 3 == 0 and n % 2 == 0:
        lit[n] = min(divid(int(n/3))+1, divid(int(n/2))+1, divid(n-1)+1);
    if n % 3 == 0 and n % 2 != 0:
        lit[n] = min(divid(int(n/3))+1, divid(n-1)+1);
    if n % 3 != 0 and n % 2 == 0:
        lit[n] = min(divid(int(n/2))+1, divid(n-1)+1);
    else :
        lit[n] = divid(n-1) + 1;

print(divid(a));