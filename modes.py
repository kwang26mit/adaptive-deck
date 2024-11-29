def full_automatic(topic, quantity, example=False, context=False):
    ''' create a deck using full-automatic mode'''

    def parse_fullauto(result):
        ''' parses full-automatic model result '''
        
        result = re.findall(r'\d+[.)]\s+([\w\s]+)\n', result)
        result = [r.strip('\n') for r in result]
        return result
    
    english_prompt = f'Topic: {topic}\nQuantity: {quantity}\nFlashcards:'
    english_response = query_model(model, system_info_fullauto, ex_prompts_fullauto + english_prompt)
    english_result = get_answer(english_response)
    english_cards = parse_fullauto(english_result)
    japanese_cards = []
    
    for en_card in english_cards:
        jp_card = translate(en_card)
        if example:
            jp_card.ex = ex(en_card)
        if context:
            jp_card.ctx = translate(ctx(en_card)).jp
        
        japanese_cards.append(jp_card)
    return japanese_cards

def full_automatic_text(text, quantity, example=False, context=False):
    ''' create a deck using full-automatic text mode'''

    def parse_fullautotext(result):
        ''' parses full-automatic text model result '''
        
        result = re.findall(r'\d+[.)]\s+([\w\s]+)\n', result)
        result = [r.strip('\n') for r in result]
        return result
    
    english_prompt = f'Text: {text}\nQuantity: {quantity}\nFlashcards:'
    english_response = query_model(model, system_info_fullautotext + ex_prompts_fullautotext, english_prompt)
    english_result = get_answer(english_response)
    english_cards = parse_fullautotext(english_result)
    japanese_cards = []
    
    for en_card in english_cards:
        jp_card = translate(en_card)
        if example:
            jp_card.ex = ex(en_card)
        if context:
            jp_card.ctx = translate(ctx(en_card)).jp
        
        japanese_cards.append(jp_card)
    return japanese_cards

def un_automatic(path, example=False, context=False):
    '''　create a deck using unautomatic mode　'''
    
    cards = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if line[0] == '#':
                continue
            line = line.strip()
            fields = [line]
            if '\t' in line:
                fields = line.split('\t')
            if ',' in line:
                fields = line.split(',')
            elif ';' in line:
                fields = line.split(';')
            cards.append(Flashcard(fields[0], fields[1]))
    
        for card in cards:
            if example:
                card.ex = ex(card)
            if context:
                card.ctx = translate(ctx(card)).jp

    return cards

