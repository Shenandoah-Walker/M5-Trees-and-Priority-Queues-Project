import heapq

class TriageSystem:

    arrivel_counter = 0

    def __init__(T):
        T.queue = []

    def AddPatient(T, name, severity):
        if name == None:
            raise ValueError("Patient must have a name.")
        if (severity < 1) or (severity > 5):
            raise ValueError("Severity must be between 1 and 5.")
