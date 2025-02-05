#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Use custom objects to create a wall in front of Vector.

This example demonstrates how you can create custom objects in the world, and
automatically have Vector path around them as if they are real obstacles.

It creates a wall in front of Vector and tells him to drive around it.
He will plan a path to drive 200mm in front of himself after these objects are created.

The `show_3d_viewer=True` argument causes the 3D visualizer to open in a new
window - this shows where Vector believes this imaginary object is.
"""

import anki_vector
from anki_vector.util import Pose, degrees


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial,
                           show_3d_viewer=True,
                           enable_nav_map_feed=True) as robot:
        robot.behavior.drive_off_charger()

        fixed_object = robot.world.create_custom_fixed_object(Pose(100, 0, 0, angle_z=degrees(0)),
                                                              100, 50, 100, relative_to_robot=True)
        if fixed_object:
            print("fixed custom object created successfully")

        robot.behavior.go_to_pose(Pose(200, 0, 0, angle_z=degrees(0)), relative_to_robot=True)
        robot.world.delete_custom_objects()


if __name__ == "__main__":
    main()
