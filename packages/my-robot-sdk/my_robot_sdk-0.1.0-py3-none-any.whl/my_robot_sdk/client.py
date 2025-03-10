# my_robot_sdk/client.py

import requests

class RobotSDK:
    """
    Robot SDK to control and monitor robot status.

    Args:
        base_url (str): The base URL for the robot's API.
    """

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_status(self):
        """
        Get the current status of the robot.

        Returns:
            dict: The robot's status.
        """
        response = requests.get(f"{self.base_url}/status")
        response.raise_for_status()
        return response.json()

    def move(self, direction: str, speed: int):
        """
        Move the robot in a specified direction and speed.

        Args:
            direction (str): Direction to move ('forward', 'backward', etc.).
            speed (int): Speed of movement.

        Returns:
            dict: Result of the move command.
        """
        data = {"direction": direction, "speed": speed}
        response = requests.post(f"{self.base_url}/move", json=data)
        response.raise_for_status()
        return response.json()
