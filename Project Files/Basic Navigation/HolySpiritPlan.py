import anki_vector
import time
from anki_vector.util import Pose, degrees, Speed

def main():
	args = anki_vector.util.parse_command_args()
	objectx = [500.0,0.0,0.0,0.0]
	objecty = [0.0,0.0,0.0,0.0]
	with anki_vector.Robot(args.serial, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		x = 0.0
		y = 0.0
		a = 0.0
		i = 0
		fixed_object = robot.world.create_custom_fixed_object(Pose(objectx[0], objecty[0], 0, angle_z=degrees(90)), 50, 50, 50, relative_to_robot=False)
		robot.behavior.go_to_pose(Pose(0, 0, 0, angle_z=degrees(0)), relative_to_robot=False)
		while (a != 1000):
			if (x == 0 and y == 0):
				while(x != 1000 and y == 0):
					x = x + 50
					robot.behavior.go_to_pose(Pose(x, 0, 0, angle_z=degrees(0)), relative_to_robot=False)
					

if __name__ == "__main__":
	main()
