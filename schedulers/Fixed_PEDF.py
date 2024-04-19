#!/usr/bin/python
# coding=utf-8

from core.Scheduler import SchedulerInfo
from schedulers.EDF_mono import EDF_mono
from utils import PartitionedScheduler
from schedulers import scheduler

@scheduler("schedulers.Fixed_PEDF")
class Fixed_PEDF(PartitionedScheduler):
    def init(self):
        PartitionedScheduler.init(self, SchedulerInfo("EDF_mono", EDF_mono))

    def packer(self):
        for task in self.task_list:
            # Affect it to the task.
            cpu = next(proc for proc in self.processors
                       if proc.identifier == task.data["cpu"])
            self.affect_task_to_processor(task, cpu)
        return True
