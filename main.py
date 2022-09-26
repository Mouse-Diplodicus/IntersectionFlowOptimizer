import cityflow


class Model:

    def __init__(self, config_path, num_threads=1):
        self.config_path = config_path
        self.engine = cityflow.Engine(config_path, thread_num=num_threads)

    def simulate(self, num_steps):
        wait_time = 0
        for i in range(0, num_steps):
            # since interval is 1 wait_time is sum of the number of vehicles waiting
            self.engine.next_step()
            wait_time += sum(self.engine.get_lane_waiting_vehicle_count().values())
        print(wait_time)


if __name__ == '__main__':
    test = Model("examples/config.json")
    test.simulate(1000)
