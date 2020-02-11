import anki_vector
from anki_vector.util import Pose, degrees


def main():
	args = anki_vector.util.parse_command_args()
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		robot.behavior.drive_off_charger()				
		robot.behavior.go_to_pose(Pose(100, 0, 0, angle_z=degrees(0)), relative_to_robot=False)
		robot.behavior.go_to_pose(Pose(100, 100, 0, angle_z=degrees(0)), relative_to_robot=False)
		robot.behavior.go_to_pose(Pose(200, 100, 0, angle_z=degrees(0)), relative_to_robot=False)
		robot.behavior.go_to_pose(Pose(200, 50, 0, angle_z=degrees(0)), relative_to_robot=False)
		robot.behavior.go_to_pose(Pose(250, 50, 0, angle_z=degrees(0)), relative_to_robot=False)
		robot.behavior.go_to_pose(Pose(250, 300, 0, angle_z=degrees(0)), relative_to_robot=False)

if __name__ == "__main__":
	main()
