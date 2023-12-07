from mrjob.job import MRJob
from mrjob.step import MRStep
import sys
import heapq

class top_unigramas(MRJob):
  def steps(self):
    return [
        MRStep(mapper=self.mapper1,
                reducer=self.reducer1),
        MRStep(mapper = self.mapper2,
                reducer=self.reducer2)
      ]


  def mapper1(self, _, line):

    # palabra     año         apariciones     num_libros

    items = line.strip().split('\t')
    palabra = items[0]
    anho = int(items[1])
    apariciones = int(items[2])

    decada = (anho // 10) * 10
    if 1950 <= decada <= 2010:
        yield ((decada, palabra), apariciones)

  def reducer1(self, decada_palabra, apariciones):
    yield (decada_palabra, sum(apariciones))

  def mapper2(self, decada_palabra, apariciones):
    decada, palabra  = decada_palabra
    yield (decada, (palabra, apariciones))

  def reducer2(self, decada, palabra_apariciones):

    # yield (decada, top_palabras)
    # yield (decada, max(palabra_apariciones, key = lambda x : x[1]))                       # solo la top 1

    # Find the top 5 words with the highest occurrences
    top_5_words = heapq.nlargest(5, palabra_apariciones, key=lambda x: (x[1], x[0]))        # el top 5

    # Sort the top words alphabetically in case of ties
    sorted_top_5_words = sorted(top_5_words, key=lambda x: x[0])                            #orden alfabético

    # yield the result
    yield (decada, sorted_top_5_words)

if __name__ == '__main__':
    top_unigramas.run()

  
