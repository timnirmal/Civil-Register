from tkinter import *
from tkinter import filedialog

from lib import FingerPrintScan


def logout():
    root.destroy()


def headerRender():
    global img, label, label
    # Create Widgets
    # Image Widget for top frame in x=84 y=48 size=34x48
    img = PhotoImage(file='image 2.png')
    label = Label(top, image=img, width=34, height=48, bg='white')
    # resize image to fit label size
    label.image = img
    label.place(x=84, y=30)
    # Label Widget right of image in x=128 y=48 size=200x48
    label = Label(top, text='Civil Registration', font=('arial', 26), fg='black', bg='white')
    label.place(x=128, y=30)
    # Image Widget for top frame in x=1120 y=48 size=51x51
    img = PhotoImage(file='circle.png')
    label = Label(top, image=img, width=51, height=51, bg='white')
    # resize image to fit label size
    label.image = img
    label.place(x=1120, y=30)
    # Label Widget right of image in x=1184 y=48 size=200x48 show username
    label = Label(top, textvariable=username, font=('arial', 20), fg='black', bg='white')
    label.place(x=1184, y=30)
    # Link Widget for top frame in x=1248 y=48 size=200x48 for logout button and call logout function
    link = Label(top, text='Logout', font=('arial', 10), fg='blue', bg='white', cursor='hand2')
    link.place(x=1184, y=60)
    link.bind('<Button-1>', logout)


def MiddleRender():
    global img, label, label
    """ Fingerprint section and basic info in middle frame """
    # Image Widget for middle frame in x=84 y=48 size=276x334
    img = PhotoImage(file='image 1.png')
    # label = Label(middle, image=img, width=250, height=303, bg='white')
    label = Label(middle, image=img, width=240, height=291, bg='white')
    # resize image to fit label size
    label.image = img
    label.place(x=84, y=30)
    # Two button below image in x=84 y=374 size=276x48
    btn = Button(middle, text='Capture', font=('arial', 15), width=10, height=1, bg='green', fg='white')
    btn.place(x=84, y=348)
    btn = Button(middle, text='Clear', font=('arial', 15), width=10, height=1, bg='green', fg='white')
    btn.place(x=220, y=348)
    # Label Right of image in x=420 y=48 size=200x48
    label = Label(middle, text='Basic Information', font=('arial', 20), fg='black', bg='white')
    label.place(x=420, y=30)
    # Label Right of image in x=420 y=96 size=200x48
    label = Label(middle, text='Name', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=96)
    # Label Right to Name to show name in x=600 y=96 size=200x48 show name
    label = Label(middle, textvariable=name, font=('arial', 15), fg='black', bg='white')
    label.place(x=600, y=96)
    # Label Right of image in x=420 y=144 size=200x48
    label = Label(middle, text='Status', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=144)
    # Label Right to Status to show status in x=600 y=144 size=200x48 show status
    label = Label(middle, textvariable=status, font=('arial', 15), fg='black', bg='white')
    label.place(x=600, y=144)
    # Label Right of image in x=420 y=192 size=200x48
    label = Label(middle, text='Date of Birth', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=192)
    # Label Right to Date of Birth to show dob in x=600 y=192 size=200x48 show dob
    label = Label(middle, textvariable=dob, font=('arial', 15), fg='black', bg='white')
    label.place(x=600, y=192)
    # Label Right of image in x=420 y=240 size=200x48
    label = Label(middle, text='Age', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=240)
    # Label Right to Age to show age in x=600 y=240 size=200x48 show age
    label = Label(middle, textvariable=age, font=('arial', 15), fg='black', bg='white')
    label.place(x=600, y=240)
    # Label Right of image in x=420 y=288 size=200x48
    label = Label(middle, text='Job', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=288)
    # Label Right to Job to show job in x=600 y=288 size=200x48 show job
    label = Label(middle, textvariable=job, font=('arial', 15), fg='black', bg='white')
    label.place(x=600, y=288)
    # Label Right of image in x=420 y=336 size=200x48
    label = Label(middle, text='Address', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=336)
    # Label Right to Address to show address in x=600 y=336 size=200x48 show address
    label = Label(middle, textvariable=address, font=('arial', 15), fg='black', bg='white')
    label.place(x=600, y=336)


