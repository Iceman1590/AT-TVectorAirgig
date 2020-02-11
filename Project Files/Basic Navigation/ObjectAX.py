import anki_vector
from anki_vector.util import Pose, degrees


def main():
	args = anki_vector.util.parse_command_args()
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		robot.behavior.drive_off_charger()		
		fixed_object = robot.world.create_custom_fixed_object(Pose(100, 100, 0, angle_z=degrees(90)), 50, 50, 50, relative_to_robot=True) #side wall on right
		fixed_object = robot.world.create_custom_fixed_object(Pose(-100, 100, 0, angle_z=degrees(90)), 50, 50, 50, relative_to_robot=True) #side wall on right
		fixed_object = robot.world.create_custom_fixed_object(Pose(100, -100, 0, angle_z=degrees(90)), 50, 50, 50, relative_to_robot=True) #side wall on right
		fixed_object = robot.world.create_custom_fixed_object(Pose(-100, -100, 0, angle_z=degrees(90)), 50, 50, 50, relative_to_robot=True) #side wall on right
		if fixed_object:
			print("fixed custom objects created successfully")
		robot.behavior.turn_in_place(degrees(90))
		robot.behavior.turn_in_place(degrees(90))
		robot.behavior.turn_in_place(degrees(90))
		robot.behavior.turn_in_place(degrees(90))
		robot.world.delete_custom_objects()
		latest_nav_map = robot.nav_map.latest_nav_map
		content = latest_nav_map.get_content(100.0, 100.0)
		content2 = latest_nav_map.get_content(100.0, -100.0)
		if content:
			print(f"Sampling point at 100.0, 100.0 and found content: {content}")
		if content2:
			print(f"Sampling point at 100.0, -100.0 and found content: {content2}")

if __name__ == "__main__":
	main()


# when the content returns value 1, we assume this to mean open space (light green)
# when the content returns value 2, we assume this to be an space already visited (dark green)
# 
