from tkinter import *

class Calculator:
    def create_function_buttons(self, frame):
        _width, _height = frame["width"], frame["height"]
        _button_size = (int(_width*0.02), int(_height*0.03))
        _buttons = {
                "Agregar uno": (0, 0, 0, 0),
                "Agregar cinco": (0, 1, 0, 0),
                "Restar uno": (0, 2, 0, 0),
                "Eliminar": (0, 3, 0, 0)
        }
        _callback = {
            "Agregar uno": lambda: self.add_n_item(1),
            "Agregar cinco": lambda: self.add_n_item(5),
            "Restar uno": lambda:self.minus_one_item(),
            "Eliminar": lambda: self.delete_item(),
        }

        _fonts = {
            "bg": "white",
            "fg": "black",
            "bd": 3,
            "font": ('Adobe 黑体 Std R', int(_width/37), 'normal')
        }
        self.grid_buttons(frame, _button_size, _buttons, _fonts, _callback)

    def create_calculator(self, frame):
        _width, _height = frame["width"], frame["height"]
        _button_size = (int(_width*0.027), int(_height*0.008))

        _buttons = {
            "7" : (0, 0, 0, 0),
            "8" : (0, 1, 0, 0),
            "9" : (0, 2, 0, 0),
            
            "4" : (1, 0, 0, 0),
            "5" : (1, 1, 0, 0),
            "6" : (1, 2, 0, 0),

            "1" : (2, 0, 0, 0),
            "2" : (2, 1, 0, 0),
            "3" : (2, 2, 0, 0),

            "00" : (3, 0, 0, 0),
            "0" : (3, 1, 0, 0),
            "Limpiar": (3, 2, 0, 0)
        }
        _fonts = {
            "bg": "white",
            "fg": "black",
            "bd": 3,
            "font": ('Adobe 黑体 Std R', int(_width/37), 'normal')
        }

        _call_back = {
            "7" : lambda: self.press_number("7"),
            "8" : lambda: self.press_number("8"),
            "9" : lambda: self.press_number("9"),

            "4" : lambda: self.press_number("4"),
            "5" : lambda: self.press_number("5"),
            "6" : lambda: self.press_number("6"),

            "1" : lambda: self.press_number("1"),
            "2" : lambda: self.press_number("2"),
            "3" : lambda: self.press_number("3"),

            "00" : lambda: self.press_number("00"),
            "0" : lambda: self.press_number("0"),
            "Limpiar": lambda: self.press_clear("0")
        }

        self.grid_buttons(frame, _button_size, _buttons, _fonts, _call_back)
class Cashier:
    def create_vaiables(self):
        self.unit = StringVar()
        self.total = StringVar()
        self.cash_input = StringVar()
        self.change = StringVar()

        self.unit.set("0")
        self.total.set("0")
        self.cash_input.set("0")
        self.change.set("0")
        
        # for treeview selection
        self.receipt = dict()

        # for selcet category
        self.radio_var = IntVar()
        self.radio_var.set(0)

    def create_casher(self, frame, frame_size):
        self.casher_frame = frame
        self.casher_width, self.casher_height = frame_size[0], frame_size[1]
        self._create_checkout_info()
        self._create_checkout_buttons()

    def _create_checkout_info(self):
        labels = {
            "Cantidad: ": (0, self.casher_height*0.02),
            "Total: ": (0, self.casher_height*0.14),

            "Efectivo: ": (0, self.casher_height*0.30),
            "Cambio: ": (0, self.casher_height*0.42),
        }
        _label_size = (self.casher_width*0.015, self.casher_height*0.003)
        self.create_labels(self.casher_frame, _label_size, labels)

        _split_line = {
            " "*5 + "—"*13:  (0, self.casher_height*0.22)
        }
        _line_size = (self.casher_width*0.04, self.casher_height*0.001)
        self.create_labels(self.casher_frame, _line_size, _split_line)

        _position_x = self.casher_width*0.23
        var_dict = {
            "unit": (_position_x, self.casher_height*0.022),
            "total": (_position_x, self.casher_height*0.142),

            "cash_input": (_position_x, self.casher_height*0.3),
            "change": (_position_x, self.casher_height*0.422),
        }
        var_size = (self.casher_width*0.025, self.casher_height*0.003)
        self.create_variables(self.casher_frame, var_size, var_dict)

    def _create_checkout_buttons(self):
        _grid_x0, _grid_y0 = self.casher_width*0.03, self.casher_height*0.53
        _grid_x1, _grid_y1 = self.casher_width*0.36, self.casher_height*0.71

        _buttons = {
            "Descuento": (_grid_x0, _grid_y0),
            "Tarjeta de Crédito": (_grid_x1, _grid_y0),
            "Subtotal": (_grid_x0, _grid_y1),
            "Pagar": (_grid_x1, _grid_y1),
        }
        _button_size = (self.casher_width*0.017, self.casher_height*0.004)
        _fonts = {
            "bg": "white",
            "fg": "black",
            "bd": 5
        }
        self.place_buttons(self.casher_frame, _button_size, _buttons, _fonts, \
            call_back=self.change_button_color)

