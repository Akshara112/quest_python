text1 = "12345"
text2 = "12.34"
text3 = "٢٣٤"  # Arabic numerals
text4 = "²³"   # Superscript digits

print(text1.isdigit())  # Output: True
print(text2.isdigit())  # Output: False
print(text3.isdigit())  # Output: True
print(text4.isdigit())  # Output: True



print(text1.isdecimal())  # Output: True
print(text2.isdecimal())  # Output: False
print(text3.isdecimal())  # Output: True
print(text4.isdigit())