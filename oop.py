# creates a class
class Dog:

  # runs when each "Dog" (member of Class) is created
  def __init__ (self, name, age):
    self.name = name
    self.age = age
    self.good = True
    self.fed = False
  
  # function exclusive to Dog
  def bark(self):
    print(self.name + " starts to bark!")

# create a function outside of class
def feed(dog):
  dog.fed = True

def isDogFed(dog):
  if (dog.fed == True):
    return True
  elif (dog.fed == False):
    return False
  else:
    # how do we get here?
    print("Dog is confused.")

  # return dog.fed

# ----------- create some dogs -------------------
doggo = Dog("Bowser", "7")
# b = Dog()

# ----------- play with our dogs! ----------------
doggo.bark()
# bark()

print(isDogFed(doggo))
feed(doggo)
print(isDogFed(doggo))
