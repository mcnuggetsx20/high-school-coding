inp = input()
tab = ['']
num = 0
inp = ''.join(inp.split(' '))
znaczki = ['x', '^', '+', '-']
for j in range(len(inp)):
    i = inp[j]
    if(i in znaczki):
        if(len(tab[-1])>0):
            tab.append('')
            tab[-1]+=i
            tab.append('')
        else:
            tab[-1]+=i
            tab.append('')
    else:
        tab[-1]+=i
        num+=1
    if(i=='+' or i=='-'):
        z=i
        if(inp[j-1]=='x'):
            tab[-2]='^'
            tab[-1]='1'
            tab.append(z)
            tab.append('')
for i in range(3, len(tab)):
    if(tab[i-1]=='^'):
        tab[i-3] = str(int(tab[i-3])*int(tab[i]))
        tab[i] = str(int(tab[i])-1)
tab.append('')
for i in range(len(tab)-1):
    if(tab[i] not in znaczki and i==len(tab)-2 and tab[i]!=''):
        tab[i]=''
        tab[i-1]=''
    elif(tab[i]=='^' and tab[i+1]=='0'):
        tab[i+1]=''
        tab[i]=''
        tab[i-1]=''
    elif(tab[i]=='^' and tab[i+1]=='1'):
        tab[i]=''
        tab[i+1]=''
for i in tab:
    if i!='':
        print(i, end='')
print()

