def do_stuff(number=0):
    '''
    Simple function 
    '''
    try:
        if number:
            return int(number) + 5
        else:
            return 'Please enter a number'
    except ValueError as err:
        return (err)
