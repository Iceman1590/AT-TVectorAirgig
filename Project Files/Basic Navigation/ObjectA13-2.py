import anki_vector
import time
from anki_vector.util import Pose, degrees

def main():
	args = anki_vector.util.parse_command_args()
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		x = 0.0
		y = 0.0
		a = 0.0
		robot.behavior.go_to_pose(Pose(0, 0, 0, angle_z=degrees(0)), relative_to_robot=False)
		while (a != 1000):
			if (x == 0 and y == 0):
				while(x != 1000 and y == 0):
					BTSide = True
					x = x + 50
					robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(0)), relative_to_robot=False)
					latest_nav_map = robot.nav_map.latest_nav_map
					if (BTSide == True):
						content = latest_nav_map.get_content(x+5.0, 0.0)
						print(f"Sampling point at {x+5.0}, {y} and found content: {content}")
					else:
						content = latest_nav_map.get_content(0.0, y+5.0)
						print(f"Sampling point at {x}, {y+5.0} and found content: {content}")
					if (content > 2):
						robot.behavior.go_to_pose(Pose(x, y+100.0, 0, angle_z=degrees(0)), relative_to_robot=False)
						robot.behavior.go_to_pose(Pose(x+150.0, y+100.0, 0, angle_z=degrees(0)), relative_to_robot=False)
						robot.behavior.go_to_pose(Pose(x+100.0, 0, 0, angle_z=degrees(0)), relative_to_robot=False)
				robot.behavior.go_to_pose(Pose(1000, 0, 0, angle_z=degrees(90)), relative_to_robot=False)
			if (x == 1000 and y == 0):
				while(x == 1000 and y != 500):
					BTSide = False
					y = y + 50
					robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(90)), relative_to_robot=False)
					if (BTSide == True):
						content = latest_nav_map.get_content(x+5.0, 0.0)
						print(f"Sampling point at {x+5.0}, {y} and found content: {content}")
					else:
						content = latest_nav_map.get_content(0.0, y+5.0)
						print(f"Sampling point at {x}, {y+5.0} and found content: {content}")
					if (content > 2):
						robot.behavior.go_to_pose(Pose(x, y+100.0, 0, angle_z=degrees(0)), relative_to_robot=False)
						robot.behavior.go_to_pose(Pose(x+150.0, y+100.0, 0, angle_z=degrees(0)), relative_to_robot=False)
						robot.behavior.go_to_pose(Pose(x+100.0, 0, 0, angle_z=degrees(0)), relative_to_robot=False)
			
			if (x == 1000 and y == 500):
				while(x != 0 and y == 500):
					BTSide = True
					x = x - 50
					robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(180)), relative_to_robot=False)
					if (BTSide == True):
						content = latest_nav_map.get_content(x+5.0, 0.0)
						print(f"Sampling point at {x+5.0}, {y} and found content: {content}")
					else:
						content = latest_nav_map.get_content(0.0, y+5.0)
						print(f"Sampling point at {x}, {y+5.0} and found content: {content}")
					if (content > 2):
						robot.behavior.go_to_pose(Pose(x, y+100.0, 0, angle_z=degrees(0)), relative_to_robot=False)
						robot.behavior.go_to_pose(Pose(x+150.0, y+100.0, 0, angle_z=degrees(0)), relative_to_robot=False)
						robot.behavior.go_to_pose(Pose(x+100.0, 0, 0, angle_z=degrees(0)), relative_to_robot=False)

			if (x == 0 and y == 500):
				while(x == 0 and y != 0):
					BTSide = False
					y = y - 50
					robot.behavior.go_to_pose(Pose(x, y, 0, angle_z=degrees(-90)), relative_to_robot=False)
					if (BTSide == True):
						content = latest_nav_map.get_content(x+5.0, 0.0)
						print(f"Sampling point at {x+5.0}, {y} and found content: {content}")
					else:
						content = latest_nav_map.get_content(0.0, y+5.0)
						print(f"Sampling point at {x}, {y+5.0} and found content: {content}")
					if (content > 2):
						robot.behavior.go_to_pose(Pose(x, y+100.0, 0, angle_z=degrees(0)), relative_to_robot=False)
						robot.behavior.go_to_pose(Pose(x+150.0, y+100.0, 0, angle_z=degrees(0)), relative_to_robot=False)
						robot.behavior.go_to_pose(Pose(x+100.0, 0, 0, angle_z=degrees(0)), relative_to_robot=False)
			robot.audio.stream_wav_file("OrganizationXIII.wav", 75)
			a = 1000
if __name__ == "__main__":
	main()