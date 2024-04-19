#!/usr/bin/python3

import sys
from core import Model, ProcEvent
from configuration import Configuration


def main(argv):
    if len(argv) == 2:
        # Configuration load from a file.
        configuration = Configuration(argv[1])
    else:
        # Manual configuration:
        configuration = Configuration()

        configuration.duration = 420 * configuration.cycles_per_ms

        # Add tasks:
        configuration.add_task(name="T1", identifier=1, period=7,
                               activation_date=0, wcet=3, deadline=7)
        configuration.add_task(name="T2", identifier=2, period=12,
                               activation_date=0, wcet=3, deadline=12)
        configuration.add_task(name="T3", identifier=3, period=20,
                               activation_date=0, wcet=5, deadline=20)

        # Add a processor:
        configuration.add_processor(name="CPU 1", identifier=1)

        # Add a scheduler:
        # configuration.scheduler_info.filename = "../schedulers/RM.py"
        configuration.scheduler_info.clas = "schedulers.RM"

    # Check the config before trying to run it.
    configuration.check_all()
    
    # Init a model from the configuration.
    model = Model(configuration)

    # Execute the simulation.
    model.run_model()

    # Print logs.
    for log in model.logs:
        print(log)

    # The computation time of the jobs
    for task in model.results.tasks:
        print(task.name + ":")
        for job in task.jobs:
            print("%s %.3f ms" % (job.name, job.computation_time))

    # the number of preemptions per task
    for task in model.results.tasks.values():
        print("%s %s" % (task.name, task.preemption_count))

    # the number of context switches 
    # a context switch is something that happen when 
    # the previous task running on the same processor is different
    cxt = 0
    for processor in model.processors:
        prev = None
        for evt in processor.monitor:
            if evt[1].event == ProcEvent.RUN:
                if prev is not None and prev != evt[1].args.task:
                    cxt += 1
                prev = evt[1].args.task

    print("Number of context switches: " + str(cxt))


main(sys.argv)
