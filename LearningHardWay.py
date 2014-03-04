# -- coding: utf-8 --
#Printing & Operators
print "t'is not a #comment" #but this is a comment
print 1 + 6 % 2 * 2 - 21 / 7 , "!= 0"
print 5 ,">=", 9 / 3 % 2 * 3.0 ,"is", 5 >= 2 / 3 % 2 * 3.0
#Variables
name = "monty"
shoe_brand = "python"
shoe_size = 13
shoeWidth = "wide"
print name ,"bought a", shoe_brand ,"shoe of size", shoe_size, shoeWidth,"from a shoe store"
#Format Strings
my_name = "Ashish"
my_age = 29
my_height = 1.84
my_weight = 81.25
my_eyes = "Brown"
my_teeth = "White"
my_hair = 'Black'
print 'Who is that guy with %r colored hair?' % my_hair # %r = raw string, %s = string, %d = integer
print "It's %s, he is %d years old, %.2f meters tall & weighs %.1f kgs" % (my_name, my_age, my_height, my_weight)
print "He has got %s eyes & %d %s teeth !!" % (my_eyes, 32,my_teeth), #comma at the end of print means next line will continue from here
print "His '%s' is %.2f " % ( 'BMI Ratio', (my_weight)/(my_height*my_height) )
# use %r only for debugging purposes
myLine = "%r %r %r %r"
print myLine % (1,2,3,4)
print myLine % ("one","tw'o",'three','fou"r') #by default single quotes are printed (until single quotes have been used inside double quotes)
print myLine % (myLine, myLine, myLine, myLine % (1,2,3,4) )
#More Printing
print "Ingredients for Cake:\nMaida\t\t100 gms\nBaking Powder\t20 gms\nVanilla Essence\t2-3 drops\nDry Fruit\t30-50 gms\nCurd\t\t1/2 Cup"
print """
This is a multi-line recipe string,
Mix the ingredients in a bowl
Beat using a beater and Leave for 10 minutes
"""
print """
Pre-heat the oven and oil the baking plate
Put the mixture in baking plate
Put the baking plate in oven"""
print """Set the oven to 180 degress for 30 minutes
Voila"""
#Escape Sequences
reply1 = "It's \"aweeesome\" !!"
reply2 = 'T\'waas Yummmy'
print "Ear1 = %r" % reply1 #raw string prints escape sequence(s)
print "Ear2 = %s & %s" % (reply1,reply2)
print """\\ \'\" \abell\bbackspace
..\nLineFeed \fFormFeed \fEven more formFeed
\N{Unicode CharacterName} \rCarrraigeReturn
\u8377
end of string"""
print u'\u20b9 \u3020'

