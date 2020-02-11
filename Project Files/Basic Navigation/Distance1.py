import anki_vector
import time

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot() as robot:
        for _ in range(10):
            if robot.proximity.last_sensor_reading:
                distance = robot.proximity.last_sensor_reading.distance
                print("=====================================================================")
                print(distance.distance_inches)
                print("=====================================================================")
                time.sleep(1.0)
            else:
                print("Can't be bothered to work right now")
                robot.say_text("Hold your horses")
                time.sleep(3.0)

if __name__ == "__main__":
    main()