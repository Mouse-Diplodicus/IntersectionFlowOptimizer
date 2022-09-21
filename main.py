import cityflow


class Model:

    def __init__(self, config_path, num_threads = 1):
        self.config_path = config_path
        self.engine = cityflow.Engine(config_path, thread_num=num_threads)
        self.age = age

    def simulate(self, num_steps):
        for i in range(0, num_steps):
            print(self.engine.get_vehicle_count())
            self.engine.next_step()


if __name__ == '__main__':
    test = Model("examples/config.json")
    test.simulate(1000)
