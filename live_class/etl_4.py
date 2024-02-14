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

result = [{title: "Asdf", views: 6, author_name: "Teena Burgess"}]
author_hash = {1: "Jazz Calahan", 2: "Ichabod Loadbearer", 4: "Teena Burgess"}



# print(etl4(videos, authors))

# Return a new array of videos in the following format,
# and only include videos that have at least 100 views:

# result = [
# {title: 'How to Seem Perfect', views: 111, author_name: 'Teena Burgess' }
# {title: 'Review of the New "Unbreakable Mug"', views: 202, 
# author_name: 'Ichabod Loadbearer' },
# ]