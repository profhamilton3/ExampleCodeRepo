#test_runner.py - pytest will run this automatically
#we will list it explicitely in the yml file just in case


def test_one():
  assert 1+1 == 2


def test_two():
  s1 = pandas.Sequence([0,1,2,4,5,6,2])
  assert False == s1.empty
  print(s1)
