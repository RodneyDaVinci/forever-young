from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:

for i in range(3):

 robotArm.grab()
 robotArm.moveRight()
 robotArm.drop()
 robotArm.moveLeft()
 robotArm.grab()

robotArm.moveLeft()
robotArm.moveRight()
robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()