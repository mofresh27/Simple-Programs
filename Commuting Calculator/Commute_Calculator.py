def commute_calulator():
    lifx = int(input("How many years do you plan on commuting?\n"))

    try:
     
            
        days = 261 * 24 
        commute = 2/24 

        # print ( days)
        # print ( commute)

        life = (lifx * days) * commute

        time = life/261
        daysx = time * 8 
        years = daysx/365
        hours = time * 24



        print ("You will spend approximatley", time, "days commuting to work.")
        print ("That is equal to", daysx,"workdays.")
        print ( "Which is", years, " years,")
        print ("and......", hours ,"hours.")
        print("                                          ")

        print("That is too much time wasted, go find your beach!")

    except ValueError:
        print("Invalid Entry, please use a whole number")
        print("******************************************************")
        print("[][]][[][][][][][][][][[]][][][][[]][][][][][]][][][][]")
        print("                                          ")
        print("                                          ")
        print("                                          ")


        commute_calulator()
    





commute_calulator()