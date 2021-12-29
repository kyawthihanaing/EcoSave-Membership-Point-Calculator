#Name:KYAW THIHA NAING
#ID:B1901850

#Question 1:

#Task 1

#sys library is imported so that the user can quit the program using 'Q' or 'q' options
import sys                    
def inputDetails():
    
    print()
    print("Please input your details below:")
    userName= input("Name:")
    age= eval(input("Age:"))
    gender= str(input("Gender[F/M]:"))
    paperQuantity= eval(input("Paper Quantity [kg]:"))
    plasticQuantity= eval(input("Plastic Quantity [kg]:"))
    oilQuantity= eval(input("Oil Quantity [bottle]:"))
    electricQuantity= eval(input("Electrical [unit]:"))

    return userName, gender, age, paperQuantity, plasticQuantity, + \
    oilQuantity, electricQuantity

def menu():

    print()
    print("Choose your option below:")
    print("1 - Points Calculator")
    print("2 - Membership Tier")
    print("3 - Reset")
    print("Q/q - Quit")

    alloptions = ['1','2','3','Q','q']
    
    choice = input("Your choice? ")

    #The user chose an invalid option. Their input is being asked again.
    
    while choice not in alloptions:
        print()
        print("Invalid choice! Please select from the list of choices.")
        print()
        print("Choose your option below: ")
        print("1 - Points Calculator")
        print("2 - Membership Tier")
        print("3 - Reset")
        print("Q/q - Quit")
        choice = input("Your choice? ")   
        
    return choice

def pointCalculator(paperQuantity, plasticQuantity, oilQuantity, electricQuantity):
    
    collectorPoint= (paperQuantity*30)+(plasticQuantity*50)+(oilQuantity*70)+(electricQuantity*90)
    recyclerPoint= (paperQuantity*40)+(plasticQuantity*60)+(oilQuantity*80)+(electricQuantity*100)

    return collectorPoint, recyclerPoint

def viewMembership(collectorPoint, recyclerPoint):

    #Conditions required for each status is implemented using if and elif statements
    
    if collectorPoint >= 1000:
        status = "ecowarrior"

    elif collectorPoint >= 800 and collectorPoint < 1000:
        remainingPoint = 1000 - collectorPoint
        status = "ecohero"

    elif collectorPoint >= 500 and collectorPoint < 800:
        remainingPoint = 800 - collectorPoint
        status = "ecosaver"

    elif collectorPoint >= 0 and collectorPoint < 500:
        remainingPoint = 500 - collectorPoint
        status = "nostatus"

    elif recyclerPoint >= 1000:
        status = "ecowarrior"

    elif recyclerPoint >= 800 and recyclerPoint < 1000:
        remainingPoint = 1000 - recyclerPoint     
        status = "ecohero"

    elif recyclerPoint >= 500 and recyclerPoint < 800:
        remainingPoint = 800 - recyclerPoint
        status = "ecosaver"
  
    elif recyclerPoint >= 0 and recyclerPoint < 500:
        remainingPoint = 500 - recyclerPoint
        status = "nostatus"
        
    return status, remainingPoint

