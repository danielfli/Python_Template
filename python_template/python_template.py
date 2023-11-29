"""
This module contains examples of Python code.
# MVC Example see https://nazmul-ahsan.medium.com/how-to-organize-multi-frame-tkinter-application-with-mvc-pattern-79247efbb02b
"""

from gui.models.main_m import Model
# from gui.views.main_v import View
# from gui.controllers.main_c import Controller

from gui.models.license.timestamp import Timestamp

def main():
    model = Model()

    tp_now = Timestamp()

    print("current time: ", tp_now.get_current_time)

    try:
        model.db.load()
        print("secet data: ", model.db.get_data())
        s_array = model.db.get_data()
        a_arr_ts = s_array[1]
        if tp_now.get_timestamp > a_arr_ts:
            print("license expired! valid until: ", tp_now.return_timestamp(a_arr_ts))
        else:
            print("license valid until: ", tp_now.return_timestamp(a_arr_ts))

    except Exception as e:
        print(e)




    print("done")



    # view = View()
    # controller = Controller(model, view)
    # controller.start()


if __name__ == "__main__":
    main()
