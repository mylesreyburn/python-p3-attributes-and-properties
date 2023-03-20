#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    
    def __init__(self, name = None, job = None) -> None:
        self.name = name
        self.job = job

    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) == str and (1 <= len(name) <= 25):
            self._name = name.title()
        elif name == None:
            pass
        else:
            print("Name must be string between 1 and 25 characters.")
    
    name = property(get_name, set_name,)

    def get_job(self):
        return self._job
    
    def set_job(self, job):
        if type(job) == str and job in APPROVED_JOBS:
            self._job = job
        elif job == None:
            pass
        else:
            print("Job must be in list of approved jobs.")
    
    job = property(get_job, set_job,)