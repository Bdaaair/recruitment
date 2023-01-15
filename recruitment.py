# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
# welcome1 = ("Welcome to the special recruitment program, please answer the following questions:")
# print(welcome1)
def get_skills():
    index = 1
    skils_list = [
        "eating",
        "python",
        "C++",
        "Javascript",
        "juggling",
        "running",
        ]
    for skill in skils_list:
        print(index, skill)
        index += 1

        # return skill
# get_skills()



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
def get_user_skills():
    skills = []
    skil1 = int(input("Choose a skill from above by entering its number: "))
    skil2 = int(input("Choose another skill from above by entering its number: "))
    skills.append(skil1)
    skills.append(skil2)
    if skil1 == 1:
        skills.append("eating")
    elif skil1 == 2:
        skills.append("python")
    elif skil1 == 3:
        skills.append("C++")
    elif skil1 == 4:
        skills.append("Javascript")
    elif skil1 == 5:
        skills.append("juggling")
    elif skil1 == 6:
        skills.append("running")
    else:
        print("try again")
    if skil2 == 1:
        skills.append("eating")
    elif skil2 == 2:
        skills.append("python")
    elif skil2 == 3:
        skills.append("C++")
    elif skil2 == 4:
        skills.append("Javascript")
    elif skil2 == 5:
        skills.append("juggling")
    elif skil2 == 6:
        skills.append("running")
    else:
        print("try again")
    print(*skills,sep='\n')
get_user_skills()



# # This function will get the user's cv from their inputs
# # HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    cv = {
        "age" : "iuyouyuio",
        "experience" : "ljkhkj"
    }
    name = input("What's your name ? ")
    age = input("How old are you ? ")
    experience = input("How many years of experience do you have ? ")
    cv["name"] = name 
    print(cv)

    
get_user_cv(20)

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
