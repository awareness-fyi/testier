from argparse import ArgumentParser


def get_args():
    arg_parse = ArgumentParser()
    arg_parse.add_argument("--pull-request", type=str, required=True, help="GitHub PR")
    arg_parse.add_argument("--repository", type=str, required=True, help="GitHub repository")
    return arg_parse.parse_args()


def main():
    # pull the diff
    # add the diff of the coverage to main branch
    pass


if __name__ == '__main__':
    pass
