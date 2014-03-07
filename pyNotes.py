Points to note in Python

Python,
	is simple to use
	allows you to split your program into modules that can be reused in other Python programs
	is an interpreted language, which can save you considerable time during program development
	enables programs to be written compactly and readably
	is extensible: it is easy to add a new built-in function or module to the interpreter, 

Interpreter,
	python -c command [arg] : executes the statement(s) in command
	python -m module [arg] : executes the source file for module as if you had spelled out its full name on the command line

Argument Passing,
	import sys
	sys.argv : is a list of strings - the script name and additional arguments thereafter 
	sys.argv[0] : is the script name

Interactive Mode,
	>>> Primary prompt, prompts for the next command
	... Secondary prompt, prompts for continuation lines

Error Handling,
	When an error occurs, the interpreter prints an error message and a stack trace (and may cause a nonzero exit)
	All error messages are written to the standard error stream
	Exceptions may be handled by an except clause in a try statement

Executable Python Scripts,
	Python scripts can be made directly executable, by putting the line,
		#! /usr/bin/env python
	at the beginning of the script and giving the file an executable mode

Source Code Encoding,
	It is possible to use encodings different than ASCII in Python source files, by putting the special comment line,
	right after the '#!' line,
		# -*- coding: encoding -*-
		where, encoding = utf-8 or iso-8859-15 or etc.
	Using non-ASCII characters in identifiers is not supported

Python as a Calculator
	The interpreter acts as a simple calculator: you can type an expression at it and it will write the value.
	Operators:
		+, -, *, /, %, >, >=, <, <=, ==
	Operands:
		Integers: -20...,-1,0,1,2...,int(n),long(n)
		RealNumbers: 4.85, 5.21, float(x)
		Complex: complex(real,imag) or <real>+<imag>J or <real>+<imag>j
			eg. x=2+3j or complex(4,3), x.real=4, x.imag=3, abs(x)=5 (magnitude of x, sq.rt. of  sum of real^2 & imag^2)
		Variable(s): One or more alphanumeric(a-z,A-Z,0-9,_) characters, starting with (a-z,A-Z,_), used to represent/store value(s)
			eg. tax=12.5/100, Income=50000, _Pay=tax*Income
		_ : _ is a variable representing last evaluated value. Can be overwritten (but avoid).
		int(x),long(x),float(x): Convert operand x to int, long or float value
		abs(x): Absolute/Magnitude value of operand x.(+ve value in case of Ints or Reals,Magnitude in case of complex)
		round(x,d): Round operand x to d decimal places, eg. round(22/7.0,3)=3.143
	Strings:
		Expressed in single ' or double " quotes
		  eg. 'this is a string', "t'is string"
		String literals can span multiple lines in several ways,
		  #1. Using \
		  "this string literal \
		  span over multiple\n\
		  lines for fun"
		  #2. MultiLine Comments """ or '''
		  """This is really
		  a multi-line string
		  spread over 3 lines"""
		  or
		  '''
		  this is also
		  a mutliline string
		  '''
		Raw strings, ignore escape sequences
		  r'this is a raw\n\
		   spread over 2 lines'
		  prints 'this is a raw\n\ spread over 2 lines'
		Strings can be,
		  Concatenated (glued together) with the + operator,
		    >>>'hello'+'World'
		    helloWorld
		  Repeated with *,
		    >>>'hello'*2
		    hellohello
		  Subscripted (indexed), like in C,
		    >>>y="hello"
		    >>>y[0]
		    'h'
		    >>>y[4]
		    'o'
		  Sliced to form substrings, using slice notation: two indices separated by a colon,
		    >>> word = 'Hello'
		    >>> word[0:2]
			'He'
		    >>> word[2:4]
		    'll'
		    >>> word[:2]    #omitted first index defaults to zero
		    'He'
		    >>> word[2:]    #omitted second index defaults to the size of the string being sliced
		    'llo'
		    >>> word[0]='x' #Unlike a C string, Python strings cannot be changed

File I/O functions
-open(fname [,mode [,buffering ] ] ) -> Returns file object
  mode = ( r-read , w-write , a-append )
		+ [ + :Simultaneous read & write , U :Universal Newline i.e.line endings seen as \n in read mode, b :mode for BinaryFiles ]
  buffering = 0 for unbuffered, 1 for line buffered, >1 specifies bufferSize
