import cv2
import numpy as np
import argparse
import time 


def sepia(image):
    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]

    rp = 0.393*r + 0.796*g + 0.189*b  
    gp = 0.349*r + 0.686*g + 0.168*b  
    bp = 0.272*r + 0.534*g + 0.131*b

    rp = np.where(rp>255,255,rp)
    gp = np.where(gp>255,255,gp)
    bp = np.where(bp>255,255,bp)

    
    new_image = np.stack((bp,gp,rp),axis=2)
    return new_image.astype(np.uint8)
    

def to_gris(image):
    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]

    i = 0.2989*r + 0.5870*g + 0.1140*b  
    i = np.where(i>255,255,i)

    return i.astype(np.uint8)



if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Sepia 2D color Image Processing - UNICAMP")
    parser.add_argument("file", help="input file image .png" )
    parser.add_argument("-e","--effect", help="Choose effect", type=str, choices=["sepia","gray"] , default="sepia")
    parser.add_argument("-s","--save", help="Save Image", type=str )



    args = parser.parse_args()


    print( "File: ",args.file )

    image = cv2.imread( args.file)

    t1 = time.time()
    if ( args.effect =="sepia" ):
        image_new = sepia(image)
    elif ( args.effect == "gray" ):
        image_new = to_gris(image)
    else:
        print ( "Option unkwon")
        


    t2 = time.time()

    print("Time: ", t2-t1 ,"s")
    if ( args.save ):
        cv2.imwrite(args.save, image_new)
    else:
        cv2.imshow(args.file,image_new)
    print("Press any key to exit")
    cv2.waitKey()


