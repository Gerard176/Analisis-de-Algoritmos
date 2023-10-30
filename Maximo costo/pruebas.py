import random

rep = 0
vol = 50  # mejor solucion
v = vol

if v > 26:
    v = 0

print(vol)
while rep < 20:
    r = random.randint(0, 9)
    print("Rand:", r)
    if vol < 26:
        vol = vol + r
    else:
        vol = vol - r
        print("restando:", vol)

    if vol > v and vol <= 26:
        v = vol
        print("mejoro:", vol)
    
    rep = rep + 1

print("mejor valor:", v)
print(vol)
        
           