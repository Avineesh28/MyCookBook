import re
email=[];
uname=[];
pwd=[];
c=input();
while(1):
    if c=="1":
        while(1):
            s=input("Email:\t");
            if re.match("^[a-z0-9._]*@[a-z]*[\.][a-z]*[\.a-z]?$",s):
                email.append(s)
                s=input("Username:\t");
                flag=0;
                for i in range(len(uname)):
                    if uname[i]==s:
                        flag+=1;
                        break;
                if flag==0:
                    uname.append(s);
                    s=input("Password:\t")
                    if len(s)>5 and len(s)<14:
                        pwd.append(s)
                        break;
                    else:
                        email.pop(len(email)-1)
                        uname.pop(len(uname)-1)
                        print("Password Invalid\n")
                else:
                    email.pop(len(email)-1)
                    print("This Username has already been taken please choose a different Username\n");
            else:
                print("Please enter valid email-id\n")
    elif c=="2":
           s=input("Username:\t")
           p=input("Password:\t")
           f=0;
           for i in range(len(uname)):
                if uname[i]==s:
                    if pwd[i]==p:
                        print("Welcome!")
                    else:
                        print("Incorrect Password\n")
                    f+=1
           if f==0:
               print("Username Not Found\n")
        
    else:
        break;
    c=input()
    
        
