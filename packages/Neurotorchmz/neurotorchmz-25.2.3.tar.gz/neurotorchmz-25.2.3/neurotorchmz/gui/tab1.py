from .window import *
from ..utils.image import ImgObj

import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import cm
import numpy as np

class TabImage_ViewChangedEvent(TabUpdateEvent):
    pass

class TabImage(Tab):
    def __init__(self, gui: Neurotorch_GUI):
        super().__init__(gui)
        self.tab_name = "Tab Image"
        self.gui = gui
        self.root = gui.root
        self.imshow2D = None
        self.imshow3D = None
        self.colorbar = None

    def Init(self):
        self.tab = ttk.Frame(self.gui.tabMain)
        self.gui.tabMain.add(self.tab, text="Image")

        self.frameRadioImageMode = tk.Frame(self.tab)
        self.radioDisplayVar = tk.StringVar(value="imgMean")
        self.radioDisplay1 = tk.Radiobutton(self.frameRadioImageMode, variable=self.radioDisplayVar, indicatoron=False, command=lambda:self.Update(TabImage_ViewChangedEvent()), text="Image mean (imgMean)", value="imgMean")
        self.radioDisplay1b = tk.Radiobutton(self.frameRadioImageMode, variable=self.radioDisplayVar, indicatoron=False, command=lambda:self.Update(TabImage_ViewChangedEvent()), text="Image standard deviation (imgStd)", value="imgStd")
        self.radioDisplay2 = tk.Radiobutton(self.frameRadioImageMode, variable=self.radioDisplayVar, indicatoron=False, command=lambda:self.Update(TabImage_ViewChangedEvent()), text="Difference Image Maximum (imgDiffMax)", value="diffMax")
        self.radioDisplay3 = tk.Radiobutton(self.frameRadioImageMode, variable=self.radioDisplayVar, indicatoron=False, command=lambda:self.Update(TabImage_ViewChangedEvent()), text="Difference Image Standard deviation (imgDiffStd)", value="diffStd")
        self.radioDisplay4 = tk.Radiobutton(self.frameRadioImageMode, variable=self.radioDisplayVar, indicatoron=False, command=lambda:self.Update(TabImage_ViewChangedEvent()), text="imgDiffMax without signal", value="diffMaxWithoutSignal")
        self.radioDisplay1.grid(row=0, column=0)
        self.radioDisplay1b.grid(row=0, column=1)
        self.radioDisplay2.grid(row=0, column=2)
        self.radioDisplay3.grid(row=0, column=3)
        self.radioDisplay4.grid(row=0, column=4)
        self.frameRadioImageMode.pack()

        self.frameMainDisplay = tk.Frame(self.tab)
        self.frameMainDisplay.pack(expand=True, fill="both")
        self.frameMetadata = tk.LabelFrame(self.frameMainDisplay,  text="Metadata")
        self.frameMetadata.pack(side=tk.LEFT, fill="y")
        self.frameMetadataTop = tk.Frame(self.frameMetadata)
        self.frameMetadataTop.pack(expand=True, fill="both", padx=10)
        self.treeMetadata = ttk.Treeview(self.frameMetadataTop, columns=("Value"))
        self.treeMetadata.pack(expand=True, fill="y", padx=2, side=tk.LEFT)
        self.treeMetadata.heading('#0', text="Property")
        self.treeMetadata.heading('Value', text='Value')
        self.treeMetadata.column("#0", minwidth=0, width=200)
        self.treeMetadata.column("Value", minwidth=0, width=120)
        self.scrollTreeMetadata = ttk.Scrollbar(self.frameMetadataTop, orient="vertical", command=self.treeMetadata.yview)
        self.scrollTreeMetadata.pack(side=tk.LEFT, expand=True, fill="y")
        self.scrollXTreeMetadata = ttk.Scrollbar(self.frameMetadata, orient="horizontal", command=self.treeMetadata.xview)
        self.scrollXTreeMetadata.pack(fill="x")
        
        self.treeMetadata.configure(yscrollcommand=self.scrollTreeMetadata.set)
        self.treeMetadata.configure(xscrollcommand=self.scrollXTreeMetadata.set)


        self.notebookPlots = ttk.Notebook(self.frameMainDisplay)
        self.notebookPlots.bind('<<NotebookTabChanged>>',lambda _:self.Update(TabImage_ViewChangedEvent()))
        self.tab2D = ttk.Frame(self.notebookPlots)
        self.tab3D = ttk.Frame(self.notebookPlots)
        self.notebookPlots.add(self.tab2D, text="2D")
        self.notebookPlots.add(self.tab3D, text="3D")
        self.notebookPlots.pack(side=tk.LEFT, expand=True, fill="both")

        self.figure2D = plt.Figure(figsize=(6,6), dpi=100)
        self.figure2D.tight_layout()
        self.ax2D = self.figure2D.add_subplot()  
        self.ax2D.set_axis_off()
        self.canvas2D = FigureCanvasTkAgg(self.figure2D, self.tab2D)
        self.canvtoolbar2D = NavigationToolbar2Tk(self.canvas2D,self.tab2D)
        self.canvtoolbar2D.update()
        self.canvas2D.get_tk_widget().pack(fill="both", expand=True)
        self.canvas2D.draw()

        self.figure3D = plt.Figure(figsize=(6,6), dpi=100)
        self.figure3D.tight_layout()
        self.ax3D = self.figure3D.add_subplot(projection='3d')  
        self.canvas3D = FigureCanvasTkAgg(self.figure3D, self.tab3D)
        self.canvtoolbar3D = NavigationToolbar2Tk(self.canvas3D,self.tab3D)
        self.canvtoolbar3D.update()
        self.canvas3D.get_tk_widget().pack(fill="both", expand=True)
        self.canvas3D.draw()

    def Update(self, event: TabUpdateEvent):
        if not (isinstance(event, ImageChangedEvent) or isinstance(event, TabImage_ViewChangedEvent)):
            return
        if isinstance(event, ImageChangedEvent):
            if self.colorbar is not None:
                self.colorbar.remove()
                self.colorbar = None
            self.ax2D.clear()
            self.ax3D.clear()
            self.ax2D.set_axis_off()
            self.imshow2D = None
            self.imshow3D = None    
            self.treeMetadata.delete(*self.treeMetadata.get_children())
            if self.gui.ImageObject is not None:
                self.treeMetadata.insert('', 'end', iid="providedImageData", text="General Image Properties", open=True)
                self.treeMetadata.insert('providedImageData', 'end', text="Name", values=([self.gui.ImageObject.name]))
                if self.gui.ImageObject.img is not None:
                    self.treeMetadata.insert('providedImageData', 'end', text="Frames", values=([self.gui.ImageObject.img.shape[0]]))
                    self.treeMetadata.insert('providedImageData', 'end', text="Width [px]", values=([self.gui.ImageObject.img.shape[2]]))
                    self.treeMetadata.insert('providedImageData', 'end', text="Height [px]", values=([self.gui.ImageObject.img.shape[1]]))
                    self.treeMetadata.insert('providedImageData', 'end', text="Numpy dtype", values=([self.gui.ImageObject.img.dtype]))
                    self.treeMetadata.insert('providedImageData', 'end', text="Maximum", values=([self.gui.ImageObject.imgProps.max]))
                    self.treeMetadata.insert('providedImageData', 'end', text="Minimum", values=([self.gui.ImageObject.imgProps.min]))
                else:
                    self.treeMetadata.insert('providedImageData', 'end', text="Only diffImage provided", values=(["True"]))
                if self.gui.ImageObject.pims_metadata is not None:
                    self.treeMetadata.insert('', 'end', iid="nd2ImageData", text="ND2 Image Data (Selected)", open=True)
                    for k,v in ImgObj.nd2_relevantMetadata.items():
                        if k in self.gui.ImageObject.pims_metadata.keys():
                            value = self.gui.ImageObject.pims_metadata[k]
                            self.treeMetadata.insert('nd2ImageData', 'end', text=v, values=([value]))
                        else:
                            self.treeMetadata.insert('nd2ImageData', 'end', text=v, values=(["Not set"]))
                    self.treeMetadata.insert('', 'end', iid="nd2RawImageData", text="ND2 Image Data (All)", open=False)
                    for k,v in self.gui.ImageObject.pims_metadata.items():
                        if "#" in k:
                            continue
                        self.treeMetadata.insert('nd2RawImageData', 'end', text=k, values=([v]))

        _selected = self.radioDisplayVar.get()
        if self.colorbar is not None:
            self.colorbar.remove()
            self.colorbar = None
        if self.imshow2D is not None:
            self.imshow2D.remove()
            self.imshow2D = None
        if self.imshow3D is not None:
            self.imshow3D.remove()
            self.imshow3D = None
        

        imgObj = self.gui.ImageObject

        if imgObj is None or imgObj.img is None or imgObj.imgDiff is None:
            self.canvas2D.draw()
            self.canvas3D.draw()
            return
        match (_selected):
            case "imgMean":
                self.ax2D.set_axis_on()
                self.imshow2D = self.ax2D.imshow(imgObj.imgView(ImgObj.SPATIAL).Mean, cmap="Greys_r")
            case "imgStd":
                self.ax2D.set_axis_on()
                self.imshow2D = self.ax2D.imshow(imgObj.imgView(ImgObj.SPATIAL).Std, cmap="Greys_r")
            case "diffMax":
                self.ax2D.set_axis_on()
                self.imshow2D = self.ax2D.imshow(imgObj.imgDiffView(ImgObj.SPATIAL).Max, cmap="inferno")
            case "diffStd":
                self.ax2D.set_axis_on()
                self.imshow2D = self.ax2D.imshow(imgObj.imgDiffView(ImgObj.SPATIAL).Std, cmap="inferno")
            case "diffMaxWithoutSignal":
                if self.gui.signal.imgObj_Sliced is not False and self.gui.signal.imgObj_Sliced is not None and self.gui.signal.imgObj_Sliced.imgDiff is not None:
                    self.ax2D.set_axis_on()
                    self.imshow2D = self.ax2D.imshow(self.gui.signal.imgObj_Sliced.imgDiffView(ImgObj.SPATIAL).Max, cmap="inferno")
                else:
                    self.ax2D.set_axis_off()
            case _:
                self.ax2D.set_axis_off()
        if (self.notebookPlots.tab(self.notebookPlots.select(), "text") == "2D"):
            if self.imshow2D is not None:
                self.colorbar = self.figure2D.colorbar(self.imshow2D, ax=self.ax2D)
            self.canvas2D.draw()
            return
        if self.notebookPlots.tab(self.notebookPlots.select(), "text") != "3D":
            print("Assertion Error: The tabMain value is not 2D or 3D")

        X = np.arange(0,imgObj.imgDiff.shape[2])
        Y = np.arange(0,imgObj.imgDiff.shape[1])
        X, Y = np.meshgrid(X, Y)
        match (_selected):
            case "imgMean":
                self.imshow3D = self.ax3D.plot_surface(X,Y, imgObj.imgView(ImgObj.SPATIAL).Mean, cmap="Greys_r")
            case "imgStd":
                self.imshow3D = self.ax3D.plot_surface(X,Y, imgObj.imgView(ImgObj.SPATIAL).Std, cmap="Greys_r")
            case "diffMax":
                self.imshow3D = self.ax3D.plot_surface(X,Y, imgObj.imgDiffView(ImgObj.SPATIAL).Max, cmap="inferno")
            case "diffStd":
                self.imshow3D = self.ax3D.plot_surface(X,Y, imgObj.imgDiffView(ImgObj.SPATIAL).Std, cmap="inferno")
            case "diffMaxWithoutSignal":
                if self.gui.signal.imgObj_Sliced is not False and self.gui.signal.imgObj_Sliced is not None:
                    self.imshow3D = self.ax3D.plot_surface(X,Y, self.gui.signal.imgObj_Sliced.imgDiffView(ImgObj.SPATIAL).Max, cmap="inferno")
            case _:
                pass
        if self.imshow3D is not None:
            self.colorbar = self.figure3D.colorbar(self.imshow3D, ax=self.ax3D)
        self.canvas3D.draw()
