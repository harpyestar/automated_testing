
from tkinter import *
import random
import string
from datetime import datetime


# ====== 界面初始化 ======
root = Tk()
root.title("Python打字练习")
root.geometry("600x500")
Label(root, text='系统题目：').grid(row=0)
Label(root, text='用户作答：').grid(row=1)
Label(root, text='考试结果：').grid(row=2)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

v1.set("点击'开始测试'按钮开始做题")

e1 = Entry(root, text=v1, state='disabled', width=40, font=('宋体', 14))
e2 = Entry(root, textvariable=v2, width=40, font=('宋体', 14))
e3 = Label(root, textvariable=v3, width=40, font=('宋体', 14), foreground='red') # 前景色红色
e1.grid(row=0, column=1, padx=10, pady=20)
e2.grid(row=1, column=1, padx=10, pady=20)
e3.grid(row=2, column=1, padx=10, pady=20)

text = Text(root, width=80, height=7)
text.grid(row=4, column=0, columnspan=2, pady=5) # 元素横跨的列数

# ======== 打字类 =========
class TypingTest:
    def __init__(self):
        self.time_list = []
        self.letterNum = 20
        self.letterStr = "".join(
            random.sample(string.printable.split(" ")[0], self.letterNum)
        )
        self.examination_paper = ""

    def time_calc(self):
        self.time_list.append(datetime.now())
        yield


    def create_exam(self):
        text.delete(0.0, END)
        v1.set(self.letterStr)
        self.time_calc().__next__()
        text.insert(END, "开始：%s \n" % str(self.time_list[-1]))
        # todo - #占位符、# args、# 断点debug
        user_only1.config(state="active")


    def score(self):
        wrong_index = []
        self.time_calc().__next__()
        text.insert(END, "结束：%s \n" % str(self.time_list[-1]))
        use_time = (self.time_list[-1] - self.time_list[-2]).seconds
        self.examination_paper = v2.get()

        if len(self.examination_paper) > self.letterNum:
            v3.set("输入数据有误，作答数大于考题数")
        else:
            right_num = 0
            for z in range(len(self.examination_paper)):
                if self.examination_paper[z] == self.letterStr[z]:
                    right_num += 1
                else:
                    wrong_index.append(z)

            if right_num == self.letterNum:
                v3.set("完全正确，正确率%.2f%%用时：%s秒" % ((right_num*1.0)/self.letterNum*100, use_time))
            else:
                v3.set("正确率%.2f%%用时：%s秒" % ((right_num * 1.0) / self.letterNum * 100, use_time))
                text.insert(END, "题目：%s\n" % self.letterStr)
                tag_info = list(map(lambda x:'4.'+str(x+3), wrong_index))
                text.insert(END, "作答：%s\n" % self.examination_paper)

                for i in range(len(tag_info)):
                    text.tag_add("tag1", tag_info[i])
                    text.tag_config("tag1", background="red")
                    user_only1.config(state="disabled")


TypingTest1 = TypingTest()

Button(root, text="开始测试", width=10, command=TypingTest1.create_exam).grid(row=3, column=0, sticky=W, padx=30, pady=5)
user_only1 = Button(root, text="交卷", width=10, command=TypingTest1.score, state="disabled")
user_only1.grid(row=3, column=1, sticky=E, padx=30, pady=5)


mainloop()



# if __name__ == '__main__':
#     # 该结构以下代码只在本py文件生效
#     print(string.printable.split(" "))


