from tkinter import *
from PIL import ImageTk, Image
import run
import global_var
import sig

# Create the main window
root = Tk()
root.title("Reconfigurable Circuit")

# Create the main-caption
main_caption = Label(root, text="Reconfigurable Circuit Remote-Control Interface", font=("Arial", 24))
main_caption.grid(row=1, column=1, columnspan=4, pady=30)

# Create the test button
test_Flag = 0
def led_test():
    global test_Flag
    if test_Flag == 0:
        run.ledTestOn()
        test_Flag = 1
        print("Test LED is ON")

    elif test_Flag == 1:
        run.ledTestOff()
        test_Flag = 0
        print("Test LED is OFF")

test_caption = Label(root, text="You can test the connection by clicking the button below", font=("Arial", 12))
test_caption.grid(row=2, column = 2, columnspan=2)
button_test = Button(root, text="Test LED (ON/OFF)",command=led_test)
button_test.grid(row=3, column=2, columnspan=2, pady=10)

# Create the sub-caption
sub_caption = Label(root, text="Please choose your circuit", font=("Arial", 16))
sub_caption.grid(row=6, column=2, columnspan=2, pady=10)

'----------Parameters----------'

R1 = IntVar()
R1.set(0)
R2 = IntVar()
R2.set(0)
wave1 = IntVar()
wave1.set(0)
sigFreq_value = IntVar()
sigFreq_value.set(0)
sigVpp_value = IntVar()
sigVpp_value.set(0)
'----------Home Page----------'
def inverting():
    global circuitType
    circuitType = 1
    print("Circuit type is selected to be number " + str(circuitType))
    global top1
    top1 = Toplevel()
    top1.title('Inverting Amplifier Circuit')
    radio_inverting()

def noninverting():
    global circuitType
    circuitType = 2
    print("Circuit type is selected to be number " + str(circuitType))
    global top2
    top2 = Toplevel()
    top2.title('Non-Inverting Amplifier Circuit')
    radio_noninverting()

def integrator():
    global circuitType
    circuitType = 3
    print("Circuit type is selected to be number " + str(circuitType))
    global top3
    top3 = Toplevel()
    top3.title('Integrator Amplifier Cirucit')
    radio_integrator()

def passive():
    global circuitType
    circuitType = 4
    print("Circuit type is selected to be number " + str(circuitType))
    global top4
    top4 = Toplevel()
    top4.title('Passive Circuit Configuration')
    radio_passive()

def signal():
    print("Signal generator panel opened")
    global top5
    top5 = Toplevel()
    top5.title('Signal Generator Control Panel')
    radio_signal()

def radio_group_1():
    print("R1 is selected to be number " + str(R1.get()))

def radio_group_2():
    print("R2 is selected to be number " + str(R2.get()))

