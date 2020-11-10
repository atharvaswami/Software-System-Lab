import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from collections import Counter

#-----------------------------------------------Q1----------------------------------------------

def randGen():
    # create a file named dataset.txt if it doesn't exists or write in it if it exists
    output_file = open("dataset.txt", "w")

    # uniformly distributed integer between 1 and 100
    age = random.uniform(low = 1, high = 100, size = 10000).astype(int)

    # randomly marked as Male or Female
    gender = random.choice(['Male','Female'], size=(10000))

    # randomly chosen from the 28 states of India
    state = random.choice(
        ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"],
        size=(10000)
    )

    # random 10-digit numbers starting with 6, 7, 8 or 9
    phone_number = []
    first_digit = random.choice([6,7,8,9], size=(10000))
    for i in range(10000):
        remaining_digits = random.randint(low=1,high=9, size=(9))
        phone_number.append( str(first_digit[i]) + ''.join(map(str, remaining_digits)) )

    # Gaussian distributed real number with mean 160 cm and deviation 10 cm
    height = random.normal(loc=160, scale=10, size=(10000))

    # Gaussian distributed real number with mean 70 kg and deviation 5 kg
    weight = random.normal(loc=70, scale=5, size=(10000))
    
    # printing data into the file dataset.txt
    for i in range(10000):
        print("{}, {}, {}, {}, {} cm, {} kg".format(age[i],gender[i],state[i],phone_number[i],round(height[i],2),round(weight[i],2)),file=output_file)

    output_file.close()

#-----------------------------------------------Q2----------------------------------------------

class Person:

    def __init__(self,age,gender,state,phone,height,weight):
        self.age = int(age);
        self.gender = gender;
        self.state = state;
        self.phone = phone;
        self.height = float(height);
        self.weight = float(weight);

    # Functions to return each variables of the class Person    
    def give_age(self):
        return (self.age)

    def give_gender(self):
        return (self.gender)

    def give_state(self):
        return (self.state)
    
    def give_phone(self):
        return (self.phone[0])

    def give_height(self):
        return (self.height)

    def give_weight(self):
        return (self.weight)


#-------------------------------------------MAIN FUNCTION---------------------------------------

if __name__=="__main__":

    # call the Q1 function to create the file dataset.txt with 10000 data values
    randGen();

    #-----------------------------------------------Q3----------------------------------------------

    People = []
    input_file = open("dataset.txt", "r")
    for line in input_file:
        x = line.split(", ")
        People.append( Person(x[0],x[1],x[2],x[3],x[4][:4],x[5][:4]) )
    input_file.close()


    #-----------------------------------------------Q4----------------------------------------------

    append_file = open("dataset.txt", "a")
    height_sum = 0
    weight_sum = 0
    for inst in People:
        height_sum += inst.give_height()
        weight_sum += inst.give_weight()
    print("Average Height : ",round(height_sum/10000,2),file=append_file)
    print("Average Weight : ",round(weight_sum/10000,2),file=append_file)
    append_file.close()

    #-----------------------------------------------Q5----------------------------------------------

    HeightMale = []
    HeightFemale = []
    WeightMale = []
    WeightFemale = []
    Gender = [0 , 0]
    AgeMale = []
    AgeFemale = []
    Phone = [0,0,0,0]
    State = []

    for obj in People:
        State.append(obj.give_state())

        if(obj.give_gender() == "Male"):
            HeightMale.append(obj.give_height())
            WeightMale.append(obj.give_weight())
            Gender[0] += 1
            AgeMale.append(obj.give_age())
        else:
            HeightFemale.append(obj.give_height())
            WeightFemale.append(obj.give_weight())
            Gender[1] += 1
            AgeFemale.append(obj.give_age())

        if(obj.give_phone() == "6"):
            Phone[0] += 1
        elif(obj.give_phone() == "7"):
            Phone[1] += 1
        elif(obj.give_phone() == "8"):
            Phone[2] += 1
        elif(obj.give_phone() == "9"):
            Phone[3] += 1

    # creates two subplots, namely, histogram of male and female heights
    plt.figure()
    plt.subplot(1,2,1)
    plt.hist(HeightMale,bins=200,color="blue")
    plt.title("Heights of Male")
    plt.xlabel('Height (in cm)')
    plt.ylabel('Number of Male')
    plt.subplot(1,2,2)
    plt.hist(HeightFemale,bins=200,color="red")
    plt.title("Heights of Female")
    plt.xlabel('Height (in cm)')
    plt.ylabel('Number of Female')
    plt.tight_layout()
    plt.savefig("height.jpg")

    # creates two subplots, namely, histogram of male and female weights
    plt.figure()
    plt.subplot(1,2,1)
    plt.hist(WeightMale,bins=200,color="blue")
    plt.title("Weights of Male")
    plt.xlabel('Weight (in kg)')
    plt.ylabel('Number of Male')
    plt.subplot(1,2,2)
    plt.hist(WeightFemale,bins=200,color="red")
    plt.title("Weights of Female")
    plt.xlabel('Weight (in kg)')
    plt.ylabel('Number of Female')
    plt.tight_layout()
    plt.savefig("weight.jpg")

    # creates a pie chart of male and female gender
    plt.figure()
    plt.pie(Gender, labels = ["Male","Female"])
    plt.legend(title = "Gender:",loc = "best")
    plt.savefig("gender.jpg")

    # creates a pie chart of numbers starting with 6, 7, 8 and 9
    plt.figure()
    plt.pie(Phone, labels = ["6","7","8","9"])
    plt.legend(title = "Phone Numbers starting with:",loc = "best")
    plt.savefig("phone.jpg")

    # creates two line plots (with legend) of cumulative distribution function of male age and female age
    plt.figure()
    x1 = list(Counter(sorted(AgeMale)).keys())
    y1 = list(Counter(sorted(AgeMale)).values())
    cdfMale = np.cumsum(y1)
    x2 = list(Counter(sorted(AgeFemale)).keys())
    y2 = list(Counter(sorted(AgeFemale)).values())
    cdfFemale = np.cumsum(y2)
    plt.plot(x1,cdfMale,label="Male")
    plt.plot(x2,cdfFemale,label="Female")
    plt.legend(title = "CDF of Ages:",loc = "best")
    plt.xlabel('Age')
    plt.ylabel('Number of People Lying below a Age')
    plt.savefig("age.jpg")

    # creates bar plot with state name on x-axis and number of people in that state (based on the dataset) as the bar height
    plt.figure()
    x = list(Counter(sorted(State)).keys())
    y = list(Counter(sorted(State)).values())
    plt.bar(x,y)
    plt.xticks(x, x, rotation ='vertical') 
    plt.xlabel('States')
    plt.ylabel('Number of People')
    plt.savefig("state.jpg",bbox_inches = 'tight')