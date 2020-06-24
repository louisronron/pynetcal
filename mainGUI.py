from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ipaddress import IPv4Network, IPv4Address, IPv6Network, IPv6Address

from pynetcal.ipv6pynetcal import PyNIPv6Address, PyNIPv6Network
from pynetcal.ipv4pynetcal import PyNIPv4Address, PyNIPv4Network

import pynetcal.validator as validator

import GUI.helpers as helpers #Modified helpers for GUI

class Popup:
    '''
    Original Author: Suraj Singh
    Original Script Found at: https://www.bitforestinfo.com/2017/05/how-to-add-right-click-context-popup-menu-in-tkinter-text-widget-python-magicstick-text-edito-part-7.html

    This version is modified for Python3 and also a few fixes etc. --RDabok
    '''
    def __init__(self, text):
        self.text = text
        self.functions_binding_key()
        self.functions_configurations()

    def functions_configurations(self):
        self.menu = Menu(self.text,tearoff=0)
        self.menu.add_command(label="Copy", command=self.text.storeobj['Copy'])
        self.menu.add_command(label="Cut", command=self.text.storeobj['Cut'])
        self.menu.add_command(label="Paste", command=self.text.storeobj['Paste'])
        self.menu.add_separator()
        self.menu.add_command(label="Select All", command=self.text.storeobj['SelectAll'])
        self.menu.add_separator()
        return

    def functions_binding_key(self):
        self.text.bind("<Button-3>",self.show_menu_)
        return
    
    def show_menu_(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)
        return
    
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # tkinter variables
        self.outputVar = StringVar()
        self.conFromVar = StringVar()
        self.conToVar = StringVar()
        self.optionVar = StringVar()
        self.opvals = ["Statistics","Convert"]
        self.fromtoRadios = []
        self.flsmwidgets = []
        self.subcomVar = StringVar()
        self.priorVar = BooleanVar()
        # fonts and stuff
        self.fHint = ("","6","italic")
        # make widgets!
        self.createWidgets()
        self.setOutput("")
        self.optionChange(None)
        #self.switchCom()

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

        #
        self.processWidgets(self.main)
        
        # Output frame
        self.outFrame = LabelFrame(self.main, text="Output")
        self.outFrame.pack(side=TOP,anchor='n',fill='both')
        self.outWidgets(self.outFrame)
        
    def outWidgets(self, master):
        self.outScroll = Scrollbar(master)
        self.outScroll.pack(side=RIGHT,fill='y')
        self.outText = Text(master,yscrollcommand=self.outScroll.set)
        self.outText.pack(side=LEFT,fill='x')
        def outTextCopy():
            self.outText.event_generate('<<Copy>>')
        def outTextCut():
            self.outText.event_generate('<<Cut>>')
        def outTextPaste():
            self.outText.event_generate('<<Paste>>')
        def outTextSelAll():
            self.outText.event_generate('<<SelectAll>>') 
        self.outText.storeobj={'SelectAll':outTextSelAll,"Copy":outTextCopy,"Cut":outTextCut,"Paste":outTextPaste}
        Popup(self.outText)
        self.outScroll.config(command=self.outText.yview)
        
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
        self.snWidgets(self.snframe)
        master.add(self.snframe,text="Subnetting")

        # Frame for about information
        self.atframe = Frame(master)
        self.atframe.pack(side=TOP)
        self.aWidgets(self.atframe)
        master.add(self.atframe,text="About")
        
    def aWidgets(self, master):
        info = helpers.show_version()
        self.heading = Label(master, text=info["name"], font=("","20","bold"))
        self.heading.pack(side=TOP)
        self.vers = Label(master, text=info["version"],font=("","8","italic"))
        self.vers.pack(side=TOP)
        self.desc = Label(master, text=info["description"])
        self.desc.pack(side=TOP)
        self.more = Label(master, text=info["more"])
        self.more.pack(side=TOP)
        
    def setOutput(self,nstr):
        self.outText.delete("0.0",END)
        self.outText.insert("0.0",nstr)
        
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
            
    def decideCommand(self):
        operation = self.tabs.tab("current")["text"].lower()
        if operation == 'ip':
            self.calculateIP()
        elif operation == 'subnetting':
            self.calculateSubnets()
            
    def calculateSubnets(self):
        subnetLimit = self.limitEntry.get()
        network = self.netadd.get()
        hosts = self.hosts.get()
        subnets = self.snets.get()
        priorityHosts = self.priorVar.get()
        scom = self.subcomVar.get()
        output = ''
        # Validation
        if(not validator.ipv4network(network) and not validator.ipv6network(network)):
            messagebox.showerror("Invalid Network", "IPv4/IPv6 network address supplied is invalid.")
            return False
        isIpv4 = validator.ipv4network(network)
        isIpv6 = validator.ipv6network(network)
        if scom == 'flsm':
            try:
                subnetLimit = int(subnetLimit)
            except:
                subnetLimit=None
            if not subnetLimit:
                subnetLimit=None
            if(not validator.integer(subnets)):
                messagebox.showerror("Invalid Subnet Number", "Number of subnets must be an integer.")
                return False
            elif (not validator.integer(hosts)):
                messagebox.showerror("Invalid Host Number", "Number of hosts must be an integer.")
                return False
            subnetList = []
            try:
                if isIpv4:
                    subnetList = PyNIPv4Network(network).subnets_flsm(int(hosts),int(subnets),priorityHosts)
                    numOfSubnets = PyNIPv4Network(network).num_of_subnets(int(hosts), int(subnets), priorityHosts)
                    output = helpers.show_ipv4_subnet_table(network, hosts, subnets, subnetList, numOfSubnets, subnetLimit)
                else:
                    subnetList = PyNIPv6Network(network).subnets_flsm(int(hosts),int(subnets),priorityHosts)
                    numOfSubnets = PyNIPv6Network(network).num_of_subnets(int(hosts), int(subnets), priorityHosts)
                    output = helpers.show_ipv6_subnet_table(network, hosts, subnets, subnetList, numOfSubnets, subnetLimit)
                self.setOutput(output)
                return True
            except TypeError:
                messagebox.showerror("Invalid Network", "IPv4/IPv6 network address supplied is invalid.")
                return False
            except:
                messagebox.showerror("Error", "Unknown Error Occured")
                return False
        elif scom == "vlsm":
            ss = self.subSize.get()
            ss = ss.split(',')
            hosts = list(map(lambda i: int(i), ss))
            try:
                if isIpv4:
                    subnetList = PyNIPv4Network(network).subnets_vlsm(hosts)
                    output = helpers.show_ipv4_subnet_table(network, hosts, len(hosts), subnetList, len(hosts))
                else:
                    subnetList = PyNIPv6Network(network).subnets_vlsm(hosts)
                    output = helpers.show_ipv6_subnet_table(network, hosts, len(hosts), subnetList, len(hosts))
                self.setOutput(output)
                return True
            except ValueError:
                messagebox.showerror("Error", "Specified number of hosts or subnets cannot be accommodated")
                
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
        self.ipEntry = Entry(self.ipEntryFrame,width=60)
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

    def processWidgets(self, master):
        self.buttonsFrame = Frame(master)
        self.buttonsFrame.pack(side=TOP)
        clearConsole = lambda: self.setOutput('')
        # Go!
        self.ipCalculate = Button(self.buttonsFrame,text="Calculate",command=self.decideCommand)
        self.ipCalculate.pack(side=LEFT)
        # Copy to clipboard
        self.ipCopyToClip = Button(self.buttonsFrame,text="Copy Output",command=self.copyOutput)
        self.ipCopyToClip.pack(side=LEFT)
        # Clear console
        self.ipClearCon = Button(self.buttonsFrame,text="Clear",command=clearConsole)
        self.ipClearCon.pack(side=LEFT)

    def copyOutput(self):
        self.clipboard_clear()
        self.clipboard_append(self.outText.get("0.0",END))
        
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
        
    def switchCom(self):
        com = self.subcomVar.get()
        if com == "vlsm":
            self.subSize.config(state="normal")
            for widget in self.flsmwidgets:
                widget.config(state="disabled")
        else:
            self.subSize.config(state="disabled")
            for widget in self.flsmwidgets:
                widget.config(state="normal")
            
    def snWidgets(self, master):
        self.netaddLabel = Label(master, text="Network Address")
        self.netaddLabel.pack(side=TOP,anchor='w')
        self.netandrad = Frame(master)
        self.netandrad.pack(side=TOP,anchor='w')

        self.exFrame = Frame(master)
        self.exFrame.pack(side=TOP,anchor='w')
        self.hostsFrame = Frame(self.exFrame)
        self.hostsFrame.pack(side=LEFT,anchor='n')
        self.hostsLabel = Label(self.hostsFrame,text="Hosts")
        self.hostsLabel.pack(side=TOP,anchor='w')
        self.hosts=Entry(self.hostsFrame)
        self.hosts.pack(side=TOP,anchor='w')
        self.flsmwidgets.append(self.hosts)
        
        self.snetsFrame = Frame(self.exFrame)
        self.snetsFrame.pack(side=LEFT,anchor='n')
        self.snetsLabel = Label(self.snetsFrame,text="Subnets")
        self.snetsLabel.pack(side=TOP,anchor='w')
        self.snets=Entry(self.snetsFrame)
        self.snets.pack(side=TOP,anchor='w')
        self.flsmwidgets.append(self.snets)
        
        self.subSizeFrame = Frame(self.exFrame)
        self.subSizeFrame.pack(side=LEFT,anchor='n')
        self.subSizeLabel = Label(self.subSizeFrame,text="Subnet Size")
        self.subSizeLabel.pack(side=TOP,anchor='w')
        self.subSize = Entry(self.subSizeFrame,width=50)
        self.subSize.pack(side=TOP, anchor='w')
        self.subHint = Label(self.subSizeFrame,text="Separate with comma's (\",\")",font=self.fHint)
        self.subHint.pack(side=TOP, anchor='w')
        
        self.moreOpsFrame = Frame(master)
        self.moreOpsFrame.pack(side=TOP,anchor='w')
        self.prioFrame = LabelFrame(self.moreOpsFrame, text="Priority")
        self.prioFrame.pack(side=LEFT)
        self.limitFrame = LabelFrame(self.moreOpsFrame, text="Limit")
        self.limitFrame.pack(side=LEFT)
        
        # Okay the entry and radios
        self.netadd = Entry(self.netandrad,width=60)
        self.netadd.pack(side=LEFT)
        self.rbFlsm = Radiobutton(self.netandrad, text="flsm", variable=self.subcomVar, value="flsm",command=self.switchCom)
        self.rbFlsm.pack(side=LEFT)
        self.rbFlsm.invoke()
        self.rbVlsm = Radiobutton(self.netandrad, text="vlsm", variable=self.subcomVar, value="vlsm",command=self.switchCom)
        self.rbVlsm.pack(side=LEFT)

        # Widgets for more opts
        self.priHosts = Radiobutton(self.prioFrame, text="Hosts", variable=self.priorVar, value=True)
        self.priHosts.pack(side=TOP,anchor='w')
        self.priHosts.invoke()
        self.flsmwidgets.append(self.priHosts)
        self.priSNets = Radiobutton(self.prioFrame, text="Subnets", variable=self.priorVar, value=False)
        self.priSNets.pack(side=TOP,anchor='w')
        self.flsmwidgets.append(self.priSNets)

        self.limitEntry = Entry(self.limitFrame)
        self.limitEntry.pack(side=TOP)
        self.flsmwidgets.append(self.limitEntry)
        self.limitLabel = Label(self.limitFrame,font=self.fHint,text="Use 0 for no limit")
        self.limitLabel.pack(side=TOP,anchor='w')
        
                         
root = Tk()
root.title("PyNetCal")
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)
app = Application(master=root)
app.mainloop()