class Merchandise:
    def create_category(self, frame):
        _width, _height = frame["width"], frame["height"]
        _button_size = (int(_width*0.03), int(_height*0.004))
        _pos_x, _pos_y = _button_size[0]*5, _button_size[1]*18

        _buttons = {
                _category: (_pos_x + _button_size[0], _pos_y + _button_size[1]*i*70)
                for i, _category in enumerate(self.items.keys())
            }
        _call_back = {
            _category: self.change_category for _category in self.items.keys()
        }
        _fonts = {
            "bg": "white",
            "fg": "black",
            "bd": 10
        }
        self.create_radio_buttons(frame, _button_size, _buttons, _fonts, _call_back)

    def _iter_items(self, item_list, pads, call_back_fcn, row_max=3):
        _output_dict = {}
        _x, _y = 0, 0
        for item in item_list:
            if _y > row_max:
                _x, _y = _x+1, 0
            _output_dict[item["name"]] = (_x, _y, pads[0], pads[1])
            _y += 1

        _lambda_fcns = [lambda i=i:call_back_fcn(i) for i in item_list]
        _call_back = dict(zip([i["name"] for i in item_list], _lambda_fcns))

        return _output_dict, _call_back


    def create_items(self, frame, selected_category):
        _width, _height = frame["width"], frame["height"]
        _padx, _pady = (int(_width*0.02), int(_height*0.02))
        _button_size = (int(_width*0.01), int(_height*0.007))

        _buttons, _call_back = self._iter_items(self.items[selected_category], \
            (_padx, _pady), self.press_item)

        _fonts = {
            "bg": "white",
            "fg": "black",
            "bd": 1
        }
        self.item_buttons = self.grid_buttons(frame, _button_size, _buttons, _fonts, _call_back)

    def create_options(self, frame, selected_category):
        _width, _height = frame["width"], frame["height"]
        _padx, _pady = (int(_width*0.02), int(_height*0.02))
        _button_size = (int(_width*0.02), int(_height*0.005))

        _buttons, _call_back = self._iter_items(self.options[selected_category], \
            (_padx, _pady), self.press_option, row_max=1)

        _fonts = {
            "bg": "white",
            "fg": "black",
            "bd": 1
        }
        self.option_buttons = self.grid_buttons(frame, _button_size, _buttons, _fonts, _call_back)

class Receipt:
    def create_receipt(self, frame):
        _width, _height = frame["width"], frame["height"]
        tree_size = (int(_width*0.1), int(_height*0.043))
        frame.pack_propagate(False)

        tree_dict = {
            'No': (tree_size[0], "No"),
            'Name': (int(tree_size[0]*6.5), "Nombre"),
            'Unit': (tree_size[0], "Cantidad"),
            'Amount': (tree_size[0], "Monto")
        }

        _font = ('Adobe 黑体 Std R', 20, 'normal')
        self.receipt_frame = self.create_treeview(frame, tree_size, tree_dict, _font)
        