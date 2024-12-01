class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production", 
        "Legal", "Finance", "Sales", "General Management", 
        "Research & Development", "Marketing", "Purchasing"
    ]

    def __init__(self, name="John Doe", job="Admin"):
        self.name = name  # Calls the setter for name
        self.job = job  # Calls the setter for job

    # Name property
    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()  # Convert to title case
            print(f"Setting name to {self._name}.")
        else:
            print("Name must be a string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # Job property
    def get_job(self):
        print("Retrieving job.")
        return self._job

    def set_job(self, job):
        if job in Person.approved_jobs:
            print(f"Setting job to {job}.")
            self._job = job
        else:
            print("Job must be in the list of approved jobs.")

    job = property(get_job, set_job)
