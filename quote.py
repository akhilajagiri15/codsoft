def get_quote():
    """
    Function to return a quote.
    """
    # You can replace this with any source of quotes you prefer
    quote = "This is a sample quote. Make each day your masterpiece!"
    return quote

def main():
    """
    Main function to run the quote app.
    """
    name = input("Enter your name: ")
    print(f"\nHello, {name}! Here's a quote for you:")
    print(get_quote())

if __name__ == "__main__":
    main()
