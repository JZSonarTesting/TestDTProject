from PIL import Image
import imagehash
import cv2


if __name__ == '__main__':
    differnet_percentage = 0.05
    im1 = cv2.imread('1_1.jpeg')

    hash0 = imagehash.average_hash(Image.open('2.jpg'))
    hash1 = imagehash.average_hash(Image.open('1_1.jpeg'))
    cutoff = (im1.shape[0]*im1.shape[1]) * differnet_percentage
    print(hash0-hash1)
    cv2.imshow('img', hash0-hash1)
    cv2.waitKey(0)
    print(im1.shape[0]*im1.shape[1])
    # maximum bits that could be different between the hashes.

    if hash0 - hash1 < cutoff:
        print('images are similar')
    else:
        print('images are not similar')