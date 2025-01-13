#the first thing you should really know about this is what a import really is. heres an example of one down below
import numpy
#this will import a library called numpy this library was written in a c laungage but we wont worry about that for now. if we feel the import is to long then we can do this
from bs4 import BeautifulSoup #this is long to call so in this case we can do this
from bs4 import BeautifulSoup as BS4 #now instead of having to call BeautifulSoup() all the time we can call BS4()
#the basics to making an import you usualy make it on another file by doing this

class import_name():
  #now usualy if we want to store a variable across functions we would make the following function
  def __init__(self, value):
    self.value = value
    #this function will be called by running import_name(value) this will store the value across all function
  def print_value(self):
    print(self.value)

#now time for list comps we want to shorten the following code
list1 = [2, 1, 5, 2, 3]
for i in list1:
  if i > 5:
    list1.index(i) += 5
print(list1)
#now the first this we notice about this is the if statement. because its inside of the for loop instead of using the if statement we will use and
(i > 5) and (list1.index(i) += 5)
#Now we would get an error for this code that we can use += on this so we will have to use a function introduced in python 3 := so our code will now look like
(i > 5) and (list1.index(i) := i + 5)
#now we readd it to the code
list1 = [2, 1, 5, 2, 3]
for i in list1:
  (i > 5) and (list1.index(i) := i + 5)
print(list1)
#now that there is 1 line in the for statement we can use a list comp to make it look like this
list1 = [2, 1, 5, 2, 3]
[((i > 5) and (list1.index(i) := i + 5)) for i in list1]
print(list1)

#another way of writing it is like this
list1 = [2, 1, 5, 2, 3]
list1 = [((i > 5) and i + 5 for i in list1]
print(list1)
#now note in this one it does the exact same thing but it requires less logic making it slightly fatser instead of setting the value of list 1 in there the list comp will return the value with the conditions

