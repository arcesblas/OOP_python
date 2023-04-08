# Your task is to:
"""
Write docstrings for this class after analyzing the code carefully.

Document the __init__() function and the properties with their corresponding docstrings.

Explain why the help() function and the __doc__ attribute 
are helpful for working with docstrings.
"""

# Code
class Flight:
    """Class that represents a flight.
    
    Attributes:
        number (str): flight number represented as a string.
		origin (str): a three-letter abbreviation of the country of origin. e.g. "USA".
		destination (str):  a three-letter abbreviation of the destination. e.g. "USA".
		num_passengers (int): an integer that represents the number of passengers that are
		currently registered for the flight.
    Methods:
		display_flight_data(): displays the data of the flight.
    
    """
       
    def __init__(self, number, origin, destination, num_passengers, total_weight, pilot, crew):
        """Initializes the values of the instance attributes of Flight.

        Args:
            number (str): the flight number represented as a string.
            origin (str): a three-letter abbreviation of the country of origin. e.g. "USA".
            destination (str): a three-letter abbreviation of the destination. e.g. "USA".
            num_passengers (int): an integer that represents the number of passengers that are
			currently registered for the flight.
		    total_weight (float): the approximate weight of the flight including baggage, passengers,
            fuel, crew, and other elements.
            pilot (Pilot): the pilot assigned to the flight.
            crew (list of Crew): the crew assigned to the flight.   
        """
        
        self.number = number
        self.origin = origin
        self.destination = destination
        self.num_passengers = num_passengers
        self._total_weight = total_weight
        self._pilot = pilot 
        self._crew = crew
 
    @property
    def total_weight(self):
        return self._total_weight
 
    @total_weight.setter
    def total_weight(self, weight):
        if weight > 0 and isinstance(weight, float):
            self._total_weight = weight	
 
    @property
    def pilot(self):
        return self._pilot
 
    @pilot.setter
    def pilot(self, new_pilot):
        self._pilot = new_pilot
 
    @property
    def crew(self):
        return self._crew
	
    @crew.setter
    def crew(self, new_crew):
        self._crew = new_crew
 
    def display_flight_data(self):
        print("== Flight ==")
        print("Number:", self.number)
        print("Number of Passengers:", self.num_passengers)
        print("Weight:", self._total_weight)
        print("Pilot:", self._pilot)
        print("Crew:", self._crew)

# Explain why the help() function and the __doc__ attribute are helpful for working with docstrings.
"""
They are important because they allow us to read docstrings 
that are linked to a class, function, method or property in an easy way, 
they give us in a direct way and without reviewing 
the source code the information we need to know how to use that piece of code. 
It is a good practice to document your code, because this way if someone else 
comes to see your code they don't need to go directly to you to know
how it works but in the code itself they can understand it.
"""