"------------------------------"
def realise():
    #Reset all Pico's output (Test LED excluded)
    run.S_reset()
    #----------------------------------------------------
    #1. Inverting
    #R1=1

    if circuitType==1 and R1.get()==1 and R2.get()==1:
        run.S1_81on()
        run.S1_91on()
        run.S1_92on()
        run.S1_82on()
        print("Circuit 111 Realised")
    elif circuitType==1 and R1.get()==1 and R2.get()==2:
        run.S1_81on()
        run.S1_91on()
        run.S2_92on()
        run.S1_82on()
        print("Circuit 112 Realised")
    elif circuitType==1 and R1.get()==1 and R2.get()==3:
        run.S1_81on()
        run.S1_91on()
        run.S3_92on()
        run.S1_82on()
        print("Circuit 113 Realised")
    elif circuitType==1 and R1.get()==1 and R2.get()==4:
        run.S1_81on()
        run.S1_91on()
        run.S4_92on()
        run.S1_82on()
        print("Circuit 114 Realised")
    #R1=2
    elif circuitType==1 and R1.get()==2 and R2.get()==1:
        run.S1_81on()
        run.S2_91on()
        run.S1_92on()
        run.S1_82on()
        print("Circuit Realised")
    elif circuitType==1 and R1.get()==2 and R2.get()==2:
        run.S1_81on()
        run.S2_91on()
        run.S2_92on()
        run.S1_82on()
        print("Circuit Realised")
    elif circuitType==1 and R1.get()==2 and R2.get()==3:
        run.S1_81on()
        run.S2_91on()
        run.S3_92on()
        run.S1_82on()
        print("Circuit Realised")
    elif circuitType==1 and R1.get()==2 and R2.get()==4:
        run.S1_81on()
        run.S2_91on()
        run.S4_92on()
        run.S1_82on()
        print("Circuit Realised")
    #R1=3
    elif circuitType==1 and R1.get()==3 and R2.get()==1:
        run.S1_81on()
        run.S3_91on()
        run.S1_92on()
        run.S1_82on()
        print("Circuit Realised")
    elif circuitType==1 and R1.get()==3 and R2.get()==2:
        run.S1_81on()
        run.S3_91on()
        run.S2_92on()
        run.S1_82on()
        print("Circuit Realised")
    elif circuitType==1 and R1.get()==3 and R2.get()==3:
        run.S1_81on()
        run.S3_91on()
        run.S3_92on()
        run.S1_82on()
        print("Circuit Realised")
    elif circuitType==1 and R1.get()==3 and R2.get()==4:
        run.S1_81on()
        run.S3_91on()
        run.S4_92on()
        run.S1_82on()
        print("Circuit Realised")
    #R1=4
    elif circuitType==1 and R1.get()==4 and R2.get()==1:
        run.S1_81on()
        run.S4_91on()
        run.S1_92on()
        run.S1_82on()
        print("Circuit Realised")
    elif circuitType==1 and R1.get()==4 and R2.get()==2:
        run.S1_81on()
        run.S4_91on()
        run.S2_92on()
        run.S1_82on()
        print("Circuit Realised")
    elif circuitType==1 and R1.get()==4 and R2.get()==3:
        run.S1_81on()
        run.S4_91on()
        run.S3_92on()
        run.S1_82on()
        print("Circuit Realised")
    elif circuitType==1 and R1.get()==4 and R2.get()==4:
        run.S1_81on()
        run.S4_91on()
        run.S4_92on()
        run.S1_82on()
        print("Circuit Realised")
    #----------------------------------------------------
    #----------------------------------------------------
    #2. Non-inverting
    #R1=1
    elif circuitType==2 and R1.get()==1 and R2.get()==1:
        run.S2_81on()
        run.S1_91on()
        run.S1_92on()
        run.S2_82on()
        print("Circuit Realised")
    elif circuitType==2 and R1.get()==1 and R2.get()==2:
        run.S2_81on()
        run.S1_91on()
        run.S2_92on()
        run.S2_82on()
        print("Circuit Realised")
    elif circuitType==2 and R1.get()==1 and R2.get()==3:
        run.S2_81on()
        run.S1_91on()
        run.S3_92on()
        run.S2_82on()
        print("Circuit Realised")
    elif circuitType==2 and R1.get()==1 and R2.get()==4:
        run.S2_81on()
        run.S1_91on()
        run.S4_92on()
        run.S2_82on()
        print("Circuit Realised")
    #R1=2
    elif circuitType==2 and R1.get()==2 and R2.get()==1:
        run.S2_81on()
        run.S2_91on()
        run.S1_92on()
        run.S2_82on()
        print("Circuit Realised")
    elif circuitType==2 and R1.get()==2 and R2.get()==2:
        run.S2_81on()
        run.S2_91on()
        run.S2_92on()
        run.S2_82on()
        print("Circuit Realised")
    elif circuitType==2 and R1.get()==2 and R2.get()==3:
        run.S2_81on()
        run.S2_91on()
        run.S3_92on()
        run.S2_82on()
        print("Circuit Realised")
    elif circuitType==2 and R1.get()==2 and R2.get()==4:
        run.S2_81on()
        run.S2_91on()
        run.S4_92on()
        run.S2_82on()
        print("Circuit Realised")
    #R1=3
    elif circuitType==2 and R1.get()==3 and R2.get()==1:
        run.S2_81on()
        run.S3_91on()
        run.S1_92on()
        run.S2_82on()
        print("Circuit Realised")
    elif circuitType==2 and R1.get()==3 and R2.get()==2:
        run.S2_81on()
        run.S3_91on()
        run.S2_92on()
        run.S2_82on()
        print("Circuit Realised")
    elif circuitType==2 and R1.get()==3 and R2.get()==3:
        run.S2_81on()
        run.S3_91on()
        run.S3_92on()
        run.S2_82on()
        print("Circuit Realised")
    elif circuitType==2 and R1.get()==3 and R2.get()==4:
        run.S2_81on()
        run.S3_91on()
        run.S4_92on()
        run.S2_82on()
        print("Circuit Realised")
    #R1=4
    elif circuitType==2 and R1.get()==4 and R2.get()==1:
        run.S2_81on()
        run.S4_91on()
        run.S1_92on()
        run.S2_82on()
        print("Circuit Realised")
    elif circuitType==2 and R1.get()==4 and R2.get()==2:
        run.S2_81on()
        run.S4_91on()
        run.S2_92on()
        run.S2_82on()
        print("Circuit Realised")
    elif circuitType==2 and R1.get()==4 and R2.get()==3:
        run.S2_81on()
        run.S4_91on()
        run.S3_92on()
        run.S2_82on()
        print("Circuit Realised")
    elif circuitType==2 and R1.get()==4 and R2.get()==4:
        run.S2_81on()
        run.S4_91on()
        run.S4_92on()
        run.S2_82on()
        print("Circuit Realised")
    #----------------------------------------------------
    #----------------------------------------------------
    #3. Integrator
    #R1=1
    elif circuitType==3 and R1.get()==1 and R2.get()==1:
        run.S3_81on()
        run.S1_93on()
        run.S1_94on()
        run.S3_82on()
        print("Circuit Realised")
    elif circuitType==3 and R1.get()==1 and R2.get()==2:
        run.S3_81on()
        run.S1_93on()
        run.S2_94on()
        run.S3_82on()
        print("Circuit Realised")
    elif circuitType==3 and R1.get()==1 and R2.get()==3:
        run.S3_81on()
        run.S1_93on()
        run.S3_94on()
        run.S3_82on()
        print("Circuit Realised")
    elif circuitType==3 and R1.get()==1 and R2.get()==4:
        run.S3_81on()
        run.S1_93on()
        run.S4_94on()
        run.S3_82on()
        print("Circuit Realised")
    #R1=2
    elif circuitType==3 and R1.get()==2 and R2.get()==1:
        run.S3_81on()
        run.S2_93on()
        run.S1_94on()
        run.S3_82on()
        print("Circuit Realised")
    elif circuitType==3 and R1.get()==2 and R2.get()==2:
        run.S3_81on()
        run.S2_93on()
        run.S2_94on()
        run.S3_82on()
        print("Circuit Realised")
    elif circuitType==3 and R1.get()==2 and R2.get()==3:
        run.S3_81on()
        run.S2_93on()
        run.S3_94on()
        run.S3_82on()
        print("Circuit Realised")
    elif circuitType==3 and R1.get()==2 and R2.get()==4:
        run.S3_81on()
        run.S2_93on()
        run.S4_94on()
        run.S3_82on()
        print("Circuit Realised")
    #R1=3
    elif circuitType==3 and R1.get()==3 and R2.get()==1:
        run.S3_81on()
        run.S3_93on()
        run.S1_94on()
        run.S3_82on()
        print("Circuit Realised")
    elif circuitType==3 and R1.get()==3 and R2.get()==2:
        run.S3_81on()
        run.S3_93on()
        run.S2_94on()
        run.S3_82on()
        print("Circuit Realised")
    elif circuitType==3 and R1.get()==3 and R2.get()==3:
        run.S3_81on()
        run.S3_93on()
        run.S3_94on()
        run.S3_82on()
        print("Circuit Realised")
    elif circuitType==3 and R1.get()==3 and R2.get()==4:
        run.S3_81on()
        run.S3_93on()
        run.S4_94on()
        run.S3_82on()
        print("Circuit Realised")
    #R1=4
    elif circuitType==3 and R1.get()==4 and R2.get()==1:
        run.S3_81on()
        run.S4_93on()
        run.S1_94on()
        run.S3_82on()
        print("Circuit Realised")
    elif circuitType==3 and R1.get()==4 and R2.get()==2:
        run.S3_81on()
        run.S4_93on()
        run.S2_94on()
        run.S3_82on()
        print("Circuit Realised")
    elif circuitType==3 and R1.get()==4 and R2.get()==3:
        run.S3_81on()
        run.S4_93on()
        run.S3_94on()
        run.S3_82on()
        print("Circuit Realised")
    elif circuitType==3 and R1.get()==4 and R2.get()==4:
        run.S3_81on()
        run.S4_93on()
        run.S4_94on()
        run.S3_82on()
        print("Circuit Realised")
    #----------------------------------------------------
    #----------------------------------------------------
    #4. Passive Circuit
    #R1=1
    elif circuitType==4 and R1.get()==1 and R2.get()==1:
        run.S4_81on()
        run.S1_93on()
        run.S1_94on()
        run.S4_82on()
        print("Circuit Realised")
    elif circuitType==4 and R1.get()==1 and R2.get()==2:
        run.S4_81on()
        run.S1_93on()
        run.S2_94on()
        run.S4_82on()
        print("Circuit Realised")
    elif circuitType==4 and R1.get()==1 and R2.get()==3:
        run.S4_81on()
        run.S1_93on()
        run.S3_94on()
        run.S4_82on()
        print("Circuit Realised")
    elif circuitType==4 and R1.get()==1 and R2.get()==4:
        run.S4_81on()
        run.S1_93on()
        run.S4_94on()
        run.S4_82on()
        print("Circuit Realised")
    #R1=2
    elif circuitType==4 and R1.get()==2 and R2.get()==1:
        run.S4_81on()
        run.S2_93on()
        run.S1_94on()
        run.S4_82on()
        print("Circuit Realised")
    elif circuitType==4 and R1.get()==2 and R2.get()==2:
        run.S4_81on()
        run.S2_93on()
        run.S2_94on()
        run.S4_82on()
        print("Circuit Realised")
    elif circuitType==4 and R1.get()==2 and R2.get()==3:
        run.S4_81on()
        run.S2_93on()
        run.S3_94on()
        run.S4_82on()
        print("Circuit Realised")
    elif circuitType==4 and R1.get()==2 and R2.get()==4:
        run.S4_81on()
        run.S2_93on()
        run.S4_94on()
        run.S4_82on()
        print("Circuit Realised")
    #R1=3
    elif circuitType==4 and R1.get()==3 and R2.get()==1:
        run.S4_81on()
        run.S3_93on()
        run.S1_94on()
        run.S4_82on()
        print("Circuit Realised")
    elif circuitType==4 and R1.get()==3 and R2.get()==2:
        run.S4_81on()
        run.S3_93on()
        run.S2_94on()
        run.S4_82on()
        print("Circuit Realised")
    elif circuitType==4 and R1.get()==3 and R2.get()==3:
        run.S4_81on()
        run.S3_93on()
        run.S3_94on()
        run.S4_82on()
        print("Circuit Realised")
    elif circuitType==4 and R1.get()==3 and R2.get()==4:
        run.S4_81on()
        run.S3_93on()
        run.S4_94on()
        run.S4_82on()
        print("Circuit Realised")
    #R1=4
    elif circuitType==4 and R1.get()==4 and R2.get()==1:
        run.S4_81on()
        run.S4_93on()
        run.S1_94on()
        run.S4_82on()
        print("Circuit Realised")
    elif circuitType==4 and R1.get()==4 and R2.get()==2:
        run.S4_81on()
        run.S4_93on()
        run.S2_94on()
        run.S4_82on()
        print("Circuit Realised")
    elif circuitType==4 and R1.get()==4 and R2.get()==3:
        run.S4_81on()
        run.S4_93on()
        run.S3_94on()
        run.S4_82on()
        print("Circuit Realised")
    elif circuitType==4 and R1.get()==4 and R2.get()==4:
        run.S4_81on()
        run.S4_93on()
        run.S4_94on()
        run.S4_82on()
        print("Circuit Realised")
    else:
        print("Please Select Both Parameters")
    #----------------------------------------------------
