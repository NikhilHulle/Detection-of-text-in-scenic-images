import cv2
import matplotlib.pyplot as plt
import numpy as np
from fuzzywuzzy import fuzz

from fuzzywuzzy import process


def apply_canny(img, sigma=0.33):
    v = np.median(img)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    return cv2.Canny(img, lower, upper)

def plt_show(*images):
    count = len(images)
    nRow = np.ceil(count / 3.)
    for i in range(count):
        plt.subplot(nRow, 3, i + 1)
        if len(images[i][0].shape) == 2:
            plt.imshow(images[i][0], cmap='gray')
        else:
            plt.imshow(images[i][0])
        plt.xticks([])
        plt.yticks([])
        plt.title(images[i][1])
    plt.show()

def get_med_name(query_string):

    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    query_string = ''.join(filter(whitelist.__contains__, query_string))
    query_string=" ".join(query_string.split())
    print(query_string)

    meds= ["Zentel","Evion", "Paracetamol", "Nopain", "Mefex", "Omacid", "Telsartan", "Zyrtec", "Elcon", "Mucosolvan", "Exylin", "Okacet", "Crestor", "Cataflam", "Rantac", "Domstal", "Motilium", "Ferose", "Concor", "Plavix", "Benedryl"]

    max_match_percent=0

    for med in meds:
        ratio = fuzz.partial_ratio(query_string.lower(), med.lower())
        print(ratio)
        if(ratio>max_match_percent):
            max_match_percent = ratio
            req_med = med

    return req_med
