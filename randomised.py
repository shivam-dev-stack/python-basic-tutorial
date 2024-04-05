import random

print(random.randint(2,100))
print(random.seed())
print(random.randrange(1,100,2))
 
a = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']
 
print(a)
 
for i in range(5):
    print(random.choice(a))

 
sequence = [random.randint(0, i) for i in range(10)]
 
print('Before shuffling', sequence)
 
random.shuffle(sequence)
 
print('After shuffling', sequence)


 
print('Random number from 0 to 1 :', random.random())
print('Uniform Distribution between [1,5] :', random.uniform(1, 5))
print('Gaussian Distribution with mean = 0 and standard deviation = 1 :', random.gauss(0, 1))
print('Exponential Distribution with lambda = 0.1 :', random.expovariate(0.1))
print('Normal Distribution with mean = 1 and standard deviation = 2:', random.normalvariate(1, 5))
