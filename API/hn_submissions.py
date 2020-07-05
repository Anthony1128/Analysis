import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/item/9884165.json'
r = requests.get(url)
print('Status code:', r.status_code)

submissions_ids = r.json()
print(submissions_ids)
submissions_dicts = []

for submission_id in submissions_ids['kids'][:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    print(response_dict)

    submissions_dict = {
        'title': response_dict.get('title'),
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submissions_dicts.append(submissions_dict)

    submissions_dicts = sorted(submissions_dicts, key=itemgetter('comments'),
                               reverse=True)

    for submission_dict in submissions_dicts:
        print("\nTitle:", submission_dict['title'])
        print("Discussion link:", submission_dict['link'])
        print("Comments:", submission_dict['comments'])





