This was my final year major project where my team and i have employed a method for the text
extraction from a given picture of medical strip. This method employs pre-processing methods like MSER, edge detection and Stroke
Width Transform for detecting text regions.Using MSER, potential text regions are identified in the image based on consistency of color
and contrast. Further ahead, we use edge detection algorithms to identify pixels belonging to an “edge”.These edge pixels are then to be
used in the stroke width algorithm to detect the strokes in the image and further filter out non-text regions. The remaining text regions
are then filtered based on their geometric properties and fed as input to Tesseract, a segmentation-free OCR software to extract text from
the image.
