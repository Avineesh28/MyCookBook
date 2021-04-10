#Assuming absolute Data base consisiting of a dictionary with dishes linked to all their ingredients
#the value of c depends on the stimuli recieved from the front end based on users choice that determines which part of code is activiated
bookmarks={};
c=(int)(input());
while(1):
    if c==1:                                      #To bookmark a recipe
        s=input("Username:\t")
        c=input("Dish Name\t")
        f=0
        for i in bookmarks.keys():
           if i==s:
               f+=1
        if f==0:
            bookmarks[s]=[c]
        else:
            bookmarks[s].append(c)
    elif c==2:                                    #To access all bookmarks
        s=input("Username:\t")
        f=0;
        for i in bookmarks.keys():
           if i==s:
               f+=1
        if f==0:
            print("Invalid Username")
        else:
            print(s+"'s Bookmarks\n")
            l=bookmarks[s]
            for i in range(len(l)):
                print((str)(i+1)+"-->\t"+(str)(l[i]))
            t=(int)(input("Choose Dish (0 to exit)"))
            if t==0:
                break;
            else:
                dish=l[t-1]
                #Further details of the Dish can be obtained by gaining access to the absolute database of dishes and their ingridients
                #In real time on choosing any of the dishes the backend communicates to the front end to proceed to that part of the web application
            
    elif c==3:                                    #To delete all ratings
       print("All bookmarks Cleared")
       bookmarks.clear()
    else:
        print("Redirecting\n")
        break;
        #exit to home screen
    c=(int)(input())
