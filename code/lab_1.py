class MobilePhone:
    """
    Represents a mobile phone with basic functionality such as turning on,
    turning off, and making calls.
    """

    def __init__(self, number: str):
        """
        Initialize a MobilePhone instance.

        Args:
            number (str): The phone number associated with the mobile phone.

        Raises:
            TypeError: If `number` is not a string.
        """
        if not isinstance(number, str):
            raise TypeError("Phone number must be a string.")
        self.number = number

    def turn_on(self) -> str:
        """
        Turn on the mobile phone.

        Args:
          None

        Returns:
            str: A message confirming that the phone has been turned on.
        """
        return f"mobile phone {self.number} is turned on"

    def turn_off(self) -> str:
        """
        Turn off the mobile phone.

        Returns:
            str: A message confirming that the phone has been turned off.
        """
        return "mobile phone is turned off"

    def call(self, number: str) -> str:
        """
        Initiate a call to another phone number.

        Args:
            number (str): The phone number to call.

        Returns:
            str: A message indicating that the call is being placed.

        Raises:
            TypeError: If `number` is not a string.
        """
        if not isinstance(number, str):
            raise TypeError("Phone number must be a string.")
        return f"calling {number}"


# Runner code
phone_1 = MobilePhone('450-123-4567')
phone_2 = MobilePhone('450-890-1234')

print(phone_1.turn_on())
print(phone_2.turn_on())
print(phone_1.call(phone_2.number))
print(phone_1.turn_off())
print(phone_2.turn_off())
