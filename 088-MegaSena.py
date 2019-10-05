from random import randint
group = []
nums = []
print('MEGA SENA')
numGroup = int(input('Quantos grupos você quer ? '))
print('-='*10,  'SORTEANDO', numGroup,  'GRUPOS', '-=' * 10)
for c in range(1, numGroup +1):
    for l in range(0, 6):
        nums.append(randint(0, 60))
    group.append(nums[:])
    nums.clear()
for c in range(0, len(group) ):
    print(f'Jogo {c + 1}: {group[c]}')
print('-='* 12, '<Boa Sorte>', '-='*12)
