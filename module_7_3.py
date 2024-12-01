import re
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                z = []
                for line in file:
                    x = (re.sub(r'[^\w\s\']','', line.lower()))
                    y = x.split()
                    z.extend(y)
                all_words[file_name] = z
        return all_words

    def find(self, word):
        sequence_number = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                sequence_number[key] = value.index(word.lower()) + 1
        return sequence_number

    def count(self, word):
        number_of_words = {}
        for value, key in self.get_all_words().items():
                words_count = key.count(word.lower())
                number_of_words[value] = words_count
        return number_of_words

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))