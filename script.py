from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings),
        MRStep(reducer=self.reducer_sorted_outp)
        ]

    def mapper_get_ratings(self, _, line):
        (Name, Rating, User) = line.split(',')
        if Rating in ( "5","4","3") and User in ("100","101","22","23","24","25"):
            yield Name, 1

    def reducer_count_ratings(self, key, values):
        yield key, str(sum(values)).zfill(5)

    def reducer_sorted_outp(self, count, names):
        for name in names:
            yield count, name


if __name__ == '__main__':
    RatingsBreakdown.run()
