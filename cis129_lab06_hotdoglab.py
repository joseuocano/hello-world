#Title: Lab 6
#Author: Jose Ocano
#Description: This program will calculate the number of packages of hot dogs, buns and leftovers
#Date: March 18, 2025

#Define local variables
def calculate_packages(people, hot_dogs_per_person):
    hot_dogs_needed = people * hot_dogs_per_person
    hot_dog_packages = (hot_dogs_needed + 9) // 10 # Round up to the nearest package of 10

    hot_dog_buns_needed = people * hot_dogs_per_person
    hot_dog_bun_packages = (hot_dog_buns_needed + 7) // 8 # Round up to the nearest package of 8

    return hot_dog_packages, hot_dog_bun_packages

#Calculating the leftovers
def calculate_leftovers(people, hot_dogs_per_person):
    hot_dogs_needed = people * hot_dogs_per_person
    hot_dogs_leftover = 10 - (hot_dogs_needed % 10) if hot_dogs_needed %10 !=0 else 0

    hot_dog_buns_needed = people * hot_dogs_per_person
    hot_dog_buns_leftover = 8 - (hot_dog_buns_needed % 8) if hot_dog_buns_needed %8 !=0 else 0

    return hot_dogs_leftover, hot_dog_buns_leftover

#Define the main function
def main():
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

    #Calculate the packages needed
    hot_dog_packages, hot_dog_bun_packages = calculate_packages(people, hot_dogs_per_person)

    #Calculate the leftovers
    hot_dogs_left, hot_dog_buns_left = calculate_leftovers(people, hot_dogs_per_person)

    #Display results
    print("\nResults:")
    print(f"Minimum number of hot dog packages needed: {hot_dog_packages}")
    print(f"Minimum number of hot dog bun packages needed: {hot_dog_bun_packages}")
    print(f"Number of hot dogs left over: {hot_dogs_left}")
    print(f"Number of hot dog buns left over: {hot_dog_buns_left}")

if __name__ == "__main__":
    main()
    
    

