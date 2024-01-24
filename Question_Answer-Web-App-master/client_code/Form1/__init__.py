from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form Properties and Data Bindings.
    self.init_components(**properties)

  def question_text_pressed_enter(self, **event_args):
        # Your code for the pressed_enter event
        pass

    # Any code you write here will run before the form opens.

  def primary_color_1_click(self, **event_args):
      # Access the values from the app
      question_text=self.question_text.text
      input_text=self.input_text.text

      # call the Google Colab uplink method
      result=anvil.server.call('answer_questions',question_text,input_text)

      # Show the result to the user
      self.answer_text.text=result 

  def input_text_show(self, **event_args):
    """This method is called when the text area is shown on the screen"""
    pass

  def input_text_focus(self, **event_args):
    """This method is called when the text area gets focus"""
    pass



  
      
