import pickle
import os.path as path


saveFileName = "tl.obj"


class Task:

    def __init__(self, name, isComplete=None):
        self.name = name
        if isComplete is None:
            self.isComplete = None
        else:
            self.isComplete = isComplete

    def complete(self):
        self.isComplete = True

    def uncomplete(self):
        self.isComplete = False

    def asString(self):
        check = ' '

        if self.isComplete:
            check = 'x'

        return "[" + check + "] " + self.name

    def print(self):
        print(self.asString)


class TaskList:

    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def remove(self, ind):
        del self.tasks[ind]

    def complete(self, ind):
        self.tasks[ind].complete()

    def uncomplete(self, ind):
        self.tasks[ind].uncomplete()

    def removeComplete(self):
        for t in self.tasks:
            if t.isComplete:
                self.tasks.remove(t)

    def print(self):
        x = 1
        for t in self.tasks:
            print(str(x) + " " + t.asString())
            x = x + 1


cont = True

print("\nTODO LIST\n")
print("a taskName = add a task called taskName")
print("r taskNumber = remove the task with that taskNumber")
print("rc = remove all completed tasks")
print("c taskNumber = complete the task with that taskNumber")
print("u taskNumber = uncomplete the task with that taskNumber")
print("e = exit")
print()

tl = TaskList()

if path.exists(saveFileName):
    if path.getsize(saveFileName) > 0:
        tl = pickle.load(open(saveFileName, "rb"))
else:
    open(saveFileName, "x")

while cont:
    tl.print()
    print()

    usrIn = input(": ")

    if usrIn[0] == 'a':
        tl.add(Task(usrIn[2: len(usrIn)]))
    elif usrIn[0] == 'r':
        if usrIn[1] == 'c':
            tl.removeComplete()
        else:
            tl.remove(int(usrIn[2:len(usrIn)]) - 1)
    elif usrIn[0] == 'c':
        tl.complete(int(usrIn[2: len(usrIn)]) - 1)
    elif usrIn[0] == 'u':
        tl.uncomplete(int(usrIn[2: len(usrIn)]) - 1)
    elif usrIn[0] == 'e':
        cont = False
    pickle.dump(tl, open(saveFileName, 'wb'))
