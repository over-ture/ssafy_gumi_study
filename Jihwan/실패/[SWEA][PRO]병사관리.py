from collections import defaultdict
import bisect

def __init__():
    global teams, scores, soldier
    teams = defaultdict(list) # 팀: [점수, 점수]
    scores = defaultdict(list) # 점수: [id, id]
    soldier = defaultdict(list) # ID: [점수, 팀]


def hire(mID, mTeam, mScore):
    # 등록: ID, 팀, 점수
    bisect.insort(teams[mTeam], mScore)
    bisect.insort(scores[mScore], mID)
    soldier[mID] = [mScore, mTeam]


def fire(mID):
    # 해고: ID
    s, t = soldier[mID].pop() # 해당 병사 점수, 팀
    teams[t].remove(s)
    scores[s].remove(mID)


def updateSoldier(mID, mScore):
    # 점수 변경: ID, 바꿀점수



def updateTeam(mTeam, mChangeScore):
    # 점수 변경: 팀 전체, 바꿀 점수
    # 이전 점수 + 바꿀 점수 > 5 = 5
    # 이전 점수 + 바꿀 점수 < 1 = 1



def bestSoldier(mTeam):
    # 팀의 최고점 병사 ID
    # 여러명이면 가장 큰 ID



