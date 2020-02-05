from collections import deque
search_que = deque()

graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search_que = search_que + deque(graph["you"])
print(search_que)

def person_is_seller(name):
    return name[-1]=='m'

def search(name):
    search_que = deque()
    search_que = search_que + deque(graph[name])
    searched = []
    while search_que:
        person = search_que.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person+" is a seller")
                return True
            else:
                search_que += deque(graph[person])
                searched.append(person)
    return False

search('you')