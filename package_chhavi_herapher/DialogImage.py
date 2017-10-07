import Tkinter, tkFileDialog

class DialogImage:
    root = Tkinter.Tk()
    root.withdraw()
    file_path = tkFileDialog.askopenfilename()
    print (file_path)