import turtle
branchLen = 30

t = turtle.Turtle() #identifies turtle

myWin = turtle.Screen() #loads a screen

t.left(90) #sets up position of turtle,

t.up()

t.backward(100)

t.down()

t.color("green")

#--------------STARTS-------------------
for drawing in range(3):
    t.forward(branchLen) #go forward branchLen

    t.right(20) #turn right #turn right 20 degrees

t.color("blue")

t.right(20) #turn left 40 degrees

t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.left(40)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.backward(branchLen)
t.color("red")
t.left(40)
t.color("red")
t.forward(branchLen)
t.color("red")
t.right(20)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.left(40)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.right(20)
t.color("red")
t.backward(branchLen)
t.color("red")
t.right(20)
t.color("red")
t.backward(branchLen)
t.color("red")
t.left(40)
t.color("red")
t.forward(branchLen)
t.color("red")
t.left(20)
t.color("red")
t.forward(branchLen)
t.color("red")
t.left(20)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.right(40)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.left(20)
t.color("red")
t.backward(branchLen)
t.color("red")
t.right(40)
t.color("red")
t.forward(branchLen)
t.color("red")
t.left(20)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.right(40)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.left(20)
t.color("red")
t.backward(branchLen)
t.color("red")
t.left(20)
t.color("red")
t.backward(branchLen)
t.color("red")
t.right(20)
t.color("red")
t.backward(branchLen)
t.color("red")

# ---------------------------------------------------

# Explain:

# What is difference in the recursive code and the iterative code?
#         The difference is that my iterative program is SOOO long and has way more lines than the original
#		  program. It is NOT a good alternative. The main difference though, is that this iterative program
#		  does not use functions, or it does not call a function inside of its own function! That is the main
#		  difference between any iterative and recursive program!
# How does the code execute differently in each?
#		  This one, since it is iterative and really doesn't use any loops, executes in a direct line in a
#		  specific order. Compared to the recursive program, that one calls functions inside of itself and
#		  does a lot of things differently. The recursive takes a function and uses itself inside of the
#		  function. Very different compared to this straightforward line by line program.
# What is the difference between recursion and iteration?
#		  The Recursive program uses a function, and that function uses itself inside of itself. Sounds kind of
#		  confusing but it is not too complex. It uses itself inside of itself. An iterative program uses while
#		  loops and for loops instead, to usually achieve the same goal. It is possible to do both for a single
#		  purpose! 
# Part 2:

#        Explain:
#
#Where would recursion be the best option?
#		Recursion would be great for any sort of larger program involving many steps that could be repeated
#		through recursion. Recursion then works to make the blocks of code longer, since it is reusing the same
#		lines over and over again. It is basically a much more code efficient way to write something for larger
#		programs.
#
#When would it not?
#		In cases where your stack space is large, recursion can cause something called Memory Overflow.
#		Basically, where it is using a lot of space and memory to do something that could be done iteratively.
#		It is also not very useful for smaller pieces that are just calculating the same value over and over,
#		Where a while loop or some sort of other loop would suffice and work just as good, maybe even better.
#What are some specific examples of recursion that can work for you?
#		A good example is the factoring recursive program. This one works for me, and it is cool to see,
#		since it is a good example of how recursion works, taking one value and carrying it through the same
#		function many times over.






myWin.exitonclick()
