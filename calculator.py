
from tkinter import  *
if __name__ == '__main__':

    main_window = Tk()

    Label(main_window, text = "Calculator").grid(row=0 ,column=0 )


    value=Entry(main_window ,width = 60 , borderwidth =5)
    value.grid(row=1,column=0 ,columnspan=3)
    value.insert(0,"")

    def on_click(number):
        s=value.get()
        value.delete(0, END)
        value.insert(0,str(s)+str(number))
    def clear() :
        value.delete(0, END)
    def evaluate(e):
        try:
            sum=0
            a=[]

            for c in e:
                if c>="0" and c<="9":
                    sum*=10
                    sum+=int(c)
                else:
                    a.append(sum)
                    sum=0
                    a.append(c)
            a.append(sum)
            b=[]
            i=0
            while i<len(a):
                if a[i]=='*':
                    val=b.pop()
                    i+=1
                    b.append(val*a[i])
                elif a[i]=='/':
                    val = b.pop()
                    i+=1
                    b.append(val / a[i])
                else :
                    b.append(a[i])
                i+=1

            ans=b[0]
            i=1
            while i<len(b) :

                if b[i]=='+':
                    i+=1
                    ans+=b[i]
                elif b[i]=='-' :
                    i+=1
                    ans-=b[i]
                i+=1
            return ans
        except Exception as e:
            print(e)
    def equal() :
        s = value.get()
        value.delete(0, END)
        num=evaluate(str(s))
        value.insert(0, str(num))

    btn1=Button(main_window, text="1" , width = 15 ,command =lambda :on_click(1)).grid(row=2, column=0)
    btn2 = Button(main_window, text="2", width = 15 ,command=lambda :on_click(2)).grid(row=2, column=1)
    btn3 = Button(main_window, text="3", width = 15 ,command=lambda :on_click(3)).grid(row=2, column=2)
    btn4 = Button(main_window, text="4",width = 15 , command=lambda :on_click(4)).grid(row=3, column=0)
    btn5 = Button(main_window, text="5",width = 15 , command=lambda :on_click(5)).grid(row=3, column=1)
    btn6 = Button(main_window, text="6",width = 15 , command=lambda :on_click(6)).grid(row=3, column=2)
    btn7 = Button(main_window, text="7", width = 15 ,command=lambda :on_click(7)).grid(row=4, column=0)
    btn8= Button(main_window, text="8",width = 15 , command=lambda :on_click(8)).grid(row=4, column=1)
    btn9 = Button(main_window, text="9",width = 15 , command=lambda :on_click(9)).grid(row=4, column=2)
    btn0 = Button(main_window, text="0", width = 15 ,command=lambda :on_click(0)).grid(row=5, column=0)
    add_btn = Button(main_window, text="+", width=15, command=lambda :on_click('+')).grid(row=5, column=1)
    mul_btn = Button(main_window, text="*", width=15, command=lambda :on_click('*')).grid(row=5, column=2)
    sub_btn = Button(main_window, text="-", width=15, command=lambda :on_click('-')).grid(row=6, column=0)
    div_btn = Button(main_window, text="/", width=15, command=lambda :on_click('/')).grid(row=6, column=1)
    equal_btn = Button(main_window, text="=", width=50, command=lambda :equal()).grid(row=7, column=0,columnspan=3)
    clear_btn = Button(main_window, text="CLEAR", width=15, command=lambda :clear()).grid(row=6, column=2)
    main_window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
