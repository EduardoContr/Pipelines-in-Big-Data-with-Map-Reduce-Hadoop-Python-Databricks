from mrjob.job import MRJob
from mrjob.step import MRStep

class Filemrjobs(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapfx,
                   reducer=self.redcrfx)
        ]

    def mapfx(self, _, line):
        (Symbol, LastPrice, Change, Changep,Ranker ) = line.split(',')
        yield Changep, 1

    def redcrfx(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    Filemrjobs.run()
