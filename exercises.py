
def reverse_list(l):
    l2=[]
    for i in range(len(l)):
	    l2.append(l[len(l)-i-1])
    return l2

def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


# ------------------------------------------------------------------------------

def reverse_string(s):
    s2=""
    for i in range(len(s)):
            s2+=s[len(s)-i-1]
    return s2

def test_reverse_string():
    assert reverse_string("foobar") == "raboof"


# ------------------------------------------------------------------------------

def is_english_vowel(c):
	if c in "euioayEYUIOA":
		return True

def test_is_english_vowel():
    assert is_english_vowel('a')
    assert is_english_vowel('e')
    assert is_english_vowel('i')
    assert is_english_vowel('o')
    assert is_english_vowel('u')
    assert is_english_vowel('y')
    assert is_english_vowel('A')
    assert is_english_vowel('E')
    assert is_english_vowel('I')
    assert is_english_vowel('O')
    assert is_english_vowel('U')
    assert is_english_vowel('Y')
    assert not is_english_vowel('k')
    assert not is_english_vowel('z')
    assert not is_english_vowel('?')


# ------------------------------------------------------------------------------

def count_num_vowels(s):
    nr=0
    for element in s:
    	if element in "euioayEYUIOA":
    		nr=nr+1
    return nr

def test_count_num_vowels():
    sentence = "hey ho let's go"
    assert count_num_vowels(sentence) == 5
    sentence = "HEY ho let's GO"
    assert count_num_vowels(sentence) == 5
    paragraph = """She told me her name was Billie Jean,
                   as she caused a scene
                   Then every head turned with eyes
                   that dreamed of being the one
                   Who will dance on the floor in the round"""
    assert count_num_vowels(paragraph) == 54


# ------------------------------------------------------------------------------

def histogram(l):
    hist=""
    for i in l:
        hist+=('#'*i)
        hist+=('\n')
    hist=hist[:-1]
    return hist


def test_histogram():
    assert histogram([2, 5, 1]) == '##\n#####\n#'


# ------------------------------------------------------------------------------

def get_word_lengths(s):
    list=s.split(sep=' ')
    word_length=[]
    for i in list:
    	word_length.append (len(i))
    return word_length


def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]


# ------------------------------------------------------------------------------

def find_longest_word(s):
    a=max(s.split(' '), key=len)
    return a

def test_find_longest_word():
    text = "Three tomatoes are walking down the street"
    assert find_longest_word(text) == "tomatoes"
    text = "foo foo1 foo2 foo3"
    assert find_longest_word(text) == "foo1"


# ------------------------------------------------------------------------------
def validate_dna(s):
    a=len(s)
    b=0
    for element in s:
        if element in "agctAGCT":
            b=b+1
    if a==b:
        answer = True
    else:
        answer = False
    return answer

def test_validate_dna():
    assert validate_dna('CCGGAAGAGCTTACTTAGccggaagagcttacttag')
    assert not validate_dna('xCCGGAAGAGCTTACTTAGccggaagagcttacttag')


# ------------------------------------------------------------------------------
def base_pair(c):
    bp = ''
    if c in 'aA':
        bp = 't'
    elif c in 'tT':
        bp = 'a'
    elif c in 'gG':
        bp = 'c'
    elif c in 'cC':
        bp = 'g'
    else:
        bp = 'unknown'
    return bp

def test_base_pair():
    assert base_pair('a') == 't'
    assert base_pair('t') == 'a'
    assert base_pair('c') == 'g'
    assert base_pair('g') == 'c'
    assert base_pair('A') == 't'
    assert base_pair('T') == 'a'
    assert base_pair('C') == 'g'
    assert base_pair('G') == 'c'
    assert base_pair('x') == 'unknown'
    assert base_pair('foo') == 'unknown'


# ------------------------------------------------------------------------------
def transcribe_dna_to_rna(s):
    rna_string=""
    for element in s:
    	if element in 'tT':
    	    rna_string += 'U'
    	else:
    	    rna_string += element.upper()
    return rna_string

def test_transcribe_dna_to_rna():
    dna = 'CCGGAAGAGCTTACTTAGccggaagagcttacttag'
    assert transcribe_dna_to_rna(dna) == 'CCGGAAGAGCUUACUUAGCCGGAAGAGCUUACUUAG'


# ------------------------------------------------------------------------------
def get_complement(s):    
    complement = ""
    for element in s:
        if element in 'aA':
            complement += 'T'
        elif element in 'tT':
            complement += 'A'
        elif element in 'gG':
            complement += 'C'
        elif element in 'cC':
            complement += 'G'
    return complement

def test_get_complement():
    assert get_complement('CCGGAAGAGCTTACTTAG') == 'GGCCTTCTCGAATGAATC'
    assert get_complement('ccggaagagcttacttag') == 'GGCCTTCTCGAATGAATC'


# ------------------------------------------------------------------------------

def get_reverse_complement(s):
    complement = ""
    for element in s:
        if element in 'aA':
            complement += 'T'
        elif element in 'tT':
            complement += 'A'
        elif element in 'gG':
            complement += 'C'
        elif element in 'cC':
            complement += 'G'
    return complement[::-1]

