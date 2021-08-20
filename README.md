This was my final year major project where my team and i have employed a method for the text
extraction from a given picture of medical strip. This method employs pre-processing methods like MSER, edge detection and Stroke
Width Transform for detecting text regions.Using MSER, potential text regions are identified in the image based on consistency of color
and contrast. Further ahead, we use edge detection algorithms to identify pixels belonging to an “edge”.These edge pixels are then to be
used in the stroke width algorithm to detect the strokes in the image and further filter out non-text regions. The remaining text regions
are then filtered based on their geometric properties and fed as input to Tesseract, a segmentation-free OCR software to extract text from
the image.

Example Input/Output


![Screenshot 2021-08-21 000007](https://user-images.githubusercontent.com/41735734/130278172-7f17474c-b782-459c-913f-2ccb7b995e09.png)
![Screenshot 2021-08-21 000034](https://user-images.githubusercontent.com/41735734/130278179-6f533b63-600b-4531-8c2b-2646fdf80015.png)
![Screenshot 2021-08-21 000056](https://user-images.githubusercontent.com/41735734/130278180-1e841041-cf72-4cea-8826-e858a858a8c9.png)
![Screenshot 2021-08-21 000109](https://user-images.githubusercontent.com/41735734/130278181-f47e14de-8849-499c-b0cd-2a41de34070e.png)



For more, please refer the report.

