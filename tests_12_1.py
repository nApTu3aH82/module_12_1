import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        dist1 = runner.Runner('walk')
        for i in range(10):
            dist1.walk()
        self.assertEqual(dist1.distance, 50)

    def test_run(self):
        dist2 = runner.Runner('run')
        for i in range(10):
            dist2.run()
        self.assertEqual(dist2.distance, 100)

    def test_challeng(self):
        dist1 = runner.Runner('walk')
        dist2 = runner.Runner('run')
        for i in range(10):
            dist1.walk()
            dist2.run()
        self.assertNotEqual(dist1.distance, dist2.distance)


if __name__ == '__main__':
    RunnerTest.main()
