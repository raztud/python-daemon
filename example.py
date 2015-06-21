__author__ = 'razvan'
from daemon import Daemon
import sched
import time


class pantalaimon(Daemon):

    def doChecks(self, sc, firstRun):
        f = open('./myfile','a+')
        f.write("Checking... ")

        if firstRun:
            f.write("First time")

        sc.enter(10, 1, self.doChecks, (sc, False))

    def run(self):
        
        s = sched.scheduler(time.time, time.sleep)
        s.enter(10, 1, self.doChecks, (s, False))
        self.doChecks(s, True)
        s.run()

pineMarten = pantalaimon('/tmp/pid.pid')
pineMarten.start()


