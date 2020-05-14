from tkinter import *
import tkinter.font as tkfont
from tkinter import messagebox
import random
from table import Mousewheel_Support,Scrolling_Area,Cell,Table

class Main(object):

	def __init__(self):

		# def resource_path(relative_path):
		# #Get absolute path to resource, works for dev and for PyInstaller
		# 	try:
		# # PyInstaller creates a temp folder and stores path in _MEIPASS
		# 		base_path = sys._MEIPASS
		# 	except Exception:
		# 		base_path = os.path.abspath(".")
		# 	return os.path.join(base_path, relative_path)

		# icon = resource_path("Calendar.ico")
		self.window = Tk()
		# self.window.iconbitmap(icon)
		self.window.title("LuckyDraw") #視窗名稱
		self.window.config(background = "#f0f0f0")#更該視窗背景顏色
		self.window.geometry("530x410+800+250") #視窗解析度 (x*y+視窗欲固定的畫面位置X+視窗欲固定的畫面位置Y)
		self.window.resizable(0,0) #不可以更改大⼩
		Font = tkfont.Font(family = "新細明體", size = 10, weight = "bold")
		Font_path = tkfont.Font(family = "新細明體", size = 10)
		path = StringVar() #輸入路徑Entry用的變數
		size = StringVar() #Radiobutton所使用的共同變數，以了解目前使用者選擇哪個按鈕並輸出相對應字串值

		def add_Name():
			if inputName.get() == "":
				messagebox.showerror(title = "Error", message = "請確實輸入抽獎者名字！！")
			else:
				Namelist.insert(END,inputName.get())
				inputName.delete(0, END)

		def add_Prize():
			if inputPrizeName.get() == "" or inputPrizeNumber.get() == "" or inputPrizeNumber.get() == "0":
				messagebox.showerror(title = "Error", message = "請確實輸入獎品和數量！！")
			else:
				try:
					d1 = int(inputPrizeNumber.get())
				except ValueError:
					messagebox.showerror("Error","請確實輸入獎品數量！！")
					inputPrizeNumber.delete(0, END)
				else:
					NowPrizenumber = len(prizetable.get_data())
					prizetable.insert_row([NowPrizenumber + 1, inputPrizeName.get(), inputPrizeNumber.get()])
					inputPrizeName.delete(0, END)
					inputPrizeNumber.delete(0, END)

		def Draw():
			try: #利用將輸入字串轉換成數字int型式判斷是否輸入為數字
				d2 = int(outputPrize.get())
			except ValueError:
				messagebox.showerror("Error","請輸入欲抽出獎品編號！！")
				outputPrize.delete(0, END)
			else:
				if len(Namelist.get(0,END)) == 0:
					messagebox.showerror(title = "Error", message = "請確實輸入抽獎者名字！！")
				elif int(outputPrize.get()) > len(prizetable.get_data()):
					messagebox.showerror(title = "Error", message = "請確認是否有輸入此編號獎品！！")
					outputPrize.delete(0, END)
				else:
					prize = prizetable.get_data() #得出的值為 [["","",""],["","",""]....]
					NameList = Namelist.get(0,END)
					if int(prize[int(outputPrize.get()) - 1][2]) == 0:
						messagebox.showerror(title = "Error", message = "此項獎品已經抽完了！！")
					else:
						prizetable.cell(int(outputPrize.get()) - 1, 2, int(prize[int(outputPrize.get()) - 1][2]) - 1) #改變Table幾之幾的參數
						getPrizeName = random.choice(NameList)
						Namelist.delete(NameList.index(getPrizeName))
						prizelist.insert(END,"恭喜！！" + getPrizeName + " 獲得：" + prize[int(outputPrize.get()) - 1][1])



		inputframe = Frame(self.window)
		inputframe.grid(row = 0, padx = 10, pady = 10)

		inputNametitle = Label(inputframe, font = Font, text = "請輸入抽獎者名單：")
		inputNametitle.grid(row = 0, padx = 5, pady = 10)

		inputName = Entry(inputframe, font = Font_path, width = 20)
		inputName.grid(row = 0, column = 1, pady = 10)

		addName = Button(inputframe, text = "添加++", font = Font, bg = "skyblue", width = 8, height = 1, command = add_Name)
		addName.grid(row = 1, column = 1, sticky = E, padx = 5, pady = 5)

		inputPrizeNametitle = Label(inputframe, font = Font, text = "請輸入獎品名單：")
		inputPrizeNametitle.grid(row = 2, column = 0, sticky = E, padx = 5, pady = 10)

		inputPrizeName = Entry(inputframe, font = Font_path, width = 20)
		inputPrizeName.grid(row = 2, column = 1, pady = 10)

		inputPrizeNumbertitle = Label(inputframe, font = Font, text = "獎項數量：")
		inputPrizeNumbertitle.grid(row = 3, column = 0, sticky = E, padx = 5, pady = 10)

		inputPrizeNumber = Entry(inputframe, font = Font_path, width = 20)
		inputPrizeNumber.grid(row = 3, column = 1, pady = 10)

		addPrize = Button(inputframe, text = "添加++", font = Font, bg = "skyblue", width = 8, height = 1, command = add_Prize)
		addPrize.grid(row = 4, column = 1, sticky = E, padx = 5, pady = 5)



		outputframe = Frame(self.window)
		outputframe.grid(row = 1, column = 0, sticky = E, padx = 10, pady = 10)

		outputPrizetitle = Label(outputframe, font = Font, text = "請輸入抽出獎項編號")
		outputPrizetitle.grid(row = 0, column = 0, padx = 5, pady = 10)

		outputPrize = Entry(outputframe, font = Font_path, width = 20)
		outputPrize.grid(row = 1, column = 0, pady = 10)

		lottery = Button(outputframe, text = "抽獎", font = Font, bg = "skyblue", width = 8, height = 3, command = Draw)
		lottery.grid(row = 0, rowspan = 2, column = 1, padx = 5, pady = 5)




		listframe = Frame(self.window)
		listframe.grid(row = 0, column = 1, padx = 10, pady = 10)

		slb = Scrollbar(listframe) #垂直滾動條元件 
		slb.pack(side = RIGHT, fill = Y) #設定垂直滾動條顯示的位置 
		Namelist = Listbox(listframe, height = 10, width = 30, font = Font_path, exportselection = False, borderwidth = 3, selectmode = "single",bg= "#b5e1f3", yscrollcommand = slb.set)
		Namelist.pack(side = LEFT, fill = BOTH)
		slb.config(command = Namelist.yview) #設定Scrollbar元件的command選項為該元件的yview()方法


		prizetable = Table(self.window, ["編號", "獎品", "數量"], height=70)
		prizetable.grid(row = 1, column = 1, padx = 10, pady = 10)



		prizelistframe = Frame(self.window)
		prizelistframe.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 10)

		slb1 = Scrollbar(prizelistframe) #垂直滾動條元件 
		slb1.pack(side = RIGHT, fill = Y) #設定垂直滾動條顯示的位置 
		prizelist = Listbox(prizelistframe, height = 3, width = 80, font = Font_path, exportselection = False, borderwidth = 3, selectmode = "single",bg= "#b5e1f3", yscrollcommand = slb1.set)
		prizelist.pack(side = LEFT, fill = BOTH)
		slb1.config(command = prizelist.yview) #設定Scrollbar元件的command選項為該元件的yview()方法

		self.window.update()

		self.window.mainloop()

if __name__ == '__main__':
	Main()
