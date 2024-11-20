'''
Create a Python script that calculate the Body Mass Index from weight (kg) and height (m), using F=string to format
'''

def is_numeric(val):
    ''' function check if is number'''
    try:
        float(val)
        return True
    except ValueError:
        return False

# creating fucntion to calculate BMI (Body Mass Index)
def bmi(w, h):
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


# call the function and printing

if __name__ == '__main__':

    weight = 'A' # start with string to ask the values
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
        your_bmi, msg = bmi(weight, height)
        print(f"Your Weight are {weight:.2f} kg")
        print(f"Your Height are {height:.2f} meters")
        print(f"Your Body Mass Index are {your_bmi:.2f} kg/m^2")
        print(f"You are {msg}")
