f=open("worldlist.txt","w+")
namef=input("enter First name:")
namel=input("last name:")
namem=input("sur name:")
dad=input("your father name:")
mom=input("enter your mother name:")
phone=input("phone no:")
while(len(phone)!=10):
     phone=input("enter correct phone no")
dobday=int(input("enter day of birth:"))
while(dobday<0 or dobday>31):
     dobday=int(input("enter correct day of birth:"))
dobm=int(input("enter month of birth in number's :"))
while(dobm<0 or dobm>12):
     dobm=int(input("enter month of birth in number's :"))
yeart=input("enter your year of birth:")
love1=input("name of u r crush or love::")
love2=input("name of u r crush or love:")
love3=input("name of the most likes word: ")
email=input("Enter your email:")


#word.title() for fist word in caps
f.write("%s\n" %(namef))
#f.close()
if(namel!=''):
     pwd=namef+namem+namel
     f.write("%s\n" %(pwd))

     pwd=namem.upper()+namef+namel
     f.write("%s\n" %(pwd))
     pwd=namem.upper()+namef
     f.write("%s\n" %(pwd))

     pwd=dad+mom
     f.write("%s\n" %(pwd))
     pwd=dad.title()+mom
     f.write("%s\n" %(pwd))

     pwd=phone+dad[0]+namef[0]+namel[0]
     f.write("%s\n" %(pwd))
     pwd=phone+dad[0].upper()+namef[0]+namel[0]
     f.write("%s\n" %(pwd))
     pwd=phone
     f.write("%s\n" %(pwd))

     pwd=namef.title()+namel+str(yeart)
     f.write("%s\n" %(pwd))
     pwd=namem.upper()+namef+namel+str(yeart)
     f.write("%s\n"%(pwd))
else:
     pwd=namef+namem
     f.write("%s\n" %(pwd))

     pwd=namem.upper()+namef
     f.write("%s\n" %(pwd))
     pwd=namem.upper()+namef
     f.write("%s\n" %(pwd))

     pwd=dad+mom
     f.write("%s\n" %(pwd))
     pwd=dad.title()+mom
     f.write("%s\n" %(pwd))

     pwd=phone+dad[0]+namef[0]
     f.write("%s\n" %(pwd))
     pwd=phone+dad[0].upper()+namef[0]
     f.write("%s\n" %(pwd))
     pwd=phone
     f.write("%s\n" %(pwd))

     pwd=namef.title()+namel+str(yeart)
     f.write("%s\n" %(pwd))
     pwd=namem.upper()+namef+namel+str(yeart)
     f.write("%s\n"%(pwd))

pwd=dad[0]+namef[0]+namem[0]+phone
f.write("%s\n" %(pwd))
pwd=dad[0].upper()+namef[0]+namem[0]+phone
f.write("%s\n"%(pwd))

pwd=namef+'@'+str(yeart)
f.write("%s\n" %(pwd))
pwd=namef.title()+'@'+str(yeart)
f.write("%s\n" %(pwd))

pwd=namef+'+'+str(dobday)+str(dobm)+str(yeart)
f.write("%s\n" %(pwd))

pwd=namef.title()+'+'+str(dobday)+str(dobm)+str(yeart)
f.write("%s\n" %(pwd))

pwd=namef+'+'+str(dobday)+str(dobm)+str(yeart[2:])
f.write("%s\n" %(pwd))

pwd=namef.title()+'+'+str(dobday)+str(dobm)+str(yeart[2:])
f.write("%s\n" %(pwd))

pwd=str(dobday)+str(dobm)+str(yeart)
f.write("%s\n" %(pwd))
pwd=str(dobday)+str(dobm)+str(yeart[2:])
f.write("%s\n" %(pwd))

# love

pwd=love1+namef
f.write("%s\n" %(pwd))

pwd=love1.title()+namef
f.write("%s\n" %(pwd))

pwd=love1+namef+love2
f.write("%s\n" %(pwd))

pwd=love2.title()+namef
f.write("%s\n" %(pwd))

pwd=love2.title()+namef
f.write("%s\n" %(pwd))

pwd=love1+love2
f.write("%s\n" %(pwd))

pwd=namef+love1+love2
f.write("%s\n" %(pwd))

#email
x=0
for i in email:
     if(i=='@'):
          f.write("%s" %(i))
          f.write("%s" %email[:x])
          a=email[:x]+str(yeart)
          b=email[:x]+str(dobday)
          c=email[:x]+str(dobday)+str(dobm)
          d=email[:x]+str(dobday)+str(dobm)+str(yeart)
          f.write("%s\n" %(a))
          f.write("%s\n" %(b))
          f.write("%s\n" %(c))
          f.write("%s\n" %(d))
     else:
          f.write("\n")
          break
     x=x+1

f.close()
