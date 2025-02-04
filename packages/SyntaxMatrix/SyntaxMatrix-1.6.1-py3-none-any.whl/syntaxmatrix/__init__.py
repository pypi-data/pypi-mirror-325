from .synta_mui import SyntaxMUI

_app_instance = SyntaxMUI()

# Expose public functions
run = _app_instance.run
text_input = _app_instance.text_input
button = _app_instance.button
set_widget_position = _app_instance.set_widget_position
get_text_input_value = _app_instance.get_text_input_value
clear_text_input_value = _app_instance.clear_text_input_value
get_chat_history = _app_instance.get_chat_history
set_chat_history = _app_instance.set_chat_history
clear_chat_history = _app_instance.clear_chat_history
write = _app_instance.write
