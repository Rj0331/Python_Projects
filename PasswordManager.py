Master_pwd = input ("What is the Master Password?\n")

def view():
    with open('password.txt','r') as f:
       for line in f.readlines():
        data = line
        user , passw = data.split("|")
        print("User : ", user , " Password : ", passw)


def add():
    name = input("Enter the username : ")
    pwd = input("Enter the password : ")
    with open('password.txt','a') as f:
        f.write(name + "|" + pwd + "\n")

while (True):
    mode = input("Do you want to add a new Password or view previous ones(view, add)? Press q to quit\n").lower()
    if mode == "q":
        break

    if mode == "view":
        view()


    elif mode == "add":
        add()


    else:
        print("Invalid Mode.")
        continue
