from argparse import ArgumentParser

from reporting.application.services.coverage_report_application_service import CoverageReportApplicationService


def get_args():
    arg_parse = ArgumentParser()
    arg_parse.add_argument("--pull-request", type=str, required=True, help="GitHub PR")
    arg_parse.add_argument("--repository", type=str, required=True, help="GitHub repository")
    return arg_parse.parse_args()


def main():
    args = get_args()
    CoverageReportApplicationService(args.repository).pull_request_merged(args.pull_request)


if __name__ == '__main__':
    pass
