

class failWithProbability(object):

  def __init__(self, f, p = 0.5):
    self.p = p # probability of failure

  def __call__(self, f):
    from random import random
    def wrapped_f(*args):
      if random() < self.p:
        f(*args)
    return wrapped_f

if __name__ == '__main__':
  print '....ta...da...dada....'