def test_get_reverse_complement():
    assert get_reverse_complement('CCGGAAGAGCTTACTTAG') == 'CTAAGTAAGCTCTTCCGG'
    assert get_reverse_complement('ccggaagagcttacttag') == 'CTAAGTAAGCTCTTCCGG'


# ------------------------------------------------------------------------------

def remove_substring(substring, string):
    a=string.replace(substring,"")
    return a

def test_remove_substring():
    assert remove_substring('GAA', 'CCGGAAGAGCTTACTTAG') == 'CCGGAGCTTACTTAG'
    assert remove_substring('CCG', 'CCGGAAGAGCTTACTTAG') == 'GAAGAGCTTACTTAG'
    assert remove_substring('TAG', 'CCGGAAGAGCTTACTTAG') == 'CCGGAAGAGCTTACT'
    assert remove_substring('GAA', 'GAAGAAGAA') == ''


# ------------------------------------------------------------------------------

def get_position_indices(triplet, dna):
    triplet_indexes=[]
    triplets = [dna[i:i+3] for i in range(0, len(dna), 3)]
    for i, j in enumerate(triplets):
        if j == triplet:
            triplet_indexes.append(i)
    return triplet_indexes

def test_get_position_indices():
    assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAG') == [1]
    assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAGGAAGAA') == [1, 6, 7]


# ------------------------------------------------------------------------------

def get_3mer_usage_chart(s):
    result=[]
    a = sorted([s[i:i+3] for i in range(len(s)-2)])
    b =sorted(set(a))
    for i in b:
        c=a.count(i)
        result.append((i,c))
    return result

def test_get_3mer_usage_chart():
    s = 'CCGGAAGAGCTTACTTAGGAAGAA'
    result = []
    result.append(('AAG', 2))
    result.append(('ACT', 1))
    result.append(('AGA', 2))
    result.append(('AGC', 1))
    result.append(('AGG', 1))
    result.append(('CCG', 1))
    result.append(('CGG', 1))
    result.append(('CTT', 2))
    result.append(('GAA', 3))
    result.append(('GAG', 1))
    result.append(('GCT', 1))
    result.append(('GGA', 2))
    result.append(('TAC', 1))
    result.append(('TAG', 1))
    result.append(('TTA', 2))
    assert get_3mer_usage_chart(s) == result


# ------------------------------------------------------------------------------
def read_column(file_name, column_number):
    output=[]
    with open(file_name, 'r') as f:
        for line in f:
            value = line.split()[column_number-1]
            output.append(float(value))
    return output

def test_read_column():

    import tempfile
    import os

    text = """1   0.1  0.001
2   0.2  0.002
3   0.3  0.003
4   0.4  0.004
5   0.5  0.005
6   0.6  0.006"""

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:
        f.write(text)

    # and now we pass the file name to the function which will read the column
    assert read_column(file_name, 2) == [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

    # we remove the temporary file
    os.unlink(file_name)


# ------------------------------------------------------------------------------
def character_statistics(file_name):
    d = {}
    with open(file_name, 'r') as f:
        for c in f.read().lower():
            if c.isalpha():
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
    # convert dictionary into a list of tuples
    l = list(d.items())
    # reverse sort list on the second items of tuples
    l = sorted(l, key=lambda x: x[1], reverse=True)
    most = l[0][0]
    least = l[-1][0]
    return (most, least) 

def test_character_statistics():

    import tempfile
    import os

    text = """
To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep;
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep: perchance to dream: ay, there's the rub;
For in that sleep of death what dreams may come
When we have shuffled off this mortal coil,
Must give us pause: there's the respect
That makes calamity of so long life;
For who would bear the whips and scorns of time,
The oppressor's wrong, the proud man's contumely,
The pangs of despised love, the law's delay,
The insolence of office and the spurns
That patient merit of the unworthy takes,
When he himself might his quietus make
With a bare bodkin? who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscover'd country from whose bourn
No traveller returns, puzzles the will
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience does make cowards of us all;
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry,
And lose the name of action.--Soft you now!
The fair Ophelia! Nymph, in thy orisons
Be all my sins remember'd."""

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:
        f.write(text)

    # and now we pass the file name to the function which will get the stats
    (most_abundant, least_abundant) = character_statistics(file_name)
    assert (most_abundant, least_abundant) == ('e', 'q')

    # we remove the temporary file
    os.unlink(file_name)


# ------------------------------------------------------------------------------

def pythagorean_triples(n):
    """
    Returns list of all unique pythagorean triples
    (a, b, c) where a < b < c <= n.
    """
    l = []
    # loop over all a < b < c <= n
    for c in range(1, n + 1):
        for b in range(1, c):
            for a in range(1, b):
                if a*a + b*b == c*c:
                    l.append((a, b, c))
    return l


# ------------------------------------------------------------------------------

def test_pythagorean_triples():
    assert pythagorean_triples(5) == [(3,4,5)]
    assert pythagorean_triples(15) == [(3,4,5),(6,8,10),(5,12,13),(9,12,15)]

