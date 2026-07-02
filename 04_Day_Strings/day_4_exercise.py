# The goal of this exercise is to mainly explore strings

# multiline string: this keeps the texts in line so that everything is kept the exact way

lineTexts = """Hello there,
here is the second line
here is the third line"""
print(lineTexts)

# lets look at formated strings
# %s, %d, %f,  %.[# of decimal]f

name = "David Ogunbanjo"
bankAmount = 12.343545
formatedString = "Helo my name is %s and I have $%.2f in my bank account"%(name, bankAmount)

# or you can also use the the f-string method
formatedString2 = f"Hello my name is {name}"

print(formatedString)

print(formatedString2)

# umpacking characters
language = "pyth"
a,b,c,d = language # the number of variables should match the size of the string

print(a)
print(b)
print(c)
print(d)