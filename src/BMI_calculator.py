'''
Create a Python script that calculate the Body Mass Index from weight (kg) and height (m), using F=string to format

Build a BMI (Body Mass Index) calculator that computes the BMI score based on a person's weight and height.
•Use conditional statements to interpret the BMI score into categories such as Underweight, Normal weight, Overweight, and Obese.
•Set the BMI classification thresholds as follows:
- Underweight: less than 18.5
- Normal weight: 18.5 to 24.9
- Overweight: 25 to 29.9
- Obese: 30 or more
•Print out the person's BMI score and interpretation

'''

def is_numeric(val):
    ''' function check if is number'''
    try:
        float(val)
        return True
    except ValueError:
        return False

# creating fucntion to calculate BMI (Body Mass Index)
def calc_bmi(w, h):
    ''' function calculate body mass index (BMI) and return message'''

    your_bmi = w / (h ** 2)
    if your_bmi < 18.5:
        msg = f"Underweight"
    elif 18.5 <= your_bmi < 25:
        msg = f"Normal weight"
    elif 25 <= your_bmi < 30:
        msg = f"Overweight"
    elif your_bmi >= 30:
        msg = f"Obese"
    return your_bmi, msg

def main_app():
    'Initial settings'
    weight = 'A'  # start with string to ask the values
    height = 'A'  # start with string to ask the values

    # validate entry as number
    while not is_numeric(weight):
        # asking for weight
        weight = input("Enter your weight in kg-> ")
        if is_numeric(weight):
            weight = float(weight)

    # validate entry as number
    while not is_numeric(height):
        # asking for height
        height = input("Enter your height in meters->")
        if is_numeric(height):
            height = float(height)

    # only call the function if both were number
    if is_numeric(weight) and is_numeric(height):
        # call method to calculate bmi
        your_bmi, msg = calc_bmi(weight, height)
        # print results
        print(f"------------------------")
        print(f"Your Weight are {weight:.2f} kg")
        print(f"Your Height are {height:.2f} meters")
        print(f"Your Body Mass Index (bmi) are {your_bmi:.2f} kg/m^2")
        print(f"You are {msg}")
        print(f"------------------------")

# call the function and printing

if __name__ == '__main__':
    main_app()



