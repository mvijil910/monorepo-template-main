# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- MObject is an abstract class because it contains only the __init__ and pass. This class is then implemented by the other classes which inherit from it.
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- *edit your response*
1. What class does Texture inherit from?
	- Texture inherits from Image which is passed to it. 
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- Texture inherits getWidth, getHeight, getPixelColor, getPixels, setPixelsToRandomValue, but not the constructor.
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- I felt that it made more sense to say Images have a textur, as opposed to saying, texture is-a Image. From a logical standpoint that made more sense to me, so I refactored the code so that Texture was a composite of Image. 
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Python does not automatically create constructors for the methods. The Texture class worked because it did not have any methods in it. Instead, it simply says to pass which indicates to the program to just kind of skip over it. When I refactored the code, I had to write a constructor using __init__. 

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?
- Because python lacks the concepts of new, private, and protected there are some drawbacks to using a Singleton. However, as the article states, "The one situation that would really demand the pattern would be an existing class that, because of a new requirement, will now operate best as a single instance." My takeaway is that a Singleton is not common practice in Python and therefore not safe for regular use, but can be beneficial in specific instances. The biggest drawbacks to Singletons is the lack of ability to create private objects since Singletons are globally accessible. 
  
