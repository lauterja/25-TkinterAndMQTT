"""
Using a fake robot as the receiver of messages.
"""

# TODONE: 1. In mqtt_remote_method_calls, set LEGO_NUMBER at line 131
# to YOUR robot's number.
import mqtt_remote_method_calls as com
import time


class DelegateThatReceives(object):

    def forward(self, left_speed_entry, right_speed_entry):
        print("Forward", left_speed_entry, right_speed_entry)

    def turn_left(self):
        print("Turn Left")

    def stop(self):
        print("Stop")

    def turn_right(self):
        print("TurnRight")

    def reverse(self, left_speed_entry, right_speed_entry):
        print("Reverse", left_speed_entry, right_speed_entry)

    def arm_up(self):
        print("Arm Up")

    def arm_down(self):
        print("Arm Down")

    def quit(self):
        print("Quit")

    def exit(self):
        print("Exit")




def main():
    name1 = input("Enter one name (Publisher): ")
    name2 = input("Enter another name (Subscriber): ")

    my_delegate = DelegateThatReceives()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    while True:
        time.sleep(0.01)  # Time to allow message processing


main()
# TODO: 2. Copy your Tkinter/ttk ROBOT gui code from the previous session (m6).
# Then modify it so that pressing a button sends a message to a teammate
# of the form:
#   (for Forward)
#        ["forward", X, y]
#   where X and Y are from the entry box.
#
# Implement and test.