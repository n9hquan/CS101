"""
This program contains one programming problem named Class Scores.

Author: Nguyen Chinh Quan
Time spent: 15 minutes
"""
import statistics
def compute_mode(quiz_scores):
    """ 
    Description: Determine the most common score on the quiz
    Parameter:
        quiz_scores: A list of quiz scores
    Return: The mode of the scores
    """
    mode_of_quiz_scores = statistics.multimode(quiz_scores)
    mode_of_quiz_scores.sort()
    return mode_of_quiz_scores