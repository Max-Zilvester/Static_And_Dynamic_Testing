### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 
/Users/mrmax/Downloads/Static_and_Dynamic_Task_A/part_1_docs/testing_task_1.md
Only comment on errors that would stop the tests running.

```python

class CardGame:
# Instances of the card game is not intialized

  def check_for_ace(self, card):
    if card.value = 1:  # missing syntax  =.
      return True
    else                 # missing syntax  :.
      return False
   
   # This code will not run. The function is not properly defined and the parameters not propery passed :, wrong indentation
  dif highest_card(self, card1 card2):       # wrong definition, 'def' required plus a missing comma after card1.
  if card1.value > card2.value:     # wrong indentation.
    return card                     # wrong indentation
  else:                             # wrong indentation
    return card2                    # wrong indentation
  


def cards_total(self, cards):
  total                         #'total' is not initialized' :
  for card in cards:
    total += card.value
    return "You have a total of" + total    #return statement not properly concantenated.
  
```
