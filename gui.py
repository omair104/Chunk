# -*- coding: utf-8 -*-
"""
Created on June 02 10:00:25 2019
@author: Babri
"""

import os
import sys
import tkinter
from tkinter import Toplevel
#from tkinter import filedialog
import chunk_creator

#For third party libraies
try:
    our_location = os.path.realpath(os.path.abspath(os.path.dirname(__file__)))
    print(our_location)
except:
    our_location = os.path.abspath(os.path.normpath(os.path.dirname(sys.argv[0])))

__base_dir = our_location
__libs_dir = os.path.join(__base_dir, 'thirdparty')

sys.path.insert(0, __base_dir)
sys.path.insert(0, __libs_dir)



class Application(tkinter.Frame):
       
    def __init__(self, directory, master=None):
        self.directory=directory        
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.QUIT = tkinter.Button(self, width=15, fg = "red", font =('bold',18))
        self.QUIT["text"] = "EXIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(row=30, sticky = 'W', pady=10)

        #------------------------------------------- WIDGETS ON MAIN GUI -------------------------------------------

        self.convertlabel=tkinter.Label(self, text='Image Chunk Generator',font=('bold',16)).grid(row=16, pady=2, sticky='W')

        #Enter Input file location 
        self.length_label = tkinter.Label(self, text='Enter input files location:').grid(row=17, sticky='W')
        self.input_location_entrybox = tkinter.Entry(self, width=45)
        self.input_location_entrybox.grid(row=18, sticky='W')
        #self.askbutton= tkinter.Button(self, text='browse', command=self.askdirectory_input).grid(row=18, column=1)

         
        #Enter Output file Location
        self.location_label=tkinter.Label(self, text='Enter output files location:').grid(row=19, sticky='W')
        self.output_location_entrybox=tkinter.Entry(self, width=45)
        self.output_location_entrybox.grid(row=20, sticky='W')
        #self.askbutton= tkinter.Button(self, text='browse', command=self.askdirectory_output).grid(row=20, column=1)
        
        #Enter Images per chunk
        self.length_label = tkinter.Label(self, text='Images per chunk:').grid(row=21, sticky='W')
        self.images_per_chunk_entrybox = tkinter.Entry(self, width=45)
        self.images_per_chunk_entrybox.grid(row=22, sticky='W')
        
        #Enter Overlap size 
        self.length_label = tkinter.Label(self, text='Overlap size:').grid(row=23, sticky='W')
        self.overlap_size_entrybox = tkinter.Entry(self, width=45)
        self.overlap_size_entrybox.grid(row=24, sticky='W')
        
        '''
        def askdirectory(self):
        #self.directory = tkFileDialog.askdirectory(**self.dir_opt)
        self.rotateddirectory = tkFileDialog.askdirectory()
        self.rotatedpath.delete(0,100)
        self.rotatedpath.insert(0,self.rotateddirectory)
        '''

        #button for converting
        self.convertbutton = tkinter.Button(self, width=20, text='Copy Images to Chunks',font=('bold',18), command=self.copyFiles)
        self.convertbutton.grid(row=28, pady=10, sticky='W')
    '''
    def askdirectory_input(self):
        filename = filedialog.askdirectory()
        self.input_location_entrybox.delete(0,500)
        self.input_location_entrybox.insert(0, filename)
        
    def askdirectory_output(self):
        filename = filedialog.askdirectory()
        self.output_location_entrybox.delete(0,500)
        self.output_location_entrybox.insert(0, filename)
    '''
        
        
    def copyFiles(self):
        self.fields_check()
        input_location_entrybox = str(self.input_location_entrybox.get())
        output_location_entrybox = str(self.output_location_entrybox.get())
        images_per_chunk_entrybox=int(self.images_per_chunk_entrybox.get())
        overlap_size_entrybox=int(self.overlap_size_entrybox.get())
        chunk_creator.main(input_location_entrybox, output_location_entrybox, images_per_chunk_entrybox, overlap_size_entrybox)
        

    def display_error(self, text_message):
        top = Toplevel()
        x = self.master.winfo_rootx()
        y = self.master.winfo_rooty()
        top.geometry("+%d+%d" %(x+250,y+150))
        #top.geometry("+550+350")
        top.title('Error')
        tkinter.Label(top, text=text_message).grid(row=1, sticky='W')
        tkinter.Button(top, text="OK", command=top.destroy).grid(row=2)


    def fields_check(self):

        self.field1=self.input_location_entrybox.get()
        self.field2=self.output_location_entrybox.get()
        self.field3=self.images_per_chunk_entrybox.get()
        self.field4=self.overlap_size_entrybox.get()

        if  not self.field1:
            text_message = "Please select input location"
            self.display_error(text_message)
            return
        else:
            pass

        if not self.field2:
            text_message = "Please select output location"
            self.display_error(text_message)
            return
        else:
            pass

        if not self.field3:
            text_message = "Please select chunk size"
            self.display_error(text_message)
            return   
        else:
            pass
        
        if not self.field4:
            text_message = "Please select overlap size"
            self.display_error(text_message)
            return   
        else:
            pass



root = tkinter.Tk()
root.geometry("800x400+300+200")
root.title("Image Chunk generator")

app = Application('', master=root)

#app.configure(background='grey')
app.mainloop()
#com= comparing(app)
root.destroy()