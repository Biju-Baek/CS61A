def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. If multiple words are tied for the smallest difference,
    return the one that appears closest to the front of WORD_LIST. If the
    difference is greater than LIMIT, instead return TYPED_WORD.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    if typed_word in word_list:
        return typed_word
    
    closest_word = min(word_list, key = lambda word: diff_function(typed_word, word, limit))
    
    if diff_function(typed_word, closest_word, limit)> limit:
        return typed_word
    else:
        return closest_word
    # END PROBLEM 5
    
    
limit=10
typed_word='cul'
word_list = ['culture', 'cult', 'cultivate']

autocorrect(typed_word, word_list, diff_function, limit