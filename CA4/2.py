def find_teams(n, m, friendships):
    graph = []
    for i in range(1,n+1):
        graph.append([i])
    for a, b in friendships:
        graph[a-1].append(b)
        graph[b-1].append(a)
    teams = []
    visited = set()
    def dfs(start):
        currentTeam = []
        for player in graph[start-1]:
            if player in visited:
                continue
            else:
                visited.add(player)
                currentTeam.append(player)
                for _ in dfs(player):
                    currentTeam.append(_)
        return currentTeam
    
    
    for i in range(1, n+1):
        teams.append(dfs(i))
        
    return teams

def main():
    n, m = map(int, input().split())
    friendships = [tuple(map(int, input().split())) for _ in range(m)]
    
    result = find_teams(n, m, friendships)

    threePlayer = []
    twoPlayer = []
    onePlayer = []
    
    for team in result:
        if(len(team) == 3):
            threePlayer.append(team)
        if(len(team) == 2):
            twoPlayer.append(team)
        if(len(team) == 1):
            onePlayer.append(team)
        if (len(team)) > 3:
            print(-1)
            return
    
    if len(twoPlayer) > len(onePlayer):
        print(-1)
        return
    
    # print(threePlayer, twoPlayer, onePlayer)

    for completeTeam in threePlayer:
        for player in completeTeam:
            print(player,end =" ")
        print("")

    for i in range(0,len(twoPlayer)):
        team = twoPlayer[i] + onePlayer[i]
        for player in team:
            print(player,end =" ")
        print("")
        
    for i in range(len(twoPlayer),len(onePlayer),3):
        team = onePlayer[i] + onePlayer[i+1] + onePlayer[i+2]
        for player in team:
            print(player,end =" ")
        print("")
                                   
if __name__ == "__main__":
    main()
