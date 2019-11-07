''' This is for generating comment for JKF robot '''
def additional(author, content):
    res = ''
    if '姊妹' in content:
        res = '我全都要'
    if '混血' in content:
        res = '混血就是強大'
    if '颱風' in content:
        res = random.choice(['拜託不要鬧','真的不要鬧','不要再下了'])
    if '成人展' in content:
        res = '好想去成人展'
    return res

def noNameAV():
    res = ''
    if random.randint(0,2) == 0:
        t1 = random.choice(['回去','等等',''])
        t2 = random.choice(['尻尻','來找找','認真'])
        t3 = random.choice(['看','..',' 嘿嘿嘿'])
        res =  t1 + t2 + t3
    else:
        t1 = random.choice(['騷貨','欠幹','騷貨欠幹','好正啊','好想騎','想幹','好想幹'])
        t2 = random.choice(['','..',' 嘿嘿嘿','嘿嘿','喔'])
        res =  t1 + t2
    return res

def noNameSexy():
    res = ''
    adj = random.choice(['騷','正','美','辣','性感'])
    t1 = random.choice(['有夠{}','好想騎騎看','想騎','{}到爆','身材很好','太{}了吧','好想被服務','最愛這種'])
    t2 = random.choice(['','','!','~','...'])
    res = t1.format(adj) + t2
    return res

def noNameBoobs():
    res = ''
    if random.randint(0,1) == 0:
        t1 = random.choice(['這個','這','她的',''])
        t2 = random.choice(['奶','乳量','奶子','胸'])
        t3 = random.choice(['我可以','很可以','很讚','很優耶','我喜歡','有夠美','也太誇張'])
        res =  t1 + t2 + t3
    else:
        t1 = random.choice(['真想揉揉看','精神都來了','騷妹妹','挺騷的 讚','有夠騷','妹仔辣喔'])
        t2 = random.choice(['','...','!','!!'])
        res =  t1 + t2
    return res

def getComment(author, content):
    jkf_list =  ['嵐嵐','凱咪','琪琪','緹芝','又又','安希','貝蒂兒','甜心','施菲亞','朵兒']
    av_list = ['蓮実','三上','明日花','篠田','高橋','橋本','天使萌']
    boobs_list = ['罩杯','乳','上圍','曲線','E奶','奶妹']
    booty_list = ['美尻','屁股']
    beauty_list = ['可愛','顏值','Instagram熱門','正妹']
    res = ''
    
    if author == 'ThaiBeauty':
        t1 = random.choice(['泰味娘','東南亞風情','泰妹','泰式奶茶','泰奶','泰國小姐','泰美眉','泰國騷貨'])
        t2 = random.choice(['','就是好','我可以','就是讚','一級棒','頂呱呱','滿分','一定要的'])
        t3 = random.choice(['','!','!!!','..','~','啦','的啦',' 嘻嘻'])
        res = t1 + t2 + t3        
        
    elif author == '46pic':
        t1 = random.choice(['很','非常','超','有夠'])
        t2 = random.choice(['正','唯美','美','扯','誇張','讚'])
        t3 = random.choice(['','!','!!!','..','~','耶',' 讚'])
        res = t1 + t2 + t3
    
    elif author == 'JVID':
        t1 = random.choice(['欠','好想','好騷 欠','超性感 好想'])
        t2 = random.choice(['幹','騎','解鎖','調教','揉揉','處理'])
        t3 = random.choice(['','!','!!!','..','~','耶',' 讚'])
        res = t1 + t2 + t3
        
    elif author == '西瓜視頻':
        t1 = random.choice(['','這個','未免太扯 '])
        t2 = random.choice(['好牛B','好強','好有質感','神人','挺無言'])
        t3 = random.choice(['','!','!!!','..','~','耶'])
        res = t1 + t2 + t3
    
    elif author == 'ETtoday新聞雲':
        t1 = random.choice(['Wow','wow','挖哩勒','這麼扯','真的假的'])
        t2 = random.choice(['',' 認真欸',' 誇張',' 無言'])
        t3 = random.choice(['','!','!!','..'])
        res = t1 + t2 + t3
        
    elif author == '抖音TikTok':
        if random.randint(0,1) == 0:
            t1 = random.choice(['這啥小','啥小啦','嗯嗯嗯','8787','為什麼要讓我看這個','先不要','不要吧','尷尬癌發作','尷尬癌又發作'])
            t2 = random.choice(['','...','?!'])
            res = t1 + t2
        else:
            t1 = random.choice(['只有我覺得','只有我感覺'])
            t2 = random.choice(['不行','還可以','還OK','尷尬','無言','頭痛','蠻正','挺正'])
            t3 = random.choice(['嗎..','嗎','嗎?!','的嗎','的嗎...','的嗎?'])
            res = t1 + t2 + t3
        
    elif 'JKF' in author:
        for name in jkf_list:
            if name in content:
                if random.randint(0,3) == 0:
                    t1 = random.choice(['一級棒',' 我喜歡妳','好辣','JKF紅牌','有夠正'])
                    t2 = random.choice(['','','!','~','...'])
                    res = name + t1 + t2
                break
        if res == '':
            if random.randint(0,3) == 0:
                res = noNameSexy()
            else:
                res = noNameBoobs()
    
    elif 'YouTube' in author:
        if '解密' in author:
            t1 = random.choice(['真的還假的','好猛喔','認真耶..','不小心就看完了','不小心看完'])
            res = t1
        elif '男人' in author:
            t1 = random.choice(['好爽喔','看得很開心','想當youtuber','不小心就看完了','直接看完','看完心癢癢..'])
            res = t1
        elif '遊戲' in author:
            t1 = random.choice(['好爽喔','等很久了','看起來很不錯','好像有看過別人玩','看了心癢癢'])
            res = t1
        elif '世界' in author:
            t1 = random.choice(['好想去玩喔','看起來超好玩','看起來很不錯','什麼時候才能去呢','不小心就看完了'])
            res = t1
    for name in av_list:
        if name in content:
            if random.randint(0,1) == 0:
                t1 = random.choice(['賽高','我老婆','是我的','我女友','一直是我的愛','總是深得我心','就是優質','就是棒'])
                t2 = random.choice(['','','!','~'])
                res = name + t1 + t2
            else:
                t1 = random.choice(['我只愛{}一個','好想騎騎看{}','有機會讓她服務嗎?','好想被服務...','就愛{}這樣'])
                res = t1.format(name)
            break
    
    if res == '' or random.randint(0,2) == 0:
        if 'AV' in content:
            if res == '':
                res = noNameAV()
            else:
                if random.randint(0,3) == 0:
                    res = noNameAV()
        
        for keyword in boobs_list:
            if keyword in content:
                res = noNameBoobs()
                break
        
        if res == '':
            res = additional(author, content)
    
    return res
