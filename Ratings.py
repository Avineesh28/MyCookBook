rating={};
c=(int)(input());
while(1):
    if c==1:                                      #To rate a posted Cuisine/Recipe
        s=input("Dish Name:\t")
        c=(float)(input("Give your rating out of 5\n"))
        if(c<0.0 or c>5.0):
            print("Invalid Rating")
            continue
        f=0
        for i in review.keys():
           if i==s:
               f+=1
        if f==0:
            rating[s]=[c]
        else:
            rating[s].append(c)
    elif c==2:                                    #To find the average rating
        s=input("Dish Name:\t")
        f=0;
        for i in rating.keys():
           if i==s:
               f+=1
        if f==0:
            print("Invalid Dish Name")
        else:
            sum=0
            for i in rating[s]:
                sum+=i;
            sum=sum/len(rating[s])
            print("Average Rating:\t"+sum)
    elif c==3:                                    #To Display all ratings
        for i in review.keys():
            print("\n"+i+":-->")
            for j in review[i]:
                print(j+"\t")
    elif c==4:                                    #To delete all ratings
       print("All Ratings Cleared")
       rating.clear()
    else:
        print("Redirecting\n")
        break;
        #exit to home screen
    c=(int)(input())