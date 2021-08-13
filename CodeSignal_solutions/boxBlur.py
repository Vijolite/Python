#Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.
#The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.
#Return the blurred image as an integer, with the fractions rounded down.

import math
def boxBlur(image):
    ans=[]
    for i in range(len(image)-2):
        ans_line=[]
        for j in range(len(image[0])-2):
            average=0
            for ii in range(i,i+3):
                for jj in range(j,j+3):
                    average+=image[ii][jj]
            average=math.floor(average/9)
            ans_line.append(average)
        ans.append(ans_line)
    return ans
