num = int(input("enter a number between 1 and 3999 : "))
roman_numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_numeral = ""
if 4000> num > 0:
    for i in range(len(roman_numerals)):
        while num >= roman_values[i]:
            num -= roman_values[i]
            roman_numeral += roman_numerals[i]
    print(roman_numeral)
else:
    print("No valid Input!")