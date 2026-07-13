def divide_numbers(a: str, b: str) -> None:
    try:
        print(int(a)/int(b))
    except Exception as er:
        print("An error occurred:", er)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
