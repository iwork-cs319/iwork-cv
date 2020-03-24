import cv2
import numpy as np
import pytesseract

def bulkPointOCR(points, img, w, h):
    compiled = []
    for p in points:
        match = cv2.cvtColor(img[p[1]-np.floor(h/2).astype(int):p[1]+np.floor(h/2).astype(int)+1, (p[0]-np.floor(w/2).astype(int)):p[0]+np.floor(w/2).astype(int)+1], cv2.COLOR_BGR2RGB)
        text = pytesseract.image_to_string(match, lang='eng',
                            config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789ABC')
        compiled.append({"x": int(p[1]), "y": int(p[0]), "workspace_name": text})
    return compiled