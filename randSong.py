import os, random;
f = os.path.dirname(os.path.abspath(__file__));
c = os.listdir(f);
c = list(filter(lambda s: s.endswith(".mp3"), c));
for i in range(int(input("AMOUNT "))):
    r = random.choice(c);
    c.remove(r);
    print(r);