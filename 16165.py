from collections import defaultdict

# n: 걸그룹의 수, m: 맞춰야 할 문제의 수
n, m = map(int, input().split())

team_to_members = defaultdict(list)
member_to_team = {}

for _ in range(n):
    team = input().strip()
    num = int(input())
    for _ in range(num):
        member = input().strip()
        member_to_team[member] = team
        team_to_members[team].append(member)

result = []
for _ in range(m):
    query = input().strip()
    quiz_type = int(input())
    if quiz_type == 0:
        # 팀 이름으로 멤버를 출력
        if query in team_to_members:
            members = sorted(team_to_members[query])  # 멤버 이름을 사전순으로 정렬
            result.extend(members)
    elif quiz_type == 1:
        # 멤버 이름으로 팀을 출력
        if query in member_to_team:
            result.append(member_to_team[query])

print('\n'.join(result))