from tkinter import *

base_buttons = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['0', '.', '=', '/'],
    ['AC', 'C', '+/-', '%']
]

scientific_buttons = [
    ['7', '8', '9', '+', '(', ')'],
    ['4', '5', '6', '-', 'x^2', 'x^2'],
    ['1', '2', '3', '*', 'x^y', '2^x'],
    ['0', '.', '=', '/', 'x!', 'e'],
    ['AC', 'C', '+/-', '%', '1/x', 'pi']
]

show_str = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '+', '-', '/', '*', '(', ')']


def center_window(root, w, h):
    """
    This function can center the window on the screen
    :param root:
    :param w: width of widget
    :param h: height of widget
    :return:
    """
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


class Calculator:

    def __init__(self, root):

        self.root = root

        self.root.title("My Calculator")
        self.root.resizable(0, 0)
        self.entry = Entry(self.root, justify="right")

        # initialization string equation to do eval()
        self.equation = ''

        # This Boolean value determines whether to clear the Entry
        self.newline = False

        # Menu
        self.menus()
        # Center the window on the screen
        # center_window(self.root, 200, 300)
        self.base_layout()

    def base_layout(self):
        self.entry.grid(row=0, column=0, columnspan=4, sticky=N + W + S + E, padx=3, pady=3)

        buttons = []

        # Create Buttons
        for i in range(5):
            for j in range(4):
                value = base_buttons[i][j]
                button = self.creatButton(value)
                buttons.append(button)

        # Put buttons in Tk widget
        count = 0
        for row in range(1, 6):  # row 0 is used for Entry
            for col in range(4):
                buttons[count].grid(row=row, column=col)
                count += 1

    def scientific_layout(self):
        self.entry.grid(row=0, column=0, columnspan=6, sticky=N + W + S + E, padx=3, pady=3)

        buttons = []

        # Create Buttons
        for i in range(5):
            for j in range(6):
                value = scientific_buttons[i][j]
                button = self.creatButton(value)
                buttons.append(button)

        # Put buttons in Tk widget
        count = 0
        for row in range(1, 6):  # row 0 is used for Entry
            for col in range(6):
                buttons[count].grid(row=row, column=col)
                count += 1

    def creatButton(self, value, show=True, width=3):
        """

        :param value:
        :param show:
        :param width:
        :return:
        """
        if value not in show_str:
            show = False

        return Button(
            self.root,
            text=value,
            command=lambda: self.click(value, show),
            width=width)

    def click(self, val, show):
        if not self.newline:
            if not show:
                if val == '=' and self.equation:
                    self.calculate()
                elif val == "AC":
                    self.clear_all()
                elif val == "C":
                    self.clear_last()
                elif val == "+/-" and self.equation:
                    self.pos_or_neg()


            else:

                self.input_entry(val)
        else:
            self.clear_all()
            if show:
                self.input_entry(val)

    def input_entry(self, value, newline=False):
        self.entry.insert(END, value)
        self.equation += str(value)
        self.newline = newline

    def calculate(self):
        """
        input = self.entry.get()
        output = str(eval(input.strip()))
        self.clear()
        self.entry.insert(END, output)
        """
        try:
            result = str(eval(self.equation))

            self.clear_all()
            # show result in Entry and make newline True
            self.input_entry(result, newline=True)

        except:
            self.clear_all()
            self.entry.insert(END, 'Error, click AC to restart')

    def pos_or_neg(self):
        pass

    def clear(self):
        self.entry.delete(0, END)

    def clear_all(self):
        self.equation = ''
        self.refresh()

    def clear_last(self):
        self.equation = self.equation[:-1]
        self.refresh()

    def refresh(self):
        self.entry.delete(0, END)
        self.entry.insert(END, self.equation)

    def menus(self):
        """
        This function defines the calculator's drop-down menu
        :return:
        """
        main_menu = Menu(self.root)
        type_menu = Menu(main_menu, tearoff=0)
        type_menu.add_command(label="Base", command=lambda: self.base_layout())
        type_menu.add_command(label="Scientific", command=lambda: self.scientific_layout())
        help_menu = Menu(main_menu, tearoff=1)
        help_menu.add_command(label="Operation")
        main_menu.add_cascade(label="Type", menu=type_menu)
        main_menu.add_cascade(label="Help", menu=help_menu)
        self.root.config(menu=main_menu)


if __name__ == '__main__':
    root = Tk()
    myCal = Calculator(root)

    root.mainloop()
