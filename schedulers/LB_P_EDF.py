"""
Partitionned EDF using PartitionedScheduler.
Try to load balance the tasks among the processors.
"""
from core.Scheduler import SchedulerInfo
from schedulers.EDF_mono import EDF_mono
from utils import PartitionedScheduler
from schedulers import scheduler

@scheduler("schedulers.LB_P_EDF")
class LB_P_EDF(PartitionedScheduler):
    def init(self):
        PartitionedScheduler.init(self, SchedulerInfo("schedulers.EDF_mono"))

    def packer(self):
        # First Fit
        cpus = [[cpu, 0] for cpu in self.processors]
        for task in self.task_list:
            m = cpus[0][1]
            j = 0
            # Find the processor with the lowest load.
            for i, c in enumerate(cpus):
                if c[1] < m:
                    m = c[1]
                    j = i

            # Affect it to the task.
            self.affect_task_to_processor(task, cpus[j][0])

            # Update utilization.
            cpus[j][1] += float(task.wcet) / task.period
        return True
