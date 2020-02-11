import time
import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps

def main():
	args = anki_vector.util.parse_command_args()
	with anki_vector.Robot(args.serial, show_viewer=True, enable_face_detection=False) as robot:
		with anki_vector.Robot() as robot:
			robot.behavior.drive_off_charger()
			for _ in range(20):
				if robot.proximity.last_sensor_reading:
					distance = robot.proximity.last_sensor_reading.distance
					prox = distance.distance_mm
					print("=====================================================================")
					print(prox)
					print("=====================================================================")
					if ((prox) < 150.0):
						robot.behavior.say_text("Turning left")
						robot.behavior.turn_in_place(degrees(90))
					else:
						robot.behavior.drive_straight(distance_mm(50), speed_mmps(200))
		time.sleep(10)
		try:
			# Shutdown the program after 30 seconds
			time.sleep(30)
		except KeyboardInterrupt:
			pass
		
		
if __name__ == "__main__":
    main()


						
	 