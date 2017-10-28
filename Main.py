import os

from ConceptExtraction import conceptExtraction as CE
from ConceptExtraction import conceptMapping as CM
import RelationExtraction.DefineDistanceByConcept as DD
import RelationExtraction.GetWikiFeature as GF
import RelationExtraction.MakeGraph as MG


def main():
    playlist_url = 'https://www.youtube.com/playlist?list=PL8dPuuaLjXtN0ge7yDk_UA0ldZJdhwkoV'
    submitCode = "1503584363%7C27ffbb267ba8d3522f0aee70b23c388d"
    defineConcept = DD.DefineDistance(submitCode)
    makeGraph = MG.MakeGraph()

    ## Concept Extraction
    C = CE.ConceptExtraction(playlist_url)
    max_concept, max_weight = 5, 0.07
    result = C._get_onlyConcepts(max_concept, max_weight)
    origins = C.Pre._get_allURLs()

    ## Concept Mapping (concept to its Wikipedia page)
        # e.g. 'inertia'(input) -> https://en.wikipedia.org/wiki/Inertia (output)
    Cmap = CM.Mapping()
    concept = 'inertia'
    wiki_url = Cmap._mapingConcept2Wiki(concept)

    ## Relation Extraction
    for index in range(len(origins)):
        sourceName = origins[index].split("v=")[1].split("&")[0] + ".json"
        print(result[index])
        print(sourceName)
        conceptRelation, All_degree = defineConcept.getConceptRelation(result[index])
        print(conceptRelation)

        ## Start Graph
        graphSource = makeGraph.py2json(result[index], conceptRelation, All_degree)
        sourceLoc = os.path.join("./Web/conceptproto/play/static/play/data/" +sourceName)
        print(sourceLoc)
        with open(sourceLoc, "w") as f:
            f.write(graphSource)


def testFeature(concept):
    for c in concept:
        c = c.replace("/wiki/", "")
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
    playlistURL = 'https://www.youtube.com/playlist?list=PL8dPuuaLjXtN0ge7yDk_UA0ldZJdhwkoV'
    C = CE.ConceptExtraction(playlistURL)
    max_concept, max_weight = 5, 0.07
    makeGraph = MG.MakeGraph()
    result = C._get_onlyConcepts(max_concept, max_weight)
    origins = C.Pre._get_allURLs()

    conceptRelation = [[0, 1, 1, 1, 2],
                       [2, 0, 2, 1, 2],
                       [1, 1, 0, 1, 2],
                       [1, 1, 1, 0, 1],
                       [2, 2, 2, 2, 0]]

    #graphSource = makeGraph.py2json(result, conceptRelation) #err
    for index in range(len(origins)):

        sourceName = origins[index].split("v=")[1].split("&")[0] + ".json"
        print(result[index])
        print(sourceName)
        submitCode = "1503382656%7Ce5c72339e330f6814ae2fe97aa5c6301"
        defineConcept = DD.DefineDistance(submitCode)

        conceptRelation, All_degree = defineConcept.getConceptRelation(result[index])
        print(conceptRelation)

        # Start graph
        graphSource = makeGraph.py2json(result[index], conceptRelation, All_degree)
        sourceLoc = os.path.join("./Web/conceptproto/play/static/play/data/" + sourceName)
        print(sourceLoc)
        with open(sourceLoc, "w") as f:
            f.write(graphSource)

def testGetSubmitCode():
    import requests
    from bs4 import BeautifulSoup
    url = "http://degreesofwikipedia.com/"
    html = requests.get(url).text
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    submit = soup.select(
        'body > form > input[type = "hidden"]'
    )
    print(submit)

if __name__ == "__main__":
    main()
    #testGraph()
    #testGetSubmitCode()