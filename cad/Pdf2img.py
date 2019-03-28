import os
from wand.image import Image


def pdf2img(pdf_name):
    filepath, filename = os.path.split(pdf_name)
    shotname, extension = os.path.splitext(filename)
    pdf = Image(filename=pdf_name, resolution=300)

    pdfImage = pdf.convert("jpeg")

    img = pdfImage.sequence[0]

    page = Image(image=img)
    
    pictureName = shotname+ ".jpg"
    page.save(filename=pictureName)

    return pictureName



# if __name__ == "__main__":
#     pdf_name = './cad3.pdf'  #导进去的pdf
#     pdf2img(pdf_name)
