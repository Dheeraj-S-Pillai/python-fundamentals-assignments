# Module End Assignment 3: Survey Feedback Analyzer

# 1 - Preloaded Feedbacks

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


# 2 - Add More Feedbacks

n = int(input("Enter how many more feedbacks you want to add: "))

for i in range(n):
    print()
    name = input("Enter name: ")
    feedback = input("Enter feedback: ")
    rating = int(input("Enter rating (1-5): "))

    s_no = len(feedback_data['S_No']) + 1
    feedback_data['S_No'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)


# 3 - Text Cleaning

def clean_text(text):
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.lower()
    words = text.split()
    text = ' '.join(words)
    return text

for i in range(len(feedback_data['Feedback'])):
    feedback_data['Feedback'][i] = clean_text(feedback_data['Feedback'][i])


# 4 - Word Count Insights

def count_word_in_feedbacks(word):
    word = word.lower()
    count = 0
    for feedback in feedback_data['Feedback']:
        if word in feedback.split():
            count += 1
    return count

print()
print("Feedbacks containing 'good':", count_word_in_feedbacks("good"))
print("Feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
print("Feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))


# 5 - Final Summary & Insights

print()
print("Final cleaned feedback data:")
print(feedback_data)

average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print()
print("Average rating:", round(average_rating, 2))

longest_index = 0
longest_word_count = 0
for i in range(len(feedback_data['Feedback'])):
    word_count = len(feedback_data['Feedback'][i].split())
    if word_count > longest_word_count:
        longest_word_count = word_count
        longest_index = i

print()
print("Feedback with the most words:", feedback_data['Name'][longest_index], "-", feedback_data['Feedback'][longest_index])

unique_words = set()
for feedback in feedback_data['Feedback']:
    for word in feedback.split():
        unique_words.add(word)

print()
print("Unique words used across all feedbacks:")
print(sorted(unique_words))


# Sort feedbacks by rating (highest to lowest)

combined = list(zip(feedback_data['Rating'], feedback_data['Name'], feedback_data['Feedback']))
combined_sorted = sorted(combined, reverse=True)

print()
print("Feedbacks sorted by rating (highest to lowest):")
for rating, name, feedback in combined_sorted:
    print(rating, "-", name, "-", feedback)
