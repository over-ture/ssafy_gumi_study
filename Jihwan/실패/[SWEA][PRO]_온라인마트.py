class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5

category = {} # id : 값 으로 저장
company = {}
price = {}
ids = [0] # id 인덱스 => (True False, int, int, price) # 카테고리, 제조사
# 첫 한개는 무시 

def init() -> None:
    # 태케 초기화
    global category, company, price, ids
    category = {}
    company = {}
    price = {}
    ids = [0]
    pass

def sell(mID : int, mCategory : int, mCompany : int, mPrice : int) -> int:
    # mID 추가할 자료의 ID, # mCategory 품목, mCompany 제조사, mPrice 가격 
    global category, company, price, ids
    category[mID] = mCategory
    company[mID] = mCompany
    price[mID] = mPrice
    ids.append([True, mCategory, mCompany, mPrice])
    
    item_cnt = 0
    for i in ids:
        if i == 0:
            continue
        
        if i[1] == mCategory and i[2] == mCompany:
            item_cnt += 1
    
    if item_cnt > 0:
        return item_cnt
    
    return -1 # mCompany가 판매중인 상품의 개수 반환

def closeSale(mID : int) -> int:
    # mID 상품 판매 종료
    # 가격 return, 판매가 종료된 상품이거나 없는 물건이면 -1
    global category, company, price, ids
    
    if len(ids) <= mID: # 없는 상품이면
        return -1
    
    if ids[mID][0]:
        ids[mID][0] = False
        return price[mID]
    
    # 종료된 상품이면
    return -1

def discount(mCategory : int, mCompany : int, mAmount : int) -> int:
    # 제조사의 품목의 모든 가격을 mAmount 만큼 낮춤
    # 0이거나 음수되면 판매 종료
    # 낮춘 후 상품 개수 반환
    global category, company, price, ids
    
    dis_cnt = 0
    
    for iid in range(1, len(ids)):
        if ids[iid][0]:
            if ids[iid][1] == mCategory and ids[iid][2] == mCompany:
                ids[iid][3] -= mAmount
                if ids[iid][3] <=0:
                    ids[iid][0] = False
                else:
                    dis_cnt += 1
        
    if dis_cnt > 0:
        return dis_cnt
    
    return -1

# def show(mHow : int, mCode : int) -> RESULT:
#     # mHow 조건 만족 상품중 가격 낮은 최대 5개 result 저장, 반환
#     # 가격이 같으면 id 적은 상품 우선
    
#     # mHOW = 0 모든 상품 mCode = 0
#     # mHow = 1 품목이 mCode인 모든 상품 mCode = 1~5
#     # mHow = 2 제조사가 mCode인 모든 상품 mCode = 1~5
#     # 판매 종료 상품은 제외
#     # 조건 만족 상품 없으면 0 저장
    
#     on_sale = []
    
#     if mHow == 0:
#         for iid in range(1, len(ids)):
#             if ids[iid][0]:
#                 on_sale.append((ids[iid][3], iid)) # 가격. id 저장
    
#     elif mHow == 1:
#         for iid in range(1, len(ids)):
#             if ids[iid] and ids[iid][1] == mCode:
#                 on_sale.append((ids[iid][3], iid))
    
#     else:
#         for iid in range(1, len(ids)):
#             if ids[iid] and ids[iid][2] == mCode:
#                 on_sale.append((ids[iid][3], iid))
    
#     cnt = 0
#     ans = []
    
#     if on_sale:
#         x = sorted(on_sale)
#         for i in range(0, len(x)):
#             if i == 5:
#                 break
#             ans.append(x[i][1])
#             cnt += 1
    
#     return RESULT(cnt, ans)


def show(mHow : int, mCode : int) -> RESULT:
    on_sale = []
    
    # 1. 조건에 맞는 상품 필터링
    for iid in range(1, len(ids)):
        # 공통 조건: 반드시 판매 중(ids[iid][0] == True)이어야 함
        if not ids[iid][0]:
            continue
            
        if mHow == 0:
            on_sale.append((ids[iid][3], iid)) # (가격, ID) 튜플 저장
        elif mHow == 1 and ids[iid][1] == mCode: # 카테고리 일치
            on_sale.append((ids[iid][3], iid))
        elif mHow == 2 and ids[iid][2] == mCode: # 제조사 일치
            on_sale.append((ids[iid][3], iid))
    
    # 2. 정렬 (가격 낮은 순 -> 가격 같으면 ID 낮은 순)
    # 파이썬 튜플은 (a, b) 형태일 때 a를 먼저 비교하고 같으면 b를 비교하므로 sorted만 쓰면 끝!
    on_sale.sort() 
    
    # 3. 최대 5개 추출
    ans = []
    for i in range(min(5, len(on_sale))):
        ans.append(on_sale[i][1]) # ID값만 추출
    
    cnt = len(ans)
    
    # 4. 저장 및 반환
    # 이 한 줄이 RESULT 클래스의 __init__을 호출하여 데이터를 상자에 담는 과정입니다.
    return RESULT(cnt, ans)
        