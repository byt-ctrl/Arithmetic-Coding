# START
from collections import Counter


def calculate_symbol_probabilities(input_message) :
    """
    calculates cumulative probabilities for each unique symbol in the message.
    Returns a dictionary with symbol : (low,high) where each symbol has its 
    cumulative probability range.
    """

    total_characters=len(input_message)
    symbol_frequency=Counter(input_message)
    
    cumulative_probabilities={}
    cumulative_range_start=0.0

    # pre-compute cumulative probabilities (without sorting every time)
    for symbol,count in symbol_frequency.items() :
        symbol_probability=count/total_characters
        cumulative_probabilities[symbol]=(cumulative_range_start , cumulative_range_start + symbol_probability)
        cumulative_range_start+=symbol_probability

    return cumulative_probabilities


def encode_message(input_message,symbol_probabilities) :
    
    """
    encodes the input message using Arithmetic Coding.
    Returns a single floating-point number that represents the encoded message.
    """
    lower_bound=0.0
    upper_bound=1.0

    # for each symbol, adjust the current range (lower_bound, upper_bound)
    for symbol in input_message :
        symbol_lower,symbol_upper=symbol_probabilities[symbol]
        range_width= upper_bound-lower_bound
        upper_bound= lower_bound + range_width * symbol_upper
        lower_bound= lower_bound + range_width * symbol_lower

    return (lower_bound + upper_bound) / 2  # return the middle of the final range


def decode_message(encoded_value,symbol_probabilities,message_length) :
    
    """
    decodes the encoded value using Arithmetic Coding and returns the original message.
    """
    decoded_message=""
    current_value=encoded_value

    for _ in range(message_length) :
        for symbol,(range_start,range_end) in symbol_probabilities.items() :
            if range_start<=current_value < range_end :
                decoded_message+=symbol
                range_width=range_end-range_start
                current_value=(current_value-range_start)/range_width
                break

    return decoded_message


""" ----------------------
      Main Program Logic
    ---------------------- """

def main() :
    print(" Welcome to Efficient Arithmetic Encoding/Decoding in Python! ")
    print("===================================================================")
    
    user_message=input("Please enter a message to encode : ")

    # calculate the cumulative probability ranges for each symbol
    symbol_probabilities=calculate_symbol_probabilities(user_message)
    
    # display the symbol probabilities
    print("\n Symbol Probability Ranges (Cumulative):")
    for symbol,(low,high) in symbol_probabilities.items() :
        print(f"'{symbol}': ({low:.4f}, {high:.4f})")  # display symbol's range

    # encode the message using Arithmetic Coding
    encoded_value=encode_message(user_message,symbol_probabilities)
    print(f"\n Encoded Value : {encoded_value:.10f}")

    # decode the encoded message to verify
    decoded_message = decode_message(encoded_value,symbol_probabilities,len(user_message))
    print(f" Decoded Message : {decoded_message}")

    # verify if decoding was successful
    if decoded_message==user_message :
        print(" Success! The decoded message matches the original one.")
    else:
        print(" Something went wrong! The decoded message does not match.")

main()
# END
