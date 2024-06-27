# author: Ramses Trejo
def create_staircase(nums):
    step = 1
    subsets = []
    while len(nums)>0:
        subset = []
        if len(nums)>=step:
            for i in range(0,step):
                subset.append(nums.pop(0))
            subsets.append(subset)
        step=step+1
    return subsets

def decode(message_file):
    source_file = open(message_file, 'r')
    file_lines = source_file.readlines()
    codes={}
    sorted_codes=[]
    for line in file_lines:
        values=line.split(' ')
        if len(values)==2:
            codes[values[0]]=values[1].strip()
            sorted_codes.append(int(values[0]))
    sorted_codes.sort()
    staircase=create_staircase(sorted_codes)
    print(staircase)
    message = ""
    for subset in staircase:
        message+=(codes[str(subset[len(subset)-1])]+ " ")
    return message.strip()

print(f'{decode('message.txt')}')