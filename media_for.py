v= [0]*4
media = 0
for x in range(len(v)):
    v[x] = int(input(f'digite a {x+1}ªnota'))
for x in range(len(v)):
    print(f'A nota {x+1}foi:{v[x]}')
    media = media + v [x] 
print(f'a media e : {media/4}')       