# ConceptMap
![][1]
## How to create a Concept Map
**1. Concept Extraction**
- Extract Concepts from Video Subtitles of the Educational Youtube channel "Crash Course" (for Physics)
- Main Algorithm : TF-IDF(Term Frequency-Inverse Document Frequency) and Hierarchical Clustering
- [Link to Concept Extraction](https://github.com/eliceio/conceptMap/tree/master/ConceptExtraction)

**2. Relation Extraction**
- Define relationships between concepts through rank-based structures using Wikipedia links
- [Link to Relation Extraction](https://github.com/eliceio/conceptMap/tree/master/RelationExtraction)

**3. Web Developement**
- Create a Concept Map in a Website using Django framework
- [Link to Web Developement](https://github.com/eliceio/conceptMap/tree/master/WebDevelopement)


## Team Members& Role
- Seongwook Na, Relation Extraction
- Yeonghak Seo, Relation Extraction& Web Developement
- Ongyeol Lee, Web Developement
- [Jahye Ha](https://github.com/jahyeha), [Concept Extraction& Wikipedia Mapping](https://github.com/eliceio/conceptMap/tree/master/ConceptExtraction)
- Hyeongyu Shin(T.A.)


## Requirements
Initial requirements are as follows.
```
 Python 3.6.0
 Django 1.11.4
 NLTK 3.2.4
 Numpy 1.13.1
 BeautifulSoup 4.5.3
```

## References
- Lee, Ga-hee, and Han-joon Kim. "Automated development of rank-based concept hierarchical structures using Wikipedia links." Journal of Society for e-Business Studies 20.4 (2016). 
- Indegree : https://en.wikipedia.org/wiki/Special:WhatLinksHere


[1]: https://github.com/eliceio/conceptMap/blob/master/ConceptExtraction/note/proto.png
