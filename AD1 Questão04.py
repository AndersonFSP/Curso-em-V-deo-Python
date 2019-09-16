def converte(numBinario, base):
    if numBinario != 0:
        numConvertido = ""
        while numBinario > 0:
            resto = numBinario % base
            numConvertido = str(resto) + numConvertido
            numBinario = numBinario // base
    else:
        numConvertido = "0"
    return numConvertido

num = 0
bin = str(input())
pot = len(bin) - 1
for i in range(len(bin)):
    num = num + (int(bin[i]) * (2 ** pot))
    pot -= 1

while num != -1:
    for c in range(3, 10+1):
        r = converte(num, c)
        print(r, end=" ")
    print()
    bin = str(input())
    pot = len(bin) - 1
    for i in range(len(bin)):
        num = num + (int(bin[i]) * (2 ** pot))
        pot -= 1