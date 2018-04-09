str='s\naa\nbbb\ncccc'

print(str.splitlines())
def line(string):
    temp=string
    index=string.find('\n')
    line=temp[0:index+1]
    while(index>0):
        yield line

# for line in line(str):
#     print(line)