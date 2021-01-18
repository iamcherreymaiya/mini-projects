# Philippines coin exchange denominations
# Open for recommendation on code efficiency

import random

change = float(input("Amount: "))

print("\nYOUR COIN DENOMINATONS:\n")

# ten peso coin
tenp = change // 10
print("- Php10: ", int(tenp))

# five peso coin
quotient = change % 10
fivep = quotient // 5
if quotient >= 5:
    print("- Php5: ", int(fivep))
else:
    print("- Php5: 0")

# one peso coin
quotient1 = quotient % 5
onep = quotient1 // 1
if quotient1 >= 1:
    print("- Php1: ", int(onep))
else:
    print("- Php1: 0")

# fifty cents coin
quotient2 = quotient1 % 1
fiftyc = quotient2 // .50
if quotient2 >= .50:
    fiftyc = quotient2 // .50
    print("- Php 0.50: ", int(fiftyc))
else:
    print("- Php 0.50: 0")

# twenty five cents coin
quotient3 = quotient2 % .50
twentyfc = quotient3 // .25
if twentyfc >= .25:
    print("- Php 0.25: ", int(twentyfc))
else:
    print("- Php 0.25: 0")

# excess output
excess = quotient2 % .25
if excess != 0:
    print(f"\n{excess:,.2f} - Excess Amount / No equivalent coins.")
else:
    print("\nCONGRATULATIONS! Full amount has equivalent coins.")









