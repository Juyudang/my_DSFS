from __future__ import division
from collections import Counter
from checktype import checktype                        # from [file] import [function]
from collections import defaultdict

# 'users' 구조 생성
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klevin" },
]
# checktype(users)                                        # user is list type
# checktype(users[1])                                     # user[i] is dict type
# print(users[0].keys())          # dict_keys(['id', 'name'])
# print(users[0]["name"])
# checktype(users[0]["name"])

# 그룹 간의 우정 암시
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
# checktype(friendship_pairs)
# checktype(friendship_pairs[1])                          # friendship_pairs[i] is tuple type

# 'friendships' 항목을 생성
friendships = {user["id"]: [] for user in users}
# print(friendships)            # {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []} 생성

for i, j in friendship_pairs:
    friendships[i].append(j) # id == i 에 우정 j 추가
    friendships[j].append(i) # id == j 에 우정 i 추가
# print(friendships)  # {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [4, 6, 7], 6: [5, 8], 7: [5, 8], 8: [6, 7, 9], 9: [8]}
# print(friendships[0])       # [1, 2]
# checktype(friendships[4])               # dict type 은 key : Value 형식으로 데이터가 들어가는데 Value에 list 형식도 가능
# checktype(friendships)     # dict

def number_of_friends(user):
    user_id = user["id"]                                  # users의 id를 따로 저장
    # print(user_id)                                      # 모든 아이디를 프린트
    friend_ids = friendships[user_id]
    # print(friend_ids)                                   # 해당 id의 friendships를 저장
    return len(friend_ids)                                # 해당 아이디의 친구 수를 return

total_connections = sum(number_of_friends(user) for user in users)      # 모든 friendships의 수를 더함
# print(total_connections)

num_users = len(users)                                    # users의 수
avg_connections = total_connections / num_users           # 관계의 평균
# print(avg_connections)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]       # ('id', '해당 유저의 친구 수')
# print(num_friends_by_id)                                # [(0, 2), (1, 3), (2, 3), ... (8, 3), (9, 1)]

num_friends_by_id.sort(
    key = lambda id_and_friends : id_and_friends[1],      # value의 값을 비교하여 정렬
    reverse = True)                                       # 역순으로 정렬
# print(num_friends_by_id)                                # [(1, 3), (2, 3), (3, 3), ... (7, 2), (9, 1)]

# def foaf_ids_bad(user):
#     '''foaf is short for "friend of a friend"'''
#     return [foaf_id
#             for friend_id in friendships[user["id"]]    # check id's friends
#             for foaf_id in friendships[friend_id]]      # show id's friends's friends
# print(friendships[0])                                   # [1, 2]
# print(friendships[1])                                   # [0, 2, 3]
# print(friendships[2])                                   # [0, 1, 3]
# print(foaf_ids_bad(users[0]))                           # [0, 2, 3, 0, 1, 3] -> it shows duplicated friendships

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]           # for each of my friends
        for foaf_id in friendships[friend_id]           # for each of my friends of friends
        if foaf_id != user_id                           # without user itself
        and foaf_id not in friendships[user_id]         # without my friends
    )                                           # return friends of friends without duplicated
# print(friends_of_friends(users[3]))                     # Counter({0: 2, 5: 1})
# print(friendships[3])                                   # [1, 2, 4]
# print(friendships[1])                                   # [0, 2, 3]
# print(friendships[2])                                   # [0, 1, 3]
# print(friendships[4])                                   # [3, 5]

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (4, "decision trees"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskall"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):          # 해당 흥미를 가진 id를 리스트로 리턴
    """Find the ids of all users who like the target interest."""
    return [user_id
    for user_id, user_interest in interests
    if user_interest == target_interest]
# print(data_scientists_who_like("Big Data"))             # [0, 8, 9]

# Keys are interest, values are lists of user_ids with that interest == 흥미 기준로 유저를 묶음
user_ids_by_interest = defaultdict(list)                # from collections import defaultdict <- 추가해야함
# print(user_ids_by_interest)                           # defaultdict(<class 'list'>, {})
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)  
# print(user_ids_by_interest)                   # defaultdict(<class 'list'>, {'Hadoop': [0, 9], 'Big Data': [0, 8, 9], ...
# print(user_ids_by_interest['Hadoop'])           # [0, 9] <- dict 으로 저장되어 key로 value 불러낼 수 있음

# Keys are user_ids, values are lists of interests for that user_id == 유저 기준으로 흥미를 묶음
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
# print(interests_by_user_id) # defaultdict(<class 'list'>, {0: ['Hadoop', 'Big Data', 'HBase', 'Java', 'Spark', 'Storm', 'Cassandra'], ...
# print(interests_by_user_id[2])  # ['Python', 'scikit-learn', 'scipy', 'numpy', 'statsmodels', 'pandas']
# print(interests_by_user_id.keys())        # dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

def most_common_interest_with(user):               # user(입력값)와 공통관심사가 있는 유저를 카운트하여 가장 겹치는 인원부터 리턴
    return Counter(
        interested_user_id                                              # 관심이 있는 특정 유저
        for interest in interests_by_user_id[user["id"]]                # user의 id 값이 보유한 인터레스트 나열
        for interested_user_id in user_ids_by_interest[interest]        # 해당 인터레스트를 가진 인원들의 아이디를 나열
        if interested_user_id != user["id"]                             # user와 다른 모든 아이디를 카운트
    )
# print(most_common_interest_with(users[0]))         # Counter({9: 3, 8: 1, 5: 1, 1: 1})
# print(most_common_interest_with(users[9]))         # Counter({0: 3, 5: 1, 8: 1})
# print(data_scientists_who_like("Hadoop"))                 # [0, 9]
# print(data_scientists_who_like("Java"))                   # [0, 5, 9]
# print(data_scientists_who_like("MapReduce"))              # [9]      
# print(data_scientists_who_like("Big Data"))               # [0, 8, 9]

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# Keys are years, values are lists of the salaries for each tenure
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
print(salary_by_tenure)

# Keys are years, each value is average salary for that tenure
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}
print(average_salary_by_tenure)           # 같은 기간의 tenure가 없기에 별다른 값이 나오지 않음

# bucket the tenrues - 경력?을 묶어보자
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# Keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
# print(salary_by_tenure_bucket)
# defaultdict(<class 'list'>, {'more than five': [83000, 88000, 76000, 69000, 76000, 83000], 'less than two': [48000, 48000], 'between two and five': [60000, 63000]})

# Keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
# print(average_salary_by_bucket)     # {'more than five': 79166.66666666667, 'less than two': 48000.0, 'between two and five': 61500.0}

words_and_counts = Counter(word
                            for user, interest in interests
                            for word in interest.lower().split())   # 만일 같은 명칭이지만 대문자를 안적을 수도 있으므로 전부 소문자로 바꿈

# for word, count in words_and_counts.most_common():      # Counter.most_common() -> 중복된 항목을 내림차순으로 정렬
#     if count > 1:
#         print(word, count)