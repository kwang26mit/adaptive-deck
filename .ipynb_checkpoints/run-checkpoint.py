def run():
    print("Adaptive Deck.")
    print("Welcome to your Adaptive Deck!\n")
    intro = '''Adaptive Deck is for intermediate Japanese learners of English. To help the user better memorize vocabulary, Adaptive Deck allows the user to generate a personalized deck of flashcards. The following are the currently supported modes.

    1) Full-Automatic
    2) Full-Automatic Text
    3) Unautomatic

    At the end, you will receive your file that so that you can upload your deck to Anki.
    '''
    print(intro)

    mode = ''
    while mode not in ['1', '2', '3']:
        mode = input('Choose a mode: ')
    print()

    if int(mode) == 1:
        deck = full_automatic()
    elif int(モード) == 2:
        deck = full_automatic_text()
    elif int(モード) == 3:
        deck = un_automatic()

run()
