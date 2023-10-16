import turtle
from datetime import datetime
import time
import math

frame = turtle.Turtle() # First turtle object created which we will use to create base structure of watch
radius = 140            #size of circle which will be used for watch
frame.speed(0)          #fastest speed of turtle
frame.hideturtle()      #dont want to show the head/arrow of turtle

second_needle_length = 100      #length of second needle
minute_needle_length = 90       #length of minute needle
hour_needle_length = 70         #length of hour needle
angle_shift_per_second = 6      #Turtle works on angle so there is a 360 degree angle but clock has 60 points
                                #so dividing 360/60 gives us 6 which mean for every one movement we want to
                                #rotate its angle 6 degree

seconds = turtle.Turtle()       #seperate turtle for second hand
seconds.hideturtle()            #hiding turtle for second hand

minutes = turtle.Turtle()       #seperate turtle for minute hand
minutes.hideturtle()            #hiding turtle for minute hand

hours = turtle.Turtle()         #seperate turtle for hour hand
hours.hideturtle()              #hiding turtle for hour hand

# function for creating circle and adding number below it
def circle(colour,angle,number):
    frame.penup()               #pen up is used when we dont want to show the trace of turtle movement 
    frame.forward(100)          #move forward 100 units
    frame.right(90)             #change direction to 90 degree so circle should be created from center
    frame.pendown()             #pen down when we want to turtle to show the trace of movement
    frame.color(colour)         #colour which will be used
    frame.begin_fill()          #filling the shape with colour which will be created in future
    frame.circle(5)             #creating circle shape
    frame.end_fill()            #stop filling the colour when shape is created
    frame.penup()               
    frame.left(90)              #when circle is created turn turtle head towards inside of circle
    frame.forward(2.5)          #move 2.5 inside this pointer circle
    type_number(angle,number)
    frame.backward(2.5)         #moveout from circle again
    if number == 12:            #when we type 12 we need to type some extra text also
        frame.backward(40)      #come downwards
        frame.left(90)          #turn left
        frame.forward(5)        #move towards left so text could allign with 12
        frame.color("red")      
        frame.write("CDU")
        frame.backward(5)       #coming back to position from where we come downwards
        frame.right(90)         #moving right so we can go up again
        frame.forward(40)       #go upwards towards pointer of 12 number
    frame.backward(100)


def type_number(angle,number):
    frame.left(angle)           #after coming inside circle turn its head towards left
    frame.backward(22)          #then moving it downward so it can come how much down it should come for typing number
    frame.right(90)             #moving head right side so number could be written more precisely below pointer
    forward_backward(number)    #for pointer on right side we want to move forward to get below pointer but for
                                #for pointer on left side we want to move backward to get below pointer 
    frame.left(90)              #after writing number and coming back to same position turn left
    frame.forward(22)           #we moved downward for typing number now we are moving forward again to come at
                                #center of pointer circle again
    frame.right(angle)          #turn same degree as we turned before coming downward from pointer

def forward_backward(number):   #number as parameter which we want to type 
    frame.color("black")        #assigning the colour to black for pointers
    forward = [3,4,5]
    backward = [7,8,9]
    extra_backward = [10,11,12]
    if number in forward:       #for number which we want to move forward
        frame.forward(2.5)      #moving forward
        frame.write(number)     #writing number
        frame.backward(2.5)     #moving backward again to come at same position
    elif number in backward:    #for number which we want to move backward
        frame.backward(2.5)     
        frame.write(number)
        frame.forward(2.5)      
    elif number in extra_backward: #for number which we want to move backward more then normal
        frame.backward(3.5)
        frame.write(number)
        frame.forward(3.5)
    else:                       #such as for 1,2,6 we dont want to move we just write the number
        frame.write(number)

# Function to creating outer circle of clock
def outer_circle():             
    frame.right(90)             #turning turtle downwards
    frame.penup()           
    frame.forward(radius)       #moving forward to start creating circle       
    frame.left(90)
    frame.pendown()
    frame.circle(radius)        #creating circle of 140 radius
    frame.penup()
    frame.right(90)
    frame.backward(radius)      #moving backward to start creating circle

