count = 0
step = 2
diag = 0
i = 1
while 1 < 2:
    diag += i
    count += 1
    i += step
    if count % 4 == 0:
        step += 2
    if step == 1002:
        diag += i
        break
print(diag)
