from argparse import ArgumentParser

from reporting.application.services.coverage_report_application_service import CoverageReportApplicationService


def main():
    args = get_args()
    file_path = args.file
    CoverageReportApplicationService().run(file_path, args.pull_request, args.repository)


def get_args():
    arg_parse = ArgumentParser()
    arg_parse.add_argument("-f", dest="file", type=str, required=True, help="Path to JSON file containing coverage report")
    arg_parse.add_argument("--pull-request", type=str, required=True, help="GitHub PR")
    arg_parse.add_argument("--repository", type=str, required=True, help="GitHub repository")
    return arg_parse.parse_args()


if __name__ == '__main__':
    main()
