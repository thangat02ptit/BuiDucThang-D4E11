name = ['ST','BD','BTL','CG','DD','HBT']
population = [150300,247100,333300,266800,420900,31800]
area = [117.43,9.224,43.35,12.04,9.96,10.09]
print('1.')
print("max population: ",max(population))
print("min population: ",min(population))

print('2.')
print("max population(name): ",name[population.index(max(population))])
print("min population(name): ",name[population.index(min(population))])

print('3.')
matdo = []
for i in range(len(name)):
    matdo.append(int(population[i]//area[i]))
print(matdo)

print('4.')
total = 0
for i in matdo:
    total += i
print("average population density: ",int(total // len(name)))

