import argparse
from vocabulary import Vocabulary
from gui_tk_designer import MyGUI


def parse_arguments():
    parser = argparse.ArgumentParser(description="Display vocabulary with specified settings")
    parser.add_argument("-s", "--seed", type=int, default="0", help="Set seed (number only, default: 0)")
    parser.add_argument("-v", "--vocabulary", type=str, default="ci.json", help="Set vocabulary file name (default: ci.json)")
    parser.add_argument("-d", "--duration", type=int, default=3, help="Set duration for each word display (default: 3)")
    parser.add_argument("-n", type=int, default=5, help="Set number of words to display at once (default: 5)")
    return parser.parse_args()


def main():
    args = parse_arguments()
    print("Seed:", args.seed)
    print("Vocabulary file:", args.vocabulary)
    print("Duration:", args.duration)
    print("Number of words:", args.n)
    vocabulary = Vocabulary(file_name=args.vocabulary, seed=args.seed, n=args.n)
    my_gui = MyGUI(vocabulary, seed=args.seed, duration=args.duration)
    my_gui.run()


if __name__ == "__main__":
    main()
