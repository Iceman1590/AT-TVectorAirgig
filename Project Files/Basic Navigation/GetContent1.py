import anki_vector
from anki_vector.util import Pose, degrees

def main():
	with anki_vector.Robot(enable_nav_map_feed=True) as robot:
		# Make sure Vector drives around so the nav map will update
		robot.behavior.drive_off_charger()
		robot.motors.set_wheel_motors(-100, 100)
		latest_nav_map = robot.nav_map.latest_nav_map
		content = latest_nav_map.get_content(0.0, 100.0)
		print(f"Sampling point at 0.0, 100.0 and found content: {content}")
		
if __name__ == "__main__":
	main()