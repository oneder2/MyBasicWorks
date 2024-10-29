def taxcalculate(margin, basic, level, tax):
    if margin >= 500 and (basic + level * 0.01) < 0.7:
        tax += 500 * (basic + level * 0.01)
        margin -= 500
        level += 1
        return taxcalculate(margin, basic, level, tax)
    else:
        tax += margin * (basic + level * 0.01)
        margin = 0
        return tax


Basic = 0.14
Level = 0
income = 1000000
pay = 0


if income > 2200:
    pay = taxcalculate(income - 2200, Basic, Level, 0)

print(pay)