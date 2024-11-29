class Flashcard:
    def __init__(self, english, japanese, ex_sentence=None, context=None):
        self.en = english
        self.jp = japanese
        self.ex = ex_sentence
        self.ctx = context
    
    def __str__(self):
        description = f'\t英語：{self.en} \n\t日本語：{self.jp}\n'
        if self.ctx is not None:
            description += f'\t使用事例：{self.ctx}\n'
        
        if self.ex is not None:
            for i, ex in enumerate(self.ex):
                description += f"\t{i + 1}) {ex}\n"
        return description

def save_cards(cards):
    output_path = 'outputs/output.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        for card in cards:
            card_str = f'{card.en};{card.jp}'
            if card.ex:
                card_str += ';'
                for sentence in card.ex:
                    card_str += sentence + "<br>"
            if card.ctx:
                card_str += f';{card.ctx}'
            f.write(card_str+'\n')