science = set()
commerce = set()
arts = set()


while True:
    print("----MENU----")
    print("1.Display Members.")
    print("2.Show All unique Members.")
    print("3.Show All Common Members.")
    print("4.Add Member.")
    print("5.Remove Member.")
    print("6.Cheak Membership.")
    print("7.Count Members.")
    print("8.Exit")
    print()
    choice = int(input("Enter Your Choice:"))

    if choice == 1:
        print(f"Science : {science}")
        print(f"Commerce : {commerce}")
        print(f"Arts : {arts}")

    elif choice == 2:
        print("All Unique Members :",science | commerce | arts)

    elif choice == 3:
        print("All Common Members :",science & commerce & arts)

    elif choice == 4:      
        mem_name.lower() = input("Enter Member Name :")
        club_choice = input("Enter Club name to join ? (Science ,Commerce or Arts):")

        if club_choice.lower() == "science":
            science.add(mem_name)
        elif club_choice.lower() == "commerce":
            commerce.add(mem_name)
        elif club_choice.lower() == "arts":
            arts.add(mem_name)
        else:
            print("Invalid club name.")

        print("Member Added Successfully in ",club_choice)

    elif choice == 5:
        mem_name.lower() = input("Enter Member Name to Delete :")
        club_choice = input("Enter Club name (Science ,Commerce or Arts):")

        if club_choice.lower() == "science" or "Science":
            science.discard(mem_name)
        elif club_choice.lower() == "commerce" or "Commerce":
            commerce.discard(mem_name)
        elif club_choice.lower() == "arts" or "Arts":
            arts.discard(mem_name)

        print("Member removed Successfully from ",club_choice)

    elif choice == 6:
        mem_name = input("Enter Member Name:")
        mem_name.lower()
        if mem_name in science:
            print(f"{mem_name} has membership in Science Club.")
        elif mem_name in commerce:
            print(f"{mem_name} has membership in Commerce Club.")
        elif mem_name in arts:
            print(f"{mem_name} has membership in Art Club.")
        else:
            print(f"{mem_name} has not ny membership.")
            

    elif choice == 7:
        print("Members in Science Club:",len(science))
        print("Members in Commerce Club:",len(commerce))
        print("Members in Art Club:",len(arts))
        print("Total number of Members are:",len(science)+len(commerce)+len(arts))

    elif choice == 8:
        print("Exiting From The Program....")
        break

    else:
        print("Invalid Choice .")
        print("Enter Choice Agian.")
        continue


    

            
        



























