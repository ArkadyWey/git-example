def greeter(user_name: str) -> None:
    greeting_string = f"Hello {user_name}!"
    print(greeting_string)
    print("hello from feature_1")


if __name__ == "__main__":
    name = input("Please enter your name: ")
    greeter(name)
