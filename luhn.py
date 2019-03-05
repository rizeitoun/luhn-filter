# Intakes a string and performs a Luhn filter.  With this, every other number starting from the right is doubled and if it is greater than 9 than 9 is subtracted from it.  If the sum is divisible by 10 then it is valid. Only valid characters are positive integers and spaces.  The value cannot be 0.

class Luhn(object):
    # Intake and removed spaces
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def process_card(self):
        # Tests for digits then modifies every value from the right.
        if self.card_num.isdigit():
            card = list(map(int,list(self.card_num)))
            if len(card) % 2 == 0:
                start = 0
            else:
                start = 1

            for i in range(start,len(card),2):
                card[i] = self.apply_transform(card[i])
            self.luhn_card = card
        else:
            self.luhn_card = [0]

    # Luhn individual value transformation.
    def apply_transform(self,i):
        temp = 2*i
        if temp > 9:
            return temp-9
        return temp

    # Tests validity
    def is_valid(self):
        self.process_card()
        if sum(self.luhn_card) % 10 == 0 and len(self.luhn_card) > 1:
            return True
        return False

# Example test case
if __name__ == "__main__":
    Luhn("095 245 88").is_valid()