## Scientia - latin word for knowledge

from UIHandler import UIHandler

#C:\Users\tromb\Downloads\Dataset (1)\Dataset\

def set_user_settings(user_settings):
    user_settings['UI'] = True
    user_settings['Time'] = 'UTC'

if __name__ == '__main__':
    user_settings = dict()
    set_user_settings(user_settings)
    app = UIHandler()
    app.mainloop()

