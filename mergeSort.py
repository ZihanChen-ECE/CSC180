#! /usr/bin/env python

#this script is for merge sort

def mergeList(list1, list2):

	len1 = len(list1)
	len2 = len(list2)
	ii, jj = 0,0
	newList = []
	while ii < len1 and jj < len2:
		if list1[ii] < list2[jj]:
			newList.append(list1[ii])
			ii+=1
		else:
			newList.append(list2[jj])
			jj+=1

	while ii<len1:
		newList.append(list1[ii])
		ii+=1
	while jj<len2:
		newList.append(list2[jj])
		jj+=1

	return newList

def MergeSort(List):
	if len(List)==1:
		return List
	else:
		left = 0
		right = len(List)
		mid = (left+right)/2
		leftList = MergeSort(List[left:mid])
		rightList = MergeSort(List[mid:right])
		List = mergeList(leftList, rightList)
		return List






if __name__=='__main__':
	L = [5,8,9,1,7,3,6,5]
	nL = MergeSort(L)
	print nL




