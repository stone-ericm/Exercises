# Code your solution here

STR_ARITHMETIC = 0
string1 = "Pokemon!"
string2 = " Gotta Catch 'em All!"

try:
    string1 + 1
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    string1 - 1
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    string1 * 1
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    string1 / 1
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    string1 ** 1
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    string1 // 1
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    string1 % 1
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    string1 + string2
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    string1 - string2
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    string1 * string2
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    string1 / string2
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    string1 ** string2
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    string1 // string2
    STR_ARITHMETIC += 1
except TypeError:
    pass

try:
    string1 % string2
    STR_ARITHMETIC += 1
except TypeError:
    pass
