from .window import *
from .components.general import *
from .components.treeview import SynapseTreeview
from ..utils import synapse_detection_integration as detection
from ..utils.image import *
from ..utils.synapse_detection import *
from ..utils.logger import logger


import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.widgets as PltWidget
import matplotlib.patches as patches
from matplotlib import cm
import matplotlib.colors as cm_colors
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd
from scipy.stats import multivariate_normal

class TabAnalysis_AlgorithmChangedEvent(TabUpdateEvent):
    pass

class TabAnalysis(Tab):

    def __init__(self, gui: Neurotorch_GUI):
        super().__init__(gui)
        self.tab_name = "Tab Analysis"
        self._gui = gui
        self.root = gui.root
        self.detectionAlgorithm = None
        self.roiPatches = {}
        self.roiPatches2 = {}
        self.treeROIs_entryPopup = None
        self.ax1Image = None
        self.ax2Image = None
        self.ax1_colorbar = None
        self.ax2_colorbar = None

        self._synapses: dict[str, ISynapse] = {}

    def Init(self):
        self.tab = ttk.Frame(self._gui.tabMain)
        self._gui.tabMain.add(self.tab, text="Synapse Analyzer (Beta version)")
        self.frameToolsContainer = ScrolledFrame(self.tab)
        self.frameToolsContainer.pack(side=tk.LEFT, fill="y", anchor=tk.NW)
        self.frameTools = self.frameToolsContainer.frame

        self.frameDetection = ttk.LabelFrame(self.frameTools, text="Detection Algorithm")
        self.frameDetection.grid(row=0, column=0, sticky="news")
        self.lblAlgorithm = tk.Label(self.frameDetection, text="Algorithm")
        self.lblAlgorithm.grid(row=0, column=0, columnspan=2, sticky="nw")
        self.radioAlgoVar = tk.StringVar(value="local_max")
        self.radioAlgo1 = tk.Radiobutton(self.frameDetection, variable=self.radioAlgoVar, indicatoron=True, text="Threshold (Deprecated)", value="threshold", command=lambda:self.Invalidate_Algorithm())
        self.radioAlgo2 = tk.Radiobutton(self.frameDetection, variable=self.radioAlgoVar, indicatoron=True, text="Hysteresis thresholding", value="hysteresis", command=lambda:self.Invalidate_Algorithm())
        self.radioAlgo3 = tk.Radiobutton(self.frameDetection, variable=self.radioAlgoVar, indicatoron=True, text="Local Max", value="local_max", command=lambda:self.Invalidate_Algorithm())
        ToolTip(self.radioAlgo1, msg=Resource.GetString("algorithms/threshold/description"), follow=True, delay=0.1)
        ToolTip(self.radioAlgo2, msg=Resource.GetString("algorithms/hysteresisTh/description"), follow=True, delay=0.1)
        ToolTip(self.radioAlgo3, msg=Resource.GetString("algorithms/localMax/description"), follow=True, delay=0.1)
        self.radioAlgo1.grid(row=1, column=0, sticky="nw", columnspan=3)
        self.radioAlgo2.grid(row=2, column=0, sticky="nw", columnspan=3)
        self.radioAlgo3.grid(row=3, column=0, sticky="nw", columnspan=3)

        tk.Label(self.frameDetection, text="Diff. Img Overlay").grid(row=11, column=0)
        self.setting_plotOverlay = GridSetting(self.frameDetection, row=11, type_="Checkbox", text="Plot raw algorithm output", default=0, tooltip=Resource.GetString("tab3/rawAlgorithmOutput"))
        self.setting_plotOverlay.var.IntVar.trace_add("write", lambda _1,_2,_3: self.Invalidate_ROIs())
        self.setting_plotPixels = GridSetting(self.frameDetection, row=12, type_="Checkbox", text="Plot ROIs pixels", default=0, tooltip=Resource.GetString("tab3/plotROIPixels"))
        self.setting_plotPixels.var.IntVar.trace_add("write", lambda _1,_2,_3: self.Invalidate_ROIs())
        self.btnDetect = tk.Button(self.frameDetection, text="Detect", command=self.Detect)
        self.btnDetect.grid(row=20, column=0)

        self.frameDisplay= ttk.LabelFrame(self.frameTools, text="Display Options")
        self.frameDisplay.grid(row=1, column=0, sticky="news")

        self.sliderFrame = GridSetting(self.frameDisplay, row=5, type_="Int", text="Frame", min_=0, max_=0, scaleMin=0, scaleMax=0)
        self.sliderFrame.var.SetCallback(self.SliderFrameChanged)
        self.sliderPeak = GridSetting(self.frameDisplay, row=6, type_="Int", text="Peak", min_=0, max_=0, scaleMin=0, scaleMax=0)
        self.sliderPeak.var.SetCallback(self.SliderPeakChanged)
        self.btn3DPlot = tk.Button(self.frameDisplay, text="3D Multiframe Plot", command=lambda:self.ShowExternalPlot("3D Multiframe Plot", self.Plot3DMultiframe))
        self.btn3DPlot.grid(row=10, column=1)


        self.detectionAlgorithm = detection.IDetectionAlgorithmIntegration()
        self.frameAlgoOptions = self.detectionAlgorithm.OptionsFrame(self.frameTools, self._gui.GetImageObject)
        self.frameAlgoOptions.grid(row=2, column=0, sticky="news")

        self.frameROIS = tk.LabelFrame(self.frameTools, text="ROIs")
        self.frameROIS.grid(row=3, column=0, sticky="news")

        self.tvSynapses = SynapseTreeview(self.frameROIS, self._gui, synapseCallback=self.Synapses,selectCallback=self.InvalidateSelectedROI, updateCallback=self.Invalidate_ROIs)
        self.tvSynapses.pack(fill="both", padx=10)
        tk.Label(self.frameROIS, text="Use Right-Click to edit").pack(fill="x")
        tk.Label(self.frameROIS, text="Double click on values to modify them").pack(fill="x")
        self.tvSynapses.option_allowAddingMultiframeSynapses = True

        self.figure1 = plt.Figure(figsize=(20,10), dpi=100)
        self.ax1 = self.figure1.add_subplot(221)  
        self.ax2 = self.figure1.add_subplot(222, sharex=self.ax1, sharey=self.ax1)  
        self.ax3 = self.figure1.add_subplot(223)  
        self.ax4 = self.figure1.add_subplot(224)  

        self.ClearImagePlot()
        self.canvas1 = FigureCanvasTkAgg(self.figure1, self.tab)
        self.canvtoolbar1 = NavigationToolbar2Tk(self.canvas1,self.tab)
        self.canvtoolbar1.update()
        self.canvas1.get_tk_widget().pack(expand=True, fill="both", side=tk.LEFT)
        self.canvas1.mpl_connect('resize_event', self._Canvas1Resize)
        self.canvas1.mpl_connect('button_press_event', self.Canvas1ClickEvent)
        self.canvas1.draw()

        #tk.Grid.rowconfigure(self.frameTools, 3, weight=1)

        self.tvSynapses.SyncSynapses()
        self.Update(TabAnalysis_AlgorithmChangedEvent())


    # Public functions

    @property
    def synapses(self) -> list[ISynapse]:
        """ The current list of synapses in this tab. If you modify values inside this list, make sure to call tvSynapses.SyncSynapses() to reflect the changes in the TreeView. """
        return list(self._synapses.values())
    
    @synapses.setter
    def synapses(self, val: list[ISynapse]):
        if not isinstance(val, list) or not all(isinstance(v, ISynapse) for v in val):
            raise ValueError("The synapse property expects a list of ISynapse")
        self._synapses = {s.uuid:s for s in val}

    @property
    def synapses_dict(self) -> dict[str, ISynapse]:
        """ 
            The current list of synapses in this tab presented as dict with the UUID as key. 
            If you modify values inside this list, make sure to call tvSynapses.SyncSynapses() to reflect the changes in the TreeView. 
        """
        return self._synapses
    
    @synapses_dict.setter
    def synapses_dict(self, val: dict[str, ISynapse]):
        if not isinstance(val, dict) or not all(isinstance(k, str) and isinstance(v, ISynapse) for k, v in val.items()):
            raise ValueError("The synapse property expects a dictionary of ISynapses with their UUID as key")
        self._synapses = val

    def Synapses(self, newval: dict[str, ISynapse]|None = None) -> dict[str, ISynapse]:
        """ Python does not provide a pointer concept. Therefore use this helper function combining a Getter/Setter"""
        if newval is not None:
            self._synapses = newval
        return self._synapses

    # Update and Invalidation functions

    def Update(self, event: TabUpdateEvent):
        """ The main function to update this tab. """
        if isinstance(event, ImageChangedEvent):
            self.tvSynapses.ClearSynapses('non_staged')
            self.tvSynapses.SyncSynapses()
            self.ClearImagePlot()
            self.Invalidate_Algorithm()
            self.Invalidate_Image()
        elif isinstance(event, SignalChangedEvent):
            self.Invalidate_Signal()
        elif isinstance(event, TabAnalysis_AlgorithmChangedEvent):
            self.Invalidate_Algorithm()
            self.Invalidate_Image()


    def Invalidate_Algorithm(self):
        match self.radioAlgoVar.get():
            case "threshold":
                if isinstance(self.detectionAlgorithm, detection.Thresholding_Integration):
                    self.detectionAlgorithm.OptionsFrame_Update(self.GetCurrentDetectionSource())
                    return
                self.detectionAlgorithm = detection.Thresholding_Integration()
            case "hysteresis":
                if type(self.detectionAlgorithm) == detection.HysteresisTh_Integration:
                    self.detectionAlgorithm.OptionsFrame_Update(self.GetCurrentDetectionSource())
                    return
                self.detectionAlgorithm = detection.HysteresisTh_Integration()
            case "local_max":
                if type(self.detectionAlgorithm) == detection.LocalMax_Integration:
                    self.detectionAlgorithm.OptionsFrame_Update(self.GetCurrentDetectionSource())
                    return
                self.detectionAlgorithm = detection.LocalMax_Integration()
            case _:
                self.detectionAlgorithm = None
                return
        if (self.frameAlgoOptions is not None):
            self.frameAlgoOptions.grid_forget()
        self.frameAlgoOptions = self.detectionAlgorithm.OptionsFrame(self.frameTools, self._gui.GetImageObject)
        self.detectionAlgorithm.OptionsFrame_Update(self.GetCurrentDetectionSource())
        self.frameAlgoOptions.grid(row=2, column=0, sticky="news")

    def ClearImagePlot(self):
        if self.ax1_colorbar is not None:
            self.ax1_colorbar.remove()
            self.ax1_colorbar = None
        if self.ax2_colorbar is not None:
            self.ax2_colorbar.remove()
            self.ax2_colorbar = None
        for ax in [self.ax1, self.ax2, self.ax3, self.ax4]: 
            ax.clear()
            ax.set_axis_off()
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        self.ax1.set_title("Image (Mean)")
        self.ax2.set_title("Diff Image")

    def Invalidate_Signal(self):
        if self._gui.signal.peaks is not None:
            self.sliderPeak.SetRange(min_=1, max_=len(self._gui.signal.peaks), syncScale=True)
        else:
            self.sliderPeak.SetRange(0,0, syncScale=True)
        

    def Invalidate_Image(self):
        imgObj = self._gui.ImageObject

        self.ax1Image = None
        if self.ax1_colorbar is not None:
            self.ax1_colorbar.remove()
            self.ax1_colorbar = None
        for axImg in self.ax1.get_images(): 
            axImg.remove()
        self.ax1.set_axis_off()

        self.Invalidate_Signal()
        
        if imgObj is None or imgObj.img is None or imgObj.imgDiff is None:
            self.sliderFrame.SetRange(0,0, syncScale=True)
            self.Invalidate_DiffImage()
            return
        
        self.ax1Image = self.ax1.imshow(imgObj.imgView(imgObj.SPATIAL).Mean, cmap="Greys_r") 
        self.ax1.set_axis_on()
        self.ax1_colorbar = self.figure1.colorbar(self.ax1Image, ax=self.ax1)
        
        self.sliderFrame.SetRange(min_=1, max_=imgObj.imgDiff.shape[0], syncScale=True)
        self.Invalidate_DiffImage()


    def Invalidate_DiffImage(self):
        imgObj = self._gui.ImageObject
        self.ax2Image = None    

        if self.ax2_colorbar is not None:
            self.ax2_colorbar.remove()
            self.ax2_colorbar = None
        for axImg in self.ax2.get_images(): 
            axImg.remove()
        self.ax2.set_axis_off()
            
        if imgObj is None or imgObj.img is None or imgObj.imgDiff is None:
            self.Invalidate_ROIs()
            return
        frame = self.sliderFrame.Get() - 1
        if frame < 0 or frame >= imgObj.imgDiff.shape[0]:
            self.Invalidate_ROIs()
            return
        
        vmin, vmax = 0, imgObj.imgDiffProps.max
        self.ax2Image = self.ax2.imshow(imgObj.imgDiff[frame], cmap="inferno", vmin=vmin, vmax=vmax)
        self.ax2_colorbar = self.figure1.colorbar(self.ax2Image, ax=self.ax2)
        self.ax2.set_axis_on()

        self.ax2.set_title(f"Diff. Image (Frame {frame + 1})")

        self.Invalidate_ROIs()

        

    def Invalidate_ROIs(self):
        for axImg in self.ax1.get_images():
            if axImg != self.ax1Image: axImg.remove()
        for axImg in self.ax2.get_images():
            if axImg != self.ax2Image: axImg.remove()
        for p in reversed(self.ax1.patches): p.remove()
        for p in reversed(self.ax2.patches): p.remove()
        self.roiPatches = {}
        self.roiPatches2 = {}

        if self.tvSynapses.modified:
            self.frameROIS["text"] = "ROIs*"
        else:
            self.frameROIS["text"] = "ROIs"

        _ax1HasImage = len(self.ax1.get_images()) > 0
        _ax2HasImage = len(self.ax2.get_images()) > 0

        frame = self.sliderFrame.Get() - 1
        
        # Plotting the ROIs

        for synapse in self.synapses:
            for roi in synapse.rois:
                if roi.location is None:
                    continue
                if isinstance(roi, detection.CircularSynapseROI):
                    c = patches.Circle(roi.location, roi.radius+0.5, color="red", fill=False)
                    c2 = patches.Circle(roi.location, roi.radius+0.5, color="green", fill=False)
                elif isinstance(roi, detection.PolygonalSynapseROI):
                    c = patches.Polygon(roi.polygon, color="red", fill=False)
                    c2 = patches.Polygon(roi.polygon, color="green", fill=False)
                else:
                    continue
                if _ax1HasImage:
                    self.ax1.add_patch(c)
                    self.roiPatches[roi.uuid] = c
                if _ax2HasImage and (roi.frame is None or roi.frame == frame):
                    self.ax2.add_patch(c2)
                    self.roiPatches2[roi.uuid] = c2
                    
        self.tvSynapses._OnSelect(None)

    def InvalidateSelectedROI(self, synapse: ISynapse|None=None, roi: ISynapseROI|None=None):
        """ Called by self.tvSynapses when a item is selected. If root item is selected, synapse and roi are None. If a ISynapse is selected, roi is None """
        if synapse is not None and roi is None:
            roi_uuids = list(synapse.rois_dict.keys())
        elif synapse is not None and roi is not None:
            roi_uuids = [roi.uuid]
        else:
            roi_uuids = []
        for patch_name, patch in self.roiPatches.items():
            if patch_name in roi_uuids:
                patch.set_color("yellow")
            else:
                patch.set_color("red")
        for patch_name, patch in self.roiPatches2.items():
            if patch_name in roi_uuids:
                patch.set_color("yellow")
            else:
                patch.set_color("green")

        self.figure1.tight_layout()
        self.canvas1.draw()    
        
    def Detect(self, waitCompletion:bool=False):
        imgObj = self._gui.ImageObject
        if self.detectionAlgorithm is None or imgObj is None or imgObj.img is None or imgObj.imgDiff is None:
            self._gui.root.bell()
            return

        def _Detect(job: Job, frames: list[int]):
            self.tvSynapses.ClearSynapses('non_staged')
            self.tvSynapses.SyncSynapses()
            rois: list[ISynapseROI] = []
            for i, p in enumerate(peaks):
                job.SetProgress(i, f"Detecting ROIs in frame {p}")
                rois.extend([r.SetFrame(p) for r in self.detectionAlgorithm.DetectAutoParams(imgObj.imgDiff_FrameProps(p))])
            synapses = SimpleCustering.Cluster(rois)
            self._synapses = {s.uuid: s for s in synapses}
            self.tvSynapses.SyncSynapses()
            job.SetStopped("Detecting ROIs")
            self.Invalidate_ROIs()

        peaks = self._gui.signal.peaks
        if peaks is None or len(peaks) == 0:
            messagebox.showwarning("Neurotorch", "You must first get at least one signal frame in the Signal Finder Tab before you can detect Multiframe Synapses")
            return
        job = Job(steps=len(peaks))
        self._gui.statusbar.AddJob(job)
        _thread = threading.Thread(target=_Detect, args=(job,peaks), daemon=True)
        _thread.start()
        if waitCompletion:
            _thread.join()

    # Helper function

    def GetCurrentDetectionSource(self) -> ImageProperties|None:
        imgObj = self._gui.ImageObject
        if imgObj is None or imgObj.img is None or imgObj.imgDiff is None:
            return None
        return imgObj.imgDiffView(ImgObj.SPATIAL).MaxProps
    
    def SliderFrameChanged(self):
        frame = self.sliderFrame.Get() - 1
        if self._gui.signal.peaks is not None and len(peaks_index := (np.where(np.array(self._gui.signal.peaks) == frame)[0])) == 1:
            peak = self._gui.signal.peaks[peaks_index[0]]
            self.sliderPeak.Set(peaks_index[0] + 1)
            
        self.Invalidate_DiffImage()

    def SliderPeakChanged(self):
        peak = self.sliderPeak.Get() - 1
        if self._gui.signal.peaks is not None and len(self._gui.signal.peaks) > peak:
            self.sliderFrame.Set(self._gui.signal.peaks[peak] + 1)
        


    def ShowExternalPlot(self, name:str,  plotFunction):
        dialog_figure = plt.Figure(figsize=(20,10), dpi=100)
        if plotFunction(dialog_figure) != True:
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.wm_title(f"Neurotorch: {name}")

        dialog_canvas = FigureCanvasTkAgg(dialog_figure, dialog)
        dialog_canvtoolbar = NavigationToolbar2Tk(dialog_canvas, dialog)
        dialog_canvtoolbar.update()
        dialog_canvas.get_tk_widget().pack(expand=True, fill="both", side=tk.LEFT)
        dialog_canvas.draw()

    def Plot3DMultiframe(self, figure):
        ax = figure.add_subplot(111, projection="3d")  

        if self._gui.ImageObject is None or self._gui.ImageObject.img is None or len(self.ax2.get_images()) == 0:
            messagebox.showerror("Neurotorch", f"You first need to load an image to plot the 3D Multifram synapse plot")
            return False

        img = np.full(shape=self.ax2.get_images()[0].get_size(), fill_value=0.0)
        mesh_X, mesh_Y = np.mgrid[0:img.shape[0], 0:img.shape[1]]
        pos = np.dstack((mesh_X, mesh_Y))
        for synapse in self.synapses:
            for roi in synapse.rois:
                if roi.location is None: continue
                if isinstance(roi, CircularSynapseROI):
                    cov = roi.radius
                else:
                    cov = roi.regionProps.equivalent_diameter_area/2 if roi.regionProps is not None else 6
                img += multivariate_normal.pdf(x=pos, mean=roi.location, cov=cov)

        #overlay_img_props = self._gui.ImageObject.imgView(ImgObj.SPATIAL).MeanProps
        #norm = cm_colors.Normalize(vmin=overlay_img_props.min, vmax=overlay_img_props.max)
        #cmap = cm.get_cmap("Greys_r")
        #img_plot = ax.plot_surface(mesh_X, mesh_Y, img, rcount=100, ccount=100, facecolors = cmap(norm(overlay_img_props.img)))
        img_plot = ax.plot_surface(mesh_X, mesh_Y, img, rcount=150, ccount=150,  cmap="inferno")
        figure.colorbar(img_plot, ax=ax)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("Surface plot of detected synapses per signal frame merged to a single image by multiplying each ROI location\nwith a normal probability distribution with covariance set to radius (or equivalent radius for non circular ROIs)")
        return True
    
    def Canvas1ClickEvent(self, event):
        if not event.dblclick or event.inaxes is None:
            return
        x, y = event.xdata, event.ydata
        if event.inaxes == self.ax1:
            rois = [r for s in self.synapses for r in s.rois]
        elif event.inaxes == self.ax2:
            rois = [r for s in self.synapses for r in s.rois if r.uuid in self.roiPatches2.keys()]
        else:
            return
        if len(rois) == 0: return
        rois.sort(key=lambda r: (r.location[0]-x)**2+(r.location[1]-y)**2 if r.location is not None else np.inf)
        roi = rois[0]
        d = ((roi.location[0]-x)**2+(roi.location[1]-y)**2)**0.5 if roi.location is not None else np.inf
        if d <= 40:
            self.tvSynapses.selection_set(roi.uuid)

    def _Canvas1Resize(self, event):
        if self.tab.winfo_width() > 300:
            self.figure1.tight_layout()
            self.canvas1.draw()