from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as tkmb
from PIL import Image
import time
import os

image = None

def upload() : 
    file = filedialog.askopenfilename(initialdir="C:", title="Select File", filetypes=(("JPG", ".jpg"), ("PNG", ".png"), ("WEBP", ".webp"), ("TIFF", ".tiff"), ("ICO", ".ico"), ("BMP", ".bmp")))
    global image
    image = Image.open(file)
    but1.config(bg="#9EE489", state=DISABLED, text="Image Uploaded")
    
def confi() :
    newpath = 'Results'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    global image 
    ctime = time.strftime("%d%b%Y%H%M%S")
    info = form.get()
    if info == "PNG (.png)" : 
        image.save(f"Results\\{ctime}.png", "PNG")
        tkmb.showinfo("Sucessfully changed the format!", f"The image has been saved in the 'Results' folder with the name '{ctime}'. Thanks for using our application 😄")
    elif info == "JPEG (.jpg)" : 
        image= image.convert('RGB')
        image.save(f"Results\\{ctime}.jpg", "JPEG")
        tkmb.showinfo("Sucessfully changed the format!", f"The image has been saved in the 'Results' folder with the name '{ctime}'. Thanks for using our application 😄")
    elif info == "ICO (.ico)" : 
        image.save(f"Results\\{ctime}.ico", "ICO")
        tkmb.showinfo("Sucessfully changed the format!", f"The image has been saved in the 'Results' folder with the name '{ctime}'. Thanks for using our application 😄")
    elif info == "BMP (.bmp)" : 
        image.save(f"Results\\{ctime}.bmp", "BMP")
        tkmb.showinfo("Sucessfully changed the format!", f"The image has been saved in the 'Results' folder with the name '{ctime}'. Thanks for using our application 😄")
    elif info == "TIFF (.tiff)" : 
        image.save(f"Results\\{ctime}.tiff", "TIFF")
        tkmb.showinfo("Sucessfully changed the format!", f"The image has been saved in the 'Results' folder with the name '{ctime}'. Thanks for using our application 😄")
    elif info == "WEBP (.webp)" : 
        image.save(f"Results\\{ctime}.webp", "WEBP")
        tkmb.showinfo("Sucessfully changed the format!", f"The image has been saved in the 'Results' folder with the name '{ctime}'. Thanks for using our application 😄")
    elif image == None : 
        tkmb.showerror("Image not selected!", "You didn't upload the image. Please try again!")
    else : 
         tkmb.showerror("Image Format not selected!", "You didn't select the format of the image from the dropdown list. Please try again!")
          
def unload() : 
    global image
    image = None
    but1.config(bg="#FF8484", text="Upload Image", state=NORMAL)


root = Tk()
root.geometry("450x150")
root.title("Image Format Changer")
root.resizable(False, False)
img11 = PhotoImage(file="images/downloadimg.png")
img22 = PhotoImage(file="images/uploadimg.png")
img1 = img11.subsample(20,20)
img2 = img22.subsample(20,20)

but1 = Button(root, text="Upload Image", command=upload, image=img2, compound=LEFT)
but2 = Button(root, text="Change and save", command=confi, image=img1, compound=LEFT)
but3 = Button(root, text="Unload Image", command=unload)

form = StringVar()

picform = OptionMenu(root, form, "JPEG (.jpg)", "PNG (.png)", "ICO (.ico)", "WEBP (.webp)", "BMP (.bmp)", "TIFF (.tiff)")
form.set("Select the format")

picform.config(bg="#BFFFFD")
but1.config(bg="#FF8484")
but3.config(fg="#0C2C8E")

picform.grid(row=0, column=0, padx=10)
but1.grid(row = 0, column=1, padx = 20)
but2.grid(row = 0, column=2)
but3.grid(row=1, column=1, pady=50)

root.mainloop()