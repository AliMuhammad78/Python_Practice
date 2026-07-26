# To print the poem in python 

print("""Twinke Twinke little star
How i wonder what you are 
Up above the world so high 
like a diamond in the sky  """)




 
# import matplotlib.pyplot as plt

# plt.plot([1,2,3], [3,5,1])
# plt.show()

import pyttsx3

engine = pyttsx3.init()
engine.say("Allahuma salli ala Muhammad")
engine.runAndWait()