"""
The Collatz sequence, also called the 3n + 1 problem.

From a starting number, n, follow three rules to get the next 
number in the sequence:
1. If n is even, the next number n is n / 2.
2. If n is odd, the next number n is n * 3 + 1.
3. If n is 1, stop. Otherwise, repeat.

It is generally thought, but so far not mathematically proven, that 
every starting number eventually terminates at 1. 
More information about the Collatz sequence can be found at 
https://en.wikipedia.org/wiki/Collatz_conjecture 
"""

def get_collatz_sequence(num):
    sequence = []
    sequence.append(num)
    while num != 1:

        if num % 2 == 0:
            num = num / 2
            sequence.append(int(num))

        elif num % 2 == 1:
            num = 3 * num + 1
            sequence.append(int(num))
    
    return sequence

def get_collatz_sequence_length(sequence):
    return len(sequence)

# test a collatz sequence based on an input integer 

print("Enter a starting number (greater than 0) or QUIT")
my_num = int(input())
my_sequence = get_collatz_sequence(my_num)
print(my_sequence)


# ----------------------------------------------------------------
# testing some successive sequences to see if there are obvious patterns
# in their respective lengths

# lengths_sequences = []

# for num in range(1,25):
#     loop_sequnece = get_collatz_sequence(num)
#     sequence_len = get_collatz_sequence_length(loop_sequnece)
#     lengths_sequences.append(sequence_len)
    
# print(lengths_sequences)

# ----------------------------------------------------------------

# Are the Collatz sequences for starting numbers that are powers of two 
# (2, 4, 8, 16, 32, 64, 128, on so on) always composed of only even num-bers
# (aside from the fnal 1)?

# powers_of_two = [2**x for x in range(2,15)]

# for num in powers_of_two:
#     print(get_collatz_sequence(num))