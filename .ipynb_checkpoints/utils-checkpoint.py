def translate(card):
    ''' translates english card into japanese '''

    def parse_translate(card, result):
        ''' parses flashcard translation result '''
        pattern = r'[^\u3040-\u30FF\u4E00-\u9FFF\u3000-\u303F\uFF01-\uFF5E]'
        result = re.sub(pattern, '', result)
        
        return Flashcard(card, result)

    prompt = f'English: {card} \nJapanese: '
    result = Flashcard('', '')
    while result.jp.strip() == '':
        response = query_model(model, system_info_translate, ex_prompts_translate + prompt)
        result = get_answer(response)
        result = parse_translate(card, result)
    return result

def ex_sent(word):
    ''' generates example sentences for english word '''

    def parse_ex(result):    
        result = re.findall(r'\d+[.)]\s+([^\n]+)\n', result)
        result = [r.strip('\n') for r in result]
        if len(result) > 3:
            result = result[:3]
        return result

    prompt = f'Word: {word} \nExample Sentences: '
    response = query_model(model, system_info_ex, ex_prompts_ex + prompt)
    result = get_answer(response)
    return parse_ex(result)

def ctx(word):
    ''' generates use case for english word '''
    
    def parse_ctx(result):
        ind = result.index("Context: ")
        result = result[ind + len("Context: "):]
        return result
    
    prompt = f'Word: {word} \nContext: '
    response = query_model(model, system_info_ctx, ex_prompts_ctx + prompt)
    result = get_answer(response)
    return parse_ctx(result)
