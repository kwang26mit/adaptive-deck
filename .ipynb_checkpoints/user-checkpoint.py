def u_full_automatic():
    ''' user interface for full-automatic mode '''
    print("Welcome to Full-Automatic mode. Here, you can specify a topic and quantity, and this program will generate a deck.")
    
    topic = input("Please enter a topic: ")
    quantity = input("Please enter a quantity: ")
    ex = input("Would you like to generate example sentences? This will take longer. (yes/no) ")
    ex = True if ex == 'yes' else False
    ctx = input("Would you like to generate use cases? (yes/no) ")
    ctx = True if ctx == 'yes' else False
    
    while True:
        print("Please wait a moment.")
        print()

        deck = []
        while len(deck) == 0:
            deck = full_automatic(topic, quantity, example=ex, context=ctx)

        print("Your deck has been completed.")
        print()
        print(f"Here is your {quantity}-card deck on {topic}:")
        
        for i, card in enumerate(deck):
            print(f"{i + 1}) {card}")        
        
        regen = ''
        while regen != 'yes' and regen != 'no':
            regen = input("Are you satisfied? (yes/no) ")
        if regen == 'yes':
            print("Thank you for using Adaptive Deck. You can access your deck from the output.")
            save_cards(deck)
            return deck

def u_full_automatic_text():
    ''' user interface for full-automatic text mode '''
    print("Welcome to Full-Automatic Text mode. Here, you can specify a text and quantity, and this program will generate a deck.")
    
    text = input("Please enter a short text: ")
    quantity = input("Please enter a quantity: ")
    ex = input("Would you like to generate example sentences? This will take longer. (yes/no) ")
    ex = True if ex == 'yes' else False
    ctx = input("Would you like to generate use cases? (yes/no) ")
    ctx = True if ctx == 'yes' else False
    
    while True:
        print("Please wait a moment.")
        print()

        deck = []
        while len(deck) == 0:
            deck = full_automatic_text(text, quantity, example=ex, context=ctx)

        print("Your deck has been completed.")
        print()
        print(f"Here is your {quantity}-card deck generated from your given text:")
        
        for i, card in enumerate(deck):
            print(f"{i + 1}) {card}")        
        
        regen = ''
        while regen != 'yes' and regen != 'no':
            regen = input("Are you satisfied? (yes/no) ")
        if regen == 'yes':
            print("Thank you for using Adaptive Deck. You can access your deck from the output.")
            save_cards(deck)
            return deck

def u_un_automatic():
    ''' user interface for un-automatic mode '''
    print("Welcome to Unautomatic mode. Here, you can upload a pre-existing deck, and this program will generate a new deck with added components.")

    finish = ''
    while finish != 'yes':
        finish = input("Please upload your current deck. Once you have finished uploading, please enter \"yes\". )
    
    print("These are the uploaded files.")
    files = [f[0] + '/' + f[2][0] for f in os.walk('../input/') if len(f[2]) > 0 and f[2][0].endswith('.txt')]
    
    for i, f in enumerate(files):
        print(f'\t{i + 1}){f}')
        
    num = ''
    while num not in [str(i + 1) for i in range(len(files))]:
        num = input("Please choose a file: ")

    num = int(num)
    file = files[num - 1]
        
    ex = input("Would you like to generate example sentences? This will take longer. (yes/no) ")
    ex = True if ex == 'yes' else False
    ctx = input("Would you like to generate use cases? (yes/no) ")
    ctx = True if ctx == 'yes' else False
    
    while True:
        print("Please wait a moment.")
        print()

        deck = []
        while len(deck) == 0:
            deck = un_automatic(file, example=ex, context=ctx)

        print("Your deck has been completed.")
        print()
        print("Here is your augmented deck.")
        
        for i, card in enumerate(deck):
            print(f"{i + 1}) {card}")        
        
        regen = ''
        while regen != 'yes' and regen != 'no':
            regen = input("Are you satisfied? (yes/no) ")
        if regen == 'yes':
            print("Thank you for using Adaptive Deck. You can access your deck from the output.")
            save_cards(deck)
            return deck