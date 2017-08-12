'''Merge sorting algorithm
10.08.17 by Andrew Polochanin'''


def compare(arr):
	arr1 = devDown(arr) 
	arr2 = devUp(arr)
	if len(arr1) != 1:
		arr1 = compare(arr1)
	if len(arr2) != 1:
		arr2 = compare(arr2)
	return sortSeq(arr1, arr2)	

def sortSeq(arr1, arr2):
	nArr = []
	while arr1:
		while arr2:
			if arr1[0] > arr2[0]:
				nArr.append(arr2.pop(0))
			else: break
		nArr.append(arr1.pop(0))
	return nArr + arr1 + arr2			

def devDown(seq):
	return seq[:int(len(seq)/2)]

def devUp(seq):
	return seq[int(len(seq)/2):]




if __name__ == '__main__':
	#sequence = [4, 8, 2, 0, 5, 1, 9, 3, 7, 6]
	sequence = [3, 8, 0, 1, 4, 9, 5, 7, 2, 6]
	print(sequence)
	print(compare(sequence))
