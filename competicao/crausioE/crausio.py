nums1 = input().split(" ")
nums = []
for i in nums1:
    nums.append(int(i))

posicao1 = input().split(" ")
posicao = []
for i in posicao1:
    posicao.append(int(i))
    
rotina = input()
movimento = []  
for char in rotina:
    movimento.append(char)


casa = [ [0 for i in range(nums[0]+1)] for j in range(nums[1]+1)]
posicao[0]-=1
posicao[1]-=1

casa[posicao[0]][posicao[1]] = 1

batida = 0 

for i in range(0, nums[2]):
    if(rotina[i]) == 'C':
        if((posicao[0] - 1) < 0 ):
            batida += 1
        else : 
            casa[posicao[0]][posicao[1]] = 0
            posicao[0] -= 1
            casa[posicao[0]][posicao[1]] = 1
    elif(rotina[i]) == 'B':
        if((posicao[0] + 1) >= nums[0]):
            batida += 1
        else : 
            casa[posicao[0]][posicao[1]] = 0
            posicao[0] += 1
            casa[posicao[0]][posicao[1]] = 1        
    elif(rotina[i]) == 'D':
        if((posicao[1] + 1) >= nums[1]):
            batida += 1
        else : 
            casa[posicao[0]][posicao[1]] = 0
            posicao[1] += 1
            casa[posicao[0]][posicao[1]] = 1 
    elif(rotina[i]) == 'E':
        if((posicao[1] - 1) < 0 ):
            batida += 1
        else : 
            casa[posicao[0]][posicao[1]] = 0
            posicao[1] -= 1
            casa[posicao[0]][posicao[1]] = 1
    
print((posicao[0] + 1), (posicao[1] + 1), (batida), end="")  
       
