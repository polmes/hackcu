import pytesseract
import pandas as pd
from PIL import Image
from PIL import ImageFilter

def ocr_text(image_path):
    """Extracts ocr data and returns a string for it or returns none if no data present"""
    image = Image.open(image_path).convert('RGB')
    image.filter(ImageFilter.SHARPEN)
    df = pytesseract.image_to_data(image, output_type = "data.frame" )
    if (df['conf'] > 95).any():
        df = df.loc[df['conf'] > 70]
        seen = []
        for i in df.text:
            seen.append(i)
        ret = "and it says: "
        if seen[len(seen) - 1] == "" or seen[len(seen) - 1][0] == " ":
            seen.pop()
        newphrase = True
        for i in seen:
            if i == "" or i[0] == " ":
                ret += "\" and"
                newphrase = True
            elif newphrase:
                newphrase = False
                ret += " \"" + i
            else:
                ret += " " + i
        ret += "\"."
    else:
        ret = None
    return ret

if __name__ == '__main__':
    print(get_text("8b6.jpg"))
    
def resList(response):
    """breaks response into chunks less than 280 characters"""
    responseList = []
    
    while len(response) > 280:
        inThaCut = True
        current_char = 0
        response_len = 1
        word_len = 0
        while current_char < 273:
            if response[current_char] == " ":
                response_len += word_len
                word_len = 0
            word_len += 1
            current_char += 1
        responseList.append(response[:response_len] + "...")
        response = "..." + response[response_len:]
    responseList.append(response)
    return responseList