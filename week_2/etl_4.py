def etl4(videos, authors):
    authors_hash_table = {}

    for author in authors:
        authors_hash_table[author.get('id')] = author

    result_data = []

    for video in videos:
        views = video['views']
        if views >= 100:
            title = video['title']
            author_details = authors_hash_table.get(video['author_id'])
            author_first_name = author_details['first_name']
            author_last_name = author_details['last_name']

            result_data.append({'title': title, 'views': views, 'name': author_first_name + ' ' + author_last_name})

    return result_data


videos = [
    {'title': 'How to Make Wood', 'author_id': 4, 'views': 6},
    {'title': 'How to Seem Perfect', 'author_id': 4, 'views': 111},
    {'title': 'Review of the New "Unbreakable Mug"', 'author_id': 2, 'views': 202},
    {'title': 'Why Pigs Stink', 'author_id': 1, 'views': 12}
]

authors = [
    {'id': 1, 'first_name': 'Jazz', 'last_name': 'Callahan'},
    {'id': 2, 'first_name': 'Ichabod', 'last_name': 'Loadbearer'},
    {'id': 3, 'first_name': 'Saron', 'last_name': 'Kim'},
    {'id': 4, 'first_name': 'Teena', 'last_name': 'Burgess'},
]

print(etl4(videos, authors))

# Return a new array of videos in the following format,
# and only include videos that have at least 100 views:

# result = [
# {title: 'How to Seem Perfect', views: 111, author_name: 'Teena Burgess' }
# {title: 'Review of the New "Unbreakable Mug"', views: 202, 
# author_name: 'Ichabod Loadbearer' },
# ]