def main():
    print()
    print("Hello there!")
    print("Welcome to Ecosave's Membership Status Program!")

    userName, gender, age, paperQuantity, plasticQuantity, oilQuantity, electricQuantity= inputDetails()
    specificoptions= ['Q','q']

    choice = menu()
    
    store1,store2 = None, None

    #While loop is used so that user can still continue to use the program until he/she decides to quit.
    
    while True:

        #The condition below will allow the user to quit as sys.exit() function is used from the imported sys library.
        
        if choice in specificoptions:
            print()
            print("Thank you for using this program.")

            sys.exit()

        #The condition below will carry out the point calculation if user chose 1.
            
        elif choice == '1':

            collectorPoint, recyclerPoint= pointCalculator(paperQuantity, plasticQuantity, oilQuantity, electricQuantity)
            print()
            print("Choose your option below: ")
            print("1 - collector")
            print("2 - recycler")

            choice2A= input("Your choice? ")

            #Either one of the two conditions below will be executed according to what the user chose for choice2A
            
            if choice2A == '1':
                print()
                print("Collector "+userName+" earned",int(collectorPoint),"points.")
                store1 = collectorPoint
                choice = menu()

            elif choice2A == '2':
                print()
                print("Recycler "+userName+" earned",int(recyclerPoint),"points.")
                store2 = recyclerPoint
                choice = menu()

        #The condition below will allow the user to view membership status.
                
        elif choice == '2':
            
            status, remainingPoint = viewMembership(collectorPoint, recyclerPoint)
            
            tierpos= ["Eco saver", "Eco Hero", "Eco Warrior"]
            
            print()
            print("Choose your option below: ")
            print("1 - collector")
            print("2 - recycler")

            choice2B= input("Your choice? ")

            #The condition below will allow the user to view membership status for collector.
            
            if choice2B == '1':

                #The condition below is applied when the user chose to calculate collector points.
                
                if choice2A == '1':

                    if status == "nostatus":
                        print()
                        print("Collector "+userName+" does not meet the minimum required points. Collect another",int(remainingPoint),"points to become the "+"\""+tierpos[0]+"\""+".")
                        choice = menu()
                        
                    elif status == "ecosaver":
                        print()
                        print("Congratulations! Collector "+userName+" is the "+"\""+tierpos[0]+"\""+"."+" Collect another",int(remainingPoint),"points to become the "+"\""+tierpos[1]+"\""+".")
                        choice = menu()
                        
                    elif status == "ecohero":
                        print()
                        print("Congratulations! Collector "+userName+" is the "+"\""+tierpos[1]+"\""+"."+" Collect another",int(remainingPoint),"points to become the "+"\""+tierpos[2]+"\""+".")
                        choice = menu()
                        
                    elif status == "ecowarrior":
                        print()
                        print("Congratulations! Collector "+userName+" is now the "+"\""+tierpos[2]+"\""+".")
                        choice = menu()

                #The condition below is applied when the user chose to calculate recycler points.
                        
                elif choice2A == '2':

                    #The condition below is applied when the user didn't choose to calculate collector points when going back to the menu.
                    #Store 1 will remain null.
                    
                    if store1 is None:
                        print()
                        print("There is no collector point.")
                        choice = menu()

                    #The condition below is applied when the user chose to calculate collector points when going back to the menu.
                    
                    elif store1 is not None:
                        
                        if status == "nostatus":
                            print()
                            print("Collector "+userName+" does not meet the minimum required points. Collect another",int(remainingPoint),"points to become the "+"\""+tierpos[0]+"\""+".")
                            choice = menu()
                        
                        elif status == "ecosaver":
                            print()
                            print("Congratulations! Collector "+userName+" is the "+"\""+tierpos[0]+"\""+"."+" Collect another",int(remainingPoint),"points to become the "+"\""+tierpos[1]+"\""+".")
                            choice = menu()
                            
                        elif status == "ecohero":
                            print()
                            print("Congratulations! Collector "+userName+" is the "+"\""+tierpos[1]+"\""+"."+" Collect another",int(remainingPoint),"points to become the "+"\""+tierpos[2]+"\""+".")
                            choice = menu()
                            
                        elif status == "ecowarrior":
                            print()
                            print("Congratulations! Collector "+userName+" is now the "+"\""+tierpos[2]+"\""+".")
                            choice = menu()

            #The condition below will allow user to view membership status for recycler.
            
            elif choice2B == '2':

                #The condition below is applied when the user chose to calculate recycler points.
                
                if choice2A == '2':

                    recyclerPoint= (paperQuantity*40)+(plasticQuantity*60)+(oilQuantity*80)+(electricQuantity*100)
                    
                    if recyclerPoint >= 1000:
                        status = "ecowarrior"
                        print()
                        print("Congratulations! Recycler "+userName+" is now the "+"\""+tierpos[2]+"\""+".")
                        choice = menu()

                    elif recyclerPoint >= 800 and recyclerPoint < 1000:
                        remainingPoint = 1000 - recyclerPoint     
                        status = "ecohero"
                        print()
                        print("Congratulations! Recycler "+userName+" is the "+"\""+tierpos[1]+"\""+"."+" Collect another",int(remainingPoint),"points to become the "+"\""+tierpos[2]+"\""+".")
                        choice = menu()

                    elif recyclerPoint >= 500 and recyclerPoint < 800:
                        remainingPoint = 800 - recyclerPoint
                        status = "ecosaver"
                        print()
                        print("Congratulations! Recycler "+userName+" is the "+"\""+tierpos[0]+"\""+"."+" Collect another",int(remainingPoint),"points to become the "+"\""+tierpos[1]+"\""+".")
                        choice = menu()
                        
                    elif recyclerPoint < 500:
                        remainingPoint = 500 - recyclerPoint
                        status = "nostatus"
                        print()
                        print("Recycler "+userName+" does not meet the minimum required points. Collect another",int(remainingPoint),"points to become the "+"\""+tierpos[0]+"\""+".")
                        choice = menu()

                #The condition below is applied when the user chose to calculate collector points.
                
                elif choice2A == '1':

                    #The condition below is applied when the user didn't choose to calculate recycler points when going back to the menu.
                    #Store2 will remain null.

                    if store2 is None:
                        print()
                        print("There is no recycler point.")
                        choice = menu()

                    #The condition below is applied when the user chose to calculate recycler points when going back to the menu.
                        
                    elif store2 is not None:

                        recyclerPoint= (paperQuantity*40)+(plasticQuantity*60)+(oilQuantity*80)+(electricQuantity*100)
                        
                        if recyclerPoint >= 1000:
                            status = "ecowarrior"
                            print()
                            print("Congratulations! Recycler "+userName+" is now the "+"\""+tierpos[2]+"\""+".")
                            choice = menu()

                        elif recyclerPoint >= 800 and recyclerPoint < 1000:
                            remainingPoint = 1000 - recyclerPoint     
                            status = "ecohero"
                            print()
                            print("Congratulations! Recycler "+userName+" is the "+"\""+tierpos[1]+"\""+"."+" Collect another",int(remainingPoint),"points to become the "+"\""+tierpos[2]+"\""+".")
                            choice = menu()

                        elif recyclerPoint >= 500 and recyclerPoint < 800:
                            remainingPoint = 800 - recyclerPoint
                            status = "ecosaver"
                            print()
                            print("Congratulations! Recycler "+userName+" is the "+"\""+tierpos[0]+"\""+"."+" Collect another",int(remainingPoint),"points to become the "+"\""+tierpos[1]+"\""+".")
                            choice = menu()
                            
                        elif recyclerPoint < 500:
                            remainingPoint = 500 - recyclerPoint
                            status = "nostatus"
                            print()
                            print("Recycler "+userName+" does not meet the minimum required points. Collect another",int(remainingPoint),"points to become the "+"\""+tierpos[0]+"\""+".")
                            choice = menu()

        #The condition below will allow user to reset all information.   
        elif choice == '3':
            print()
            print("All information has been reset.")
            main()
main()

    


            
            
            
            
        
          

         
        
              

        
        

