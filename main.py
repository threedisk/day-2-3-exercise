# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
line = "============"
new_age = int(age)
total_age_day = 90 * 365
left_age_day = total_age_day - new_age * 365
#print (f"Total age day : {total_age_day} days" )
#print (f"Left age day : {left_age_day} days")
#print (line)

total_age_week = 90 * 52
left_age_week = total_age_week - new_age * 52
#print (f"Total age week :{total_age_week} weeks")
#print (f"Left age week :{left_age_week} weeks")
#print (line)

total_age_month = 90 * 12
left_age_month = total_age_month - new_age * 12
#print (f"Total age month :{total_age_month} months")
#print (f"Left age month :{left_age_month} months")
#print (line)

print (f"You have {left_age_day} days, {left_age_week} weeks, {left_age_month} months left")





