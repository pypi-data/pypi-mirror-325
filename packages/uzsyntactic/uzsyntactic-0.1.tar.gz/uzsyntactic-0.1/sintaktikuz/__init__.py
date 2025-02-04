import pandas as pd
import csv
import re

# Step 1: Load root.csv containing root words and categories
def load_root_words(csv_file):
    try:
        df = pd.read_csv(csv_file, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(csv_file, encoding='ISO-8859-1')
    
    # Normalize apostrophes in the root words
    df['lotin'] = df['lotin'].str.replace('.', '').str.replace('`', '`').str.replace('’', '`').str.lower()
    return df

# Step 2: Tokenize the sentence into words, standardizing apostrophes

def tokenize(sentence):
    # Normalize apostrophes in the input sentence
    normalized_sentence = sentence.replace('`', '`').replace('’', '`')
    
    # Remove punctuation except for backticks (`) and hyphens (-) within words
    normalized_sentence = re.sub(r'(?<!\w)-|-(?!\w)|[^\w\s`-]', '', normalized_sentence)  # Keep hyphens in words
    normalized_sentence = re.sub(r'\s+', ' ', normalized_sentence)  # Replace multiple spaces with one
    
    # Split into tokens
    return [token.lower() for token in normalized_sentence.strip().split()]



# Enhanced stemmer to handle verb suffixes
def stem_word(word):
    # Separate suffixes by type
    noun_suffixes = ['i', 'ka', 'dagi', 'im', 'larim', 'lari', 'larni', 'ni', 'ga', 'dan', 'lar', 'ning', 'da', 'ngiz']
    verb_suffixes = ['m', 'ib', 'yapman', 'aman', 'yapsan', 'yapti', 'yapmiz', 'yapsiz', 'yaptilar',
                     'dim', 'di', 'dik', 'ganman', 'gansan', 'gan', 'ganmiz', 'ganlar',
                     'man', 'san', 'miz', 'siz', 'moqdalar']
    adjective_suffixes = ['lik', 'li', 'siz', 'dor', 'viy', 'gina', 'qina', 'roq', 'tar', 'simon']

    suffixes = noun_suffixes + verb_suffixes + adjective_suffixes

    # Sort suffixes by length to prioritize longer matches
    suffixes = sorted(suffixes, key=len, reverse=True)

    # Check for suffixes and remove them
    for suffix in suffixes:
        if len(word) > len(suffix) and word.endswith(suffix):
            return word[:-len(suffix)], suffix  # Return the root word and the stripped suffix
    return word, ''  # If no suffix found, return the word itself

# Step 3: Get word categories for each token along with the line number
def get_word_categories(tokens, root_df):
    categories = []
    line_numbers = []  # To store line numbers of root words in root.csv
    
    for token in tokens:
        token_lower = token.lower()
        
        # First, check the original word directly in root.csv
        match = root_df[root_df['lotin'] == token_lower]
        if not match.empty:
            category = match['turkum'].values[0]
            line_number = match.index[0]  # Get the line number (index) of the matched word
            categories.append(category)
            line_numbers.append(line_number)
            continue  # Skip stemming if exact match is found

        # If not found, apply stemming
        stemmed_token, suffix = stem_word(token_lower)
        match = root_df[root_df['lotin'] == stemmed_token]
        if not match.empty:
            category = match['turkum'].values[0]
            line_number = match.index[0]  # Get the line number (index) of the matched word
            categories.append(category)
            line_numbers.append(line_number)
        else:
            # If still not found, infer category based on the suffix
            if suffix in ['i', 'lik', 'lari', 'larni', 'ni', 'ga', 'dan', 'lar', 'ning', 'da']:  # Noun suffixes
                categories.append('NOUN')
                line_numbers.append(None)  # No match in root.csv
            elif suffix in ['m', 'yapman', 'aman', 'yapsan', 'yapti', 'yapmiz', 'yapsiz', 'yaptilar', 
                            'dim', 'di', 'dik', 'ganman', 'gansan', 'gan', 'ganmiz', 'ganlar',
                            'man', 'san', 'miz', 'siz', 'moqdalar']:  # Verb suffixes
                categories.append('VERB')
                line_numbers.append(None)  # No match in root.csv
            # Infer based on suffix or assign 'unknown'
            elif suffix == 'lik':  # Handle suffix-specific logic
                categories.append('ADJ')
                line_numbers.append(None)  # No match in root.csv
            else:
                categories.append('unknown')  # Default if word not found
                line_numbers.append(None)  # No match in root.csv
    
    return categories


# Step 4: Identify the subject (*ega*) based on specific rules
def find_ega(tokens, categories, identified_tokens=None):
    ega = None
    print(f"Tokens: {tokens}")
    print(f"Categories: {categories}")

    # Define common pronoun suffixes and their associated pronouns
    pronoun_suffixes = {
        'miz': 'Biz',  # We
        'man': 'Men',  # I
        'siz': 'Siz',  # You (formal)
        'san': 'Sen',  # You (informal)
        'lar': 'Ular',  # They
        'di': 'U',
    }
    
    # Define common pronoun suffixes and their associated pronouns
    pronoun_suffixes0 = {
        'miz': 'Biz',  # We
        'man': 'Men',  # I
        'siz': 'Siz',  # You (formal)
        'san': 'Sen',  # You (informal)
        'dim': 'Men',
    }

    # Excluded quantifiers that cannot serve as ega
    excluded_quantifiers = [
        'doim', 'har', 'ko`p', 'ko`plab', 'bir nechta', 'bir qancha', 'barcha', 'hamma', 'ba`zi', 'bir', 'oz', 'ozgina',
        'ko`pchilik', 'bir talay', 'bir qator', 'bir narsa', 'bir juft', 'yana', 'shuncha', 'bir oz',
        'hech kim', 'birorta', 'bittasi', 'bir to`da', 'deyarli', 'qanchadir', 'bir nechog`li'
    ]
    
    # List of words answering "where" question
    location_words = [
        'maktab', 'bog‘', 'bog‘cha', 'ko‘cha', 'uy', 'hovli', 'binolar', 'mehmonxona', 
        'katta bozor', 'choyxona', 'do‘kon', 'ofis', 'tosh', 'yangi mahalla', 'ko‘l', 
        'dengiz', 'orol', 'masjid', 'xonadon', 'yo‘lak', 'universitet', 'litsey', 
        'kollej', 'kutubxona', 'o‘quv markazi', 'oliy o‘quv yurtlari', 'park', 
        'chorvoq', 'tog‘', 'changalzor', 'sayilgoh', 'dalalar', 'xiyobon', 
        'shahar', 'suv havzasi', 'maydon', 'sport zali', 'bekat', 'avtovokzal', 
        'aeroport', 'temir yo‘l vokzali', 'stansiya', 'metro', 'avtomagistral', 
        'hokimiyat', 'poliklinika', 'shifoxona', 'davlat idoralari', 'bank', 'sud', 
        'vazirlik', 'elchixona', 'mahalla idorasi', 'kinoteatr', 'teatr', 'muzey', 
        'ko‘ngilochar markaz', 'stadion', 'amfiteatr', 'zoopark', 'galereya', 'plyaj', 
        'o‘yingoh', 'daryo', 'tog‘', 'cho‘l', 'vodiy', 'soy', 'kanyon', 'o‘rmon', 
        'qir', 'yaylov', 'qoya', 'toshkent', 'samarqand', 'buxoro', 'urganch', 'xiva', 
        'qarshi', 'navoiy', 'nukus', 'farg‘ona', 'andijon'
    ]
    
    locative_suffixes = {'da', 'dan', 'ga', 'ning'}  # Add as needed
    location_words = {'joy', 'shahar', 'maktab'}  # Context-specific location words
    personal_pronouns = ['men', 'sen', 'siz', 'u', 'biz', 'ular']
    
    excluded_suffixes = ['da', 'ni', 'ga', 'da', 'dan', 'bilan', 'im', 'ing', 'i', 'miz', 'ingiz', 'lari', 
                     'cha', 'chalik', 'dek', 'day', 'moq', 'ish', 'gan', 'uvchi', 'niki']

    
    # Ensure identified_tokens is not None
    if identified_tokens is None:
        identified_tokens = set()
        
    # Sequential rules for identifying ega
    for i, (word, category) in enumerate(zip(tokens, categories)):
        # Skip tokens already assigned to another role
        if word in identified_tokens:
            continue
        
        if any(word.endswith(suffix) for suffix in excluded_suffixes):
            continue  # Skip this word as it cannot be Ega

        # Skip locative/directional nouns or nouns in location words
        if any(word.endswith(suffix) for suffix in locative_suffixes) or word in location_words:
            continue    
        
        # Rule 8: Hidden Pronouns (Suffix-Based Inference)
        sorted_suffixes = sorted(pronoun_suffixes0.keys(), key=len, reverse=True)

        for i, word in enumerate(tokens):
            if i == len(tokens) - 1:  # Ensure we are checking the last word
                for suffix in sorted_suffixes:
                    if word.endswith(suffix):  # Match suffix at the end of the word
                        hidden_ega = pronoun_suffixes0[suffix]  # Get the implied pronoun
                        print(f"Hidden 'ega' found by Rule 8 (Suffix '{suffix}' in '{word}' implies '{hidden_ega}')")
                        ega = hidden_ega  # Set the hidden subject (ega)
                        identified_tokens.add(ega)
                        break

        for i, (word, category) in enumerate(zip(tokens, categories)):
            # Skip words after the predicate
            if i >= len(tokens):
                break

            # Prioritize animate nouns as ega
            if category == 'NOUN' and word.endswith('lar'):
                print(f"Ega found (Animate Noun): {word}")
                ega = word
                break

                
        if ega is None:
            if tokens[0] in personal_pronouns:
                print(f"Ega found by Rule 2 (Pronoun): {word}")
                ega = tokens[0]
                identified_tokens.add(ega)
                break
        
        # Rule 1: Explicit Nouns (apply only if no pronoun was found)
        if ega is None:
            for i, (word, category) in enumerate(zip(tokens, categories)):
                # Skip if the word ends with excluded suffixes or is a location word
                if word.endswith(('ni', 'da', 'dan')) or word in location_words:
                    continue

                # Allow directional nouns ('ga') only if contextually valid as Ega
                if word.endswith('ga') and (i + 1 < len(tokens) and categories[i + 1] == 'VERB'):
                    # Ensure the noun is not part of a location or directional phrase (Hol)
                    if word in location_words or any([suffix in word for suffix in ['qayerga', 'nimaga', 'kimga']]):
                        continue  # Skip as it's likely a Hol (Adverbial)

                    # Identify as Ega if no other valid Ega is found
                    if ega is None:
                        print(f"Ega found by Rule 1 (Directional Noun in Action Context): {word}")
                        ega = word
                        identified_tokens.add(ega)
                        break


                # Skip if the word is a quantifier
                if word in excluded_quantifiers:
                    continue

                # Exclude compound or descriptive forms ending with 'dagi', 'lik', etc.
                if word.endswith(('ga', 'dagi', 'lik', 'siz', 'dor')):
                    continue

                # Default to the first valid noun as Ega, ensuring it is not in an excluded form
                if category == 'NOUN':
                    print(f"Ega found by Rule 1 (Explicit Noun): {word}")
                    ega = word
                    identified_tokens.add(ega)
                    break

                    
        # Rule: Identify explicit nouns as Ega, including location words in certain contexts
        if category == 'NOUN' and word not in identified_tokens:
            # Exclude location words unless directly preceding or following a predicate
            if word in location_words and (i < len(categories) - 1 and categories[i + 1] == 'VERB'):
                print(f"Ega found by Rule (Location word acting as Subject): {word}")
                ega = word
                identified_tokens.add(word)
                break  # Stop further processing once Ega is found


        # Rule 2: Pronouns
        if ega is None:
            if category == 'P' and not word.endswith('ning'):
                print(f"Ega found by Rule 2 (Pronoun): {word}")
                ega = word
                identified_tokens.add(ega)
                break

        # Rule 3: Proper Nouns
        if category == 'PROPER_NOUN':
            print(f"Ega found by Rule 3 (Proper Noun): {word}")
            ega = word
            identified_tokens.add(ega)
            break
            

             # Rule 4: Compound Nouns
        if category == 'NOUN' and i > 0 and categories[i - 1] == 'NOUN':
            # Exclude locative nouns or nouns with possessive/adjectival suffixes
            locative_suffixes = ('da', 'dan', 'ga', 'dagi', 'ning')
            if word.endswith(locative_suffixes) or tokens[i - 1].endswith(locative_suffixes):
                continue  # Skip locative nouns

            # Ensure the first word is not a quantifier, adverb, or adjective
            excluded_categories = ['ADV', 'ADJ']
            if categories[i - 1] in excluded_categories or categories[i] in excluded_categories:
                continue  # Skip invalid combinations

            # Avoid including location words in compound nouns
            if tokens[i - 1] in location_words or word in location_words:
                continue
             
            # Confirm this is a valid compound noun and not a dependency of another role
            print(f"Ega found by Rule 4 (Compound Noun2): {tokens[i - 1]} {word}")
            ega = f"{tokens[i - 1]} {word}"
            identified_tokens.update([tokens[i - 1], word])  # Mark as identified
            break

        '''
        if category == 'NOUN' and i > 0 and categories[i - 1] == 'ADJ':
            # Skip locative/directional nouns or nouns in location words
            if any(word.endswith(suffix) for suffix in locative_suffixes) or word in location_words:
                continue

            # Check for compound adjectives
            compound_adj = []
            for j in range(i - 1, -1, -1):  # Traverse backward for consecutive ADJ
                if categories[j] == 'ADJ':
                    compound_adj.insert(0, tokens[j])
                else:
                    break

            # Identify Ega as Adjective-Noun Pair
            ega = f"{' '.join(compound_adj)} {word}"
            print(f"Ega found by Rule 5 (Compound Adjective-Noun Pair): {ega}")
            identified_tokens.update(compound_adj + [word])  # Add all tokens to identified

            # Recognize modifiers
            for adj in compound_adj:
                print(f"Aniqlovchi found by Rule (Adjective modifying Noun): {adj}")
            break
        '''

        # Rule 6: Infinitive Verbs as Subject
        if category == 'INF' and (i < len(categories) - 1 and categories[i + 1] == 'VERB'):
            print(f"Ega found by Rule 6 (Infinitive as Subject): {word}")
            ega = word
            identified_tokens.add(ega)
            break

        # Rule 7: Gerunds or "-chi" Suffix
        if category == 'GERUND' or word.endswith('chi'):
            print(f"Ega found by Rule 7 (Gerund or '-chi' Suffix): {word}")
            ega = word
            identified_tokens.add(ega)
            break
            
    # Rule 8: Hidden Pronouns (Suffix-Based Inference)
    if ega is None:  # Only proceed if no ega is found yet
        sorted_suffixes = sorted(pronoun_suffixes.keys(), key=len, reverse=True)
        for word in tokens:  # Iterate through all tokens
            for suffix in sorted_suffixes:
                if word.endswith(suffix):
                    print(f"Hidden 'ega' found by Rule 88 (Suffix '{suffix}' in '{word}' implies '{pronoun_suffixes[suffix]}')")
                    ega = pronoun_suffixes[suffix]
                    identified_tokens.add(ega)
                    break
            if ega:  # Exit if found
                print(f"'ega' already identified: {ega}, stopping suffix search.")
                break
                    
        
    # Rule 9: Fallback to First Noun
    if ega is None and categories[0] == 'NOUN':
        print(f"Ega found by Rule 9 (Fallback to First Word): {tokens[0]}")
        ega = tokens[0]
        identified_tokens.add(ega)

    # Final check
    if ega is None:
        print("No Ega found.")
    else:
        print(f"Ega found: {ega}")

    return ega


# Step 5: Identify kesim based on the rules (as you have already)
def find_kesim(tokens, categories, identified_tokens=None):
    kesim = None
    print(f"Tokens: {tokens}")
    print(f"Categories: {categories}")
    
    # Return None if tokens or categories are empty
    if not tokens or not categories:
        print("No tokens or categories left to process for Hol.")
        return None
    
    # Ensure identified_tokens is not None
    if identified_tokens is None:
        identified_tokens = set()
        
    # Rule 1: If the word is a conjugated finite verb (present, past, or future tense)
    for i, (word, category) in enumerate(zip(tokens, categories)):
        print(f"Checking word: {word}, Category: {category}")
        
        # Skip tokens already assigned to another role
        if word in identified_tokens:
            continue
            
       # Rule 1: Finite verb check (refined)
        if category == 'VERB' and is_finite_verb(word):
            # Check if this VERB is followed by a NOUN (indicating it might be a modifier)
            if i < len(categories) - 1 and categories[i + 1] == 'NOUN':
                print(f"Skipping {word}: Likely modifying {tokens[i + 1]}")
                continue

            # Check if this VERB is preceded by a NOUN it might modify
            if i > 0 and categories[i - 1] == 'NOUN' and word.endswith(('gan', 'uvchi')):
                print(f"Skipping {word}: Likely modifying {tokens[i - 1]}")
                continue

            # If not modifying, it's a finite verb (kesim)
            print(f"Kesim found by Rule 1 (finite verb): {word}")
            kesim = word
            break  # Kesim found, exit loop

        
        # Rule 1: Attach ADV modifying the verb to the kesim
        if category == 'ADV' and i < len(categories) - 1 and categories[i + 1] == 'NOUN' and  (i+1 == len(tokens) - 1):
            kesim = f"{word} {tokens[i + 1]}"
            print(f"Kesim found by ADV Rule: {kesim}")
            break

            
        # Rule 2: If a noun/adjective is the last word in the sentence, implying "bo`lmoq"
        if (category in ['NOUN', 'ADJ', 'V', 'VERB', 'ADV', 'EXL']) and (i == len(tokens) - 1):
            print(f"Kesim found by Rule 2 (implied 'bo`lmoq'): {word}")
            kesim = word
            break

        # Rule 3: If the current word is a noun or adjective and the next word is a verb (last word in the sentence)
        if category in ['NOUN', 'ADJ', 'VERB', 'V'] and categories[i + 1] == 'VERB' and i + 1 == len(tokens) - 1:
            # Check if the current word is part of a complement
            if word not in identified_tokens:  # Avoids combining complements
                kesim = f"{word} {tokens[i + 1]}"
                print(f"Kesim found by Rule 3 (compound verb): {kesim}")
                identified_tokens.add(word)
                identified_tokens.add(tokens[i + 1])
                return kesim



        # Rule 4: Gerund or infinitive verb form, followed by auxiliary verb (complex verb structure)
        if category == 'GERUND' and i < len(tokens) - 1:
            next_word = tokens[i + 1]
            next_category = categories[i + 1]
            if next_category == 'VERB' and is_auxiliary_verb(next_word):
                print(f"Kesim found by Rule 4 (gerund/infinitive + auxiliary verb): {word} {next_word}")
                kesim = f"{word} {next_word}"
                identified_tokens.add(word)
                identified_tokens.add(next_word)
                break

        # Rule 5: Modal verb (e.g., "kerak", "mumkin") followed by an infinitive verb
        if category == 'MODAL' and i > 0:
            prev_word = tokens[i - 1]
            prev_category = categories[i - 1]
            if prev_category == 'VERB':
                print(f"Kesim found by Rule 5 (modal + infinitive verb): {prev_word} {word}")
                kesim = f"{prev_word} {word}"
                identified_tokens.add(prev_word)
                identified_tokens.add(word)
                break

        # Rule 6: Adjective (or noun) with implied "bo`lmoq" in nominal sentences
        if category == 'ADJ' and i == len(tokens) - 1:
            print(f"Kesim found by Rule 6 (adjective at the end of sentence, implied 'bo`lmoq'): {word}")
            kesim = word
            identified_tokens.add(word)
            break

        # Rule 7: If a pronoun is the subject and followed by a noun/adjective, implying "bo`lmoq"
        if category in ['conditional', 'modal', 'pronoun']:
            print(f"Kesim found by Rule 7 (conditional/modal/pronoun): {word}")
            identified_tokens.add(word)
            return word

       # Qoida: Komplementni kesimga qo‘shish
        if kesim is None and category == 'VERB' and i > 0 and i == len(tokens) - 1:
            previous_word = tokens[i - 1]
            previous_category = categories[i - 1]

            # Check if the previous word is a complement and not part of the predicate
            if previous_category == 'NOUN' and not previous_word.endswith(('da', 'dan', 'ga', 'ning')):
                print(f"Toldiruvchi found: {previous_word}")
                toldiruvchi = previous_word
                identified_tokens.add(previous_word)

            # Assign the current word as Kesim
            print(f"Kesim found: {word}")
            kesim = word
            identified_tokens.add(word)
            break


        # Check for V_N followed by VERB and last word is the same VERB
        if category == 'V_N' and i < len(categories) - 1 and categories[i + 1] == 'VERB':
            # Check if the following verb is the last word or part of the compound Kesim
            if tokens[-1] == tokens[i + 1] or tokens[-1] in ['edi', 'bo‘ldi', 'qilgan']:
                compound_kesim = f"{word} {tokens[i + 1]}"
                print(f"Kesim found by Rule (V_N + Following Verb): {compound_kesim}")
                kesim = compound_kesim
                identified_tokens.add(word)
                identified_tokens.add(tokens[i + 1])
                break

       
    # New Rule: Last word with verb suffixes
    if kesim is None and is_finite_verb(tokens[-1]):
        print(f"Kesim found by New Rule (last word with verb suffixes): {tokens[-1]}")
        kesim = tokens[-1]

    return kesim

def find_aniqlovchi(tokens, categories, ega=None, identified_tokens=None):
    aniqlovchi = []
    print(f"Tokens: {tokens}")
    print(f"Categories: {categories}")

    # List of quantifiers (may act as aniqlovchi in specific contexts)
    quantifiers = [
        'doim', 'har', 'ko`p', 'ko`plab', 'bir nechta', 'bir qancha', 'barcha', 'hamma', 'ba`zi', 'bir', 'oz',
        'ozgina', 'ko`pchilik', 'bir talay', 'bir qator', 'bir narsa', 'bir juft', 'yana', 'shuncha', 'bir oz',
        'hech kim', 'birorta', 'bittasi', 'bir to`da', 'deyarli', 'qanchadir', 'bir nechog`li', 'joyda'
    ]

    # Return None if tokens or categories are empty
    if not tokens or not categories:
        print("No tokens or categories left to process for Aniqlovchi.")
        return None

    # Ensure identified_tokens is not None
    if identified_tokens is None:
        identified_tokens = set()

    # Apply rules sequentially to identify 'aniqlovchi'
    for i, (word, category) in enumerate(zip(tokens, categories)):
        # Skip tokens already assigned to another role
        if word in identified_tokens:
            continue

        # Exclude locative nouns from Aniqlovchi
        if category == 'NOUN' and word.endswith(('da', 'dan', 'ga')):
            continue
            
        # Exclude locative nouns from Aniqlovchi
        if category == 'ADV':
            continue

        # Exclude nouns with "-ni" if a verb exists and "-ni" noun is closer to the verb
        if category == 'NOUN' and word.endswith('ni') and 'VERB' in categories and categories.index('VERB') > i:
            continue

        # Rule 1: Verb acting as a modifier (Participial Verb modifying Noun, e.g., "yig'ilgan pullarini")
        if (category in ['VERB', 'V_PASS']) and i < len(categories) - 1 and categories[i + 1] == 'NOUN':
            # Ensure the verb is functioning as a participial modifier
            if not word.endswith('ni') and tokens[i + 1] not in identified_tokens:
                print(f"Aniqlovchi found by Rule 1 (Participial Verb modifying Noun): {word}")
                aniqlovchi.append(word)
                identified_tokens.add(word)
                continue



        # Rule 3: Quantifiers modifying nouns (e.g., "bir qancha kitoblar")
        if word in quantifiers and i < len(categories) - 1 and categories[i + 1] == 'NOUN':
            print(f"Aniqlovchi found by Rule 3 (Quantifier modifying Noun): {word}")
            aniqlovchi.append(word)
            identified_tokens.add(word)
            continue

        # Rule 4: Adjectives modifying nouns (e.g., "chiroyli uy")
        if category == 'ADJ' and i < len(categories) - 1 and categories[i + 1] == 'NOUN':
            print(f"Aniqlovchi found by Rule 4 (Adjective modifying Noun): {word}")
            aniqlovchi.append(word)
            identified_tokens.add(word)
            continue

        if category == 'NUM' and i < len(categories) - 2 and categories[i + 1] == 'NUM' and categories[i + 2] == 'NOUN':
            # Ensure the phrase modifies a noun or subject
            if categories[i - 1] in ['NOUN', 'P']:
                aniqlovchi_phrase = f"{word} {tokens[i + 1]} {tokens[i + 2]}"
                print(f"Aniqlovchi found by Quantifier Phrase Rule: {aniqlovchi_phrase}")
                aniqlovchi.append(aniqlovchi_phrase)
                identified_tokens.update(aniqlovchi.split())
                continue
        
        
        # Rule: Adjective modifying a Noun
        if category == 'ADJ' and i < len(categories) - 1 and categories[i + 1] == 'NOUN':
            print(f"Aniqlovchi found by Rule (Adjective modifying Noun): {word}")
            identified_tokens.add(word)
            aniqlovchi.append(word)
            continue
        
        # Rule 1: Pronoun modifying a Noun
        if category == 'P' and i < len(categories) - 1 and not word.endswith(('ga', 'ni')) and tokens[i] not in ['men', 'sen', 'biz', 'ular', 'siz', 'man']:
            if word in quantifiers:
                continue  # Skip quantifiers
            # Handle possessive pronoun ending with 'ning'
            if word not in identified_tokens:
                print(f"Aniqlovchi found by Rule 1 (Possessive Pronoun): {word}")
                aniqlovchi.append(word)
                identified_tokens.add(word)
            continue  # Stop after identifying the Aniqlovchi

        # Rule 2: Quantifier modifying Adverb or Noun
        if word in quantifiers and i < len(categories) - 1 and categories[i + 1] in ['NOUN', 'PROPER_NOUN', 'ADV']:
            print(f"Aniqlovchi found by Rule 2 (Quantifier modifying Adverb/Noun): {word}")
            if tokens[i-1] == 'har':
                aniqlovchi.append(tokens[i-1])
                aniqlovchi.append(word)
                identified_tokens.add(word)
                identified_tokens.add(tokens[i-1])
                continue
            else:
                aniqlovchi.append(word)
                identified_tokens.add(word)
                continue

        # Rule 3: Noun modifying another Noun
        if (
            not word.endswith('ni')  # Exclude accusative case
            and category == 'NOUN'
            and i < len(categories) - 1
            and categories[i + 1] == 'NOUN'
            and word != ega
        ):
            # List of compound heads to skip
            compound_heads = ['tomosha', 'sayohat']  # Add specific compound heads
            if tokens[i + 1] in compound_heads:
                # Ensure the first noun (e.g., 'film') is still identified if valid
                if word not in compound_heads:
                    print(f"Aniqlovchi found by Rule 3 (Part of Compound): {word}")
                    identified_tokens.add(word)
                    aniqlovchi.append(word)
                print(f"Skipping compound structure: {word} {tokens[i + 1]}")
                continue

            # List of compound exceptions to skip
            compound_exceptions = ['tuman', 'shahar', 'viloyat', 'universitet']  # Add specific exceptions
            if tokens[i + 1] in compound_exceptions or word in compound_exceptions:
                print(f"Skipping compound phrase: {word} {tokens[i + 1]}")
                continue

            # Identify as Aniqlovchi if no other skipping conditions apply
            print(f"Aniqlovchi found by Rule 3 (Noun modifying Noun): {word}")
            identified_tokens.add(word)
            aniqlovchi.append(word)





        # Rule 4: Gerund modifying Noun
        if category == 'GERUND' and i < len(categories) - 1 and categories[i + 1] in ['NOUN', 'PROPER_NOUN']:
            print(f"Aniqlovchi found by Rule 4 (Gerund modifying Noun): {word}")
            aniqlovchi.append(word)
            identified_tokens.add(aniqlovchi)
            continue

        # Rule 5: Proper Noun modifying another Noun
        if category == 'PROPER_NOUN' and i < len(categories) - 1 and categories[i + 1] == 'NOUN':
            print(f"Aniqlovchi found by Rule 5 (Proper Noun modifying Noun): {word}")
            aniqlovchi.append(word)
            identified_tokens.add(aniqlovchi)
            continue

        # Rule 6: Hidden aniqlovchi (Adjective modifying implied Noun)
        if category == 'ADJ' and i < len(categories) - 1 and categories[i + 1] in ['unknown', 'NOUN', 'PROPER_NOUN']:
            print(f"Aniqlovchi found by Rule 6 (Hidden Adjective modifying implied Noun): {word}")
            aniqlovchi.append(word)
            identified_tokens.add(aniqlovchi)
            continue
        
        #if category == 'NOUN' and not word.endswith(('da', 'dan', 'ga', 'bilan')) and i < len(categories) - 1:
        #    if categories[i + 1] in ['NOUN', 'ADJ']:
        #        aniqlovchi.append(word)
        #        aniqlovchi.append(tokens[i + 1])
        #        print(f"Aniqlovchi found by Rule (Noun modifying Noun): {aniqlovchi}")
        #        identified_tokens.add(word)  # Mark current token as identified
        #        identified_tokens.add(tokens[i + 1])  # Mark the next token as identified

        
        # Exclude adjectives that act as adverbs from Aniqlovchi
        if category == 'ADJ' and i < len(categories) - 1 and categories[i + 1] == 'VERB':
            print(f"Aniqlovchi excluded due to Adjective acting as Adverb: {word}")
            if word in aniqlovchi:
                aniqlovchi.remove(word)  # Remove from Aniqlovchi list if already added
            continue

    if not aniqlovchi:
        print("No Aniqlovchi found.")
        aniqlovchi = None
    else:
        aniqlovchi = ", ".join(aniqlovchi)
        print(f"Aniqlovchi: {aniqlovchi}")


    return aniqlovchi


def find_toldiruvchi(tokens, categories, ega=None, identified_tokens=None):
    toldiruvchi = []
    print(f"Tokens: {tokens}")
    print(f"Categories: {categories}")
    
    excluded_words = [
        'buning', 'u', 'ekan', 'ham', 'balki', 'shuning uchun', 'sababi', 'chunki', 'nega', 'yo', 'biroq', "qayerda", "qayerga", "qayerdan", "nimaga", "nima uchun", 
        "qachon", "qanday", "qancha", "necha", "kimga", "kimdan",
        "hozir", "kecha", "bugun", "ertaga", "bu yerda", "u yerda", 
        "yo‘lda", "tez", "asta", "juda", "har doim", "kamdan-kam", 
        "tez-tez",
        "bilan", "uchun", "oldin", "keyin", "ustida", "ostida",
        "va", "yoki", "lekin", "ammo", "shuningdek",
        "u", "bu", "shu", "o‘z",
        "bir", "ikki", "uchta",
        "voy", "eh", "ha", "yo‘q"
    ]
    
    personal_pronouns = ['men', 'sen', 'siz', 'u', 'biz', 'ular']


    # Return None if tokens or categories are empty
    if not tokens or not categories:
        print("No tokens or categories left to process for Toldiruvchi.")
        return None
    
    # Ensure identified_tokens is not None
    if identified_tokens is None or not isinstance(identified_tokens, set):
        identified_tokens = set()
        
    
    # Apply rules sequentially to identify 'toldiruvchi'
    for i, (word, category) in enumerate(zip(tokens, categories)):
        # Skip tokens already assigned to another role
        if word in identified_tokens:
            continue
        
        if word in excluded_words:
            continue
            
        # Exclude locative nouns from Aniqlovchi
        if word.endswith(('chi', 'uvchi', 'da', 'dan')) and category == 'NOUN':
            continue
        
        # Skip V_N if it's followed by a verb (part of the predicate)
        if category == 'V_N' and i < len(categories) - 1 and categories[i + 1] == 'VERB':
            print(f"Skipping V_N '{word}' as part of the predicate structure.")
            continue

        # Rule: Noun directly preceding a verb with 'ni' suffix
        if not toldiruvchi and category == 'NOUN' and i < len(categories) - 1 and categories[i + 1] == 'VERB':
            # Check if the verb ends with 'ni' and is not the last word
            if tokens[i + 1].endswith('ni') and i + 2 < len(categories):
                combined_toldiruvchi = f"{word} {tokens[i + 1]}"
                if combined_toldiruvchi not in toldiruvchi:
                    if tokens[i+1] not in identified_tokens:
                        toldiruvchi = [x for x in toldiruvchi if x != tokens[i+1]]
                        toldiruvchi.append(tokens[i + 1])
                    print(f"Toldiruvchi found by Rule (Noun + Verb with 'ni'): {combined_toldiruvchi}")
                    toldiruvchi.append(word)
                    identified_tokens.add(word)
                    identified_tokens.add(tokens[i + 1])
                    continue
            else:
                # Regular handling of noun preceding a verb
                if word not in toldiruvchi:
                    print(f"Toldiruvchi found by Additional Rule (Noun preceding Verb): {word}")
                    toldiruvchi.append(word)
                    identified_tokens.add(word)
                    continue

        if not toldiruvchi and category == 'NOUN' and word.endswith('ni'):
            if word not in toldiruvchi:
                toldiruvchi.append(word)
                print(f"Toldiruvchi found by Rule (Accusative Case): {word}")
            
        if not toldiruvchi and category == 'VERB' and word.endswith('ni'):
            if word not in toldiruvchi:
                print(f"Toldiruvchi found by Rule (Accusative Case2): {word}")
                toldiruvchi.append(word)
        
        if i > 0 and categories[i] == 'V_N' and not word.endswith('ga') and categories[i - 1] == 'NOUN':  # Check boundaries and conditions
            # Ensure it's not part of the predicate
            if i + 1 < len(categories) and categories[i + 1] == 'VERB':  # Verbal noun followed by a verb
                print(f"Skipping verbal noun '{tokens[i]}' as part of predicate structure.")
                continue

            phrase = f"{tokens[i - 1]} {tokens[i]}"  # Combine NOUN + V_N
            if phrase not in toldiruvchi:  # Ensure the phrase is not already added
                print(f"Toldiruvchi found by Rule (NOUN + Verbal Noun): {phrase}")
                
                # Remove individual tokens if they were previously added
                toldiruvchi = [x for x in toldiruvchi if x != tokens[i]]
                toldiruvchi = [x for x in toldiruvchi if x != tokens[i - 1]]

                # Append individual tokens separately (to avoid duplication)
                if tokens[i - 1] not in identified_tokens:
                    toldiruvchi.append(tokens[i - 1])  # Add NOUN
                    identified_tokens.add(tokens[i - 1])  # Mark NOUN as identified

        # Rule: NOUN preceding Verbal Noun (V_N), ensuring V_N is not the last word
        if categories[i] == 'NOUN' and i < len(categories) - 1 and categories[i + 1] == 'V_N' and i + 2 < len(categories):
            if tokens[i] not in toldiruvchi:
                print(f"Toldiruvchi found by Rule (NOUN preceding V_N): {tokens[i]}")
                toldiruvchi.append(tokens[i])
                identified_tokens.add(tokens[i])

                    
        if categories[i] == 'V_N' and categories[i + 1] == 'ADP':
            if i + 1 < len(tokens) - 1:  # Ensure ADP is not the last word
                phrase = f"{tokens[i]} {tokens[i + 1]}"
                if phrase not in toldiruvchi:
                    print(f"Toldiruvchi found by Rule (Verbal Noun + ADP): {phrase}")
                    toldiruvchi = [x for x in toldiruvchi if x != tokens[i]]
                    if tokens[i+1] not in identified_tokens:
                        toldiruvchi = [x for x in toldiruvchi if x != tokens[i+1]]
                        toldiruvchi.append(tokens[i + 1])
                    
                    toldiruvchi.append(tokens[i])
                
                    identified_tokens.add(word)
                    identified_tokens.add(tokens[i + 1])
                
        # Rule 1: Identify Toldiruvchi (NOUN directly linked to VERB)
        if not toldiruvchi and category == 'NOUN' and i > 0 and categories[i - 1] == 'VERB' and i == len(categories) - 1:
            # Check if the noun has an accusative suffix (e.g., '-ni')
            if word.endswith('ni'):
                if word not in toldiruvchi:
                    print(f"Toldiruvchi found by Rule 1 (Accusative Noun following Verb): {word}")
                    toldiruvchi.append(word)
                    continue

            # Check if it's part of a multi-word complement (VERB + NOUN + VERB)
            if i + 1 < len(categories) and categories[i + 1] == 'VERB':
                multi_word = f"{tokens[i - 1]} {word}"
                if multi_word not in toldiruvchi:
                    if tokens[i-1] not in identified_tokens:
                        toldiruvchi = [x for x in toldiruvchi if x != tokens[i-1]]
                        toldiruvchi.append(tokens[i - 1])
                    print(f"Toldiruvchi found by Rule 1 (Multi-word Complement): {multi_word}")
                    toldiruvchi.append(word)
                    continue

            # Default case: Single NOUN following VERB
            if word not in toldiruvchi:
                print(f"Toldiruvchi found by Rule 1 (Noun following Verb): {word}")
                toldiruvchi.append(word)
                continue


        
        # Rule 2: Proper nouns (PROPER_NOUN) following a verb can be toldiruvchi
        if not toldiruvchi and category == 'PROPER_NOUN' and i > 0 and categories[i - 1] == 'VERB':
            if word not in toldiruvchi:
                print(f"Toldiruvchi found by Rule 2 (Proper Noun following Verb): {word}")
                toldiruvchi.append(word)
                break

        # Rule 3: Pronouns (P) following a verb are treated as toldiruvchi
        if not toldiruvchi and category == 'P' and i > 0 and categories[i - 1] == 'VERB' and word not in excluded_words:
            if word not in toldiruvchi:
                print(f"Toldiruvchi found by Rule 3 (Pronoun following Verb): {word}")
                toldiruvchi.append(word)
                break

        # Rule 4: Numerals (NUM) following a verb can be toldiruvchi if they act as a direct object
        if not toldiruvchi and category == 'NUM' and i > 0 and categories[i - 1] == 'VERB' and word not in excluded_words:
            if word not in toldiruvchi:
                print(f"Toldiruvchi found by Rule 4 (Numeral following Verb): {word}")
                toldiruvchi.append(word)
                break
        

       # Rule 4: Locative or Directional Nouns
        if category in ['NOUN'] and (
            word.endswith('ga') or 
            word.endswith('ni') or 
            word.endswith('bilan')
        ):
            # Skip V_N if it's followed by a verb (part of the predicate)
            if category == 'V_N' and i < len(categories) - 1 and categories[i + 1] == 'VERB':
                print(f"Skipping V_N '{word}' as part of the predicate structure.")
                continue
                
            print(f"Toldiruvchi found by Rule 4 (Locative/Directional Noun): {word}")
            
            # Ensure the word is not already added to the toldiruvchi list
            if word not in toldiruvchi:
                toldiruvchi.append(word)  # Append the word to the toldiruvchi list
            
            identified_tokens.add(word)  # Mark it as identified to avoid duplication
            continue



        # Rule: Verbal Nouns in Accusative Case
        if not toldiruvchi and category in ['V_N', 'INF', 'VERB'] and word.endswith('ni') and word not in identified_tokens:
            print(f"Toldiruvchi found by Rule (Verbal Noun with Accusative Case): {word}")
            if word not in toldiruvchi:
                toldiruvchi.append(word)
                identified_tokens.add(word)  # Mark it as identified
            continue
    
        # Rule 4: Last Noun as Default Toldiruvchi
        if not toldiruvchi and len(tokens) == 1 and category == 'NOUN' and word != ega:
            if word not in toldiruvchi:
                print(f"Toldiruvchi found by Rule 4 (Single Remaining Noun): {word}")
                toldiruvchi.append(word)
                break
            
        # Rule 5: Gerunds (GERUND) can be toldiruvchi if they follow a verb
        if not toldiruvchi and category == 'GERUND' and i > 0 and categories[i - 1] == 'VERB':
            if word not in toldiruvchi:
                print(f"Toldiruvchi found by Rule 5 (Gerund following Verb): {word}")
                toldiruvchi.append(word)
                break

        # Rule 6: Infinitive verbs (INF) following another verb can be toldiruvchi (e.g., "bajarishni xohladi")
        if not toldiruvchi and category == 'INF' and i > 0 and categories[i - 1] == 'VERB':
            if word not in toldiruvchi:
                print(f"Toldiruvchi found by Rule 6 (Infinitive following Verb): {word}")
                toldiruvchi.append(word)
                break

        # Check if the current word is a NOUN and follows an ADJ
        # Define Rule 7
        if not toldiruvchi and category == 'NOUN' and i > 0 and categories[i - 1] == 'ADJ':
            # List of transitive verbs that require complements
            transitive_verbs = ['qiladi', 'oladi', 'ko`radi', 'yaxshilaydi', 'o`rganadi', 'topadi']

            # Check if the last token (verb) requires a complement
            if tokens[-1] in transitive_verbs and word not in excluded_words:
                print(f"Toldiruvchi found by Rule 7 (Noun following Adjective): {word}")
                toldiruvchi.append(word)
                break


        # Rule 8: Noun-Noun pairs after a verb can form a toldiruvchi phrase
        if not toldiruvchi and category == 'NOUN' and i > 0 and categories[i - 1] == 'NOUN' and i > 1 and categories[i - 2] == 'VERB':
            if word not in toldiruvchi:
                print(f"Toldiruvchi found by Rule 8 (Noun-Noun Pair following Verb): {tokens[i - 1]} {word}")
                toldiruvchi.append(word)
                if tokens[i-1] not in identified_tokens:
                        toldiruvchi = [x for x in toldiruvchi if x != tokens[i-1]]
                        toldiruvchi.append(tokens[i - 1])
                break

        # Rule 9: Proper Nouns in Noun-Noun pairs after a verb can be a compound toldiruvchi
        if not toldiruvchi and category == 'PROPER_NOUN' and i > 0 and categories[i - 1] in ['NOUN', 'PROPER_NOUN'] and i > 1 and categories[i - 2] == 'VERB':
            if word not in toldiruvchi:
                print(f"Toldiruvchi found by Rule 9 (Proper Noun Compound following Verb): {tokens[i - 1]} {word}")
                toldiruvchi.append(word)
                if tokens[i-1] not in identified_tokens:
                        toldiruvchi = [x for x in toldiruvchi if x != tokens[i-1]]
                        toldiruvchi.append(tokens[i - 1])
                break
        
        # Additional Rule: Noun (NOUN) directly preceding a verb (VERB)
        if not toldiruvchi and category == 'NOUN' and i < len(categories) - 1 and categories[i + 1] == 'VERB':
            if word not in toldiruvchi:
                print(f"Toldiruvchi found by Additional Rule (Noun preceding Verb): {word}")
                toldiruvchi.append(word)
                break
                
        # Rule 10: If the sentence starts with a pronoun and a verb is present, check if the pronoun acts as a Toldiruvchi
        if not toldiruvchi and categories[0] == 'P' and 'VERB' in categories[1:]:
            # Ensure the pronoun is not the Ega
            if tokens[0] not in personal_pronouns and tokens[0] != 'har':
                # Additional constraint: Ensure the verb requires a complement
                verb_index = categories.index('VERB') if 'VERB' in categories else None
                if verb_index is not None and tokens[verb_index] not in identified_tokens:
                    # Ensure the pronoun isn't functioning as a modifier or part of another structure
                    if tokens[0] not in identified_tokens:
                        if tokens[0] not in toldiruvchi:
                            print(f"Toldiruvchi found by Rule 10 (Sentence starts with Pronoun): {tokens[0]}")
                            toldiruvchi.append(tokens[0])
                            identified_tokens.add(tokens[0])  # Add the token, not the list



        # Rule 11: Last noun in a sentence without a clear subject might be a toldiruvchi
        if not toldiruvchi and len(categories) >= 2 and categories[-1] == 'NOUN' and categories[-2] == 'VERB':
            if tokens[-1] not in toldiruvchi:
                print(f"Toldiruvchi found by Additional Rule (Last Noun in Sentence): {tokens[-1]}")
                if tokens[i-1] not in identified_tokens:
                        toldiruvchi = [x for x in toldiruvchi if x != tokens[i-1]]
                        toldiruvchi.append(tokens[i - 1])
                        identified_tokens.add(word)
                        
        if not toldiruvchi and category == 'ADP':  # Check if the current word is an ADP
        # Ensure the word is not already assigned to another role
            if word not in identified_tokens:
                if word not in toldiruvchi:
                    print(f"Toldiruvchi found by Rule 12 (ADP): {word}")
                    toldiruvchi.append(word)
                    identified_tokens.add(word)
                    break

        # Rule 13: NOUN + Specific Postpositions (e.g., 'uchun', 'bilan', 'tufayli')
        if not toldiruvchi and i < len(categories) - 1 and categories[i] == 'NOUN' and tokens[i + 1] in ['uchun', 'tufayli']:
            if tokens[i] not in toldiruvchi:
                print(f"Toldiruvchi found by Rule 13 (NOUN + Specific Postpositions): {tokens[i]} {tokens[i + 1]}")
                toldiruvchi.append(tokens[i])
                if tokens[i+1] not in identified_tokens:
                        toldiruvchi = [x for x in toldiruvchi if x != tokens[i+1]]
                        toldiruvchi.append(tokens[i + 1])
                break
        
        
        # Rule for Toldiruvchi (Numeric/Temporal Tokens)
        if not toldiruvchi and category == 'NUM' and word not in identified_tokens:
            # Check if this token is already part of a compound hol
            if i > 0 and categories[i - 1] == 'NOUN':
                continue  # Skip if it's part of a compound hol
            if word not in toldiruvchi:
                print(f"Toldiruvchi found by Rule (Numeric/Temporal Token): {word}")
                toldiruvchi.append(word)
                identified_tokens.add(word)
        
        # Rule for Toldiruvchi (Recipient Complement)
        if not toldiruvchi and category == 'P' and word.endswith(('ga', 'ni')):
            if word not in toldiruvchi:
                print(f"Toldiruvchi found: {word}")
                toldiruvchi.append(word)
                identified_tokens.add(word)
                continue
        
        if categories[i] == 'V_N' and tokens[i].endswith('ga'):
            # Check if the next token is a motion/purpose verb
            if i + 1 < len(categories) and categories[i + 1] == 'VERB':
                print(f"Toldiruvchi found by Rule (Purpose Complement): {tokens[i]}")
                toldiruvchi.append(tokens[i])
        
        if i < len(categories) - 1 and categories[i] == 'NOUN' and tokens[i + 1] == 'bilan':
            # Check if the main verb indicates engagement or association
            if any(main_verb in tokens for main_verb in ['shug`ullanadi', 'ishlaydi', 'yordam beradi']):
                # Include modifiers if present
                if i > 0 and categories[i - 1] == 'ADJ':
                    toldiruvchi_phrase = f"{tokens[i - 1]} {tokens[i]} {tokens[i + 1]}"
                    print(f"Toldiruvchi found by Rule (Engagement with Object): {toldiruvchi_phrase}")
                    if tokens[i-1] not in identified_tokens:
                        toldiruvchi = [x for x in toldiruvchi if x != tokens[i-1]]
                        toldiruvchi.append(tokens[i - 1])
                    
                    toldiruvchi.append(word)
                    toldiruvchi.append(tokens[i + 1])
                    identified_tokens.update([tokens[i - 1], tokens[i], tokens[i + 1]])
                else:
                    toldiruvchi_phrase = f"{tokens[i]} {tokens[i + 1]}"
                    print(f"Toldiruvchi found by Rule (Engagement with Object): {toldiruvchi_phrase}")
                    toldiruvchi.append(toldiruvchi_phrase)
                    identified_tokens.update([tokens[i], tokens[i + 1]])

        if categories[i] == 'NOUN' and i + 1 < len(tokens) and tokens[i + 1] == 'bilan':
            phrase = f"{tokens[i]} {tokens[i + 1]}"
            if phrase not in toldiruvchi:  # Avoid duplicates
                print(f"Toldiruvchi found by Rule (Accompaniment): {phrase}")
                
                # Add noun + bilan as complement
                toldiruvchi.append(phrase)
                
                # Mark tokens as identified
                identified_tokens.add(tokens[i])
                identified_tokens.add(tokens[i + 1])


    toldiruvchi = ", ".join(toldiruvchi)

    # If no toldiruvchi is found through the rules
    if not toldiruvchi:
        print("No Toldiruvchi found.")
    else:
        print(f"Toldiruvchi found: {toldiruvchi}")

    return toldiruvchi


def find_hol(tokens, categories, identified_tokens=None):
    hol = []
    print(f"Tokens: {tokens}")
    print(f"Categories: {categories}")

    # Return None if tokens or categories are empty
    if not tokens or not categories:
        print("No tokens or categories left to process for Hol.")
        return None

    # Excluded words that do not typically serve as 'hol'
    excluded_words = [
        'va', 'lekin', 'ammo', 'biroq', 'yoki', 'yo', 'nega', 'chunki', 'sababi',
        'shuning uchun', 'balki', 'ha', 'yo`q', 'ham', 'ekan', 'u', 'buning', 'bu'
    ]

    # List of words answering "where" question
    location_words = [
        'piknik','maktab', 'bog‘', 'bog‘cha', 'ko‘cha', 'uy', 'hovli', 'binolar', 'mehmonxona', 
        'katta bozor', 'choyxona', 'do‘kon', 'ofis', 'tosh', 'yangi mahalla', 'ko‘l', 
        'dengiz', 'orol', 'masjid', 'xonadon', 'yo‘lak', 'universitet', 'litsey', 
        'kollej', 'kutubxona', 'o‘quv markazi', 'oliy o‘quv yurtlari', 'park', 
        'chorvoq', 'tog‘', 'changalzor', 'sayilgoh', 'dalalar', 'xiyobon', 'qishloq', 
        'shahar', 'suv havzasi', 'maydon', 'sport zali', 'bekat', 'avtovokzal', 
        'aeroport', 'temir yo‘l vokzali', 'stansiya', 'metro', 'avtomagistral', 
        'hokimiyat', 'poliklinika', 'shifoxona', 'davlat idoralari', 'bank', 'sud', 
        'vazirlik', 'elchixona', 'mahalla idorasi', 'kinoteatr', 'teatr', 'muzey', 
        'ko‘ngilochar markaz', 'stadion', 'amfiteatr', 'zoopark', 'galereya', 'plyaj', 
        'o‘yingoh', 'daryo', 'tog‘', 'cho‘l', 'vodiy', 'soy', 'kanyon', 'o‘rmon', 
        'qir', 'yaylov', 'qoya', 'toshkent', 'samarqand', 'buxoro', 'urganch', 'xiva', 
        'qarshi', 'navoiy', 'nukus', 'farg‘ona', 'andijon', 'qayerga', 'soat beshda', 'doim', 'davom',
    ]

    # Ensure identified_tokens is not None
    if identified_tokens is None:
        identified_tokens = set()

    # Rule 1: Adjectives acting as adverbs (e.g., 'yaxshi', 'tez', 'sekin')
    for i, (word, category) in enumerate(zip(tokens, categories)):
        if word in identified_tokens:
            continue
        if category == 'ADJ' and i < len(categories) - 1 and categories[i + 1] == 'VERB':
            print(f"Hol found by Rule 1 (Adjective Acting as Adverb): {word}")
            if word not in hol:
                hol.append(word)
                identified_tokens.add(word)
                break
        
    # Rule 2: General Adverbs (ADV)
    for i, (word, category) in enumerate(zip(tokens, categories)):
        if word in identified_tokens:
            continue
        if category == 'ADV' and word not in excluded_words:
            print(f"Hol found by Rule 2 (Adverb): {word}")
            if word == 'doim' and tokens[i-1] == 'har':
                hol.append(tokens[i-1])
                hol.append(word)
                identified_tokens.add(tokens[i-1])
                identified_tokens.add(word)
                break
            elif word not in hol:
                hol.append(word)
                identified_tokens.add(word)
                break
            
            
    for i, (word, category) in enumerate(zip(tokens, categories)):
        if word in identified_tokens:
            continue  # Skip already identified tokens
        if category == 'ADV' and i > 0 and categories[i - 1] == 'ADV':
            # Add the current adverb and the previous one separately to hol
            if tokens[i - 1] not in hol:  # Add the previous adverb if not already in hol
                print(f"Hol found by Rule (Consecutive Adverbs): {tokens[i - 1]}")
                hol.append(tokens[i - 1])
                identified_tokens.add(tokens[i - 1])  # Mark it as identified
            if word not in hol:  # Add the current adverb if not already in hol
                print(f"Hol found by Rule (Consecutive Adverbs): {word}")
                hol.append(word)
                identified_tokens.add(word)  # Mark it as identified
            continue
        elif category == 'ADV':
            # Handle standalone adverbs
            if word not in hol:
                print(f"Hol found by Rule (Standalone Adverb): {word}")
                hol.append(word)
                identified_tokens.add(word)




    # Rule 3: Locative nouns (e.g., '-da', '-dan')
    for i, (word, category) in enumerate(zip(tokens, categories)):
        if word in identified_tokens:
            continue  # Skip already identified words
        if category == 'NOUN' and (word.endswith('da') or word.endswith('dan')):  # Check for locative suffixes
            if word not in excluded_words:  # Skip excluded words
                print(f"Hol found by Rule 3 (Locative Noun): {word}")
                if word not in hol:  # Avoid duplicates
                    hol.append(word)
                    identified_tokens.add(word)

    # Rule for Postposition 'tashqari' (Exception Hol)
    for i, (word, category) in enumerate(zip(tokens, categories)):
        if word == 'tashqari' and i > 0:  # Check for 'tashqari' not at the start
            previous_word = tokens[i - 1]
            if previous_word.endswith('dan') and previous_word not in identified_tokens:
                phrase = f"{previous_word} {word}"  # Combine with preceding -dan word
                print(f"Hol found by Rule (Postpositional Exception 'tashqari'): {phrase}")
                if phrase not in hol:  # Avoid duplicates
                    hol.append(phrase)
                    identified_tokens.add(previous_word)
                    identified_tokens.add(word)

    # **New Rule**: Words indicating location + suffix ('ga', 'da', 'dan')
    for word in tokens:
        if any(word.startswith(location) and word.endswith(suffix) 
               for location in location_words for suffix in ['ka', 'ga', 'da', 'dan']):
            print(f"Hol found by New Rule (Location Word + Suffix): {word}")
            if word not in hol:
                hol.append(word)
                identified_tokens.add(word)
                break
    
    # Rule for compound temporal expressions (NOUN + NUM)
    for i in range(len(categories) - 1):
        if categories[i] == 'NOUN' and categories[i + 1] == 'NUM':
            compound_expression = f"{tokens[i]} {tokens[i + 1]}"  # Combine NOUN + NUM
            if compound_expression not in hol:  # Avoid duplicates
                print(f"Hol found by Rule (Compound Temporal Expression): {compound_expression}")
                hol.append(compound_expression)  # Add as a single compound entry
                identified_tokens.update([tokens[i], tokens[i + 1]])  # Mark both as identified
            break  # If only one compound expression per sentence is expected

    for i, (word, category) in enumerate(zip(tokens, categories)):
        if category == 'V_N' and word.endswith('ga'):
            # Log and append the Hol if valid
            print(f"Hol found by Rule (Directional Suffix '-ga'): {tokens[i]}")
            hol.append(tokens[i])
            identified_tokens.add(tokens[i])  # Mark it as identified



    # Rule 5: Sentence-starting adverbs (ADV at start)
    if hol is None and categories and categories[0] == 'ADV' and tokens[0] not in excluded_words:
        print(f"Hol found by Rule 5 (Sentence-starting Adverb): {tokens[0]}")
        if tokens[0] not in hol:
            hol.append(tokens[0])
            identified_tokens.add(tokens[0])
    
    for i, (word, category) in enumerate(zip(tokens, categories)):
        if word in identified_tokens:
            continue

        # Check for locative nouns with suffixes (e.g., 'shahriga', 'uyda')
        if category == 'NOUN' and word.endswith(('da', 'dan', 'ga')):
            # Check for a compound locative phrase (e.g., 'tuman shahriga')
            if i > 0 and categories[i - 1] == 'NOUN':
                compound_hol = f"{tokens[i - 1]} {word}"
                if compound_hol not in hol:
                    hol.append(compound_hol)
                    print(f"Hol found by Rule 77 (Compound Locative): {compound_hol}")
                    identified_tokens.add(tokens[i - 1])
                    identified_tokens.add(word)
            else:
                if word not in hol:
                    hol.append(word)
                    print(f"Hol found by Rule 77 (Locative Noun): {word}")
                    identified_tokens.add(word)



        # Check for compound adverbial phrases (e.g., 'kun davomida')
           # Rule for Hol (Compound Adverbial)
        if category == 'NOUN' and i + 1 < len(categories) and tokens[i + 1] in ['davomida']:
            compound_phrase = f"{tokens[i]} {tokens[i + 1]}"
            if tokens[i] not in hol:
                print(f"Hol found by Rule (Compound Adverbial): {tokens[i]}")
                hol.append(tokens[i])
                identified_tokens.update(tokens[i])
            if tokens[i + 1] not in hol:
                print(f"Hol found by Rule (Compound Adverbial): {tokens[i + 1]}")
                hol.append(tokens[i + 1])
                identified_tokens.update(tokens[i + 1])



        if category == 'ADV':
            if word not in hol:  # Ensure the word is not already in hol
                if word not in hol:
                    hol.append(word)
                    print(f"Hol found by Rule (Standalone Adverb): {word}")
                    identified_tokens.add(word)
                    break
        
        if i < len(categories) - 1 and categories[i] == 'NOUN' and tokens[i + 1] == 'bilan':
            if i > 0 and categories[i - 1] == 'ADJ':  # Handle modifiers
                hol_phrase = f"{tokens[i - 1]} {tokens[i]} {tokens[i + 1]}"
                print(f"Hol found by Rule (Accompaniment with Modifier): {hol_phrase}")
                hol.append(hol_phrase)
                identified_tokens.update([tokens[i - 1], tokens[i], tokens[i + 1]])
            else:
                hol_phrase = f"{tokens[i]} {tokens[i + 1]}"
                print(f"Hol found by Rule (Accompaniment): {hol_phrase}")
                hol.append(hol_phrase)
                identified_tokens.update([tokens[i], tokens[i + 1]])
         # Mark both tokens as identified

    for i, (word, category) in enumerate(zip(tokens, categories)):
        if word in identified_tokens:
            continue
                
            # Rule: Compound Purpose Expression (V_N + VERB)
        if category == 'VERB' and i + 1 < len(categories):  # Ensure i + 1 is within bounds
            if categories[i + 1] == 'V_N' and tokens[i + 1].endswith('ga'):
                compound_expression = f"{word} {tokens[i + 1]}"  # Combine VERB and following V_N
                if compound_expression not in hol:  # Prevent duplicates
                    if compound_expression not in hol:
                        hol.append(compound_expression)
                        print(f"Hol found by Rule (Compound Purpose Expression): {compound_expression}")
                        identified_tokens.update([word, tokens[i + 1]])  # Mark both as identified
                continue
        
        # Rule 1: Verbal noun with suffix '-dan' or '-dan'
        if category == "V_N" and word.endswith("dan"):
            hol.append(word)
        # Rule 2: Compound hol (verbal noun + adverb like 'oldin' or 'keyin')
        if i > 0 and categories[i - 1] == "V_N" and tokens[i - 1].endswith("dan") and category == "ADV":
            hol.append(f"{tokens[i - 1]} {word}")
        # Rule 3: Adverbs ('ADV') are automatically hol
        if category == "ADV":
            hol.append(word)
            
        
    hol = ", ".join(hol)  # Create a comma-separated string of unique locative nouns
    # If no hol is found
    if not hol:
        print("No Hol found.")
    else:
        print(f"Hol found: {hol}")

    return hol

# Helper functions to check different verb forms and rules
def is_finite_verb(word):
    # Suffixes indicating finite verbs
    finite_verb_suffixes = [
        'yman', 'ydilar', 'yapman', 'yapsan', 'yapti', 'yapmiz', 'yapsiz', 'yaptilar',
        'dim', 'ding', 'di', 'dik', 'dingiz', 'dilar',
        'ganman', 'gansan', 'gan', 'ganmiz', 'gansiz', 'ganlar',
        'arman', 'arsan', 'adi', 'amiz', 'asiz', 'adilar',
        'man', 'san', 'miz', 'siz', 'di', 'lar',
        'madi', 'mayapti'
    ]
    return any(word.endswith(suffix) for suffix in finite_verb_suffixes)

def is_negative_form(word):
    # Check if the verb contains negation (e.g., "ma" or "mas")
    return 'ma' in word or 'mas' in word
    
def is_implied_bolmoq(tokens, i):
    # Logic to check if the sentence implies "bo`lmoq"
    return True  # Placeholder logic

def is_auxiliary_verb(word):
    auxiliary_verbs = ['turdi', 'bo`ldi', 'edi']
    return word in auxiliary_verbs

# Main function to run the analysis
def main():
    # Step 1: Load root words from root.csv
    root_df = load_root_words('root.csv')
    print("Iltimos, tekshirish uchun jumlalarni kiriting (har birini yangi qatorda).")
    print("Tugatish uchun bo'sh qatorni kiriting.")

    sentences = []
    while True:
        sentence = input("Jumla: ")
        if sentence.strip() == "":  # Empty input to stop
            break
        sentences.append(sentence)

    # Step 2: Display entered sentences
    print("\nSiz kiritgan jumlalar:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")

    # Step 3: (Optional) Call your analysis function here
    # analyze_sentences(sentences)  # Uncomment and replace with your actual function

    
    # Step 3: Create a CSV file to store results
    with open('sentence_analysis.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Sentence', 'Ega', 'Aniqlovchi', 'Toldiruvchi', 'Hol', 'Kesim']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # Write the CSV header
        
        # Step 4: Process each sentence
        for sentence in sentences:
            print(f"\nAnalyzing sentence: {sentence}")
            
            # Tokenize the sentence
            tokens = tokenize(sentence)
            
            # Get categories for each token
            categories = get_word_categories(tokens, root_df)
            
            # Initialize role tracking
            identified_roles = {
                'kesim': None,
                'ega': None,
                'aniqlovchi': None,
                'toldiruvchi': None,
                'hol': None
            }
            identified_tokens = set()  # Track tokens assigned to roles
            
           
            
            # Step 6: Find Ega (Subject)
            ega = find_ega(tokens, categories, identified_tokens)
            if ega:
                identified_roles['ega'] = ega
                identified_tokens.add(ega)
                
            # Step 7: Find Aniqlovchi (Modifier)
            aniqlovchi = find_aniqlovchi(tokens, categories, ega, identified_tokens)
            if aniqlovchi:
                identified_roles['aniqlovchi'] = aniqlovchi
                identified_tokens.update(aniqlovchi.split())  # Handle multi-word aniqlovchi
            
            # Step 8: Find Toldiruvchi (Object or Complement)
            toldiruvchi = find_toldiruvchi(tokens, categories, ega, identified_tokens)
            if toldiruvchi:
                identified_roles['toldiruvchi'] = toldiruvchi
                identified_tokens.update(toldiruvchi.split())  # Handle multi-word toldiruvchi
            
            # Step 9: Find Hol (Adverbial)
            hol = find_hol(tokens, categories, identified_tokens)
            if hol:
                identified_roles['hol'] = hol
                identified_tokens.add(hol)
            
             # Step 5: Find Kesim (Predicate)
            kesim = find_kesim(tokens, categories, identified_tokens)
            if kesim:
                identified_roles['kesim'] = kesim
                identified_tokens.add(kesim)
                
            # Debugging Output
            print(f"Ega: {identified_roles['ega']}")
            print(f"Aniqlovchi: {identified_roles['aniqlovchi']}")
            print(f"Toldiruvchi: {identified_roles['toldiruvchi']}")
            print(f"Hol: {identified_roles['hol']}")
            print(f"Kesim: {identified_roles['kesim']}")
            
            # Write results to CSV file
            writer.writerow({
                'Sentence': sentence,
                'Ega': identified_roles['ega'] if identified_roles['ega'] else 'None',
                'Aniqlovchi': identified_roles['aniqlovchi'] if identified_roles['aniqlovchi'] else 'None',
                'Toldiruvchi': identified_roles['toldiruvchi'] if identified_roles['toldiruvchi'] else 'None',
                'Hol': identified_roles['hol'] if identified_roles['hol'] else 'None',
                'Kesim': identified_roles['kesim'] if identified_roles['kesim'] else 'None'
            })


if __name__ == "__main__":
    main()