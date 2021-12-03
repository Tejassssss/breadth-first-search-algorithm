from tkinter import ttk
from tkinter import *
import build_path, shortest_path
global path_mode
global point_dict
global point_letter
global connection_dict
path_mode = False
point_dict = []
connection_dict = []
point_letter = 65
window = Tk()
start_point = StringVar(window)
end_point = StringVar(window)

window.geometry("700x350")

def draw_line(event):
    global click_num
    global x1, y1, x2, y2
    global a1, b1
    global path_mode
    global point_dict
    global point_letter
    global first_point
    global current_letter
    if path_mode == True:
        if click_num == 0:
            x1 = event.x
            y1 = event.y
            for i in point_dict:
               if i and (i[1] >= x1-13 and i[1] <= x1+13) and (i[2] >= y1-13 and i[2] <= y1+13):
                x1,y1 = i[1],i[2]
                first_point = str(i[0])
                click_num = 1
                current_letter = i[0]
                break
        else:
            x2 = event.x
            y2 = event.y
            for i in point_dict:
                if i and (i[1] >= x2-13 and i[1] <= x2+13) and (i[2] >= y2-13 and i[2] <= y2+13):
                    x2,y2 = i[1],i[2]
                    if x1 != x2 and y1 != y2:
                        click_num = 0
                        if [first_point, str(i[0])] not in connection_dict and [str(i[0]), first_point] not in connection_dict:
                            canvas.create_line(x1,y1,x2,y2, fill="black", width=10)
                            connection_dict.append([first_point, str(i[0])])
                            redo_point(current_letter, i[0])
                    break
    elif path_mode == False:
        a1 = event.x
        b1 = event.y
        point_dict.append([chr(point_letter),a1,b1])
        point_letter = point_letter + 1
        canvas.create_oval(point_dict[point_letter-66][1]-13,point_dict[point_letter-66][2]-13,point_dict[point_letter-66][1]+13,point_dict[point_letter-66][2]+13,fill='black',width=10)
        canvas.create_oval(point_dict[point_letter-66][1]-10,point_dict[point_letter-66][2]-10,point_dict[point_letter-66][1]+10,point_dict[point_letter-66][2]+10,fill='white',width=0)
        canvas.create_text(a1, b1, fill='black',font='Calibre 16', text=point_dict[point_letter-66][0])
        print(point_dict[point_letter-66])

def make_point():
    global path_mode
    path_mode = False
    print("Point Mode")

def make_path():
    global path_mode
    path_mode = True
    print("Path Mode")

def run_graph():
    path_label.config(text = shortest_path.BFS_SP(build_path.build_graph(connection_dict), start_entry.get(), end_entry.get()))

def redo_point(symbol1, symbol2):
    global x1,y1,x2,y2,current_letter
    canvas.create_oval(x1-13,y1-13,x1+13,y1+13,fill='black',width=10)
    canvas.create_oval(x1-10,y1-10,x1+10,y1+10,fill='white',width=0)
    canvas.create_text(x1, y1, fill='black',font='Calibre 16', text = symbol1)
    canvas.create_oval(x2-13,y2-13,x2+13,y2+13,fill='black',width=10)
    canvas.create_oval(x2-10,y2-10,x2+10,y2+10,fill='white',width=0)
    canvas.create_text(x2, y2, fill='black',font='Calibre 16', text = symbol2)

canvas = Canvas(window, width=700, height=350, background="white")
canvas.grid(row=0,column=0)
canvas.bind('<Button-1>',draw_line)
click_num=0

point_button = Button(window, text='Make Point', command = make_point)
point_button.place(relx='0.4',rely='0.04')
path_button = Button(window, text='Add Path', command = make_path)
path_button.place(relx='0.5',rely='0.04')
start_entry = Entry(window, textvariable=start_point, font='Calibre 10', width=8)
start_entry.place(relx='0.4',rely='0.12')
end_entry = Entry(window, textvariable=end_point, font='Calibre 10', width=8)
end_entry.place(relx='0.5',rely='0.12')
run_button = Button(window, text='Run', command = run_graph, width=20)
run_button.place(relx='0.5', rely='0.18', anchor = 'n')
path_label  = Label(window, text = 'Shortest Path', font = 'Calibre 10', width = 50, bg='white')
path_label.place(relx='0.5', rely='0.25', anchor='n')

window.mainloop()