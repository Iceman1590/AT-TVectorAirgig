import time
import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps

def main():
	args = anki_vector.util.parse_command_args()
	num = 1
	with anki_vector.Robot(args.serial, show_viewer=True, enable_face_detection=False, show_3d_viewer=True, enable_nav_map_feed=True) as robot:
		with anki_vector.Robot() as robot:
			robot.behavior.set_head_angle(degrees(0.0))
			robot.behavior.drive_off_charger()
			for _ in range(500):
				if robot.proximity.last_sensor_reading:
					distance = robot.proximity.last_sensor_reading.distance
					prox = distance.distance_mm
					print("=====================================================================")
					print(num) 
					print(prox)
					print("=====================================================================")
					if ((prox) < 100.0):
						robot.motors.set_wheel_motors(0, 0)
						robot.behavior.turn_in_place(degrees(-45))
					else:
						robot.motors.set_wheel_motors(75, 75)
					num = num + 1

		time.sleep(10)
		try:
			# Shutdown the program after 30 seconds
			time.sleep(30)
		except KeyboardInterrupt:
			pass
		
		
if __name__ == "__main__":
    main()


						
	 