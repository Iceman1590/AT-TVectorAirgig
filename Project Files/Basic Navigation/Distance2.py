import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps
import time

args = anki_vector.util.parse_command_args()
with anki_vector.Robot() as robot:
	for _ in range(10):
		if robot.proximity.last_sensor_reading:
			distance = robot.proximity.last_sensor_reading.distance
			prox = distance.distance_mm
			print("=====================================================================")
			print(prox)
			print("=====================================================================")
			time.sleep(1.0)
			if ((prox) < 100.0):
				robot.behavior.turn_in_place(degrees(-90))
			else:
				robot.behavior.drive_straight(distance_mm(50), speed_mmps(100))
