class Pop:
    def __init__(self):
        self.sound = 'pop'

    def makeSound(self, s, e):
        print(self.sound[s:e])

listt = []
nlist = ['q', 'w', 'e']
nnlist = ['a', 's', 'd']
nnnlist = ['z', 'x', 'c']


listt.append(nlist)
listt.append(nnlist)
listt.append(nnnlist)
listt.append(nlist)
listt.append(nnlist)
listt.append(nnnlist)

for i in range(3):
    print(listt[i])

print("")
print(listt)
print(listt[2][1])

Tr = "White"
Fa = "White"

print(Tr == Fa)

# import time
#
# print(time.gmtime())
# hours = int(time.strftime("%H"))
# print(hours)
# # Pop.makeSound()
# inp = int(input("Hvor mange timer vil du holde? "))
# total = hours + inp
# print(total)
