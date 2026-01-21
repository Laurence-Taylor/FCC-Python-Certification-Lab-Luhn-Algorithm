def verify_card_number(card):
    # Delete spaces and minus sign
    card_number = card.replace(" ","").replace("-","")
    # Invert Card Number
    card_number_inverted = card_number[::-1]
    total_sum = 0
    # For each element in the inverted card number
    for i in range(len(card_number_inverted)):
        # Check if is an even digit
        if ((i+1)%2) == 0:
            # Duplicate de digit
            duplicated_digit = int(card_number_inverted[i]) * 2
            # If result has two digits
            if duplicated_digit > 9:
                # Delete 9 to the duplicated_digit and sum to the total
                total_sum += (duplicated_digit - 9)
            else:
                # Sum duplicated_digit to the total
                total_sum += duplicated_digit
        else:
            # Sum the digit to the total
            total_sum +=  int(card_number_inverted[i])
    # Return vaid total
    if total_sum % 10 == 0:
        return 'VALID!'
    return 'INVALID!'
if __name__ == '__main__':
    print(verify_card_number('4111-1111-1111-1111'))