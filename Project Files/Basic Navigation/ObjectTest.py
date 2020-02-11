import anki_vector
from anki_vector.util import Pose, degrees


def main():
	args = anki_vector.util.parse_command_args()
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		robot.behavior.go_to_pose(Pose(500, 0, 0, angle_z=degrees(0)), relative_to_robot=False)
		
if __name__ == "__main__":
	main()


# when the content returns value 1, we assume this to mean open space (light green)
# when the content returns value 2, we assume this to be an space already visited (dark green)
# 



