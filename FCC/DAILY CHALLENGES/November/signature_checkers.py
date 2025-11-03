import string

def verify(message, key, signature):
    # just assigning both capitalized and non-capitalized alphabets to their variables
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    # empty dictionary so that I can give each letter their respective value
    numbs = {

    }

    # the actual process of assigning the values 
    for i, char in enumerate(alphabet_lower, 1):
        numbs[char] = i



    for n, char in enumerate(alphabet_upper, 27):
        numbs[char] = n
    
    # computing the sum of the message and key

    msg_sum = sum(numbs[char] for char in message if char.isalpha())
    key_sum = sum(numbs[char] for char in key if char.isalpha())



    return signature == msg_sum + key_sum

print(verify("Is this valid?","no",57))