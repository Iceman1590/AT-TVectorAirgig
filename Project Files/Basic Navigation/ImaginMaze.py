import anki_vector
from anki_vector.util import Pose, degrees


def main():
	args = anki_vector.util.parse_command_args()
	x = 0
	y = 0
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		robot.behavior.drive_off_charger()		
		robot.behavior.go_to_pose(Pose(200, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
		robot.world.delete_custom_objects()
		xcord = []
		ycord = []
		total = xcord + ycord
		n = 0
		if (n < 100):
			xcord.append(x)
			ycord.append(y)
			print(xcord)
			print(ycord)
			x = x + 1
			y = y + 1
			n = n + 1

if __name__ == "__main__":
	main()