# setting default states of needles
def needles_intial_configuration():
    now = datetime.now()        #getting system time
    current_time = now.strftime("%I:%M:%S")     #format of time Hours in 12 Hour, Minutes and Seconds
    time_values = current_time.split(":")       #Seperating Hour,Minute,Second by using : because its between them           

    #converting hours,minutes and seconds to integer  
    time_values[0] = int(time_values[0])
    time_values[1] = int(time_values[1])
    time_values[2] = int(time_values[2])

    # how much angle every handle needs to move is being calculated
    time_values[0] = (time_values[0] * angle_shift_per_second * 5) + (math.floor((time_values[1] * angle_shift_per_second)/72)*6)
    time_values[1] = time_values[1] * angle_shift_per_second
    time_values[2] = time_values[2] * angle_shift_per_second

    hours.speed(0)  # hours
    hours.width(7)  #width of handle
    hours.color("green")
    hours.left(90)                  #rotating turtle upwards
    hours.right(time_values[0])     #turning at right degree
    hours.forward(hour_needle_length)   #moving forward to create hours hand
    hours.backward(hour_needle_length)  

    minutes.speed(0)  # minutes
    minutes.width(4)
    minutes.color("red")
    minutes.left(90)
    minutes.right(time_values[1])
    minutes.forward(minute_needle_length)
    minutes.backward(minute_needle_length)

    seconds.speed(0)  # seconds
    seconds.width(2)
    seconds.goto(0, 0)      #move towards center of page
    seconds.left(90)        #rotating turtle upwards
    seconds.right(time_values[2])
    seconds.forward(second_needle_length)
    seconds.backward(second_needle_length)
    
def hour_needle_rotate(angle):
    hours.clear()               #clear all frames created by hour hand
    hours.setheading(90)        #set head upwards
    hours.right(angle)          #rotate at angle
    hours.forward(hour_needle_length)
    hours.backward(hour_needle_length)

def minutes_needle_rotate(angle):
    minutes.clear()             #clear all frames created by minute hand
    minutes.setheading(90)      #set head upwards 
    minutes.right(angle)        #rotate at angle
    minutes.forward(minute_needle_length)
    minutes.backward(minute_needle_length)

def seconds_needle():
    prev_hour = 0
    prev_minute = 0
    current_hour = 0
    current_minute = 0
    prev_seconds = 0
    current_seconds = 0
    while True:
        now = datetime.now()
        hour_minute = now.strftime("%I:%M")

        hour_minute = hour_minute.split(":")
        hour_minute[0] = int(hour_minute[0])
        hour_minute[1] = int(hour_minute[1])

        current_hour = (hour_minute[0] * angle_shift_per_second * 5) + (math.floor((hour_minute[1] * angle_shift_per_second)/72)*6)
        current_minute = hour_minute[1] * angle_shift_per_second 
        if(current_minute != prev_minute):          #if minute value is changed only then rotate minute hand
            minutes_needle_rotate(current_minute)
        if(current_hour != prev_hour):              #if hour value is changed only then rotate hour hand
            hour_needle_rotate(current_hour)
        prev_hour = current_hour                    #assigning value to compare it after every second
        prev_minute = current_minute
        now = datetime.now()
        current_seconds = now.strftime("%S")
        current_seconds = int(current_seconds)
        if(current_seconds != prev_seconds):
            seconds.clear()                             #removing all the frames created by seconds turtle
            seconds.setheading(90)                      #set head upwards
            angle = current_seconds * angle_shift_per_second
            seconds.right(angle)
            seconds.forward(second_needle_length)
            seconds.penup()
            seconds.goto(0, 0)
            seconds.pendown()
        prev_seconds = current_seconds

#function for creating small circles which are used as pointers for numbers
def main_call():
    red_colours = [3,6,9,12]        #points which we want to change colour as red
    angle = 90
    points_angle = 30               #we need 12 circle pointers for clock and we have 360 degree so 360/12
                                    #Every pointer should be at 30 degree from each other
    for i in range(12):             #Iterating loop 12 times because we want to create 12 circles
        number = i                  #we will modify number for conditions so if we did same with loop variable
                                    #and thats why we assign to another variable so loop variable shouldn't change 
        number = number + 3         #because turtle start creating circles from right side which is 3rd Number in clock
        if(number > 12):            #when number is increased from 12 we will reset it to create 1 and then 2
            number = number - 12
        colour = "blue"             #normally all circles will be blue assigning it here is important because
                                    #when colour will be red for any circle we again want others circles to be blue
        if(number in red_colours):  #if number exist in list of red colours
            colour = "red"          #then we override the colour of circle to red
        circle(colour,angle,number) #function that creates circle and add number below it we just want to give
                                    #it the colour,number and angle becuase for every circle the degree of number
                                    # below it is different so we need to adjust it accordingly 
        frame.right(points_angle)   #after creating circle pointer and number move turtle 30 degree right for next circle
        angle = angle + points_angle#adjusting angle for passing to function

    frame.color("black")

main_call()
outer_circle()
needles_intial_configuration()
seconds_needle()
