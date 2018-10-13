from src.Algorithm.IAlgorythm import IAlgorythm


def _print(filename, array):
    with open(filename, 'w') as f:
        for item in array:
            f.write("%s\n" % item)


def logic(algo: IAlgorythm):
    while not algo.is_resolved():
        try:
            algo.compute()
        except (Exception, KeyboardInterrupt) as e:
            print(e)
            print(*algo.get_debug_infos(), sep='')
            return
        """ Todo: Write to a file """
        print("New computing action from the algorithm")
    algo.display_winning_path()
    print(*algo.get_debug_infos(), sep='')
    winning_path = algo.get_winning_path()
    _print(algo.get_file_name(), winning_path)
