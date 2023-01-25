def LCSubStr(X, Y):

	m = len(X)
	n = len(Y)


	result = 0

	end = 0

	length = [[0 for j in range(m)]
				for i in range(2)]

	currRow = 0


	for i in range(0, m + 1):
		for j in range(0, n + 1):
			if (i == 0 or j == 0):
				length[currRow][j] = 0
			
			elif (X[i - 1] == Y[j - 1]):
				length[currRow][j] = length[1 - currRow][j - 1] + 1
				
				if (length[currRow][j] > result):
					result = length[currRow][j]
					end = i - 1
			else:
				length[currRow][j] = 0


		currRow = 1 - currRow

	if (result == 0):
		return "-1"

	
	return X[end - result + 1 : end + 1]
	
# Driver code
if __name__=="__main__":
	
	X = "RepublicDay"
	Y = "Republic"
	
	# Function call
	print(LCSubStr(X, Y))

# This code is contributed by rutvik_56
