def verify_card_number(card):
    # Delete spaces and minus sign
    card_number = card.replace(" ","").replace("-","")
    # Invert Card Number
    card_number_inverted = card_number[::-1]
    total_sum = 0
    # For each element in the inverted card number
    for i in range(1,len(card_number_inverted)):
        if (i%2) == 0:
            duplicate_digit = int(card_number_inverted[i]) * 2
            if duplicate_digit > 9:
                total_sum += (duplicate_digit - 9)
            else:
                total_sum += duplicate_digit
        else:
            total_sum +=  int(card_number_inverted[i])
    return total_sum
if __name__ == '__main__':
    print(verify_card_number('4111-1111-1111-1111'))