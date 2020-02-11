import anki_vector
import time
import argparse
from anki_vector.util import Pose, degrees, Speed

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--new_param")
	args = anki_vector.util.parse_command_args(parser)
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		x = 0.0
		y = 0.0
		i = 0
		objectx = [0.0,0.0,0.0,0.0]
		objecty = [0.0,0.0,0.0,0.0]
		robot.behavior.go_to_pose(Pose(0, 0, 0, angle_z=degrees(0)), relative_to_robot=False)
		if (x == 0 and y == 0):
			while(x != 500 and y == 0):
				latest_nav_map = robot.nav_map.latest_nav_map
				content = latest_nav_map.get_content(x+50,y)
				print(f"Sampling point at {x+50.0}, {y} and found content: {content}")
				if(content > 2):
					print("object detected")
					print("saving object position")
					objectx[i] = x + 50.0 
					objecty[i] = y 
					i = i + 1
					print(objectx)
					print(objecty) 
					robot.behavior.go_to_pose(Pose(0, 100, 0, angle_z=degrees(0)), relative_to_robot=True)
					robot.behavior.go_to_pose(Pose(200, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
					robot.behavior.go_to_pose(Pose(0, -100, 0, angle_z=degrees(0)), relative_to_robot=True)
					x = x + 200
				x = x + 50
				robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(0)), relative_to_robot=False)
		fixed_object = robot.world.create_custom_fixed_object(Pose(objectx[0], objecty[0], 0, angle_z=degrees(90)), 50, 50, 50, relative_to_robot=False)
		if (x == 500 and y == 0):
			while(x != 0 and y == 0):
				x = x - 50
				robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(180)), relative_to_robot=False)
				
if __name__ == "__main__":
	main()				
				