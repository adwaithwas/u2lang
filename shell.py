import u2lang as u2

while True:
    text = input('~~ ')
    result, error = u2.run(text)

    if text == 'u2.exit':
        print('Thank you for Trying u2lang :)')
        break
    
    if error:
        print(error.print_error())
    else: print(result)