"------------------------------"

def radio_inverting():
    global tk_image
    pic_frame = LabelFrame(top1)
    pic_frame.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
    image = Image.open('Inverting.png')
    tk_image = ImageTk.PhotoImage(image)
    image_label = Label(pic_frame, image=tk_image)
    image_label.pack()

    group_frame_1 = LabelFrame(top1, text="Please Choose R_in")
    group_frame_1.grid(row=2, rowspan=3, column=1, padx=20, pady=20)

    button_1_1 = Radiobutton(group_frame_1, text="33k Ohms", variable=R1, value=1, command=radio_group_1)
    button_1_1.pack(pady=5)

    button_1_2 = Radiobutton(group_frame_1, text="100k Ohms", variable=R1, value=2, command=radio_group_1)
    button_1_2.pack(pady=5)

    button_1_3 = Radiobutton(group_frame_1, text="180k Ohms", variable=R1, value=3, command=radio_group_1)
    button_1_3.pack(pady=5)

    button_1_4 = Radiobutton(group_frame_1, text="330k ohms", variable=R1, value=4, command=radio_group_1)
    button_1_4.pack(pady=5)

    group_frame_2 = LabelFrame(top1, text="Please Choose R_f")
    group_frame_2.grid(row=2, rowspan=3, column=2, padx=20, pady=20)

    button_2_1 = Radiobutton(group_frame_2, text="33k Ohms", variable=R2, value=1, command=radio_group_2)
    button_2_1.pack(pady=5)

    button_2_2 = Radiobutton(group_frame_2, text="100k Ohms", variable=R2, value=2, command=radio_group_2)
    button_2_2.pack(pady=5)

    button_2_3 = Radiobutton(group_frame_2, text="180k Ohms", variable=R2, value=3, command=radio_group_2)
    button_2_3.pack(pady=5)

    button_2_4 = Radiobutton(group_frame_2, text="330k Ohms", variable=R2, value=4, command=radio_group_2)
    button_2_4.pack(pady=5)

    button_realise_frame = LabelFrame(top1, highlightbackground = "grey", highlightthickness = 2, bd=0)
    button_realise_frame.grid(row=3, column=3, padx=15)
    button_realise = Button(button_realise_frame, font=("Arial", 10, 'bold'), text="Realise Circuit", command=realise)
    button_realise.pack()

    button_reset = Button(top1, text="Reset Circuit", command=run.S_reset)
    button_reset.grid(row=4, column=3, padx=15)

