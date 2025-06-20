

#elif- ეს გამოიყენება დაზუსტდებისთვის როდესაც იფ არგაამართლებს
#else- ეს არის სხვა შემთვხევებისსს დროს
#if- არის შესამოწმებლად თუ კოდი სიმართლეა გამოიტანს (true)


my_surname = "rezesidze"
user_surname = input("Enter your surname: ")

if my_surname == user_surname:
    print("Our surnames are similar")
else:
    print("Our surnames are not similar")



my_height = 175  # ჩაწერე შენი სიმაღლე სანტიმეტრებში
user_height = int(input("Enter your height in cm: "))




my_height= 1.75
if my_height > user_height:
    print("I'm taller than you.")
elif my_height < user_height:
    print("You're taller than me.")
else:
    print("We have equal heights.")
