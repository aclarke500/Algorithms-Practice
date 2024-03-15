startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

def do_jobs_conflict(job1, job2):
    # Check if job1 ends before job2 starts or job2 ends before job1 starts
    return not (job1['end'] <= job2['start'] or job2['end'] <= job1['start'])

def schedle_jobs(start_times, end_times, profit):

  jobs = []
  for i in range(len(profit)):
    jobs.append({
      "start":start_times[i],
      "end":end_times[i],
      "profit":profit[i],
      "ratio":profit[i]/(end_times[i]-start_times[i])
    })

  jobs_sorted = sorted(jobs, key=lambda job:job["profit"], reverse=True)
  selected_jobs = []
  for job in jobs_sorted:
    violated=False
    for added_job in selected_jobs:
      if do_jobs_conflict(job, added_job):
        violated = True

    if not violated:
      selected_jobs.append(job)

  print(selected_jobs)
  total = 0
  for s in selected_jobs:
    total+=s["profit"]

  print(total)

#   added_jobs = []
#   for job in jobs_sorted:
#     conflict = False
#     for added_job in added_jobs:
#       if (job["start"] < added_job["start"] and job["end"] > added_job["start"] or job["start"] < added_job["end"] and job["end"] > added_job["start"]):
#         conflict = True
#     if not conflict:
#       added_jobs.append(job)

#   print(added_jobs)

schedle_jobs(startTime, endTime, profit)