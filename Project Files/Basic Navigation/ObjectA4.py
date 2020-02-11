import anki_vector
from anki_vector.util import Pose, degrees


def main():
	args = anki_vector.util.parse_command_args()
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		robot.behavior.drive_off_charger()		
		fixed_object = robot.world.create_custom_fixed_object(Pose(100, 0, 25, angle_z=degrees(90)), 50, 50, 50, relative_to_robot=True) #side wall on right		
		if fixed_object:
			print("fixed custom objects created successfully")
		robot.behavior.go_to_pose(Pose(250, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
		robot.world.delete_custom_objects()


if __name__ == "__main__":
	main()
