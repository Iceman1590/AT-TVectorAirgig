import anki_vector
from anki_vector.util import Pose, degrees


def main():
	args = anki_vector.util.parse_command_args()
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		robot.behavior.drive_off_charger()
		robot.motors.set_lift_motor(5)
		n = 0.0
		i = 0.0
		while (i<1000.0):
			robot.behavior.go_to_pose(Pose(n, 0, 0, angle_z=degrees(0)), relative_to_robot=False)
			latest_nav_map = robot.nav_map.latest_nav_map
			content = latest_nav_map.get_content(n+5.0, 0.0)
			print(f"Sampling point at {n}, 100.0 and found content: {content}")
			n = n + 50.0
			i = i + 1.0
			if (content > 1):
				robot.behavior.go_to_pose(Pose(0, 10, 0, angle_z=degrees(0)), relative_to_robot=True)
				robot.behavior.go_to_pose(Pose(10, 10, 0, angle_z=degrees(0)), relative_to_robot=True)
				robot.behavior.go_to_pose(Pose(20, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
			robot.behavior.go_to_pose(Pose(100, 0, 0, angle_z=degrees(0)), relative_to_robot=True)

if __name__ == "__main__":
	main()


# when the content returns value 1, we assume this to mean open space (light green)
# when the content returns value 2, we assume this to be an space already visited (dark green)
# 

					