import sys

a = int(sys.stdin.readline());
lit = [0 for i in range(301)];

for i in range(a):
    b = int(sys.stdin.readline());
    lit[i] = b;

scores = [0 for i in range(301)];

scores[0] = lit[0];
scores[1] = lit[0] + lit[1];
scores[2] = max(lit[0] + lit[2], lit[1] + lit[2]);

for i in range(3,a):
    scores[i] = max(scores[i-3] + lit[i-1] + lit[i], scores[i-2] + lit[i]);

print(scores[a-1]);

