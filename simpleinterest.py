def simInt(principal, intrest, time):
    return (principal*intrest*time)/100

if __name__ == "__main__":
    p = int(input("Enter principal amount"))
    i = int(input("Enter intrest"))
    t = int(input("Enter time"))

    print("Simple intrest: ", simInt(p,i,t))