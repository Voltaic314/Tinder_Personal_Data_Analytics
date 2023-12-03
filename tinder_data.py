"""
Author: Logan Maupin

Have you ever wanted to hate yourself more than you already do? 
Well you're in luck! If you request your data from Tinder, you can
use this python script to analyze the data for you. :) 
"""
from json import load


class TinderData:

    def __init__(self, data_filename='data.json') -> None:

        self.data_filename = data_filename
        self.likes = 0
        self.super_likes = 0
        self.left_swipes = 0
        self.matches = 0
        self.match_rate = 0
        self.like_rate = 0

    def get_total_from_file(self, metric_key_name: str) -> int:
        '''
        This method will read the data.json file (or whatever the user named it),
        and from there will populate whatever metric they were trying to find
        
        Parameters:
        metric_key_name: str - name of the metric you want to populate.
        Possible choices are swipes_likes, swipes_passes, superlikes, matches, app_opens 
        
        Returns: int - total of that key's value for all entries
        '''
        json_file = open(self.data_filename, "r", encoding="UTF-8")
        json_to_parse = load(fp=json_file)
        metric: dict[str, int] = json_to_parse["Usage"][metric_key_name]

        total = 0
        for value in metric.values():
            total += value

        return total

    def update_totals_from_files(self) -> None:
        '''
        This method calls the get_total_from_file method to populate our
        object attributes. 
        '''

        # this list is here just to remind the users what strings to pass in as arguments.
        # metrics = ["swipes_likes", "swipes_passes", "superlikes", "matches", "app_opens"]

        self.likes = self.get_total_from_file("swipes_likes")
        self.super_likes = self.get_total_from_file("superlikes")
        self.left_swipes = self.get_total_from_file("swipes_passes")
        self.matches = self.get_total_from_file("matches")

    def get_match_rate(self) -> None:
        '''
        This method performs some basic math between the likes, superlikes, and matches,
        to get the match success ratio. It will then set the match rate attribute 
        as a percentage rounded to 2 decimals.
        '''
        total_likes = self.likes + self.super_likes
        rate = total_likes / self.matches
        percentage = round(rate / 100, 2)
        self.match_rate = percentage

    def get_like_rate(self) -> None:
        '''
        THis method performs basic math with the likes, super likes, and left swipes,
        to get the swipe right ratio. It will then set the like rate attribute to the resulting value
        in percentage form rounded to 2 decimals.
        '''
        like_amount = self.likes + self.super_likes
        total = like_amount + self.left_swipes
        self.like_rate = round((like_amount / total) * 100, 2)

    def prepare_for_report(self):
        '''
        This method calls the other methods to populate our special values for our report.
        '''
        self.update_totals_from_files()
        self.get_like_rate()
        self.get_match_rate()

    def display_data(self):
        '''
        This method displays the analytics in a basic unstylized report form.
        '''
        self.prepare_for_report()
        
        print()
        print("Tinder Success Rate Stats\n")
        print(f"Total likes sent: {self.likes + self.super_likes}")
        print(f"Total left swipes: {self.left_swipes}")
        print(f"Total Matches: {self.matches}")
        print()
        print(f"Percentage of girls you swipe right on: {self.like_rate}%")
        print(f"Percentage of matches you get: {self.match_rate}%")
        print()


def main():
    data = TinderData("data.json")
    data.display_data()


if __name__ == "__main__":
    main()
