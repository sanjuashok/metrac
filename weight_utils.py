import math

# weight in pounds, height in inches
def get_bmi(weight, height):
    return round(weight * 0.45 / (height*0.025)**2, 2)

# weight in pounds, height in inches
def get_bmr(weight, height):
    return round(66 + (6.2 * weight) + (12.7*height) - (6.76*31), 2)

def get_tdee(bmr):
    return round(bmr*1.2, 2)
