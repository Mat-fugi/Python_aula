f = input('Digite uma Frase: ').strip()
ch = '\u2588'
for i in range (len(f) + 4):
    print(ch, end='')
print(f'\n{ch} {f} {ch}')
for i in range (len(f) + 4):
    print(ch, end='')
