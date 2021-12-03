try:
    from participant import Participant
    from questions import Question
    from random import randint, shuffle
except ImportError as err:
    print("No such class or module")


def get_questions(fname):
    content = get_content(fname)
    q_list = create_question_dict(content)
    return get_random_5(q_list)

def get_content(fname):
    with open(fname) as f:
        return f.readlines()

def create_question_object(line):
    tmp = line.split(",")
    quest = Question(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5])
    return quest

def create_question_dict(mlist):
    questions_list = []
    for el in mlist:
        questions_list.append(create_question_object(el))
    return questions_list

def get_5_index(ml):
    ind = []
    while len(ind) < 7:
        tmp = randint(0, len(ml) - 1)
        if tmp not in ind:
            ind.append(tmp)
    return ind

def get_random_5(qlist):
    five_ind = get_5_index(qlist)
    return [qlist[ind] for ind in five_ind]

def fifty(qobj):
    ml = []
    ml.append(qobj.corrans)
    wrans = [qobj.answ2, qobj.answ3, qobj.answ4]
    ind = randint(0,2)
    ml.append(wrans[ind])
    return ml

def call_friend(qobj):
    answ = [qobj.answ2, qobj.answ3, qobj.answ4, qobj.corrans]
    ind = randint(0,3)
    return answ[ind]

def audience(qobj):
    audience_obj = {}
    answ = [qobj.answ2, qobj.answ3, qobj.answ4, qobj.corrans]
    fpercent = randint(0,100)
    audience_obj[qobj.answ2] = fpercent
    spercent = randint(0, 100-fpercent)
    audience_obj[qobj.answ3] = spercent
    tpercent = randint(0, 100-fpercent-spercent)
    audience_obj[qobj.answ4] = tpercent
    audience_obj[qobj.corrans] = 100 - fpercent - spercent - tpercent
    return audience_obj

def shuffle_answers(qobj):
    answ_list = [qobj.answ2, qobj.answ3, qobj.answ4, qobj.corrans]
    shuffle(answ_list)
    return answ_list

def get_top(fname):
    with open(fname) as f:
        return f.readlines()

def create_top_obj(top_list):
    ml = []
    for el in top_list:
        el.replace("\n", "")
        tmp = el.split("-")
        ml.append(Participant(tmp[0], int(tmp[1])))
    return ml

def rewrite_top_file(fname, plist):
    with open(fname, "w") as f:
        for player in plist:
            f.write(player + "\n")

def name_in_list(ml, name):
    for el in ml:
        if el.isname(name):
            return True
    return False
