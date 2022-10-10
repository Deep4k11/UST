para="""Python is a widely used general-purpose, high level programming language. 
It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. 
It was designed with an emphasis on code readability, and its syntax allows programmers to express their 
concepts in fewer lines of code"""

vow_count = 0
cons_count = 0
tempcount=0
para = para.lower()

for i in range(0, len(para)) :
    if para[i] in ('a','e','i','o','u'):
     vow_count +=1
    if para[i].isalpha() is True:
        tempcount += 1


cons_count = tempcount-vow_count

print('No of vowels =',vow_count)
print('No of consonents =',cons_count)

