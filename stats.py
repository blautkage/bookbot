def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    lowercase = text.lower()
    counts = {}
    for char in lowercase:
        if char in counts:
            counts[char] = counts[char] +1
        else:
            counts[char] = 1
    return counts
        
def sort_on(item):
    return item["num"]

def report_sort(counts):
    character_list = []
    for k, v in counts.items():
        character_list.append({"char": k, "num": v})
    character_list.sort(reverse=True, key=sort_on)
    return character_list