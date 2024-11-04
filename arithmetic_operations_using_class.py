from colorsys import yiq_to_rgb
from os import device_encoding


class arithmetic_op:
    def sum(self):
        x=200
        y=100
        return x+y
    def mul(self):
        a=50
        b=2
        return a*b
    def sub(self):
        p=20
        q=50
        return p-q

    def div(self):
        c = 200
        d = 30
        return c/d

    def mod(self):
        x = 30
        y = 2
        return x//y
    def even_odd(self):
        n = 5
        if n%2==0:
            return "Even"
        else:
            return "Odd"
    def pos_negative(self):
        x = 20
        if x<0:
            return "negative number"
        else:
            return "Positive number"

    def fact(self):
        n = 5
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        return f"factorical of {n} is: {fact}"

    def perimeter_circle(self):
        radius = 60
        perimeter = 2 * 3.14 * radius
        return f"perimeter is {perimeter} for radius is {radius}"

    def interest_calc(self):
        p = 20000
        r = 20
        t = 6
        si = (p * t * r) / 100
        return f"Simple interest for principal amount:{p}, time period:{t}, rate of interest:{r} is {si}"
    def celcius_to_foreign_heat(self):
        C = 38.9
        F = (C * 9 / 5) + 32
        return f"Fahrenheit is {F} for Celsius is {C}"
    def bmi_calc(self):
        weight = 68
        height = 5.5
        BMI = weight / (height/100)**2
        return f"Body Mass Index for weight:{weight}, height:{height} is {BMI}"
    def speed_calc(self):
        u = 100
        a = 40
        t = 20
        s = (u * t) + (0.5 * a * (t ** 2))
        return f"speed: {s}"

    def discount_calc(self):
        purchase = 1000
        dis = 0
        if (purchase >= 500):
            dis = 0.2
        elif (purchase >= 200 and purchase < 500):
            dis = 0.1
        else:
            dis = 0

        final_discount= dis * 1000
        return f"Total amount to be paid is {(purchase - (purchase * dis))} Rs and discount is {final_discount} Rs"

    def prime_no(self):
        n = 6
        prime = False
        if n == 0 or n == 1:
            return f"Given number {n} Prime number is {prime}"
        elif n > 1:
            for i in range(2, n):
                if n % i == 0:
                    prime = True
            if prime:
                return f"Given number {n} Prime number is {prime}"
            else:
                return f"Given number {n} Prime number is {prime}"
    def mobile_no_validation(self):
        ph = "9676075317"
        if len(ph) == 10:
            return "Given phone number is valid"
        else:
            return "Given phone number is not valid"