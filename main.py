# import Day811
# from Day788_palindrome_integer import Palindrome
# from Day812_Chess_Elo_rating_system import Elo
# from Day815_Monte_Carlo_Method_compute_Pi_number import MonteCarlo
# from Day845_rotate_a_list_by_k_elements import listRotator
from Day852_Maximum_Subarray_Sum import max_subarray

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Palindrome(int(input('Type your number: '))).symmetrical()
    # Elo(input('Rating of A: '), input('Rating of B: '), input('if A wins put 1, if B wins put 0: ')).get_rating
    # MonteCarlo(input('Please indicate how many iterations are needed: ')).pi_num_by_montecarlo()
    # listRotator(input('Please provide your list: '), input('Please provide rotating number: ')).rotator()
    max_subarray(input('Please provide your list of numbers: '), input('what length of subarray do you like: ')).calc_max_subarray()