def radio_noninverting():
    global tk_image
    pic_frame = LabelFrame(top2)
    pic_frame.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
    image = Image.open('Noninverting.png')
    tk_image = ImageTk.PhotoImage(image)
    image_label = Label(pic_frame, image=tk_image)
    image_label.pack()

    group_frame_1 = LabelFrame(top2, text="Please Choose R_1")
    group_frame_1.grid(row=2, rowspan=3, column=1, padx=20, pady=20)

    button_1_1 = Radiobutton(group_frame_1, text="33k Ohms", variable=R1, value=1, command=radio_group_1)
    button_1_1.pack(pady=5)

    button_1_2 = Radiobutton(group_frame_1, text="100k Ohms", variable=R1, value=2, command=radio_group_1)
    button_1_2.pack(pady=5)

    button_1_3 = Radiobutton(group_frame_1, text="180k Ohms", variable=R1, value=3, command=radio_group_1)
    button_1_3.pack(pady=5)

    button_1_4 = Radiobutton(group_frame_1, text="330k Ohms", variable=R1, value=4, command=radio_group_1)
    button_1_4.pack(pady=5)

    group_frame_2 = LabelFrame(top2, text="Please Choose R_2")
    group_frame_2.grid(row=2, rowspan=3, column=2, padx=20, pady=20)

    button_2_1 = Radiobutton(group_frame_2, text="33k Ohms", variable=R2, value=1, command=radio_group_2)
    button_2_1.pack(pady=5)

    button_2_2 = Radiobutton(group_frame_2, text="100k Ohms", variable=R2, value=2, command=radio_group_2)
    button_2_2.pack(pady=5)

    button_2_3 = Radiobutton(group_frame_2, text="180k Ohms", variable=R2, value=3, command=radio_group_2)
    button_2_3.pack(pady=5)

    button_2_4 = Radiobutton(group_frame_2, text="330k Ohms", variable=R2, value=4, command=radio_group_2)
    button_2_4.pack(pady=5)

    button_realise_frame = LabelFrame(top2, highlightbackground = "grey", highlightthickness = 2, bd=0)
    button_realise_frame.grid(row=3, column=3, padx=15)
    button_realise = Button(button_realise_frame, font=("Arial", 10, 'bold'), text="Realise Circuit", command=realise)
    button_realise.pack()

    button_reset = Button(top2, text="Reset Circuit", command=run.S_reset)
    button_reset.grid(row=4, column=3, padx=15)

