import sys
sys.path.insert(0,'\\venv\\Lib\\site-packages')
import PySimpleGUI as sg
import DB.DB as db

def GUI():
    headers, vals = db.get("KeToan")
    table_columns = [
            [sg.Table(values = vals,headings=headers,
            num_rows=len(vals),
            key='-TABLE-',
            auto_size_columns=True,
            justification="center",
            max_col_width= 100,
            row_height = 27)],
            [sg.Button("Encrypt",key="-Encrypt-"), sg.Button("Decrypt",key="-Decrypt-"),\
                 sg.In(size=(20,3),key="-pw-",\
                    password_char="?")]
    ]
    add_column = [
        [
            sg.Text("Họ"),
            sg.In(size=(25,2), enable_events=True, key="-Ho-")
        ],
        [
            sg.Text("Tên"),
            sg.In(size=(25,2), enable_events=True, key="-Ten-")
        ],
        [
            sg.Text("Địa chỉ"),
            sg.In(size=(25,2), enable_events=True, key="-Diachi-")
        ],
        [
            sg.Text("SĐT"),
            sg.In(size=(25,2), enable_events=True, key="-SDT-")
        ],
        [
            sg.Text("CMT"),
            sg.In(size=(25,2), enable_events=True, key="-CMT-")
        ],
        [
            sg.Button("Add",key="-Add")
        ]
    ]
    layout = [
        [sg.Column(table_columns),
        sg.VSeparator(),
        sg.Column(add_column)
        ]
    ]

    window = sg.Window("Mã hoá Database",layout,resizable=True)

    while True:
        event,value = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "-Decrypt-":
            try:
                # print(window["-pw-"].get())
                headers, vals = db.get_Decrypt("KeToan",window["-pw-"].get())
                window["-TABLE-"].update(values = vals)
            except Exception as e:
                sg.popup_error_with_traceback(f'Wrong PassWord')

        if event == "-Encrypt-":
            headers, vals = db.get("KeToan")
            window["-TABLE-"].update(values = vals)
        
        if event =="-Add":
            db.add(window["-Ho-"].get(),window["-Ten-"].get(),window["-Diachi-"].get(),\
                window["-SDT-"].get(),window["-CMT-"].get())
            headers, vals = db.get("KeToan")
            window["-TABLE-"].update(values=vals, num_rows=len(vals))
            window["-Ho-"].update("")
            window["-Ten-"].update("")
            window["-Diachi-"].update("")
            window["-SDT-"].update("")
            window["-CMT-"].update("")

    window.close()


