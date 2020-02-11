import anki_vector


def main():
	args = anki_vector.util.parse_command_args()
	with anki_vector.Robot(args.serial, enable_nav_map_feed=True) as robot:
		# Make sure Vector drives around so the nav map will update
		robot.behavior.drive_off_charger()
		robot.motors.set_wheel_motors(-100, 100)
		latest_nav_map = robot.nav_map.latest_nav_map
		
if __name__ == "__main__":
	main()
