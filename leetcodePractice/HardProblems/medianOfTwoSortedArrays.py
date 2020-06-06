# Divide and conquer method

def medianOfArray(nums1,nums2):
    n1=len(nums1)
    n1initial=n1
    n2=len(nums2)
    nFinal=n1+n2
    while n1<nFinal:
        nums1.append('null')
        n1=n1+1
    i=0
    j=0
    k=0

    while i<n1 and j<n2:
        if nums1[i]=='null':
            break
        if nums1[i]<=nums2[j]:
            nums1[k]=nums1[i]
            i=i+1
            k=k+1
        else:
            valueOfIndex=nums1.index('null')
            nums1[k],nums1[valueOfIndex]=nums1[valueOfIndex],nums1[k]
            nums1[k]=nums2[j]
            j=j+1
            k=k+1
            i=i+1
    if nums1[i]!='null':
        while i<n1:
            nums1[k]=nums1[i]
            i=i+1
            k=k+1
    while j<n2:
        nums1[k]=nums2[j]
        j=j+1
        k=k+1
    print("final",nums1)

# nums1=[1,2,4,5,6]
# nums2=[3]

nums1=[0,0,3]
nums2=[-1,1,1,1,2,3]
medianOfArray(nums1,nums2)