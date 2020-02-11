import anki_vector
from anki_vector.util import Pose, degrees


def main():
	args = anki_vector.util.parse_command_args()
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		robot.behavior.drive_off_charger()		
		fixed_object = robot.world.create_custom_fixed_object(Pose(250, -100, 50, angle_z=degrees(90)), 400, 50, 50, relative_to_robot=True) #side wall on right
		fixed_object = robot.world.create_custom_fixed_object(Pose(88, 75, 50, angle_z=degrees(0)), 275, 50, 50, relative_to_robot=True) #top wall
		fixed_object = robot.world.create_custom_fixed_object(Pose(25, -100, 50, angle_z=degrees(0)), 150, 75, 50, relative_to_robot=True) #big box	
		fixed_object = robot.world.create_custom_fixed_object(Pose(75, -300, 50, angle_z=degrees(0)), 75, 75, 50, relative_to_robot=True) #small box		
		fixed_object = robot.world.create_custom_fixed_object(Pose(-75, -200, 50, angle_z=degrees(90)), 600, 50, 50, relative_to_robot=True) #side wall on left		
		fixed_object = robot.world.create_custom_fixed_object(Pose(135, -425, 50, angle_z=degrees(45)), 300, 50, 50, relative_to_robot=True) #diagonal
		fixed_object = robot.world.create_custom_fixed_object(Pose(0, -500, 50, angle_z=degrees(0)), 150, 50, 50, relative_to_robot=True) #bottom wall			
		if fixed_object:
			print("fixed custom objects created successfully")
		robot.behavior.go_to_pose(Pose(175, 0, 0, angle_z=degrees(0)), relative_to_robot=False)
		robot.behavior.go_to_pose(Pose(175, 50, 0, angle_z=degrees(0)), relative_to_robot=False)		
		robot.world.delete_custom_objects()


if __name__ == "__main__":
	main()
