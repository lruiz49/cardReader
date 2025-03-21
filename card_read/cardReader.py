import cv2 as cv
import easyocr as ocr

reader = ocr.Reader(['en'],gpu=False) # this needs to run only once to load the model into memory



def draw_bounding_boxes(original, detections, threshold=0.25):

    words = []

    for bbox, text, score in detections:

        if score > threshold:

            cv.rectangle(original, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 5)

            cv.putText(original, text, tuple(map(int, bbox[0])), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255, 0, 0), 2)
            words.append(text)

    return words


def prepareImage(img, type):

    if img is None:
        raise ValueError("The input image is None. Please check the file path or image loading process.")
    
    grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    blur = cv.GaussianBlur(grey,(3,3), cv.BORDER_DEFAULT)
    
    if type == 1:
        cropp = blur[0:100,0:img.shape[0]- 250]
    else: 
        cropp = blur[0:100]

    dilate = cv.dilate(cropp, (3,3), iterations=1)
    
    
    return cropp, reader.readtext(dilate)



#returns a tuple (name, image proccesed)
#Type 0 for magic, 1 for pokemon, 2 for yugi
#If not correct type error may happen 
def readCard(card, type, treshold = 0.25):
    
    img = cv.imread(card)

    if img is None:
        raise ValueError("The input image is None. Please check the file path or image loading process.")

    img = cv.resize(img,(int(img.shape[1]*0.75),int(img.shape[0]*0.75)),interpolation=cv.INTER_AREA)
    

    original = img.copy()

    preparedImage, detections = prepareImage (img, type)

    result = (draw_bounding_boxes(original, detections, treshold),original)

    return result

