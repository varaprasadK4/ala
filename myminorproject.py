from tkinter import *
import datetime
import winsound

root = Tk()
root.title("Alarm Clock")

myframe1 = LabelFrame(root,bd=0)
myframe1.pack(padx=70,pady=8,side='top')

myframe = LabelFrame(root,bd=0)
myframe.pack(padx=300,pady=50)

addclock = LabelFrame(root,bd=2)
addclock.pack(padx=70,pady=10,side='right')

addalarm = Frame(root,bd=0)
addalarm.pack(padx=100,side='bottom')

def update():
    current_time = datetime.datetime.now()
    global current_time1
    current_time1 =str(str(current_time.hour).zfill(2)+":"+str(current_time.minute).zfill(2)+":"+str(current_time.second).zfill(2))
    my.configure(text=str(current_time.hour).zfill(2))
    my2.configure(text=str(current_time.minute).zfill(2))
    my4.configure(text=str(current_time.second).zfill(2))
    root.after(1000, update)

current_time = datetime.datetime.now()
my0 = Label(myframe1,text = "____ALARM CLOCK_____",bg='black',padx=80,fg='white',font=('Helvetica',20,'bold'))
my0.pack()

my = Label(myframe,text = str(current_time.hour),bg='pink',bd=5,fg='black',padx=20,pady=20,font=('TimesNewRoman',15))
my.grid(row=3,rowspan=3,column=0,columnspan=4)

my1 = Label(myframe,text=":",bg='pink',bd=5,fg='black',padx=20,pady=20,font=50)
my1.grid(row=3,rowspan=3,column=5,columnspan=4)

my2 = Label(myframe,text=str(current_time.minute),bg='pink',bd=5,fg='black',padx=20,pady=20,font=('TimesNewRoman',15))
my2.grid(row=3,rowspan=3,column=10,columnspan=4)

my3 = Label(myframe,text=":",bg='pink',bd=5,fg='black',padx=20,pady=20,font=50)
my3.grid(row=3,rowspan=3,column=15,columnspan=4)

my4 = Label(myframe,text=str(current_time.second),bg='pink',bd=5,fg='black',padx=20,pady=20,font=('TimesNewRoman',15))
my4.grid(row=3,rowspan=3,column=19,columnspan=4)

update()

list = []
list1 = []
list2 = []

for i in range(0,24):
    if(i>=0 and i<=9):
        list.append(str(0)+str(i))
    else:
        list.append(str(i))
print(list)
for i in range(0,61):
    if(i>=0 and i<=9):
        list1.append(str(0)+str(i))
    else:
        list1.append(str(i))

for i in range(0,61):
    if (i >= 0 and i <= 9):
        list2.append(str(0) + str(i))
    else:
        list2.append(str(i))

class create():
    def __init__(self,addalarm,list1,list2,list):
        global prasad,Hari,Deeku,mylabel,var
        self.prasad = StringVar()
        self.Hari = StringVar()
        self.Deeku = StringVar()
        self.var = IntVar()
        self.var.set(0)
        self.prasad.set(list[0])
        self.Hari.set(list1[0])
        self.Deeku.set(list2[0])
        self.frame1 = LabelFrame(addalarm, padx=60, pady=4, bd=2,bg='black')
        self.frame1.pack(side='bottom',pady=8)
        self.hours_i = OptionMenu(self.frame1, self.prasad, *list)
        self.hours_i.grid(row=0, rowspan=2, column=0, columnspan=2)
        self.minutes_i = OptionMenu(self.frame1, self.Hari, *list1)
        self.minutes_i.grid(row=0, rowspan=2, column=3, columnspan=2)
        self.seconds_i = OptionMenu(self.frame1, self.Deeku, *list2)
        self.seconds_i.grid(row=0, rowspan=2, column=5, columnspan=2)
        self.mylabel2 = Label(self.frame1,bg='black')
        self.mylabel2.grid(row=0,rowspan=2,column=8,columnspan=3,padx=5)
        self.mylabel = Label(self.frame1,padx=7,pady=3,text="Alarm set at" + self.prasad.get() + ":" + self.Hari.get() + ":" + self.Deeku.get(),bg='pink')
        self.mylabel.grid(row=0, rowspan=2, column=12, columnspan=4,padx=5)
        self.mylabel1 = Label(self.frame1,bg='black')
        self.mylabel1.grid(row=0,rowspan=2,column=16,columnspan=3)
        self.click_button = Checkbutton(self.frame1, text="click to on", variable=self.var, onvalue=1, offvalue=0,bg='yellow',
                                   command=lambda: setalarm(self.var),font=('TimesNewRoman',8))
        self.click_button.grid(row=0, rowspan=2, column=19, columnspan=3)

        def setalarm(var):
            global alarmtime
            self.alarmtime = str(self.prasad.get() + ":" + self.Hari.get() + ":" + self.Deeku.get())
            if self.var.get() == 1:
                self.mylabel.configure(text="Alarm set at" + self.prasad.get() + ":" + self.Hari.get() + ":" + self.Deeku.get())
                check()
            else:
                self.mylabel.configure(text="Alarm is in off state")

        def check():
            self.alarm_datetime = datetime.datetime.strptime(self.alarmtime, "%H:%M:%S")
            current_datetime = datetime.datetime.strptime(current_time1, "%H:%M:%S")
            if self.alarm_datetime <= current_datetime and ((int(current_datetime.second) - int(self.alarm_datetime.second) <= 20) and (int(current_datetime.hour)-int(self.alarm_datetime.hour)==0) and (int(current_datetime.minute)-int(self.alarm_datetime.minute)==0)):
                winsound.PlaySound("path_to_my_ring_tone.wav", winsound.SND_ASYNC)
            if self.var.get()==1:
                root.after(1000,check)

def harsha():
    vlp = create(addalarm,list1,list2,list)

addclock_1 = Button(root,text="Add an Alarm",bg='black',fg='light green',font=('TimesNewRoman',15),padx=2,pady=3,command=harsha,bd=3)
addclock_1.place(x=750,y=197)

root.mainloop()