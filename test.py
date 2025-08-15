x = "engineer"

def myfunc():
	global x
    x = "engineer"
	print("qamar is a" + x)
	myfunc()

    print("qamar is a " + x)
