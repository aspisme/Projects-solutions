'''Bubble sort algorithm
I thik this migth be better solution.
11.08.17 by Andrew Polochanin'''

def bubbleSort(seq):
	for count in range(len(seq)):
		for i in range(len(seq)-1):
			if seq[i] > seq[i+1]:
				bf = seq[i]
				seq[i] = seq[i+1]
				seq[i+1] = bf
	return seq

if __name__ == '__main__':
	sequence = [8, 5, 0, 2, 1, 7, 3, 6, 9, 4]
	print(sequence)
	print(bubbleSort(sequence), sep='\n')
	
