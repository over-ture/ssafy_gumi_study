text = input()
if text == ' ' :
    print(0)
else : 
    text = text.strip()
    text = text.split(" ")
    cnt = 0
    for i in text :
        cnt += 1 

    print(cnt)