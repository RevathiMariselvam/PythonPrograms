import pymongo

connect=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=connect["MovieTicketBooking"]
mycol=mydb["Movie_Theater_Time_Seats_List"]

data=[{"movie":"Beast","theater":"Balaji",
       "showtime_seats":[{"show":"morning_show","seats":"30"},{"show":"matinee","seats":"30"},
                         {"show":"first_show","seats":"30"},{"show":"night_show","seats":"30"}]},
      {"movie":"Vikram","theater":"PVR_Cinemas",
       "showtime_seats":[{"show":"morning_show","seats":"30"},{"show":"matinee","seats":"30"},
                         {"show":"first_show","seats":"30"},{"show":"night_show","seats":"30"}]},
      {"movie":"RRR","theater":"Raja",
       "showtime_seats":[{"show":"morning_show","seats":"30"},{"show":"matinee","seats":"30"},
                         {"show":"first_show","seats":"30"},{"show":"night_show","seats":"30"}]},
      {"movie":"Beast","theater":"PVR_Cinemas",
       "showtime_seats":[{"show":"morning_show","seats":"30"},{"show":"matinee","seats":"30"},
                         {"show":"first_show","seats":"30"},{"show":"night_show","seats":"30"}]},
      {"movie":"Vikram","theater":"Balaji",
       "showtime_seats":[{"show":"morning_show","seats":"30"},{"show":"matinee","seats":"30"},
                         {"show":"first_show","seats":"30"},{"show":"night_show","seats":"30"}]},
      {"movie":"RRR","theater":"PVR_Cinemas",
       "showtime_seats":[{"show":"morning_show","seats":"30"},{"show":"matinee","seats":"30"},
                         {"show":"first_show","seats":"30"},{"show":"night_show","seats":"30"}]},
      ]

##for x in mycol.find({},{"_id": 0,"movie":1,"theater":1,"showtime_seats":1}):
##    print(x)

##for x in mycol.find({},{"_id":0,"showtime_seats":1}):
##    for y in x["showtime_seats"]:
##        print(y["morning_show"])


print("Movie List")
print("1. Beast")
print("2. Vikram")
print("3. RRR")
choice=int(input("Enter your Choice for Movie: "))
if(choice==1):
    movie_name="Beast"
elif(choice==2):
    movie_name="Vikram"
elif(choice==3):
    movie_name="RRR"
else:
    print("Enter the Correct Choice of Movie\n")

temp_theater=[]

for x in mycol.find({},{"_id": 0,"movie":1,"theater":1}):
    if x["movie"]==movie_name:
        temp_theater.append(x["theater"])
print("\nTheater List")
for i in range(0,len(temp_theater)):
    print(f"{i+1}.", temp_theater[i])
choice_theater=int(input("Enter the Choice for Theatre: "))

if(choice_theater<=len(temp_theater)):
    movie_theater=temp_theater[choice_theater-1]
else:
    print("Enter the Correct Choice of Movie\n")

print("\nShow Timings")
print("1. Morning Show Time at 9:00 AM")
print("2. Matinee Show Time at 2:00 PM")
print("3. First Show Time at 6:00 PM")
print("4. Night Show Time at 9:00 PM")
choice_time=int(input("Enter the Choice for the Movie Time:"))
if(choice_time==1):
    movie_time="morning_show"
elif(choice_time==2):
    movie_time="matinee"
elif(choice_time==3):
    movie_time="first_show"
elif(choice_time==4):
    movie_time="night_show"
else:
    print("Enter the Correct Choice of Show Time\n")
 
myquery={"movie":movie_name,"theater":movie_theater}

for x in mycol.find(myquery):
    for y in x["showtime_seats"]:
        if(y["show"]==movie_time):
            total_seats=y["seats"]
            
print("Total No.of Seats Availability:",total_seats)
seats=input("Enter the No. of Seats for Booking:")
print("")
if(total_seats>=seats):
    left_over_seats=int(total_seats)-int(seats)
    if(left_over_seats<0):
        print("Only Limited seats available")
    else:
        old_value={"movie":movie_name,"theater":movie_theater,"showtime_seats.show":movie_time}
        new_value={"$set":{"showtime_seats.$.seats":str(left_over_seats)}}
        mycol.update_one(old_value,new_value)
        print("Yours seats are Booked Now")
elif(total_seats==0):
    print("Sorry, No Seats Available")


