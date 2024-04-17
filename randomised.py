import random

print(random.randint(2,100),"\n")
print(random.seed(),"\n")
print(random.randrange(1,100,2),"\n")
 
a = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']
 
print(a, "\n")

print(random.choice(a), "\n")
 
sequence = [random.randint(0, i) for i in range(10)]
 
print('\n Before shuffling', sequence)
 
random.shuffle(sequence)
 
print('\n After shuffling', sequence)

print('\n Random number from 0 to 1 :', random.random())

print('\n Uniform Distribution between [1,5] :', random.uniform(1, 5))

print('\n Gaussian Distribution with mean = 0 and standard deviation = 1 :', random.gauss(0, 1))

print('\n Exponential Distribution with lambda = 0.1 :', random.expovariate(0.1))

print('\n Normal Distribution with mean = 1 and standard deviation = 2:', random.normalvariate(1, 5))
