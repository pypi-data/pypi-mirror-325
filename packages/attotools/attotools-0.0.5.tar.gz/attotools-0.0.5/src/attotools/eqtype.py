import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class EquaType:
    def __init__(self):
         # Create a windowpip install Pillow
        self.window = tk.Tk()
        self.window.tk.call('tk', 'scaling', 1) 
        self.window.option_add("*Font", "Helvetica 50")
        self.window.title("Equation editor")
        # Maximize window
        #self.window.wm_state('zoomed')
             
        # Get the image dimensions
        self.FrameWidth = 800
        self.GUI_Layout()

        # 导入宏包
        plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
        self.window.update()

    def getEqPos(self):
        xx = self.eq.get_window_extent(self.eq.figure.canvas.get_renderer()).get_points()
        x = xx[0,0]
        y = xx[0,1]
        width = xx[1,0] - xx[0,0]
        height = xx[1,1] - xx[0,1]
        return (x,y,width,height)

    def UpdateEq(self):

        tex = self.TexText.get("1.0", tk.END)
        tex = tex.rstrip()
        eqstr = r'\['+tex+r'\]'
        eqstr = eqstr.replace("\n", "")

        try:
            self.eq.set_text(eqstr)
            #self.eq.set_position((0.5,0.5))

            x,y,w,h = self.getEqPos()
            self.canvas.get_tk_widget().config(width=w+10,height=h+10)
            self.fig.canvas.draw_idle()
            self.window.update()
            self.TexText.config(background='white')
        except:
            self.TexText.config(background='red')

    def SaveEq(self):
        wf = tk.filedialog.asksaveasfile(mode='w', filetypes = (("data files", "*.pdf;*.svg;*.eps*.png") ,("all files", "*.*")))
        # asksaveasfile return `None` if dialog closed with "cancel".
        print(wf)
        if wf is None: 
            return
        else:
            self.fig.savefig(wf.name,transparent=True)


    def GUI_Layout(self):
        
        self.window.grid_rowconfigure(2, minsize=500)

        # add widgets
        self.UpdateCmd = tk.Button(self.window,text='Update',command=self.UpdateEq,relief='raised',height=2)
        self.UpdateCmd.grid(row=0,column=0,padx=10,pady=10,sticky='we')
        self.SaveCmd = tk.Button(self.window,text='Save',command=self.SaveEq,height=2)
        self.SaveCmd.grid(row=0,column=1,padx=10,pady=0,sticky='we')

        self.TexText = tk.Text(self.window,height=10)
        self.TexText.grid(row=1,column=0,columnspan=2,sticky='we',pady=5,padx=10)

        self.Frame1 = tk.Frame(self.window,height=100)
        self.Frame1.grid(row=2,column=0,columnspan=2,sticky='nswe',pady=1,padx=1)
        
        self.window.grid_rowconfigure(2, weight=1)
        #self.window.grid_columnconfigure(0, weight=1)
        r,g,b = self.Frame1.winfo_rgb(self.Frame1.cget('background'))
        # add fig
        self.fig = plt.figure(dpi=300,facecolor=(r/65536.0,g/65536.0,b/65536.0))
        # 在轴上添加一些数据
        self.eq = self.fig.text(0.5, 0.5, r'\[y=\sqrt{a^2+b^2+c^2}\]',usetex=True, fontsize=20,
            horizontalalignment='center',
            verticalalignment='center',)

        # 将图形嵌入到Tkinter窗口中
        self.canvas = FigureCanvasTkAgg(self.fig,master=self.Frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(relx=0.5,rely=0.5,anchor='c')

        # default data
        self.TexText.delete("1.0",tk.END)
        self.TexText.insert("1.0",r'y=\sqrt{a^2+b^2}')
        self.UpdateEq()
       

if __name__ == "__main__": 
  
    MainFrame =EquaType()
    # Run the window loop
    MainFrame.window.mainloop()