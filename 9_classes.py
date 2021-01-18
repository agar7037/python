# Say we wanted to represent a more complex object in python. For example, a 
# cat:

class cat:
  def __init__(self, size, color, breed):
      self.size= size
      self.color= color
      self.breed= breed
  def meow(self):
      print ("meow! I am a " + self.color + ", " + self.breed + " cat.")
  def how_big(self):
      print(f"I am {self.size} units large")


molly = cat(40, "blue", "persian")
jesse = cat(40, "grey", "tabby")

print(molly.size)
jesse.breed = "tabby"
print(molly.breed)

molly.meow()
jesse.meow()

artemis = cat(30, "black", "mixed")
artemis.how_big()

# We use classes because it allows us to store a variety of related data and 
# functions under a single variable. This is a pattern of thinking called 
# 'object-oriented' programming. It may not be relevant for all problems, 
# but like functions, it is useful for breaking problems down or classifying 
# complicated objects. 

# Many people use object-oriented programming, so it's useful to learn what 
# it looks like when you're coding with it.
