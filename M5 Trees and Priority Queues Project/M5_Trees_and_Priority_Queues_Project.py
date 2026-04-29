#Hospital Triage System Test Program

from TriageSystem import TriageSystem

#Create a TriageSystem object
Triage = TriageSystem()

#Add the patients to the triage system from the chart in Canvas
Triage.AddPatient("Sofia", 5)
Triage.AddPatient("Bob", 2)
Triage.AddPatient("Charlie", 4)
Triage.AddPatient("Diana", 3)
Triage.AddPatient("Eli", 1)
Triage.AddPatient("Tom", 4)
Triage.AddPatient("Alice", 5)
Triage.AddPatient("Rachel", 4)

#Output header
print("Processing patients:")

#Print the patients in treatment order, including their names and severities, until the triage system is empty
while not Triage.IsEmpty():
    name, severity = Triage.ProcessNext()
    print(f"Now treating: {name} (severity {severity})")