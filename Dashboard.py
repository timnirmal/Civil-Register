from tkinter import *
from tkinter import filedialog

import cv2

from lib import FingerPrintScan

max_amount = 0
label1 = None

newFingerPrint = ""
labelFingerPrint = None

newName = ""
labelName = None

newStatus = ""
labelStatus = None

newDOB = ""
labelDOB = None

newAge = ""
lableAge = None

newJob = ""
labelJob = None

newAddress = ""
labelAddress = None

newBirthPlace = ""
labelBirthPlace = None
newMothersName = ""
labelMothersName = None
newFathersName = ""
labelFathersName = None
newGrandfathersName = ""
labelGrandfathersName = None

newNicNumber = ""
labelNicNumber = None
newOtherName = ""
labelOtherName = None

newFamilyCount = ""
labelFamilyCount = None
newSexCount = ""
labelSexCount = None
newMCount = ""
labelMCount = None
newFCount = ""
labelFCount = None
# List of jobs
jobs = []

newMarriageDate = ""
labelMarriageDate = None
newmArriagePlace = ""
labelMarriagePlace = None
newHusbandName = ""
labelHusbandName = None
newWifeName = ""
labelWifeName = None



def updateData():
    data = "Thimira"

    global newName, labelName
    global newStatus, labelStatus
    global newDOB, labelDOB
    global newAge, labelAge
    global newJob, labelJob
    global newAddress, labelAddress

    newName = data
    newStatus = data
    newDOB = "1999-01-01"
    newAge = "22"
    newJob = "Student"
    newAddress = "Colombo"

    labelName.configure(text=newName)
    labelStatus.configure(text=newStatus)
    labelDOB.configure(text=newDOB)
    labelAge.configure(text=newAge)
    labelJob.configure(text=newJob)
    labelAddress.configure(text=newAddress)

    global newFingerPrint, labelFingerPrint
    newFingerPrint = r"C:\Users\timni\PycharmProjects\Civil-Register\image 1.png"
    print("Before set")
    print(newFingerPrint)
    # show image in cv2 window if image is not empty
    if newFingerPrint:
        print("After set")
        print(newFingerPrint)
        newIMG = PhotoImage(file=newFingerPrint)
        labelFingerPrint.configure(image=newIMG)

    global newBirthPlace, labelBirthPlace
    global newmOthersName, labelmOthersName
    global newFathersName, labelFathersName
    global newGrandfathersName, labelGrandfathersName
    global newNicNumber, labelNicNumber
    global newOtherName, labelOtherName
    global newFamilyCount, labelFamilyCount
    global newSexCount, labelSexCount
    global newMCount, labelMCount
    global newFCount, labelFCount
    global newMarriageDate, labelMarriageDate
    global newmArriagePlace, labelMarriagePlace
    global newHusbandName, labelHusbandName
    global newWifeName, labelWifeName

    newBirthPlace = "Colombo"
    newmOthersName = "Thimira"
    newFathersName = "Thimira"
    newGrandfathersName = "Thimira"
    newNicNumber = "Thimira"
    newOtherName = "Thimira"
    newFamilyCount = "Thimira"
    newSexCount = "Thimira"
    newMCount = "Thimira"
    newFCount = "Thimira"
    newMarriageDate = "Thimira"
    newmArriagePlace = "Thimira"
    newHusbandName = "Thimira"
    newWifeName = "Thimira"

    labelBirthPlace.configure(text=newBirthPlace)
    labelmOthersName.configure(text=newmOthersName)
    labelFathersName.configure(text=newFathersName)
    labelGrandfathersName.configure(text=newGrandfathersName)
    labelNicNumber.configure(text=newNicNumber)
    labelOtherName.configure(text=newOtherName)
    labelFamilyCount.configure(text=newFamilyCount)
    labelSexCount.configure(text=newSexCount)
    labelMCount.configure(text=newMCount)
    labelFCount.configure(text=newFCount)
    labelMarriageDate.configure(text=newMarriageDate)
    labelMarriagePlace.configure(text=newmArriagePlace)
    labelHusbandName.configure(text=newHusbandName)
    labelWifeName.configure(text=newWifeName)




def fun():
    global max_amount, label1
    max_amount = 100
    label1.configure(text='Balance :$' + str(max_amount))


def logout():
    root.destroy()


