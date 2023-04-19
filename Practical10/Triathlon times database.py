class Triathlon:
 def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = swim_time + cycle_time + run_time

 def print_details(self):
    print(f"{self.first_name} {self.last_name} competed in {self.location} and completed the triathlon in {self.total_time} seconds. Swim time: {self.swim_time} seconds. Cycle time: {self.cycle_time} seconds. Run time: {self.run_time} seconds. Total time: {self.total_time}")

# Example usage
triathlete = Triathlon("Donald", "Trump", "NewYork", 1000, 2000, 3000)
triathlete.print_details()