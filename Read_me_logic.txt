Tic Tac Toe logic
==================

The tic tac toe game is probably the easiest AI one could program.

The key behind it is to replace the X's and O'x with numbers.
That way one can calculate what is in each row. For this I chose the numbers 5 for the X and
1 for the O.
Why I didn't choose 1 and 2 is very simple.

for example we have the following situation:

	O	_	O
	_	X	_
	X	O	_
	
in numbers it would be:

	1	0	1
	0	5	0
	5	1	0
	
Now if I calculate the rows I would get:

	1	0	1	=	2
	0	5	0	=	5
	5	1	0	=	6

If I had picked 1 and 2 for the numbers instead of 1 and 5 I would get:

	1	0	1	=	2
	0	2	0	=	2
	2	1	0	=	3
	
Here I have two rows that give me the result 2, but those two rows are different. I can't truly say what is in
that row just by the number.
However like this:

	1	0	1	=	2
	0	5	0	=	5
	5	1	0	=	6
	
I know if the result is 2 I have two O's in that row.
If the result is 5 I have one X.
6 means one X and one O.
etc.

Now that we have made the field calculable it is just a matter of programming math functions.

For example if the user wants to win he has to have two X's in a row/column/diagonal together with an empty field
where he can then place his winning stone.

e.g:

	X	X	_ <=
	O	O	_
	_	O	_

For the AI to counter act this he has to find the row/column/diagonal that has a sum of 10 and then place
a O in the empty spot.

Same thing goes for when he can win except that instead of looking for a sum of 10 he looks for a sum of 2.

Of course it's a bit more complicated then that, but the basic principle is summing up the rows/columns/diagonals.



Livio Conzett
