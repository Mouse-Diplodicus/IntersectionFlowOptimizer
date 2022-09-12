import cityflow


def app():
    config_path = "examples/config.json"
    eng = cityflow.Engine(config_path, thread_num=1)
    print(eng.get_vehicle_count())
    eng.next_step()
    print(eng.get_vehicle_count())


if __name__ == '__main__':
    app()

