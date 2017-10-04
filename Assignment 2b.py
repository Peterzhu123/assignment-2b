# Created by: Peter Zhu
# Created on: 29-Sep-17
# Created for: ICS3U

import ui

def calculate_button_touch_up_inside(sender):

  # constants
    g = 9.81
    
    # input
    second = int(view['second_textbox'].text)
    
    # process
    height = 100.0 - ((0.5) * g * second ** 2)
    
    # output
    view['answer_label'].text = 'The Height is : ' + str(height) 

view = ui.load_view()
view.present('full_screen')
