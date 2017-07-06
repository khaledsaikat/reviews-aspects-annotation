#!/usr/bin/env python3
import json
from collections import Counter
from pprint import pprint


class Annotation:

    reviews = []

    topAspects = None

    def loadReviews(self, file_path):
        '''Load reviews from a json file'''
        with open(file_path) as json_data:
            self.reviews = json.load(json_data)


    def getManualAspects(self):
        '''Get all aspects name with number of reviews where the aspect were found'''
        aspects = []
        [aspects.extend(v["aspects"]) for v in self.reviews]
        return Counter(aspects)


    def _setTopAspects(self, minCount=5):
        '''Set top aspects which have minimum numbers of reviews'''
        aspects = self.getManualAspects()
        self.topAspects = Counter(
            {k: v for k, v in dict(aspects).items() if v >= minCount})


    def showManualAspects(self, minCount=5):
        '''Show all aspects and qualified aspects'''
        aspects = self.getManualAspects()
        print("Total count: ", len(aspects))
        print(aspects)

        self._setTopAspects(minCount)
        top = Counter({k: v for k, v in dict(
            aspects).items() if v >= minCount})
        print("\nTop count {} with min {} reviews".format(
            len(self.topAspects), minCount))
        pprint(self.topAspects)


    def mergeAllReviewsToLines(self):
        '''Merge all reviews into a single list'''
        lines = []
        for review in self.reviews:
            lines.extend(review["reviewTextJson"].values())
        return lines


    def getLineAspectsDict(self, review):
        '''Get line as key and aspects as list in a dict for a given review'''
        lineAspectsDict = {}
        for aspectName, aspectLines in review["aspects"].items():
            for aspectLine in aspectLines:
                if not aspectLine in lineAspectsDict:
                    lineAspectsDict[aspectLine] = []
                if aspectName in self.topAspects.keys():
                    lineAspectsDict[aspectLine].append(aspectName)
        return lineAspectsDict


    def getAllLinesAspectsDict(self):
        '''Get line as key and aspects as list in a dict for all reviews'''
        self._setTopAspects()
        lines = {}
        index = 0
        for review in self.reviews:
            lineAspectsDict = self.getLineAspectsDict(review)
            aspects = lineAspectsDict if lineAspectsDict else None
            for k, v in review["reviewTextJson"].items():
                lines[index] = lineAspectsDict[int(k)] if int(
                    k) in lineAspectsDict else None
                index += 1
        return lines


    def showLinesAspects(self):
        '''Showing line number of all reviews and their aspects'''
        lines = self.getAllLinesAspectsDict()
        pprint(lines)


    def getAspectsGruops(self):
        '''Return aspects clusters with reviews line number'''
        lines = self.getAllLinesAspectsDict()
        aspects = {}
        aspects["none"] = []
        for lineNumber, lineAspects in lines.items():
            if lineAspects:
                for aspectName in lineAspects:
                    if not aspectName in aspects:
                        aspects[aspectName] = []
                    aspects[aspectName].append(lineNumber)
            else:
                aspects["none"].append(lineNumber)
        return aspects


    def getAspectsGruopsText(self):
        '''Return aspects clusters with reviews text'''
        aspects = self.getAspectsGruops()
        lines = self.mergeAllReviewsToLines()
        for aspectName, lineNumbers in aspects.items():
            for index, lineNumber in enumerate(lineNumbers):
                aspects[aspectName][index] = lines[lineNumber]
        return aspects


    def showAspectsGruopsText(self):
        '''Showing aspects clusters with reviews text'''
        pprint(self.getAspectsGruopsText())



if __name__ == "__main__":
    a = Annotation()
    a.loadReviews("headphone100.json")
    a.showManualAspects()
    a.showLinesAspects()
    a.showAspectsGruopsText()
