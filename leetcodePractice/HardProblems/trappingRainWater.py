def trappingRainWater(height):
    left=0
    right=len(height)-1
    leftIndex=0
    rightIndex=0
    result=0
    while left<right:
        if height[left]<height[right]:
            if height[left]>=leftIndex:
                leftIndex=height[left]
            else:
                result=result+(leftIndex-height[left])
            left=left+1
        else:
            if height[right]>=rightIndex:
                rightIndex=height[right]
            else:
                result=result+(rightIndex-height[right])
            right=right-1
    return result

height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trappingRainWater(height))