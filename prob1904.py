a = int(input());

lit = [0] * 1000001;

lit[1] = 1;
lit[2] = 2;
lit[3] = 3;
lit[4] = 5;

for i in range(5,len(lit)):
    lit[i] = (lit[i-1] + lit[i-2]) % 15746;


print(lit[a]);

