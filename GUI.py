from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ipaddress import IPv4Network, IPv4Address, IPv6Network, IPv6Address

from pynetcal.ipv6pynetcal import PyNIPv6Address, PyNIPv6Network
from pynetcal.ipv4pynetcal import PyNIPv4Address, PyNIPv4Network

import pynetcal.validator as validator

import GUI.helpers as helpers #Modified helpers for GUI

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # tkinter variables
        self.conFromVar = StringVar()
        self.conToVar = StringVar()
        self.optionVar = StringVar()
        self.opvals = ["Statistics","Convert"]
        self.fromtoRadios = []
        # make widgets!
        self.createWidgets()
        self.setOutput("")
        self.optionChange(None)

    def createWidgets(self):
        # Main Frame... and no I don't mean the computer
        self.main = Frame(self.master)
        self.main.pack(side=TOP,fill='both')

        # Frame for tabs and output
        #self.taoutFrame = Frame(self.main)
        
        # Tab frames.. hehe
        self.tabFrame = Frame(self.main)
        self.tabFrame.pack(side=TOP,anchor='w',fill='x',expand='yes')
        self.inWidgets(self.tabFrame)
        
        # Output frame
        self.outFrame = LabelFrame(self.main, text="Output")
        self.outFrame.pack(side=TOP,anchor='e',fill='x',expand='yes')
        self.outWidgets(self.outFrame)
        
    def outWidgets(self, master):
        self.outLabel = Label(master,text="OUTPUT")
        self.outLabel.pack(side=TOP,fill='x')
        
    def inWidgets(self, master):
        self.tabs = Notebook(master)
        self.notebook(self.tabs)
        self.tabs.pack(side=TOP,fill='x')

    def notebook(self, master):
        # Frame for IP
        self.ipframe = Frame(master)
        self.ipframe.pack(side=TOP)
        self.ipWidgets(self.ipframe)
        master.add(self.ipframe,text="IP")

        # Frame for subnetting
        self.snframe = Frame(master)
        self.snframe.pack(side=TOP)
        master.add(self.snframe,text="Subnetting")

    def setOutput(self,nstr):
        self.outLabel.config(text=nstr)
        
    def validateIP(self,ip):
        address = ip
        if(not validator.ipv4address(address) and not validator.ipv6address(address) and not validator.ipv4network(address) and not validator.ipv6network(address)):
            return False
        try:
            PyNIPv6Address(address)
            return "ipv6"
        except:
            try:
                PyNIPv4Address(address)
                return "ipv4"
            except:
                return False
    
    def calculateIP(self):
        ipadd = self.ipEntry.get()
        ipin = self.validateIP(ipadd)
        option = self.optionVar.get().lower()
        if ipin:
            # IP Valid.. ok, let's rock
            if option == "convert":
                conto = self.conToVar.get()
                confrom = self.conFromVar.get()
                output = ""
                if conto == confrom:
                    output = ipadd
                elif conto == "bin":
                    if(ipin == "ipv4"):
                        output = PyNIPv4Address(ipadd).pn_binary
                    else:
                        output = PyNIPv6Address(ipadd).binary
                elif conto == "hex":
                    if(ipin == "ipv4"):
                        output = PyNIPv4Address(ipadd).pn_hexadecimal
                    else:
                        output = PyNIPv6Address(ipadd).hexadecimal
                else:
                    if(ipin == "ipv4"):
                        output = PyNIPv4Address(ipadd).pn_decimal
                    else:
                        output = PyNIPv6Address(ipadd).decimal
                self.setOutput("Original (%s): %s\nConverted (%s): %s" % (confrom, ipadd, conto, output))
            else:
                # show the IP address stats accordingly
                address=ipadd
                output=""
                is_ipv4 = validator.ipv4address(address)
                is_ipv6 = validator.ipv6address(address)
                is_ipv4_net = validator.ipv4network(address)
                is_ipv6_net = validator.ipv6network(address)
                if(is_ipv4):
                    addr = PyNIPv4Address(address)
                    output = helpers.show_ipv4_address_stats(addr)
                elif(is_ipv6):
                    addr = PyNIPv6Address(address)
                    output = helpers.show_ipv6_address_stats(addr)
                elif(is_ipv4_net):
                    addr = PyNIPv4Network(address)
                    output = helpers.show_ipv4_network_stats(addr)
                elif(is_ipv6_net):
                    addr = PyNIPv6Network(address)
                    output = helpers.show_ipv6_network_stats(addr)
                self.setOutput(output)
        else:
            messagebox.showerror("Invalid IP", "Please use a valid IP address")
            
    def optionChange(self, event):
        option = self.optionVar.get().lower()
        if not option == "convert":
            for radio in self.fromtoRadios:
                radio.config(state="disabled")
        else:
            for radio in self.fromtoRadios:
                radio.config(state="normal")
                
    def ipWidgets(self, master):
        self.ipMain = Frame(master)
        self.ipMain.pack(side=TOP,anchor='w')
        #IP Entry
        self.ipEntryFrame = Frame(self.ipMain)
        self.ipEntryFrame.pack(side=LEFT)
        self.ipEntryLabel = Label(self.ipEntryFrame,text="IP Address")
        self.ipEntryLabel.pack(side=TOP, anchor='w')
        self.ipEntry = Entry(self.ipEntryFrame)
        self.ipEntry.pack(side=TOP,anchor='w')
        # Options
        self.ipOptionsFrame = Frame(self.ipMain)
        self.ipOptionsFrame.pack(side=RIGHT)
        self.ipOptionsLabel = Label(self.ipOptionsFrame,text="Options")
        self.ipOptionsLabel.pack(side=TOP, anchor='w')
        self.ipOptions = Combobox(self.ipOptionsFrame,values=self.opvals,textvariable=self.optionVar)
        self.ipOptions.bind("<<ComboboxSelected>>",self.optionChange)
        self.ipOptions.current(newindex=0)
        self.ipOptions.pack(side=TOP,anchor='w')
        # Conversion
        self.conFrame = Frame(master)
        self.conFrame.pack(side=TOP,anchor='w',fill='x')
        self.conWidgets(self.conFrame)
        # Go!
        self.ipCalculate = Button(master,text="Calculate",command=self.calculateIP)
        self.ipCalculate.pack(side=TOP)
        
    def conWidgets(self, master):
        self.conLabel = Label(master, text="Conversion")
        self.conLabel.pack(side=TOP,anchor='w')
        self.fromFrame = LabelFrame(master, text="From")
        self.fromFrame.pack(side=LEFT,fill='x')
        self.toFrame = LabelFrame(master, text="To")
        self.toFrame.pack(side=LEFT,fill='x')
        # From radiobuttons
        self.fromDec = Radiobutton(self.fromFrame, text="Decimal", variable=self.conFromVar, value="dec")
        self.fromDec.pack(side=TOP,anchor='w')
        self.fromDec.invoke()
        self.fromtoRadios.append(self.fromDec)
        self.fromHex = Radiobutton(self.fromFrame, text="Hexadecimal", variable=self.conFromVar, value="hex")
        self.fromHex.pack(side=TOP,anchor='w')
        self.fromtoRadios.append(self.fromHex)
        self.fromBin = Radiobutton(self.fromFrame, text="Binary", variable=self.conFromVar, value="bin")
        self.fromBin.pack(side=TOP,anchor='w')
        self.fromtoRadios.append(self.fromBin)
        # To radiobuttons
        self.toDec = Radiobutton(self.toFrame, text="Decimal", variable=self.conToVar, value="dec")
        self.toDec.pack(side=TOP,anchor='w')
        self.fromtoRadios.append(self.toDec)
        self.toHex = Radiobutton(self.toFrame, text="Hexadecimal", variable=self.conToVar, value="hex")
        self.toHex.pack(side=TOP,anchor='w')
        self.fromtoRadios.append(self.toHex)
        self.toBin = Radiobutton(self.toFrame, text="Binary", variable=self.conToVar, value="bin")
        self.toBin.pack(side=TOP,anchor='w')
        self.fromtoRadios.append(self.toBin)
        self.toBin.invoke()
    
root = Tk()
root.title("PyNetCal")
root.minsize(width=800, height=600)
app = Application(master=root)
app.mainloop()
