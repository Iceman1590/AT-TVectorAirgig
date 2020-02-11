#Jesus'Plan - Justin's program that has vector automatically avoid objects from array
import anki_vector
import time
from anki_vector.util import Pose, degrees, Speed

def main():
	args = anki_vector.util.parse_command_args()
	objectx = [500.0,1000.0,500.0,0.0] #premade object position arrays
	objecty = [0.0,200.0,200.0,200.0]
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		x = 0.0
		y = 0.0
		a = 0.0
		i = 0 
		robot.behavior.go_to_pose(Pose(0, 0, 0, angle_z=degrees(0)), relative_to_robot=False) #Vector moves to intial point (0,0,0)
		fixed_object = robot.world.create_custom_fixed_object(Pose(objectx[0], objecty[0], 0, angle_z=degrees(90)), 50, 50, 100, relative_to_robot=False) #Vector extrapolates cubes from the position arrays onto the virtual environment
		fixed_object = robot.world.create_custom_fixed_object(Pose(objectx[1], objecty[1], 0, angle_z=degrees(90)), 50, 50, 100, relative_to_robot=False)
		fixed_object = robot.world.create_custom_fixed_object(Pose(objectx[2], objecty[2], 0, angle_z=degrees(90)), 50, 50, 100, relative_to_robot=False)
		fixed_object = robot.world.create_custom_fixed_object(Pose(objectx[3], objecty[3], 0, angle_z=degrees(90)), 50, 50, 100, relative_to_robot=False)
		while (a != 1000):
			if (x == 0 and y == 0): #if the current position is (0,0)
				while(x != 1000 and y == 0): #while Vector is not at position (1000,0)
					if(abs(x - objectx[i]) < 100 and abs(y - objecty[i]) < 100):
					#the absolute value of the location of vector - the location of the object
						# essentially sees if the object is close enough to the vector
						robot.behavior.go_to_pose(Pose(0, 100, 0, angle_z=degrees(0)), relative_to_robot=True) #Vector proceeds 100mm to his left
						robot.behavior.go_to_pose(Pose(200, 0, 0, angle_z=degrees(0)), relative_to_robot=True) #Moves 200mm forward
						robot.behavior.go_to_pose(Pose(0, -100, 0, angle_z=degrees(0)), relative_to_robot=True) #Moves 100mm right
						x = x + 200 #accounts for Vector's position change upon object detection and allows him to continue
						i = i + 1
					robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(0)), relative_to_robot=False)
					x = x + 50
			if (x == 1000 and y == 0): #process is repeated once the corners of the rectangles are reached
				while(x == 1000 and y != 400):
					if(abs(x - objectx[i]) < 100 and abs(y - objecty[i]) < 100):
						robot.behavior.go_to_pose(Pose(0, 100, 0, angle_z=degrees(0)), relative_to_robot=True)
						robot.behavior.go_to_pose(Pose(200, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
						robot.behavior.go_to_pose(Pose(0, -100, 0, angle_z=degrees(0)), relative_to_robot=True)
						y = y + 200
						i = i + 1
					robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(90)), relative_to_robot=False)
					y = y + 50
			if (x == 1000 and y == 400):
				while(x != 0 and y == 400):
					if(abs(x - objectx[i]) < 100 and abs(y - objecty[i]) < 100):
						robot.behavior.go_to_pose(Pose(0, 100, 0, angle_z=degrees(0)), relative_to_robot=True)
						robot.behavior.go_to_pose(Pose(200, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
						robot.behavior.go_to_pose(Pose(0, -100, 0, angle_z=degrees(0)), relative_to_robot=True)
						x = x - 200
						i = i + 1
					robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(180)), relative_to_robot=False)
					x = x - 50
			if (x == 0 and y == 400):
				print("a")
				while(x == 0 and y != 0):
					print("b")
					if(abs(x - objectx[i]) < 100 and abs(y - objecty[i]) < 100):
						print("c")
						robot.behavior.go_to_pose(Pose(0, 100, 0, angle_z=degrees(0)), relative_to_robot=True)
						robot.behavior.go_to_pose(Pose(200, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
						robot.behavior.go_to_pose(Pose(0, -100, 0, angle_z=degrees(0)), relative_to_robot=True)
						y = y - 200
						i = 0
					robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(270)), relative_to_robot=False)
					y = y - 50
					
if __name__ == "__main__":
	main()