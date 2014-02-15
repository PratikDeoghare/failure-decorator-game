
from FailureDecorator import failWithProbability

@failWithProbability(0.5)
def sayHello(name):
    print 'Hello, ' + name

dudes = ['tom', 'dick', 'harry', 'good', 'bad', 'ugly', 'joe', 'alice', 'bob']

for dude in dudes:
  sayHello(dude)








