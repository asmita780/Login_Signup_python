import re
import json
regex = re.compile('[@#$%^&*()<>?/\|}-}~!:]')#list of possible special characters
# dictionary = {"user":[ {"Username": "username", "Password": "password1"}]}
# with open("userdetails.json" 'w') as outfile: // for not keep json file empty
#     json.dump(dictionary,outfile)

user_input = str(input("you want login/sign up? "))
# user_input.lower()
if user_input.lower() == "sign up":
    username = input("Enter your username! ")
    password1 = input("Enter your password! ")
    if regex.search(password1) == None and password1.isdigit() == False:#search() => searching spacial character in password string, isdigit => int or not
        print("At least password should contain one special character and one number")
    else:
        password2 = input("Please confirm your password! ")
        if password1 != password2:
            print("Both passwords are not same! ")
        else:
            dictionary = {"user":[ {"Username": username, "Password": password1}]}
            with open("userdetails.json", 'r') as infile:
                 with open("userdetails.json", 'r') as infile:
                            json_data = json.load(infile)
                            if username == json_data['user'][0]["Username"]:
                                print("Username Alredy Exist")
                            
                            else:
                                    print("Congrats " + username + " YOU Signed Up Successfully")

                                    description = str(input("Enter descraption about you: "))
                                    birth_date = input("please enter you birth date: ")
                                    hobbies = input("What are you hobbies?: ")
                                    gender = input("what is your gender?: ")
                                    profile = {"Bio": description,"Dob":birth_date,"Hobbies":hobbies,"Gender":gender}
                                    dictionary['user'][0]["Profile"] = profile
                                    list_value = dictionary['user'][0]
                                    dictionary["user"].append(list_value)
                                    # print(dictionary)           
                                    with open("userdetails.json", 'w') as outfile:
                                        json.dump(dictionary, outfile)                                  
else:
    if user_input.lower() == "login":
        username = input("Enter username: ")
        password = input("Enter password: ")
        with open("userdetails.json", 'r') as infile:
            userdetails1 = json.load(infile) #corvert json object to python dictionary
            if username == userdetails1['user'][0]["Username"] and password == userdetails1['user'][0]["Password"]:#crrocte  details or not
                print(username + " You are logined successfully")

                user_items = userdetails1["user"][0]#list zero(0) index element, which is a dictionary(user-key all items)
                profile_items = user_items["Profile"]#profile - key all items
                del user_items["Password"]
                del user_items["Profile"]
                print()
                print("Profile")
                for x , y in user_items.items():#printing dictionary key & values
                    print(x,y)
                for x , y in profile_items.items():
                    print(x,y)

            else:
                print("Invalid Username and Password")
    else:
        print("wrong key")











# dic={'user':[{"name":"asmita","age":19,"year":200,"citty":{"bihar": "vilage","delhi":"study"}}]}
# # print(dic['user'][0]["name"])
# # dic['user'][0]["date"]=18
# # # print(dic)
# # des = input("enter des: ")
# # dob = input("dob")
# # prof = {"des": des, "dob ": dob}

# # dic["user"][0]["profile12"] = prof
# # # print(dic)
# a=dic["user"][0]
# print(a)

# dic["user"].append(a)
# print(dic)

# dic["user"][0]["try"]=a
# print(dic)

# del dic['user'][0]["age"]
# # print(dic)
# print(a["age"])

# print(a["citty"]["bihar"])
# print(a["bihar"])

# b=a["citty"]
# print(b)
# del a["citty"]

# # b["name"]=a["name"]
# for x,y in a.items():
#     print(x,y)
# for x,y in b.items():
#     print(x,y)
        






# check json file if empty ar not............................

                    # file_content = infile.read()
                    # if not file_content: # checking empty or not
                    #     # # print("file is empty") outfile:
                    #     #     json.dump(dictionary, outfile)   
                    #     description = str(input("Enter descraption about you: "))
                    #     birth_date = input("please enter you birth date: ")
                    #     hobbies = input("What are you hobbies?: ")
                    #     gender = input("what is your gender?: ")
                    #     profile = {"Bio": description,"Dob":birth_date,"Hobbies":hobbies,"Gender":gender}
                    #     dictionary['user'][0]["Profile"] = profile
                    #     list_value = dictionary['user'][0]
                    #     dictionary["user"].append(list_value)
                    #     with open("userdetails.json", 'w') as outfile:
                    #             json.dump(dictionary, outfile)     