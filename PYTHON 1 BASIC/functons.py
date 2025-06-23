# a = 2
# print(id(a))
s = "GeeksforGeeks"

# Initialize an empty string to hold reversed result
rev = ""

# Loop through each character in original string
for ch in s:
  
    # Add current character to front of reversed string
    rev = ch + rev

print(rev)