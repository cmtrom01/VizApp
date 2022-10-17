# This is a sample Python script.

import UIHandler as GUI

def launch_user_interface():
    GUI.launch_user_interface()

def set_user_settings(user_settings):
    user_settings['UI'] = True

if __name__ == '__main__':
    user_settings = dict()
    set_user_settings(user_settings)
    launch_user_interface()
    print('finished running successfully')

