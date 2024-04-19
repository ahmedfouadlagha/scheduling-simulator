"""
Partitionned EDF using PartitionedScheduler.
"""
from core.Scheduler import SchedulerInfo
from utils import PartitionedScheduler
from utils.PartitionedScheduler import decreasing_first_fit
from schedulers import scheduler

@scheduler("schedulers.P_EDF")
class P_EDF(PartitionedScheduler):
    def init(self):
        PartitionedScheduler.init(
            self, SchedulerInfo("schedulers.EDF_mono"), decreasing_first_fit)
