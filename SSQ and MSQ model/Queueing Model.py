import numpy as np

np.random.seed(1)


class SSQ:
    def __init__(self, q_mode, max_customer):

        self.max_customer = max_customer
        self.inter_arrivals = [0.4, 1.2, 0.5, 1.7, 0.2, 1.6, 0.2, 1.4, 1.9, 0.7]
        # 0.4, 1.6, 2.1, 3.8, 4.0, 5.6, 5.8, 7.2, 10.1, 10.8
        self.service_times = [2.0, 0.7, 0.2, 1.1, 3.7, 0.6, 0.9, 1.5, 1.2, 0.7]
        # self.inter_arrivals = list(np.random.exponential(1 / 3.0, self.max_customer + 1))
        # self.service_times = list(np.random.exponential(1 / 4.0, self.max_customer + 1))
        print(self.inter_arrivals)
        print(self.service_times)
        self.clock = 0.0
        self.Q_MODE = q_mode

        self.next_arrival = self.inter_arrivals.pop(0)
        self.next_departure_s = [float('infinity'), float('infinity'), float('infinity')]

        self.num_in_queue = 0
        self.times_of_arrival_queue = []  # store times of arrivals who are waiting in the queue
        self.service_times_in_queue = []  # store service times of waiting customers in the queue

        self.total_delay = 0.0
        self.num_of_delays = 0.0
        self.area_under_q = 0.0
        self.area_under_b1 = 0.0
        self.area_under_b2 = 0.0

        self.server1_status = 0  # 0 for IDLE , 1 for BUSY
        self.server2_status = 0
        self.last_event_time = 0.0  # we will need to store last event clock time

    def start(self):
        while self.num_of_delays < self.max_customer:
            self.timing()

        str_q_mode = ""
        if self.Q_MODE == 1:
            str_q_mode = 'FIFO'
        elif self.Q_MODE == 2:
            str_q_mode = 'LIFO'
        else:
            str_q_mode = 'SJF'

        # Showing final results
        print("Analyzed report for '" + str(self.max_customer) + "' max customer with Queueing mode '" + str(str_q_mode) + "':")
        print("random seed: ", 1)
        print("Average delay = " + str(round((self.total_delay / self.num_of_delays), 4)))
        print("Expected number of customers in queue = " + str(round(self.area_under_q / self.clock, 4)))
        print("Expected utilization of the server 1 = " + str(round(self.area_under_b1 / self.clock, 4)))
        print("Expected utilization of the server 2 = " + str(round(self.area_under_b2 / self.clock, 4)))
        print(" ")

    def timing(self):
        self.clock = min(self.next_arrival, self.next_departure_s[1], self.next_departure_s[2])

        self.update_register()

        if self.next_arrival == self.clock:
            print("Arrival at Clock:" + str(round(self.clock, 4)))
            self.arrival()
        elif self.next_departure_s[1] == self.clock:
            print("Departure from server 1 at Clock:" + str(round(self.clock, 4)))
            self.departure(1)
        else:
            print("Departure from server 2 at Clock:" + str(round(self.clock, 4)))
            self.departure(2)

        print("Server 1 Status:" + str(self.server1_status))
        print("Server 2 Status:" + str(self.server2_status))
        print("Times of arrivals in Queue: " + str(self.times_of_arrival_queue))
        print("Service times in Queue: " + str(self.service_times_in_queue))
        print("Number of Delays: " + str(self.num_of_delays))
        print("Total Delay:" + str(round(self.total_delay, 4)))
        print("Next Arrival Time: " + str(round(self.next_arrival, 4)))
        print("Next Departure Time For Server 1: " + str(round(self.next_departure_s[1], 4)))
        print("Next Departure Time For Server 2: " + str(round(self.next_departure_s[2], 4)))
        print("Area under Q(t): " + str(round(self.area_under_q, 4)))
        print("Area under B(t) for server 1: " + str(round(self.area_under_b1, 4)))
        print("Area under B(t) for server 2: " + str(round(self.area_under_b2, 4)))
        print(" ")

    def arrival(self):
        self.next_arrival += self.inter_arrivals.pop(0)  # Schedule next arrival time = arrival + next interArrival time
        selected_server = 0
        # selecting servers based on condition in the question
        if self.server1_status == 0 and self.server2_status == 0:  # both Server IDLE
            selected_server = 1
        elif self.server1_status == 0 and self.server2_status == 1:  # both Server IDLE
            selected_server = 1
        elif self.server1_status == 1 and self.server2_status == 0:  # both Server IDLE
            selected_server = 2

        if selected_server == 1:  # Server1 IDLE
            self.server1_status = 1  # make server BUSY
            delay = 0.0  # so delay is zero
            self.total_delay += delay
            self.num_of_delays += 1  # increase the number of customers delayed
            # schedule next departure, pop the first element of service_times list to get service time of this customer
            self.next_departure_s[1] = self.clock + self.service_times.pop(0)  # schedule departure of this customer
        elif selected_server == 2:  # Server 2 IDLE
            self.server2_status = 1  # make server BUSY
            delay = 0.0  # so delay is zero
            self.total_delay += delay
            self.num_of_delays += 1  # increase the number of customers delayed
            # schedule next departure, pop the first element of service_times list to get service time of this customer
            self.next_departure_s[2] = self.clock + self.service_times.pop(0)  # schedule departure of this customer

        else:
            # increase queue length, this customer will have to wait in the queue
            # print("In queue", self.server1_status, self.server2_status)
            self.num_in_queue += 1

            # store the arrival time and service time of this customer in separate lists
            self.times_of_arrival_queue.append(self.clock)
            self.service_times_in_queue.append(self.service_times.pop(0))

    def departure(self, server):
        # check number of customers in the queue
        if self.num_in_queue == 0:  # if no customer in the queue, queue empty
            # make server IDLE
            if server == 1:
                self.server1_status = 0
            else:
                self.server2_status = 0
            # schedule next departure= infinity
            self.next_departure_s[server] = float('infinity')

        else:
            # if queue not empty, pop one customer, decrease queue length
            self.num_in_queue -= 1
            self.num_of_delays += 1
            # AS FIFO, pop first arrival and service time from the queue.
            # IF LIFO we have to pop last arrival and service time.
            # For SJF, find the index of minimum service time from  service_times_in_queue list.
            # Then pop the arrival of that index from times_of_arrival_queue for delay count and others.
            if self.Q_MODE == 1:
                arrival = self.times_of_arrival_queue.pop(0)

                delay = self.clock - arrival
                self.total_delay += delay
                self.next_departure_s[server] = self.clock + self.service_times_in_queue.pop(0)
            if self.Q_MODE == 2:
                arrival = self.times_of_arrival_queue.pop(-1)

                delay = self.clock - arrival
                self.total_delay += delay
                self.next_departure_s[server] = self.clock + self.service_times_in_queue.pop(-1)
            if self.Q_MODE == 3:
                index_to_pop = self.service_times_in_queue.index(min(self.service_times_in_queue))
                arrival = self.times_of_arrival_queue.pop(index_to_pop)

                delay = self.clock - arrival
                self.total_delay += delay
                self.next_departure_s[server] = self.clock + self.service_times_in_queue.pop(index_to_pop)

    def update_register(self):
        time_difference = self.clock - self.last_event_time
        self.area_under_q += time_difference * self.num_in_queue
        self.area_under_b1 += time_difference * self.server1_status
        self.area_under_b2 += time_difference * self.server2_status
        self.last_event_time = self.clock


# Main method
if __name__ == "__main__":
    while 1:
        print("Select Queueing model:")
        print("1 for FIFO.\n2 for LIFO.\n3 for SJF.")
        try:
            q_choice = int(input("Queue Mode>>> "))
            m_c = int(input("Max Delay Count>>> "))
            if 1 <= q_choice <= 3:
                if m_c > 0:
                    model = SSQ(q_choice, m_c)
                    model.start()
                    break
                else:
                    print("\nMax customer count can't be less than ZERO!")
            else:
                print("\nWrong choice of queueing mode. Read the instruction.")
        except:
            print("Wrong input type.")
