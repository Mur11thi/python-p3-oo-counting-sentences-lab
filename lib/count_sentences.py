#!/usr/bin/env python3

class MyString:
  def __init__(self,value =""):
    self._value = value
  def get_string(self):
     return self._value 
  def set_string(self,value):
    if (type(value) == str):
       self._value = value
    else: 
      print("The value must be a string.")

  value=property(get_string ,set_string)

  def is_sentence (self):
      return self._value.endswith(".")
  
  def is_question(self):
     return self._value.endswith("?")
  
  def is_exclamation(self):
     return self._value.endswith("!")
  def count_sentences(self):
      value = self._value
      for punc in ['?','!']:
        value = value.replace(punc , '.')
      sentences= [s for s in value.split('.') if s] 


      # sentences = [s for s in value.split('.') if s]    
      return len(sentences)

string = MyString("DAS")  


      
