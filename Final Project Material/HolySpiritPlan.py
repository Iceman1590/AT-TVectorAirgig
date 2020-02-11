#HolySpiritsPlan - Vector's basic movement around objects in rectangular course
import anki_vector
import time
from anki_vector.util import Pose, degrees, Speed

def main():
	args = anki_vector.util.parse_command_args()
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		x = 0.0
		y = 0.0
		robot.behavior.go_to_pose(Pose(0, 0, 0, angle_z=degrees(0)), relative_to_robot=False) #commands Vector to proceed to position (0,0,0) at 0 degrees rotation, not relative to specifically him
		if (x == 0 and y == 0): #when Vector is at the starting position (0,0,0), he will begin moving to the right until he reaches (1000,0,0)
			while(x != 1000 and y == 0): #proceeding to (1000,0,0), Vector moves incrementally by 50mm
				latest_nav_map = robot.nav_map.latest_nav_map #provides Vector with map
				content = latest_nav_map.get_content(x+50,y) #checks position 50mm in front of Vector and assesses whether obstacle is present
				print(f"Sampling point at {x+50.0}, {y} and found content: {content}")
				if(content > 2): #should an object be present, Vector will move around it, updating his position afterwards
					print("object detected")
					robot.behavior.go_to_pose(Pose(0, 100, 0, angle_z=degrees(0)), relative_to_robot=True)
					robot.behavior.go_to_pose(Pose(200, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
					robot.behavior.go_to_pose(Pose(0, -100, 0, angle_z=degrees(0)), relative_to_robot=True)
					x = x + 200
				x = x + 50
				robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(0)), relative_to_robot=False)
				
		if (x == 1000 and y == 0): #process is repeated when moving along remaining portions of the rectangular course
			while(x == 1000 and y != 450):
				latest_nav_map = robot.nav_map.latest_nav_map
				content = latest_nav_map.get_content(x,y+50)
				print(f"Sampling point at {x}, {y+50} and found content: {content}")
				if(content > 2):
					print("object detected")
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
					print("object detected")
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
					print("object detected")
					robot.behavior.go_to_pose(Pose(100, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
					robot.behavior.go_to_pose(Pose(0, -200, 0, angle_z=degrees(0)), relative_to_robot=True)
					robot.behavior.go_to_pose(Pose(-100, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
					y = y - 200
				y = y - 50
				robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(-90)), relative_to_robot=False)

if __name__ == "__main__":
	main()