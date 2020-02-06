"""
max class finder class
"""
class Subject:
    def __init__(self, start: float, end: float, name: str):
        self.start = start
        self.end = end
        self.name = name

    def __repr__(self):
        return f"{self.start!r} {self.end}"

    def get_time(self) -> list:
        return [self.start,self.end]


art = Subject(9, 10, 'art')
eng = Subject(9.30, 10.30, 'eng')
math = Subject(10, 11, 'math')
cs = Subject(10.30, 11.30, 'cs')
chinese = Subject(10.10, 12, 'chinese')
music = Subject(11, 12, 'music')
subjects = [art, eng, math, cs, music, chinese]
count = 0
# while subjects
while subjects:
    subjects.sort(key= lambda x: x.end)
    current = subjects.pop(0)
    subjects.sort(key= lambda x: x.start)
    for i, s in enumerate(subjects):
        if s.start >= current.end:
            current = subjects.pop(i)
    count = count + 1
print(count)