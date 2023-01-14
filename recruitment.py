# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
# welcome1 = ("Welcome to the special recruitment program, please answer the following questions:")
# print(welcome1)
def get_skills():
    # name = input("what is you name ? :")
    # age = int(input("how old are you ? :"))
    # experniece = int("input(How many years of experience do you have ?")
    skils_list = ["1.eating",
     "2.coding",
     "3.fishing"
     ]
    # print(skils_list)
    return skils_list



# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# # This function doesn't return anything
def show_skills():
    
    print(get_skills())

show_skills()


# # Shows the available skills and have user pick from them two skills
# # HINT: Use previous built functions to show the skills
# # For example, if the user enters 1, the first skill in your list of skills will be added to the list
# # Return a list of the two skills that the user inputted
def get_user_skills(skills):
    skills = []

    user_skills = int(input("e5tar law sma7t : "))
    if user_skills == 1:
    print (skills.append("eating"))
    elif user_skills == 2
    print (skills.append("coding"))
    elif user_skills == 3
    print (skills.append("fishing"))
    else:
        print("try again")


    user_skills2 = int(input("e5tar again law sma7t : " ))

    # print (user_skills)
get_user_skills(show_skills())
#     print(show_skills())
# get_user_skills(get_skills())
    



# # This function will get the user's cv from their inputs
# # HINT: Use previous built functions to get the skills from the user
# def get_user_cv(skills):
#     ...


# # This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
# def check_acceptance(cv, desired_skill):
#     ...


# def main():
#     # Write your main logic here by combining the functions above into the
#     # desired outcome
#     ...


# if __name__ == "__main__":
#     main()
