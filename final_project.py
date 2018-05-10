import sentiments as pro

i=1

while i == 1:
    text = input("Enter the day in format day,hour like 1,12:	");

    print(pro.sentiment(text))
    i=int(input("Enter 1 to try more comments: "))