def ReadFinger():
    global labelFingerPrint
    """ Read finger from sensor and return image """
    # Select File dialog box
    file = filedialog.askopenfilename(initialdir=r"C:\Users\timni\PycharmProjects\Civil-Register\Data\Altered"
                                                 r"\SelectedData", title='Select File',
                                      filetypes=(('BMP', '*.bmp'), ('All Files', '*.*')))

    print("Before file")
    print(file)
    if file:
        filename, best_score, result = FingerPrintScan.matchfingerprint(file)
        print("After file")
        print(filename)
        print(best_score)
        print(result)
        imageNameLocal.set(filename)
        print("After set")
        print(imageNameLocal.get())

        newIMG = PhotoImage(file=filename)
        labelFingerPrint.configure(image=newIMG)

        updateData()

        return filename, best_score, result

def updateLabelName():
    global newName, labelName
    newName = "Thimira"
    labelName.configure(text="Hey "+newName)


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

    imageNameLocal = StringVar()

    # Set the username and userPosition
    username.set("Username")
    userPosition.set("User Position")
    name.set("Name")
    status.set("Status")
    dob.set("Date of Birth")
    age.set("Age")
    job.set("Job")
    address.set("Address")

    # if imageName != "":
    #     print("Image Name is not empty")
    #     print(imageName)
    #     imageNameLocal = imageName

    # Create Frames
    top = Frame(root, width=1440, height=100, bg='white')
    top.pack(side=TOP)
    middle = Frame(root, width=1440, height=430, bg='white')
    middle.pack(side=TOP)
    bottom = Frame(root, width=1440, height=240, bg='white')
    bottom.pack(side=BOTTOM)

    """Top Section"""
    """Top Section"""
    """Top Section"""
    """Top Section"""
    """Top Section"""

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

    """ Fingerprint section and basic info in middle frame """
    """ Fingerprint section and basic info in middle frame """
    """ Fingerprint section and basic info in middle frame """
    """ Fingerprint section and basic info in middle frame """
    """ Fingerprint section and basic info in middle frame """
    """ Fingerprint section and basic info in middle frame """
    # Image Widget for middle frame in x=84 y=48 size=276x334
    print("Before ReadFinger")

    newFingerPrint = PhotoImage(file='image 1.png')
    # label = Label(middle, image=img, width=250, height=303, bg='white')
    labelFingerPrint = Label(middle, image=newFingerPrint, width=240, height=291, bg='white')
    labelFingerPrint.place(x=84, y=30)

    # Two button below image in x=84 y=374 size=276x48 call ReadFinger function
    btn = Button(middle, text='Capture', font=('arial', 15), width=10, height=1, bg='green', fg='white',
                 command=updateData, cursor='hand2')
    btn.place(x=84, y=348)
    # btn = Button(middle, text='Clear', font=('arial', 15), width=10, height=1, bg='green', fg='white', cursor='hand2',
    #              command=fun)
    # btn.place(x=220, y=348)
    btn = Button(middle, text='Clear', font=('arial', 15), width=10, height=1, bg='green', fg='white', cursor='hand2',
                 command=updateData)
    btn.place(x=220, y=348)
    #
    # # lable1 below buttons
    # t1 = str(10)
    # label1 = Label(middle, text='Balance :$' + t1)
    # label1.place(x=84, y=408)

    # Label Right of image in x=420 y=48 size=200x48
    label = Label(middle, text='Basic Information', font=('arial', 20), fg='black', bg='white')
    label.place(x=420, y=30)
    # Label Right of image in x=420 y=96 size=200x48
    label = Label(middle, text='Name', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=96)

    # Label Right to Name to show name in x=600 y=96 size=200x48 show name
    labelName = Label(middle, text=newName, font=('arial', 15), fg='black', bg='white')
    labelName.place(x=600, y=96)


    # Label Right of image in x=420 y=144 size=200x48
    label = Label(middle, text='Status', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=144)
    # Label Right to Status to show status in x=600 y=144 size=200x48 show status
    labelStatus = Label(middle, text=newStatus, font=('arial', 15), fg='black', bg='white')
    labelStatus.place(x=600, y=144)
    # Label Right of image in x=420 y=192 size=200x48
    label = Label(middle, text='Date of Birth', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=192)
    # Label Right to Date of Birth to show dob in x=600 y=192 size=200x48 show dob
    labelDOB = Label(middle, text=newDOB, font=('arial', 15), fg='black', bg='white')
    labelDOB.place(x=600, y=192)
    # Label Right of image in x=420 y=240 size=200x48
    label = Label(middle, text='Age', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=240)
    # Label Right to Age to show age in x=600 y=240 size=200x48 show age
    labelAge = Label(middle, text=newAge, font=('arial', 15), fg='black', bg='white')
    labelAge.place(x=600, y=240)
    # Label Right of image in x=420 y=288 size=200x48
    label = Label(middle, text='Job', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=288)
    # Label Right to Job to show job in x=600 y=288 size=200x48 show job
    labelJob = Label(middle, text=newJob, font=('arial', 15), fg='black', bg='white')
    labelJob.place(x=600, y=288)
    # Label Right of image in x=420 y=336 size=200x48
    label = Label(middle, text='Address', font=('arial', 15), fg='black', bg='white')
    label.place(x=420, y=336)
    # Label Right to Address to show address in x=600 y=336 size=200x48 show address
    labelAddress = Label(middle, text=newAddress, font=('arial', 15), fg='black', bg='white')
    labelAddress.place(x=600, y=336)

    font_size = 12

    """Bottom Render"""
    """Bottom Render"""
    """Bottom Render"""
    """Bottom Render"""
    """Bottom Render"""

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
    labelBirthPlace = Label(bottom, text='Birth Place', font=('arial', font_size), fg='black', bg='white')
    labelBirthPlace.place(x=84, y=48)
    # Label below Birth Place in x=84 y=144 size=276x48 "Mother’s Name"
    labelMothersName = Label(bottom, text='Mother’s Name', font=('arial', font_size), fg='black', bg='white')
    labelMothersName.place(x=84, y=96)
    # Label below Mother’s Name in x=84 y=192 size=276x48 "Father’s Name"
    labelFathersName = Label(bottom, text='Father’s Name', font=('arial', font_size), fg='black', bg='white')
    labelFathersName.place(x=84, y=144)
    # Label below Father’s Name in x=84 y=240 size=276x48 "Grandfather’s Name"
    labelGrandfathersName = Label(bottom, text='Grandfather’s Name', font=('arial', font_size), fg='black', bg='white')
    labelGrandfathersName.place(x=84, y=192)
    # Section 2
    # Section 2 Label in x=420 y=48 size=276x48 "NIC"
    label = Label(bottom, text='NIC', font=('arial', 14), fg='black', bg='white')
    label.place(x=420, y=0)
    # NIC (Link)
    # NIC Number :
    # Other name :
    # Label below NIC in x=420 y=96 size=276x48 "NIC Number"
    labelNicNumber = Label(bottom, text='NIC Number', font=('arial', font_size), fg='black', bg='white')
    labelNicNumber.place(x=420, y=48)
    # Label below NIC Number in x=420 y=144 size=276x48 "Other name"
    labelOtherName = Label(bottom, text='Other name', font=('arial', font_size), fg='black', bg='white')
    labelOtherName.place(x=420, y=96)
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
    labelFamilyCount = Label(bottom, text='Sex Count', font=('arial', font_size), fg='black', bg='white')
    labelFamilyCount.place(x=756, y=96)
    # Label below Sexuality Count in x=756 y=192 size=276x48 "M count"
    labelSexCount = Label(bottom, text='M Count', font=('arial', font_size), fg='black', bg='white')
    labelSexCount.place(x=756, y=144)
    # Label Right to M Count in x=756 y=240 size=276x48 "F Count"
    labelFCount = Label(bottom, text='F Count', font=('arial', font_size), fg='black', bg='white')
    labelFCount.place(x=756, y=192)
    # Label below Sexuality Count in x=756 y=288 size=276x48 "Jobs"
    labelMCount = Label(bottom, text='Jobs', font=('arial', font_size), fg='black', bg='white')
    labelMCount.place(x=756, y=240)
    # Label below Jobs in x=756 y=336 size=276x48 "person name - job"
    labelJob = Label(bottom, text='person name - job', font=('arial', font_size), fg='black', bg='white')
    labelJob.place(x=756, y=288)
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
    labelMarriageDate = Label(bottom, text='Marriage Date', font=('arial', font_size), fg='black', bg='white')
    labelMarriageDate.place(x=1092, y=48)
    # Label below Marriage Date in x=1092 y=144 size=276x48 "Marriage Place"'
    labelMarriagePlace = Label(bottom, text='Marriage Place', font=('arial', font_size), fg='black', bg='white')
    labelMarriagePlace.place(x=1092, y=96)
    # Label below Marriage Place in x=1092 y=192 size=276x48 "Husband Name"
    labelHusbandName = Label(bottom, text='Husband Name', font=('arial', font_size), fg='black', bg='white')
    labelHusbandName.place(x=1092, y=144)
    # Label below Husband Name in x=1092 y=240 size=276x48 "Wife Name"
    labelWifeName = Label(bottom, text='Wife Name', font=('arial', font_size), fg='black', bg='white')
    labelWifeName.place(x=1092, y=192)

    # # Entry Right of image in x=420 y=144 size=200x48
    # entry = Entry(middle, font=('arial', 15), width=30)
    # entry.place(x=420, y=144)

    root.mainloop()
