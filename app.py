import argparse
parser = argparse.ArgumentParser()
parser.add_argument("operation", help="echo the string you use here", nargs='?', default="default")
args = parser.parse_args()
if args.operation == "test":
    import heatmap
    import flat
    print "test ok"