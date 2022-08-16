lines=[]
while True:
    s=input("Enter the characters : ")
    if s:
        lines.append(s.upper())
    else:
        break;
for sentence in lines:
    print(sentence)
    