def radio_integrator():
    global tk_image
    pic_frame = LabelFrame(top3)
    pic_frame.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
    image = Image.open('Integrating.png')
    tk_image = ImageTk.PhotoImage(image)
    image_label = Label(pic_frame, image=tk_image)
    image_label.pack()

    group_frame_1 = LabelFrame(top3, text="Please Choose R")
    group_frame_1.grid(row=2, rowspan=3, column=1, padx=20, pady=20)

    button_1_1 = Radiobutton(group_frame_1, text="33k Ohms", variable=R1, value=1, command=radio_group_1)
    button_1_1.pack(pady=5)

    button_1_2 = Radiobutton(group_frame_1, text="100k Ohms", variable=R1, value=2, command=radio_group_1)
    button_1_2.pack(pady=5)

    button_1_3 = Radiobutton(group_frame_1, text="180k Ohms", variable=R1, value=3, command=radio_group_1)
    button_1_3.pack(pady=5)

    button_1_4 = Radiobutton(group_frame_1, text="330k Ohms", variable=R1, value=4, command=radio_group_1)
    button_1_4.pack(pady=5)

    group_frame_2 = LabelFrame(top3, text="Please Choose C")
    group_frame_2.grid(row=2, rowspan=3, column=2, padx=20, pady=20)

    button_2_1 = Radiobutton(group_frame_2, text="33 nF", variable=R2, value=1, command=radio_group_2)
    button_2_1.pack(pady=5)

    button_2_2 = Radiobutton(group_frame_2, text="100 nF", variable=R2, value=2, command=radio_group_2)
    button_2_2.pack(pady=5)

    button_2_3 = Radiobutton(group_frame_2, text="180 nF", variable=R2, value=3, command=radio_group_2)
    button_2_3.pack(pady=5)

    button_2_4 = Radiobutton(group_frame_2, text="330 nF", variable=R2, value=4, command=radio_group_2)
    button_2_4.pack(pady=5)

    button_realise_frame = LabelFrame(top3, highlightbackground = "grey", highlightthickness = 2, bd=0)
    button_realise_frame.grid(row=3, column=3, padx=15)
    button_realise = Button(button_realise_frame, font=("Arial", 10, 'bold'), text="Realise Circuit", command=realise)
    button_realise.pack()

    button_reset = Button(top3, text="Reset Circuit", command=run.S_reset)
    button_reset.grid(row=4, column=3, padx=15)

