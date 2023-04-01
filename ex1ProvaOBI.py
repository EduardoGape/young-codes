idade1 = int(input())
idade2 = int(input())
valor1 = 0
valor2 = 0 

if(idade1 <= 17 or idade2<=17):
    if(idade1<=17):
        valor1 = 15
    else:
        valor2 = 15
if((idade1>17 and idade1<60) or (idade2>17 and idade2<60)):
    if(idade1>17):
        valor1 = 30
    else:
        valor2 = 30
if(idade1>59 or idade2>59):
    if(idade1>59):
        valor1 = 20
    else:
        valor2 = 20

print(valor1 + valor2)
