
# Note: the solution code from the video for OOP-practice.py is found in a separate branch in this repo.

#VERSION 1 - Totally blank


# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 




# Define a repair() method that will update the condition of the podracer to "repaired".





# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.






# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".



#VERSION 2 - Starter code in "jigsaw" style ... try to guess/replace the ???'s with the missing keyword (and use clues from errors when you run this file with python OOP-practice.py (or python3 for Mac))

# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
??? Podracer:
  def ???(self, max_speed, ???, ???):
    self.max_speed = max_speed
    self.condition = ???
    self.price = ???

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def ???(self):
    self.condition = "???"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(???):
  def ???(self, max_speed, ???, ???):
    ???.???(max_speed, ???, ???)
  
  def boost(self):
    self.max_speed ??? 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(???):
  def ???(self, max_speed, ???, ???):
    ???.???(max_speed, ???, ???)
  
  def flame_jet(self, ???):
    ???.condition = "trashed"




# For both versions, here are test instances you can run for testing and debugging

# Task 1: Instantiate a Podracer
# podracer_1 = Podracer(max_speed=300, condition="perfect", price=1500)
# print("\n--- Task 1 ---")
# print(f"Podracer 1: Speed={podracer_1.max_speed}, Condition={podracer_1.condition}, Price={podracer_1.price}")

# Task 2: Test repair method
# print("\n--- Task 2 ---")
# podracer_1.condition = "trashed"
# print(f"Before repair: {podracer_1.condition}")
# podracer_1.repair()
# print(f"After repair: {podracer_1.condition}")

# Task 3: Test AnakinsPod and boost method
# print("\n--- Task 3 ---")
# anakin_pod = AnakinsPod(max_speed=400, condition="perfect", price=3000)
# print(f"Anakin's Pod - Max Speed before boost: {anakin_pod.max_speed}")
# anakin_pod.boost()
# print(f"Anakin's Pod - Max Speed after boost: {anakin_pod.max_speed}")

# Task 4: Test SebulbasPod and flame_jet method
# print("\n--- Task 4 ---")
# sebulba_pod = SebulbasPod(max_speed=350, condition="perfect", price=2500)
# podracer_2 = Podracer(max_speed=300, condition="perfect", price=1500)
# print(f"Other Podracer's condition before flame_jet: {podracer_2.condition}")
# sebulba_pod.flame_jet(podracer_2)
# print(f"Other Podracer's condition after flame_jet: {podracer_2.condition}")


#EXPECTED OUTPUTS

# --- Task 1 ---
# Podracer 1: Speed=300, Condition=perfect, Price=1500

# --- Task 2 ---
# Before repair: trashed
# After repair: repaired

# --- Task 3 ---
# Anakin's Pod - Max Speed before boost: 400
# Anakin's Pod - Max Speed after boost: 800

# --- Task 4 ---
# Other Podracer's condition before flame_jet: perfect
# Other Podracer's condition after flame_jet: trashed


'''
Make sure to answer the following prompts about your coding experience:

How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

How in particular did Object Oriented Programming assist in the solving of this problem?

'''