def bottomRender():
    global label
    # 4 Section for bottom frame in x=84 y=48 size=276x334
    # Section 1
    # Section 1 Label in x=84 y=48 size=276x48 "Birth Certificate"
    label = Label(bottom, text='Birth Certificate', font=('arial', 14), fg='black', bg='white')
    label.place(x=84, y=0)
    # Birth Certificate (Link)
    # Birth Place :
    # Mother’s Name :
    # Father’s Name :
    # Grandfather’s Name :
    # Label below Birth Certificate in x=84 y=96 size=276x48 "Birth Place"
    label = Label(bottom, text='Birth Place', font=('arial', font_size), fg='black', bg='white')
    label.place(x=84, y=48)
    # Label below Birth Place in x=84 y=144 size=276x48 "Mother’s Name"
    label = Label(bottom, text='Mother’s Name', font=('arial', font_size), fg='black', bg='white')
    label.place(x=84, y=96)
    # Label below Mother’s Name in x=84 y=192 size=276x48 "Father’s Name"
    label = Label(bottom, text='Father’s Name', font=('arial', font_size), fg='black', bg='white')
    label.place(x=84, y=144)
    # Label below Father’s Name in x=84 y=240 size=276x48 "Grandfather’s Name"
    label = Label(bottom, text='Grandfather’s Name', font=('arial', font_size), fg='black', bg='white')
    label.place(x=84, y=192)
    # Section 2
    # Section 2 Label in x=420 y=48 size=276x48 "NIC"
    label = Label(bottom, text='NIC', font=('arial', 14), fg='black', bg='white')
    label.place(x=420, y=0)
    # NIC (Link)
    # NIC Number :
    # Other name :
    # Label below NIC in x=420 y=96 size=276x48 "NIC Number"
    label = Label(bottom, text='NIC Number', font=('arial', font_size), fg='black', bg='white')
    label.place(x=420, y=48)
    # Label below NIC Number in x=420 y=144 size=276x48 "Other name"
    label = Label(bottom, text='Other name', font=('arial', font_size), fg='black', bg='white')
    label.place(x=420, y=96)
    # Section 3
    # Section 3 Label in x=756 y=48 size=276x48 "Vital Stats"
    label = Label(bottom, text='Vital Stats', font=('arial', 14), fg='black', bg='white')
    label.place(x=756, y=0)
    # Vital Stats (Link)
    # Family Count :
    # Sex Count :
    ## -- M Count : -- F Count :
    # Jobs :
    # person name - job
    # Label below Vital Stats in x=756 y=96 size=276x48 "Family Count"
    label = Label(bottom, text='Family Count', font=('arial', font_size), fg='black', bg='white')
    label.place(x=756, y=48)
    # Label below Family Count in x=756 y=144 size=276x48 "Sex Count"
    label = Label(bottom, text='Sex Count', font=('arial', font_size), fg='black', bg='white')
    label.place(x=756, y=96)
    # Label below Sexuality Count in x=756 y=192 size=276x48 "M count"
    label = Label(bottom, text='M Count', font=('arial', font_size), fg='black', bg='white')
    label.place(x=756, y=144)
    # Label Right to M Count in x=756 y=240 size=276x48 "F Count"
    label = Label(bottom, text='F Count', font=('arial', font_size), fg='black', bg='white')
    label.place(x=756, y=192)
    # Label below Sexuality Count in x=756 y=288 size=276x48 "Jobs"
    label = Label(bottom, text='Jobs', font=('arial', font_size), fg='black', bg='white')
    label.place(x=756, y=240)
    # Label below Jobs in x=756 y=336 size=276x48 "person name - job"
    label = Label(bottom, text='person name - job', font=('arial', font_size), fg='black', bg='white')
    label.place(x=756, y=288)
    # Section 4
    # Section 4 Label in x=1092 y=48 size=276x48 "Marriage Certificate"
    label = Label(bottom, text='Marriage Certificate', font=('arial', 14), fg='black', bg='white')
    label.place(x=1092, y=0)
    # Marriage Certificate (Link)
    # Marriage Date :
    # Marriage Place :
    # Husband Name :
    # Wife Name :
    # Label below Marriage Certificate in x=1092 y=96 size=276x48 "Marriage Date"
    label = Label(bottom, text='Marriage Date', font=('arial', font_size), fg='black', bg='white')
    label.place(x=1092, y=48)
    # Label below Marriage Date in x=1092 y=144 size=276x48 "Marriage Place"'
    label = Label(bottom, text='Marriage Place', font=('arial', font_size), fg='black', bg='white')
    label.place(x=1092, y=96)
    # Label below Marriage Place in x=1092 y=192 size=276x48 "Husband Name"
    label = Label(bottom, text='Husband Name', font=('arial', font_size), fg='black', bg='white')
    label.place(x=1092, y=144)
    # Label below Husband Name in x=1092 y=240 size=276x48 "Wife Name"
    label = Label(bottom, text='Wife Name', font=('arial', font_size), fg='black', bg='white')
    label.place(x=1092, y=192)


def ReadFinger():
    """ Read finger from sensor and return image """
    # Select File dialog box
    file = filedialog.askopenfilename(initialdir=r"C:\Users\timni\PycharmProjects\Civil-Register\Data\Altered"
                                                 r"\SelectedData", title='Select File',
                                      filetypes=(('BMP', '*.bmp'), ('All Files', '*.*')))

    print("Before file")
    print(file)
    if file:
        FingerPrintScan.matchfingerprint(file)


if __name__ == '__main__':
    # Create Object and setup window
    root = Tk()
    root.title('Dashboard')

    # Create Variables for the widgets
    username = StringVar()
    userPosition = StringVar()
    name = StringVar()
    status = StringVar()
    dob = StringVar()
    age = StringVar()
    job = StringVar()
    address = StringVar()

    birthPlace = StringVar()
    mothersName = StringVar()
    fathersName = StringVar()
    grandfathersName = StringVar()

    nicNumber = StringVar()
    otherName = StringVar()

    familyCount = StringVar()
    sexCount = StringVar()
    mCount = StringVar()
    fCount = StringVar()
    # List of jobs
    jobs = []

    marriageDate = StringVar()
    marriagePlace = StringVar()
    husbandName = StringVar()
    wifeName = StringVar()

    # Set the username and userPosition
    username.set("Username")
    userPosition.set("User Position")
    name.set("Name")
    status.set("Status")
    dob.set("Date of Birth")
    age.set("Age")
    job.set("Job")
    address.set("Address")

    # Create Frames
    top = Frame(root, width=1440, height=100, bg='white')
    top.pack(side=TOP)
    middle = Frame(root, width=1440, height=430, bg='white')
    middle.pack(side=TOP)
    bottom = Frame(root, width=1440, height=240, bg='white')
    bottom.pack(side=BOTTOM)

    headerRender()

    MiddleRender()

    font_size = 12

    bottomRender()

    # # Entry Right of image in x=420 y=144 size=200x48
    # entry = Entry(middle, font=('arial', 15), width=30)
    # entry.place(x=420, y=144)

    root.mainloop()
