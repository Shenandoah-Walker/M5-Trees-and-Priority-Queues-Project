import heapq

class TriageSystem:

    arrival_counter = 0

    def __init__(T):
        T.queue = []

    def AddPatient(T, name, severity):
        if name == None:
            raise ValueError("Patient must have a name.")
        if (severity < 1) or (severity > 5):
            raise ValueError("Severity must be between 1 and 5.")

        arrival_order = TriageSystem.NextArrivalOrder()

        heapq.heappush(T.queue, (-severity, arrival_order, name))






    #Class-level static method for AddPatient
    @staticmethod
    def NextArrivalOrder():
        current_arrival_order = TriageSystem.arrival_counter
        TriageSystem.arrival_counter += 1
        return current_arrival_order