def radio_passive():
    global tk_image
    pic_frame = LabelFrame(top4)
    pic_frame.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
    image = Image.open('Passive.png')
    tk_image = ImageTk.PhotoImage(image)
    image_label = Label(pic_frame, image=tk_image)
    image_label.pack()

    group_frame_1 = LabelFrame(top4, text="Please Choose R")
    group_frame_1.grid(row=2, rowspan=3, column=1, padx=20, pady=20)

    button_1_1 = Radiobutton(group_frame_1, text="1k Ohms", variable=R1, value=1, command=radio_group_1)
    button_1_1.pack(pady=5)

    button_1_2 = Radiobutton(group_frame_1, text="2.2k Ohms", variable=R1, value=2, command=radio_group_1)
    button_1_2.pack(pady=5)

    button_1_3 = Radiobutton(group_frame_1, text="3.3k Ohms", variable=R1, value=3, command=radio_group_1)
    button_1_3.pack(pady=5)

    button_1_4 = Radiobutton(group_frame_1, text="4.7k Ohms", variable=R1, value=4, command=radio_group_1)
    button_1_4.pack(pady=5)

    group_frame_2 = LabelFrame(top4, text="Please Choose C")
    group_frame_2.grid(row=2, rowspan=3, column=2, padx=20, pady=20)

    button_2_1 = Radiobutton(group_frame_2, text="100 nF", variable=R2, value=1, command=radio_group_2)
    button_2_1.pack(pady=5)

    button_2_2 = Radiobutton(group_frame_2, text="220 nF", variable=R2, value=2, command=radio_group_2)
    button_2_2.pack(pady=5)

    button_2_3 = Radiobutton(group_frame_2, text="330 nF", variable=R2, value=3, command=radio_group_2)
    button_2_3.pack(pady=5)

    button_2_4 = Radiobutton(group_frame_2, text="470 nF", variable=R2, value=4, command=radio_group_2)
    button_2_4.pack(pady=5)

    button_realise_frame = LabelFrame(top4, highlightbackground = "grey", highlightthickness = 2, bd=0)
    button_realise_frame.grid(row=3, column=3, padx=15)
    button_realise = Button(button_realise_frame, font=("Arial", 10, 'bold'), text="Realise Circuit", command=realise)
    button_realise.pack()

    button_reset = Button(top4, text="Reset Circuit", command=run.S_reset)
    button_reset.grid(row=4, column=3, padx=15)


