file_path = "part1\\test.txt"
with open(file_path,'w') as file:
    file.write('Bergen Tech!')
    # file.seek(0)
    file.write('teterboro')
# with open(file_path,'w') as file:
#     file.write('teterboro')

with open(file_path,'w') as file:
    file.write('Bergen Tech!\n')
    file.write('teterboro\n')
    
with open(file_path,'a') as file:
    file.write('New Jersey\n')

content  = ['this is the first line',
            'this is the second line',
            'this is the third line']
with open(file_path,'w') as file:
    file.writelines(content)
    
content  = ['this is the first line\n',
            'this is the second line\n',
            'this is the third line\n']
with open(file_path,'w') as file:
    file.writelines(content)