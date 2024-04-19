"""
Partitionned EDF using PartitionedScheduler.
"""
from core.Scheduler import SchedulerInfo
from schedulers.EDF_mono import EDF_mono
from utils import PartitionedScheduler
from utils.PartitionedScheduler import decreasing_worst_fit
from schedulers import scheduler

@scheduler("schedulers.P_EDF_WF")
class P_EDF_WF(PartitionedScheduler):
    def init(self):
        PartitionedScheduler.init(
            self, SchedulerInfo("schedulers.EDF_mono"), decreasing_worst_fit)
