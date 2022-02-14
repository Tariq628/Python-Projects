while True:
    dic = {"21/01/2000":"Tariq", "21/03/2000":"Umair", "31/02/2000":"Ahmed", "30/02/2000":"Daniyal"}
    date = input("Enter the date of birth dd-mm-yyyy: ")
    list = date.split("-")
    # print(list)
    list = "/".join(list)
    # print(list)
    if list in dic.keys():
        print(f"This date of Birth {list} is {dic[list]}\n")
    press = input("Press stop to break-- ")
    if press == "stop":
        break