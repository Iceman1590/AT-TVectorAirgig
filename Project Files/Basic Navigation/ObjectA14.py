import anki_vector
import time
from anki_vector.util import Pose, degrees

def main():
	args = anki_vector.util.parse_command_args()
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		x = 50.0
		robot.behavior.go_to_pose(Pose(x, 0, 0, angle_z=degrees(0)), relative_to_robot=False)
		latest_nav_map = robot.nav_map.latest_nav_map
		content = latest_nav_map.get_content(x+5.0, 0.0)
		print(f"Sampling point at 50.0, 0.0 and found content: {content}")
		if (content != 1):
			robot.behavior.go_to_pose(Pose(0, 100, 0, angle_z=degrees(0)), relative_to_robot=True)
			robot.behavior.go_to_pose(Pose(100, 100, 0, angle_z=degrees(0)), relative_to_robot=True)
			robot.behavior.go_to_pose(Pose(100, 0, 0, angle_z=degrees(0)), relative_to_robot=True)

if __name__ == "__main__":
	main()