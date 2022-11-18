# This is a sample Python script.

from UIHandler import UIHandler

#"C:\Users\tromb\Downloads\Dataset (1)\Dataset\20200121\312\summary.csv"

def set_user_settings(user_settings):
    user_settings['UI'] = True

if __name__ == '__main__':
    user_settings = dict()
    set_user_settings(user_settings)
    app = UIHandler()
    app.mainloop()
    print('finished running successfully')

