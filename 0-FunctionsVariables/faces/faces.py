user_input = input("Enter a sentence with emoticons: ")

user_input = user_input.replace(":)", "🙂")
user_input = user_input.replace(":(", "🙁")

print(user_input)
