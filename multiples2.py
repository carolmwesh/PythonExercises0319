
import logging
logging.basicConfig(level=logging.ERROR)

def multiples_of_five_upto_hundred(num):
    output = []
    try:
        int(num)
    except ValueError:
        #return False       
        logging.error('Error! Please use a digit value')
        
    if num <= 1 or num >=101:
        #return False
        #logging.basicConfig(level=logging.ERROR)
        logging.error('Enter a number between 2 and 100!')
        
    for element in range(2, num):
        if element % 5 != 0:
            continue
        output.append(element)
    return output


