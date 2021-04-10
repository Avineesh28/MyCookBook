review={};
c=(int)(input());
while(1):
    if c==1:                                      #Just to Comment/Share personal Experiance/Suggestions/Alternatives by Users
        s=input("Username:\t")
        c=input("Type Your Comment here\n")
        f=0
        for i in review.keys():
           if i==s:
               f+=1
        if f==0:
            review[s]=[c]
        else:
            review[s].append(c)
    elif c==2:                                    #To find out all the comments ever made by a given user
        s=input("Enter Username to be searched:\t")
        #Linear search
        f=0
        l=review.keys()
        for i in l:
            if s==i:
                f+=1
                break;
        if f==0:
            print("No such Username Found\n")
        else:
            for i in review[s]:
                print("-->\t"+i+"\n")
    elif c==3:                                    #To Display all comments
        for i in review.keys():
            print("\n"+i+":")
            for j in review[i]:
                print("-->\t"+j+"\t")
    elif c==4:                                    #To delete all comments
       print("All History Cleared")
       review.clear()
    elif c==5:                                    #To delete all the comments by a particular user
        s=input("Username to be Banned:\t")
        f=0
        for i in review.keys():
           if i==s:
               f+=1
               break;
        if f==0:
            print("No such Username present\n")
        else:
            review.pop(s) 
    else:
        print("Redirecting\n")
        break;
        #exit to home screen
    c=(int)(input())
