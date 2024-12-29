import u2lang as u2

while True:
    text = input('uulang > ')
    result, error = u2.run(text)

    if error:
        print(error.print_error())
    else: print(result)