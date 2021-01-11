#Print leap year between two given years
print("prit leap year between two given years")
print("enter start year")
startyear=int(input())
print ("enter last year")
lastyear=int(input())
print("list of leap years")
#loop through between the start and last year
for year in range (startyear,lastyear):
#check if the year is a leap year if yes print
 if((year%4==0) and (year%100!=0)or(year%400==0)):
    print (year)
