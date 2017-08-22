#import ExtractConcept as EX
from ConceptExtraction import _conceptExtraction_ as CE
from ConceptExtraction import _conceptMapping_ as CM

import DefineDistanceByConcept as DD
import GetWikiFeature as GF
import wikiRocation as WR
import MakeGraph as MG
import os


def main():
    ##################Concept Extraction##################
    originURL = "ZM8ECpBuQYE"  #:로마 역사  # "ZM8ECpBuQYE / PL8dPuuaLjXtN0ge7yDk_UA0ldZJdhwkoV" :물리학
    playlistURL = 'https://www.youtube.com/playlist?list=PL8dPuuaLjXtN0ge7yDk_UA0ldZJdhwkoV'
    submitCode = "1503382656%7Ce5c72339e330f6814ae2fe97aa5c6301"
    c_extraction = CE.ConceptExtraction(playlistURL)
    defineConcept = DD.DefineDistance(submitCode)
    makeGraph = MG.MakeGraph()

    testIndex = 0
    index = 2
    num_topic = 5

    Result = c_extraction.get_Concepts(num_topic)
    #print(Result)
    #######################################################

    """e.g. of Result    ## 46개 문서(강의)에 대하여 각각 5개씩 뽑힌 컨셉리스트 입니다. ##
    [['acceleration', 'velocity', 'displacement', 'motion', 'light'],
    ['derivative', 'velocity', 'calculus', 'acceleration', 'power'],
    ['integral', 'derivative', 'acceleration', 'velocity', 'displacement'],
    ['vector', 'machine', 'velocity', 'dimension', 'motion'],
    ['force', 'gravity', 'acceleration', 'mass', 'inertia'],
    ......
    ['universe', 'radiation', 'light', 'redshift', 'plasma']]
    """

    ##################Concept Mapping##################
    """
    NOTE (e.g.)
    Input(concept) : 'inertia'
    Output(URL) : https://en.wikipedia.org/wiki/Inertia
    """
    Cmap = CM.Mapping()
    '''
    ##TEST##
    print('[첫 번째 문서(강의)에 대한 컨셉-위키피디아 URL 매핑 결과]')
    for concept in Result[0]:
        URL = Cmap.maping_Concept2Wiki(concept)
        print('\t{}의 위키피디아 URL> '.format(concept), URL)

    ##URL의 고유 path name(e.g. "Motion_(physics)")을 알고 싶을 경우##
    for concept in Result[0]:
        URL = Cmap.maping_Concept2Wiki(concept)
        idx = URL.find('/wiki/') + 6
        print('\t{}의 위키피디아 URL> '.format(URL[idx:]), URL)
    ##################################################
    '''

    #### NOTE ####
    #### 임시로 밑에 getConceptRelation2 파라미터-> Result[1]으로 해놓았습니다.
    #### Result[doc_num]   0 <= doc_num < 47
    print ("result index ",Result[index])




    #관계부분 시작
    conceptRelation, All_degree = defineConcept.getConceptRelation(Result[index])
    print(conceptRelation)
    print(All_degree)

    #관계 두번째 알고리즘
    Rocation_Algo2 = WR.WikiRotion(All_degree)
    Rocation_Algo2.get_rocation()

    testFeature(Result[index])

    #그래프 시작
    graphSource = makeGraph.py2json(Result[index], conceptRelation)
    sourceName = originURL+".json"
    sourceLoc = os.path.join("./Web/conceptproto/play/static/play/data/" +sourceName)
    print(sourceLoc)
    with open(sourceLoc, "w") as f:
        f.write(graphSource)

def testFeature(concept):
    for c in concept:
        c = c.replace("/wiki/", "")
        #print(c)
        feature = GF.GetWikiFeature(c)

        Indegree = feature.getIndegree()
        Outdegree = feature.getOutdegree()
        LanguageNum = feature.getLanguageNum()
        Categoriesdegree = feature.getCategoriesdegree()

        print("Indegree 수 : ",Indegree)
        print("Outdegree 수 : ", Outdegree)
        print("LanguageNum 수 : ", LanguageNum)
        print("Categoriesdegree 수 : ", Categoriesdegree)


def testGraph():
    originURL = "PLmhKTejvqnoOrQOcTY-pxN00BOZTGSWc3"#:로마 역사  # "PL8dPuuaLjXtN0ge7yDk_UA0ldZJdhwkoV" :물리학
    playlistURL = 'https://www.youtube.com/playlist?list=' + originURL
    #c_extraction = CE.ConceptExtraction(playlistURL)
    #defineConcept = DD.DefineDistance()

    makeGraph = MG.MakeGraph()
    Result = ['derivative', 'velocity', 'calculus', 'acceleration', 'power']
    conceptRelation = [[0, 1, 1, 1, 2],
                       [2, 0, 2, 1, 2],
                       [1, 1, 0, 1, 2],
                       [1, 1, 1, 0, 1],
                       [2, 2, 2, 2, 0]]

    graphSource = makeGraph.py2json(Result, conceptRelation)
    sourceLoc = os.path.join("./Web/conceptproto/play/static/play/data/" + originURL + ".json")
    print(sourceLoc)
    with open(sourceLoc, "w") as f:
        f.write(graphSource)


if __name__ == "__main__":
    main()
