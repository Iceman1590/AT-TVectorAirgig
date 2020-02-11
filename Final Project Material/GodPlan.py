#GodsPlan - Isaac's Program that has the Vector go through course twice
import anki_vector
import time
from anki_vector.util import Pose, degrees, Speed
def main():
	args = anki_vector.util.parse_command_args()
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		x = 0.0
		y = 0.0
		a = 0.0
		i = 0
		objectx = [0.0,0.0,0.0,0.0] #empty array for x coordinates
		objecty = [0.0,0.0,0.0,0.0] #empty array for y coordinates
		robot.behavior.say_text("Initializing")
		robot.behavior.go_to_pose(Pose(0, 0, 0, angle_z=degrees(0)), relative_to_robot=False) #commands Vector to proceed to an initial point of (0,0,0)
		if (x == 0 and y == 0): #if the current position is (0,0)
			while(x != 1000 and y == 0): #while Vector is not at position (1000,0)
				latest_nav_map = robot.nav_map.latest_nav_map #represents Vector's proximity map
				content = latest_nav_map.get_content(x+50,y) #Vector evaluates position 50mm in front of his current one
				print(f"Sampling point at {x+50.0}, {y} and found content: {content}")
				if(content > 2): #if an object is detected
					robot.behavior.say_text("Object detected")
					print("saving object position")
					objectx[i] = x + 50.0 #x position of object is stored into position array
					objecty[i] = y #y position of object is stored into position array
					i = i + 1
					print(objectx)
					print(objecty)
					robot.behavior.go_to_pose(Pose(0, 100, 0, angle_z=degrees(0)), relative_to_robot=True) #Vector proceeds 100mm to his left
					robot.behavior.go_to_pose(Pose(200, 0, 0, angle_z=degrees(0)), relative_to_robot=True) #Moves 200mm forward
					robot.behavior.go_to_pose(Pose(0, -100, 0, angle_z=degrees(0)), relative_to_robot=True) #Moves 100mm right
					x = x + 200 #accounts for Vector's position change upon object detection and allows him to continue
				x = x + 50 #Vector moves 50mm forward
				robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(0)), relative_to_robot=False)

		if (x == 1000 and y == 0): #process is repeated once the corners of the rectangles are reached
			while(x == 1000 and y != 450):
				latest_nav_map = robot.nav_map.latest_nav_map
				content = latest_nav_map.get_content(x,y+50)
				print(f"Sampling point at {x}, {y+50} and found content: {content}")
				if(content > 2):
					robot.behavior.say_text("Object detected")
					print("saving object position")
					objectx[i] = x
					objecty[i] = y + 50.0
					i = i + 1
					print(objectx)
					print(objecty)
					robot.behavior.go_to_pose(Pose(-100, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
					robot.behavior.go_to_pose(Pose(0, 200, 0, angle_z=degrees(0)), relative_to_robot=True)
					robot.behavior.go_to_pose(Pose(100, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
					y = y + 200
				y = y + 50
				robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(90)), relative_to_robot=False)

		if (x == 1000 and y == 450):
			while(x != 0 and y == 450):
				latest_nav_map = robot.nav_map.latest_nav_map
				content = latest_nav_map.get_content(x-50,y)
				print(f"Sampling point at {x-50}, {y} and found content: {content}")
				if(content > 2):
					robot.behavior.say_text("Object detected")
					print("saving object position")
					objectx[i] = x - 50.0
					objecty[i] = y
					i = i + 1
					print(objectx)
					print(objecty)
					robot.behavior.go_to_pose(Pose(0, -100, 0, angle_z=degrees(0)), relative_to_robot=True)
					robot.behavior.go_to_pose(Pose(200, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
					robot.behavior.go_to_pose(Pose(0, 100, 0, angle_z=degrees(0)), relative_to_robot=True)
					x = x - 200
				x = x - 50
				robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(180)), relative_to_robot=False)

		if (x == 0 and y == 450):
			while(x == 0 and y != 0):
				latest_nav_map = robot.nav_map.latest_nav_map
				content = latest_nav_map.get_content(x,y-50)
				print(f"Sampling point at {x}, {y-50} and found content: {content}")
				if(content > 2):
					robot.behavior.say_text("Object detected")
					print("saving object position")
					objectx[i] = x
					objecty[i] = y - 50.0
					i = i + 1
					print(objectx)
					print(objecty)
					robot.behavior.go_to_pose(Pose(100, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
					robot.behavior.go_to_pose(Pose(0, -200, 0, angle_z=degrees(0)), relative_to_robot=True)
					robot.behavior.go_to_pose(Pose(-100, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
					y = y - 200
				y = y - 50
				robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(-90)), relative_to_robot=False)
		fixed_object = robot.world.create_custom_fixed_object(Pose(objectx[0], objecty[0], 0, angle_z=degrees(90)), 50, 50, 50, relative_to_robot=False) #Vector extrapolates cubes from the position arrays onto the virtual environment
		fixed_object = robot.world.create_custom_fixed_object(Pose(objectx[1], objecty[1], 0, angle_z=degrees(90)), 50, 50, 50, relative_to_robot=False)
		fixed_object = robot.world.create_custom_fixed_object(Pose(objectx[2], objecty[2], 0, angle_z=degrees(90)), 50, 50, 50, relative_to_robot=False)
		fixed_object = robot.world.create_custom_fixed_object(Pose(objectx[3], objecty[3], 0, angle_z=degrees(90)), 50, 50, 50, relative_to_robot=False)
		if fixed_object:
			print("fixed custom objects created successfully")
		if (x == 0 and y == 0): #Vector proceeds along course once again
			while(x != 1000 and y == 0):
				x = x + 100
				robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(0)), relative_to_robot=False)

		if (x == 1000 and y == 0):
			while(x == 1000 and y != 450):
				y = y + 75
				robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(90)), relative_to_robot=False)

		if (x == 1000 and y == 450):
			while(x != 0 and y == 450):
				x = x - 100
				robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(180)), relative_to_robot=False)

		if (x == 0 and y == 450):
			while(x == 0 and y != 0):
				y = y - 75
				robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(-90)), relative_to_robot=False)

if __name__ == "__main__":
	main()