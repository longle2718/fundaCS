'''
Long Le <longle1@illinois.edu>
University of Illinois
'''
import time

def mergeSort(A):
	'''
	The merge sort base function
	'''
	recurMergeSort(A,0,len(A))
	return A
	
def recurMergeSort(A,iS,iE):
	if iE-iS <= 1:
		return # a list of 1 element is sorted
	iM = (iS+iE)//2
	recurMergeSort(A,iS,iM) #iS,...,iM-1
	recurMergeSort(A,iM,iE) #iM,...,iE-1
	merge(A,iS,iM,iE)

def merge(A,iS,iM,iE):
	B = [0]*len(A)
	i = iS
	j = iM
	for k in range(iS,iE):
		# only one subset or both, in which the smaller is taken
		if j >= iE or (i < iM and A[i] <= A[j]):
			B[k] = A[i]
			i += 1
		else:
			B[k] = A[j]
			j += 1
	copy(A,iS,iE,B)

def copy(A,iS,iE,B):
	for k in range(iS,iE):
		A[k] = B[k]

#############################
def pivotSort(A):
	'''
	The pivot sort base function
	'''
	recurPivotSort(A,0,len(A))
	return A

def recurPivotSort(A,iS,iE):
	if iS < iE-1:
		p = partition(A,iS,iE)
		recurPivotSort(A,iS,p) # iS,...,p-1
		recurPivotSort(A,p+1,iE) # p+1,...,iE-1
	return

def partition(A,iS,iE):
	p = A[iE-1]
	i = iS # the next place to be swapped
	for j in range(iS,iE-1):
		if A[j] <= p:
			#print('swaping '+str(i)+' and '+str(j))
			# fill all lower than pivot in the beginning
			swap(A,i,j)
			i += 1
	swap(A,i,iE-1)
	return i

def swap(A,k,l):
	tmp = A[l]
	A[l] = A[k]
	A[k] = tmp
	
if __name__ == '__main__':
	sTime = time.time()
	sA = mergeSort([8,4,2,5,6,9,2,1,11,25,23,10,40,33,32,31,28])
	#print('elapsed time = '+str(time.time()-sTime))
	print('elapsed time = %s' % (time.time()-sTime))
	print(sA)

	sTime = time.time()
	sA = pivotSort([8,4,2,5,6,9,2,1,11,25,23,10,40,33,32,31,28])
	#sA = pivotSort([3,4,2])
	#print('elapsed time = '+str(time.time()-sTime))
	print('elapsed time = %s' % (time.time()-sTime))
	print(sA)