global_var._init() #initiallise sig.py

def sigTypeSIN():
    global_var.set_value("sigType", "SINusoid")
    print("Sine wave is selected")

def sigTypeSQU():
    global_var.set_value("sigType", "SQUare")
    print("Square wave is selected")

def sigOutputON():
    global_var.set_value("sigFreq", sigFreq_value)
    global_var.set_value("sigVpp", sigFreq_value)
    sig.sigON()

def sigOutputOFF():
    sig.sigOFF()


def radio_signal():
    global tk_image
    pic_frame = LabelFrame(top5)
    pic_frame.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
    image = Image.open('RTB2004.jpg')
    tk_image = ImageTk.PhotoImage(image)
    image_label = Label(pic_frame, image=tk_image)
    image_label.pack()

    sigSelect_caption = Label(top5, text="Please select the signal type", font=("Arial", 12))
    sigSelect_caption.grid(row=2, column=2, columnspan=2, pady=10), 

    button_1sigSelect = Radiobutton(top5, text="Sine Wave", variable=wave1, value=1, font=("Arial", 10, 'bold'), command=sigTypeSIN)
    button_1sigSelect.grid(row=3, column=2)

    button_2sigSelect = Radiobutton(top5, text="Square Wave", variable=wave1, value=2, font=("Arial", 10, 'bold'), command=sigTypeSQU)
    button_2sigSelect.grid(row=3, column=3)

    sigFreq_caption = Label(top5, text="Please enter the signal frequency in hertz", font=("Arial", 12))
    sigFreq_caption.grid(row=4, column=2, columnspan=2, pady=10)

    sigFreq_value = Entry(top5).grid(row=5, column=2, columnspan=2)

    sigVpp_caption = Label(top5, text="Please enter Vpp in volt", font=("Arial", 12))
    sigVpp_caption.grid(row=6, column=2, columnspan=2, pady=10)

    sigVpp_value = Entry(top5).grid(row=7, column=2, columnspan=2)

    button_output = Button(top5, text="Output ON", command=sigOutputON)
    button_output.grid(row=8, column=2, pady=15)

    button_output = Button(top5, text="Output OFF", command=sigOutputOFF)
    button_output.grid(row=8, column=3, pady=15)


button_1 = Button(root, text="Inverting Amplifier Circuit", command=inverting)
button_1.grid(row=7, column=1, padx=10, pady=10)

button_2 = Button(root, text="Non-Inverting Amplifier Circuit", command=noninverting)
button_2.grid(row=7, column=2, padx=10, pady=10)

button_3 = Button(root, text="Integrator Amplifier Circuit", command=integrator)
button_3.grid(row=7, column=3, padx=10, pady=10)

button_4 = Button(root, text="Passive Circuit Configuration", command=passive)
button_4.grid(row=7, column=4, padx=10, pady=10)

sig_caption = Label(root, text="Please set the signal generator", font=("Arial", 16))
sig_caption.grid(row=4, column=2, columnspan=2, pady=10)

button_test = Button(root, text="Signal Generator Panel", command=signal)
button_test.grid(row=5, column=2, columnspan=2, pady=10)

author_caption = Label(root, text="Author: Yujie Wang", font=("Arial", 10))
author_caption.grid(row=8, column=2, columnspan=2, pady=5)

# Start the main event loop
root.mainloop()