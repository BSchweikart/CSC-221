def main():
	pass
	# variables for three actors
	# true is near, false is far
	fox = True
	chicken = True
	grain = True
	
	#start
	#update(fox, chicken, grain)
	
	# step 1
	fox = False
	print("Step 1")
	update(fox, chicken, grain)
	
	# step 2
	fox = True
	print("Step 2")
	update(fox, chicken, grain)
	#step 3
	fox = True
	print("Step 3")
	update(fox, chicken, grain)


def update(fox, chicken, grain):
	"""
	on each turn, prints out the position of th three actors.
	input: position of fox, chicken, grain (boolean) returns none
	"""
	if fox == True:
		print("Fox is on the near side")
		print("Chicken is on the far side")
		print("Grain is on the far side")
	else:
		print("Fox is on the far side ")
		print("Chicken is on the near side")
		print("Grain is on the near side")
	pass
	
#Start program	
main()