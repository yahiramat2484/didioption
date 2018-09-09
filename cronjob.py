from crontab import CronTab

job = CronTab(user="yamat")
command = job.new(command=". /Users/yamat/python/machineLearning/activate && python /Users/yamat/python/machineLearning/cron/job1.py",
        comment="Getting options")
command.setall("0 9-16 * * 1-5")
job.write()

for cron in job:
    print(cron)