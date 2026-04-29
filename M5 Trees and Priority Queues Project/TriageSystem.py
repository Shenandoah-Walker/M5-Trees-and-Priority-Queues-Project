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
    #Purpose: Removes and returns the next patient to be treated from the triage system, which is the patient with the highest severity. If there are multiple patients with the same severity, the one who arrived first is treated first.
    #Parameters:
    # - TriageSystem T : The triage system object from which the next patient will be processed
    #Returns: A tuple (name, severity) of the next patient to be treated, or None if the triage system is empty
    #Preconditions: None
    #Postconditions: If T is empty, None is returned and T is unchanged. Otherwise, the patient with the highest priority is removed and returned
    def ProcessNext(T):
        if T.IsEmpty():
            return None
        else:
            negative_severity, arrival_order, name = heapq.heappop(T.queue)
            severity = -negative_severity
            return (name, severity)

    #Method: PeekNext
    #Purpose: To return (without removing) the next patient to be treated from the triage system, which is the patient with the highest priority
    #Parameters:
    # - TriageSystem T : The triage system object from which the next patient will be peeked
    #Returns: A tuple (name, severity) of the next patient to be treated, or None if the triage system is empty
    #Preconditions: None
    #Postconditions: If T is nonempty, returns (without removing) the patient that would bereturned by ProcessNext. If T is empty, returns None. In either case, T is unchanged.
    def PeekNext(T):
        if T.IsEmpty():
            return None
        else:
            negative_severity, arrival_order, name = T.queue[0]
            severity = -negative_severity
            return (name, severity)

    #Method: IsEmpty
    #Purpose: To determine whether the triage system is empty
    #Parameters:
    # - TriageSystem T : The triage system object being checked for emptiness
    #Returns: True if T is empty, False otherwise
    #Preconditions: None
    #Postconditions: Returns True if T’s internal queue is empty, False otherwise. In either case, T is unchanged.
    def IsEmpty(T):
        if len(T.queue) == 0:
            return True
        else:
            return False

    #Method: Size
    #Purpose: To return the number of patients currently in the triage system
    #Parameters:
    # - TriageSystem T : The triage system object for which the size is being calculated
    #Returns: The number of patients currently in T
    #Preconditions: None
    #Postconditions: Returns the number of patients currently in T’s internal queue. T is unchanged.
    def Size(T):
        return len(T.queue)

    #Method: Clear
    #Purpose: To remove all patients from the triage system, making it empty
    #Parameters:
    # - TriageSystem T : The triage system object to be cleared
    #Returns: None
    #Preconditions: None
    #Removes all patients from T. Size becomes 0.
    def Clear(T):
        T.queue = []



    #Class-level static method for AddPatient
    
    #Method: NextArrivalOrder
    #Purpose: To return the next arrival order number for a new patient being added to the triage system.
    #Parameters: None
    #Returns: The next arrival order number
    #Preconditions: None
    #Postconditions:  The arrival order number is returned and the class-level arrival counter is incremented by 1.
    @staticmethod
    def NextArrivalOrder():
        current_arrival_order = TriageSystem.arrival_counter
        TriageSystem.arrival_counter += 1
        return current_arrival_order