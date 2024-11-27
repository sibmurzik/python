#"Оператор "with"
import re
import string


class WordsFinder:
    def __init__(self, *args):
        self.file_names = []
        for name in args:
            self.file_names.append(name)

    def get_all_words(self):
        words_dict = {}
        #print(string.punctuation)
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                line = file.read()
                mod_line = (regex.sub('', line).lower()).split()
                #print(mod_line)
            words_dict[name] = mod_line
        return words_dict

    def find(self, word):
        mod_word = word.lower()
        words_dict = self.get_all_words()
        finding_dict = dict()
        for key, value in words_dict.items():
            if mod_word in value:
                finding_dict[key] = value.index(mod_word)+1
        return finding_dict

    def count(self, word):
        mod_word = word.lower()
        words_dict = self.get_all_words()
        count_dict = dict()
        for key, value in words_dict.items():
            if mod_word in value:
                count_dict[key] = value.count(mod_word)
        return count_dict

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёт
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))