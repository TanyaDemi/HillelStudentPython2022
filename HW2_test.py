# HW 2

# Code option 1 - simple
s=R"""
Escape sequences
\a		Bell (alert)
\b		Backspace
\n		New line
\t		Horizontal tab
\\ 		Backslash \
\" 		Double quotation mark "
\' 		Single quotation mark '
"""
print(s)

# Code option 2
print('\n')

print('Escape sequences\n\\a\t\tBell (alert)\n\{\bb}\b\t\tBackspace\n\\n\t\tNew line\n\\t\t\tHorizontal tab')
print("\\\\ \t\tBackslash \\")
print('\\" \t\tDouble quotation mark \"')
print("\\' \t\tSingle quotation mark \'")

# Code option 3
print('\n')

print('Escape sequences')
print('\\a\t\tBell (alert)')
print('\\b\t\tBackspace')
print('\\n\t\tNew line')
print('\\t\t\tHorizontal tab')
print("\\\\ \t\tBackslash \\")
print('\\" \t\tDouble quotation mark \"')
print("\\' \t\tSingle quotation mark \'")

# Code option 4, difficult to read!
print('\n')

print('Escape sequences\n\\a\t\tBell (alert)\n\{\bb}\b\t\tBackspace\n\\n\t\tNew line\n\\t\t\tHorizontal tab\n\\\\ \t\tBackslash \\\n\\" \t\tDouble quotation mark \"\n\\\' \t\tSingle quotation mark \\')