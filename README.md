Axion Script is an innovative programming language inspired by the principles of physics and chemistry, designed to provide a unique approach to coding. The syntax and functionality reflect concepts from these fields, making programming an engaging and intuitive experience.

Axion Script:
Emit: print() 
Usage - emit(what you want to print) 
To declare a synthesised variable, put speech marks and then the name of that variable for emit to print it.


Synthesise: Create a variable 
Usage - synthesise(What will be in the variable, "What the variable name is")
When synthesising the variable, you must put "" when declaring the name.

React: React can be used to do several things with one command.
Usage - react(emit(*first variable*, *second variable*))
Another Usage - react(synthesise(*Inside the variable*, *Variable name*), emit(*Name of the variable created*))
React at the moment only has two possible uses, more will come 

Orbit: Loop 
Usage - orbit around earth(5):
		emit(*What you want to print*)
Outcome:
What you want to print
What you want to print
What you want to print
What you want to print
What you want to print

When stating an orbit, you must say, "orbit around earth(*how many times to loop, leave empty for an infinite amount of times*):"

Priorities:
Axion uses a priority list. If you were to do the line of code:

react(emit("variable"), synthesise(Variable inside, "variable"))

Because synthesise is higher in the priority list, the synthesised variable would be created, and therefore emit would have a variable to print.

Characters:
Axion heavily requires you to use '()' and ',' and ':', almost like python, which it is made out of.
