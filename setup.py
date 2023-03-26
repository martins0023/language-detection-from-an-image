import os
from PIL import Image 

def system_run():

    caption = """
     __                  / || \
    |  |                / /  \ \
    |  |               / /    \ \
    |  |              / /______\ \
    |  |             / /        \ \
    |  |            / /          \ \
    |  |_________  / /            \ \
    |____________|/ /              \ \

    """

    img = Image.open("image.jpg") #process the image 
    
    if img.height > 300 or img.width > 300: #get the height and width of the image
        output_size = (900, 900) #crop the image to the output size
        img.thumbnail(output_size) 
        ext = ['.jpeg', '.png', '.jpg'] #create list of extensions to save as 
        for extension in ext: #loop over the list 
            img.save(f"image_resize{extension}")

    os.system('python3 text_extraction.py')
    os.system('python3 detect_language.py')

    #os.system('python3 load_text.py')
    #os.system('python3 display_lang.py')
   
# os.system('python3 language_detection.py')

system_run()