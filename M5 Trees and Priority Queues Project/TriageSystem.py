import heapq

#Class: TriageSystem
#Purpose: To maintain a triage queue where patients are prioritized by severity (higher is more urgent). Ties are broken by arrival order (earlier first).

class TriageSystem:

    arrival_counter = 0

    #Method: __init__
    #Purpose: Initializes the triage system with an empty queue
    #Parameters: 
    # - TriageSystem T : The triage system object being initialized
    #Returns: None
    #Preconditions: None
    #Postconditions: A new, empty triage system T with internal queue empty is returned and the class-level arrival counter is unchanged (or initiated to 0 if first instance)
    def __init__(T):
        T.queue = []

    #Method: AddPatient
    #Purpose: Adds a patient to the triage system with the given name and severity
    #Parameters:
    # - TriageSystem T : The triage system object to which the patient will be added
    # - str name : The name of the patient being added
    # - int severity : The severity level of the patient being added
    #Returns: None
    #Preconditions: name must be a non-empty string, severity must be an integer between 1 and 5, inclusive
    #Postconditions: A new patient (name, severity) is inserted into T’s private queue with priority ordered by higher severity before lower and for equal severity, earlier arrival (as determined by the class-level counter) before later.
    def AddPatient(T, name, severity):
        if name == None:
            raise ValueError("Patient must have a name.")
        elif (severity < 1) or (severity > 5):
            raise ValueError("Severity must be between 1 and 5.")

        else:

         arrival_order = TriageSystem.NextArrivalOrder()

         heapq.heappush(T.queue, (-severity, arrival_order, name))

    #Method: ProcessNext
    def ProcessNext(T):
        if T.IsEmpty():
            return None

        else:
            negative_severity, arrival_order, name = heapq.heappop(T.queue)
            severity = -negative_severity
            return (name, severity)

    def PeekNext(T):
        if T.IsEmpty():
            return None
        else:
            negative_severity, arrival_order, name = T.queue[0]
            severity = -negative_severity
            return (name, severity)

    def IsEmpty(T):
        if len(T.queue) == 0:
            return True
        else:
            return False


    def Size(T):
        return len(T.queue)

    def Clear(T):
        T.queue = []



    #Class-level static method for AddPatient
    @staticmethod
    def NextArrivalOrder():
        current_arrival_order = TriageSystem.arrival_counter
        TriageSystem.arrival_counter += 1
        return current_arrival_order