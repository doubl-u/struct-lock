
def structure(cc, kk):
	# cc = content length, kk = key length
	
	cc=cc
	kk=kk 

	total = cc+kk
	cr = cc - 1
	kr = kk - 26
	# cr and kr are the remaining contents and keys that are not yet added to the structure

	x = 3
	y = 3
	z = 3
	# 3 is set default coz, that is the minum value (it can store 1 character in it)

	#print(f"initial structure = 3x3x3\tcontents = {cc}\tkeys = {kk}\n")

	# To find the primary structure (largest fully covered cube/cubiod) that can be build with enought contents and keys
	while True:

		if x == y and y == z:
			ax = "x"
			ax1 = y
			ax2 = z

		elif x > y and y == z:
			ax = "y"
			ax1 = x
			ax2 = z
		
		elif x == y and y > z:
			ax = "z"
			ax1 = x
			ax2 = y

		else:
			break

		check, sub_c, sub_k = structure_check(ax1,ax2,cr,kr,0,True)

		if check:
			cr -= sub_c
			kr -= sub_k
			if ax == "x":
				x+=1
			elif ax == "y":
				y+=1
			else:
				z+=1
			continue
		else: 
			#print(f"{x}x{y}x{z}\tremaining = {cr} & {kr}\t in-use: {cc-cr} & {kk-kr}\t{(cc-cr)/cc*100}%")
			break

	# type1 are the plane on the axis which contains the keys, while type2 does not
	type1_x = []
	type2_x = []
	type1_y = []
	type2_y = []
	type1_z = []
	type2_z = []

	for a in range(1,x+1):
		type1_x.append(a)
	for a in range(1,y+1):
		type1_y.append(a)
	for a in range(1,z+1):
		type1_z.append(a)

	# just place holders (index of the last type1 in each axis)
	current_x=type1_x.index(x)
	current_y=type1_y.index(y)
	current_z=type1_z.index(z)

	# To find if there are enough remaining content to fill in the primary structure
	while True:

		if x == y and y == z:
			ax = "x"
			ax1 = y
			ax2 = z

		elif x > y and y == z:
			ax = "y"
			ax1 = x
			ax2 = z
		
		elif x == y and y > z:
			ax = "z"
			ax1 = x
			ax2 = y

		else:
			break

		check,sub_c = structure_check(ax1,ax2,0,0,cr,False)
		# checks if there are enough characters for expansion of the structure (in the order of x axis first and then y axis. not z axis coz that would have already be done in the primary structure^)
		if check:
			cr -= sub_c
			if ax == "x":
				type1_x,type2_x=expand(current_x,type1_x,type2_x)
				x+=1
				current_x-=1
				if current_x==0:
					current_x=len(type1_x)-1
			elif ax == "y":
				type1_y,type2_y=expand(current_y,type1_y,type2_y)
				y+=1
				current_y-=1
				if current_y==0:
					current_y=len(type1_y)-1
			else:
				type1_z,type2_z=expand(current_z,type1_z,type2_z)
				z+=1
				current_z-=1
				if current_z==0:
					current_z=len(type1_z)-1
			continue
		else: 
			#print(f"{x}x{y}x{z}\tremaining = {cr} & {kr}\t in-use: {cc-cr} & {kk-kr}\t{(cc-cr)/cc*100}%")
			break
		break

	k_positions=position_finder(x,y,z,type2_x,type2_y,type2_z)
	
	return k_positions, cr, kr

def position_finder(x,y,z,not_x,not_y,not_z):

	k_positions = []
	x_pos = 1
	y_pos = 1
	z_pos = 1

	# The way the posuition is determined is that, it shoulc be at the surface of the structure (side, edge or corner), and it should not be in the not_*planes* 
	for position in range(1,x*y*z+1):
		check1 = (x_pos == 1 or x_pos == x) or (y_pos == 1 or y_pos == y) or (z_pos == 1 or z_pos == z) 

		check2 = x_pos not in not_x and y_pos not in not_y and z_pos not in not_z
		
		if check1 and check2:
			k_positions.append(position)
		x_pos+=1
		if x_pos > x:
			y_pos+=1
			x_pos=1
		if y_pos > y:
			z_pos+=1
			y_pos=1
		if z_pos > z:
			break
	return k_positions

def structure_check(ax1,ax2,c,k,r,primary):
	# ax = axis length
	if primary:
		if c >= ((ax1-2)*(ax2-2)) and k >= ((ax1*ax2)-(ax1-2)*(ax2-2)):
			return True, ((ax1-2)*(ax2-2)), ((ax1*ax2)-(ax1-2)*(ax2-2))
		else:
			return False, 0, 0
	else:
		if r >= (ax1*ax2):
			return True, (ax1*ax2)
		else:
			return False, 0

def expand(placeHolder,type1,type2):
	# the new plane is added just before the type1 axis, and everything from both types is shifted by 1
	for a in range(0,len(type1)):
		if a>=placeHolder:
			type1[a]+=1
	for a in range(0,len(type2)):
		if type2[a]>=type1[placeHolder]:
			type2[a]+=1

	type2.append(type1[placeHolder]-1)
	type2.sort()
	return type1,type2

if __name__=="__main__":
	
	structure(1000,100)
