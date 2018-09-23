import sys
import os
import getpass
import datetime
from network import Network
from option import Option


ERROR_FORMAT = '\n* ERROR: [%s] [%s]\n'
PRINT_FORMAT = '* %s\n'
DEFAULT_DOWNLOAD_DIR = 'downloads'


class Main:

    def __init__(self, network, option):
        self.network = network
        self.option = option

    def run(self):
        problem_list = self.get_problem_list()
        succeed_list, failed_list = self.download_solutions(problem_list)
        self.finish(succeed_list, failed_list)

    def get_problem_list(self):
        user_problem_list = []
        if len(sys.argv) >= 2:
            if not os.path.exists(sys.argv[1]):
                sys.exit(ERROR_FORMAT % ('get_problem_list', "File does not exist at '%s'" % (sys.argv[1]))) 
            f = open(sys.argv[1], 'r')
            user_problem_list = [line.rstrip() for line in f]
            f.close()
        if len(user_problem_list) != 0:
            return user_problem_list

        error, problem_list = self.network.get_problem_list()
        if error:
            sys.exit(ERROR_FORMAT % ('get_problem_list', problem_list))
        return problem_list

    def download_solutions(self, problem_list):
        total = len(problem_list)
        success = 0
        fail = 0
        succeed_list = []
        failed_list = []

        try:
            for problem_id in problem_list:
                error, solved_problem = self.network.analyze_problem(problem_id)
                if error:
                    print(ERROR_FORMAT % ('analyze_problem', '%s (problem_id: %s)' % (solved_problem, problem_id)))
                    fail += 1
                    failed_list.append(problem_id)
                    continue

                dir_name = self.option.dir_name(solved_problem)
                source_name = self.option.source_name(solved_problem)
                error, ext = self.option.get_ext(solved_problem['language'])
                if error:
                    print(ERROR_FORMAT % ('get_ext', ext))
                    fail += 1
                    failed_list.append(problem_id)
                    continue

                dir_tree = '%s/%s' % (DEFAULT_DOWNLOAD_DIR, dir_name)
                file_path = '%s/%s%s%s' % (DEFAULT_DOWNLOAD_DIR, dir_name, source_name, ext)
                if os.path.exists(file_path):
                    print(ERROR_FORMAT % ('file_path', 'Source already exists (problem_id: %s)' % (problem_id)))
                    fail += 1
                    failed_list.append(problem_id)
                    continue
       
                error, source = self.network.download_source(solved_problem['submission_id'])
                if error:
                    print(ERROR_FORMAT % ('download_source', '%s (problem_id: %s)' % (source, problem_id)))
                    fail += 1
                    failed_list.append(problem_id)
                    continue

                self.save_source(dir_tree, file_path, source)
                print("* Saved successfully: '%s' (%d+%d/%d)" % (file_path, success, fail, total))
                success += 1
                succeed_list.append(problem_id)
        except KeyboardInterrupt:
            self.finish(succeed_list, failed_list)
            raise KeyboardInterrupt
            
        print('\n* Total: %d, Success: %d, Fail: %d' % (total, success, fail))
        return succeed_list, failed_list

    def save_source(self, dir_tree, file_path, source):
        if not os.path.isdir(dir_tree):
            os.makedirs(dir_tree)

        f = open(file_path, 'w')
        f.write(source)
        f.close()

    def finish(self, succeed_list, failed_list):
        time = str(datetime.datetime.now())

        if len(succeed_list) != 0:
            f = open('%s-%s.txt' % ('succeed', time), 'w')
            for problem_id in succeed_list:
                f.write(problem_id + '\n')
            f.close()

        if len(failed_list) != 0:
            f = open('%s-%s.txt' % ('failed', time), 'w')
            for problem_id in failed_list:
                f.write(problem_id + '\n')
            f.close()


def set_options():
    option_info = {}

    flag = input('* Do you want to set options? [yes/no]: ')
    while (flag != 'yes' and flag != 'no'):
        flag = input('* Do you want to set options? [yes/no]: ')
    option_info['flag'] = True if flag == 'yes' else False
    if flag == 'no':
        return option_info

    mkdir = input('* mkdir option [true/false]: ')
    while (mkdir != 'true' and mkdir != 'false'):
        mkdir = input('* mkdir option [true/false]: ')
    option_info['mkdir'] = True if mkdir == 'true' else False
    if mkdir == 'true':
        option_info['dir_name'] = input('* Directory name format: ')
    option_info['source_name'] = input('* Source name format: ')

    return option_info
 

if __name__ == '__main__':
    try:
        if os.path.isdir(DEFAULT_DOWNLOAD_DIR):
            sys.exit(ERROR_FORMAT % ('init', "Directory '%s' already exists") % DEFAULT_DOWNLOAD_DIR)
        os.makedirs(DEFAULT_DOWNLOAD_DIR)

        network = Network()
        user_id = input('* BOJ id: ')
        user_password = getpass.getpass('* BOJ password: ')
        error, result = network.login(user_id, user_password)
        if error:
            sys.exit(ERROR_FORMAT % ('login', result))
        print(PRINT_FORMAT % (result))

        option_info = set_options()
        option = Option(option_info)

        Main(network, option).run()
    except KeyboardInterrupt:
        print('\n* bye\n')
