import cv2
import numpy as np
import argparse
from kernels import kernels
import time 

def filter(image2D,kernel,norm=True):
    padding = int((kernel.shape[0]-1)/2) 
    image2D_pad = np.pad( image2D, padding )

    new_image = np.zeros( image2D.shape )

    for x in range( image2D.shape[0] - padding ):
        for y in range ( image2D.shape[1] - padding):
            window = image2D_pad[ x : x + kernel.shape[0] , y : y + kernel.shape[0] ]
            new_image[x][y] = ( window * kernel ).sum()

    if not norm: return new_image

    new_image = np.where(new_image>255,255,new_image)
    new_image = np.where(new_image<0,0,new_image)
   
    return new_image.astype(np.uint8)


def combine(image2D,k1,k2):

    
    f1 = filter(image2D,k1,norm=False)
    f2 = filter(image2D,k2,norm=False)


    new_image = np.sqrt(f1**2 + f2**2) 

    new_image = np.where(new_image>255,255,new_image)
    new_image = np.where(new_image<0,0,new_image)
   
    return new_image.astype(np.uint8)





if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Filter 2D Gray Image Processing - UNICAMP")
    parser.add_argument("file", help="input file image .png" )
    parser.add_argument("-k","--kernel", help="Choose number of kernel to apply", type=str, choices=["1","2","3","4","5","6","7","8","9","10"] , default=0)
    parser.add_argument("-s","--save", help="Save Image", type=str )

    args = parser.parse_args()

    # print( "Kernel: " )
    # print( kernels[args.kernel] )

    print( "File: ",args.file )

    image = cv2.imread( args.file ,0)

    t1 = time.time()
    # print("asd",args.kernel)
    if(args.kernel == "10"):
        image_new = combine(image,kernels["1"],kernels["2"])
    else:
        image_new = filter(image,kernels[args.kernel])
    t2 = time.time()

    print("Time: ", t2-t1 ,"s")

    if ( args.save ):
        cv2.imwrite(args.save, image_new)
    else:
        cv2.imshow(args.file,image_new)
    print("Press any key to exit")
    cv2.waitKey()




