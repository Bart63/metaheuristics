import graphrep as gr
from input_manager import CLIManager, TXTManager
from graphtester import test_all
from datetime import datetime
from os.path import join
import json

graph_representation_methods = [gr.DirAdjacencyList, gr.UndList]

def get_input_cli():
    return CLIManager().get_input()

def get_input_txt():
    return TXTManager().get_input()

def run_tests(res, filename="out"):
    stats = test_all(res)
    json.dump(stats, open(join('output', f"{filename}.json"), "w"))

def main():
    while True:
        option = input("Type 'f' for file inpute, 'm' for manual input, 'q' for quit: ")
        if option == 'q':
            break
        res = {}
        if option == 'f':
            res = get_input_txt()
        elif option == 'm':
            res = get_input_cli()
        if not res:
            continue
        filename = 'manual' if not res['filename'] else res['filename'][:-4]
        now = datetime.now()
        filename = filename + now.strftime("_%d-%m-%Y_%H-%M-%S")
        run_tests(res, filename)

if __name__=="__main__":
    main()