# Luhn Filter in Python
#### This is a Luhn Filter exercise from the Python track of exercism.io.  Goal was to intake a string and identify if it meets Luhn filter critera. Every other number starting from the right is doubled and if it is greater than 9 than 9 is subtracted from it.  If the sum is divisible by 10 then it is valid. Only valid characters are positive integers and spaces.  The value cannot be 0.


#### Implementation code is in luhn.py
#### Example tests from exercism where showing input and output as first and second parameters into assertEqual.
```
    def test_invalid_credit_card(self):
        self.assertIs(Luhn("8273 1232 7352 0569").is_valid(), False)

    def test_valid_number_with_an_even_number_of_digits(self):
        self.assertIs(Luhn("095 245 88").is_valid(), True)
```