class Option:

    def __init__(self, option_info):
        self.option_info = option_info
        self.flag = option_info['flag']

    def mkdir(self):
        if self.flag == False:
            return False
        return self.option_info['mkdir']

    def dir_name(self, problem):
        if self.flag == False:
            return ''
        if not self.mkdir():
            return ''
        return self.replace_name(self.option_info['dir_name'], problem) + '/'

    def source_name(self, problem):
        if self.flag == False:
            return problem['problem_id']
        return self.replace_info(self.option_info['source_name'], problem)

    def replace_name(self, value, problem):
        value = value.replace('[NO]', problem['problem_id'])
        value = value.replace('[TITLE]', problem['problem_title'])
        return value

    def get_ext(self, language):
        extensions = {
            'C': '.c',
            'C++': '.cpp',
            'C++11': '.cpp',
            'C++14': '.cpp',
            'C++17': '.cpp',
            'Java': '.java',
            'Java (OpenJDK)': '.java',
            'C11': '.c',
            'Python 2': '.py',
            'Python 3': '.py',
            'PyPy2': '.py',
            'PyPy3': '.py',
            'Ruby2.5': '.rb',
            'Kotlin': '.kt',
            'Swift': '.swift',
            'C# 6.0': '.cs',
            'Text': '.txt',
            'node.js': 'js',
            'Go': '.go',
            'F#': '.fs',
            'PHP': '.php',
            'Pascal': '.pas',
            'Lua': '.lua',
            'Perl': '.pl',
            'Objective-C': '.m',
            'Objective-C++': '.mm',
            'C (Clang)': '.c',
            'C++11 (Clang)': '.cpp',
            'C++14 (Clang)': '.cpp',
            'C++17 (Clang)': '.cpp',
            'Golfscript': '.gs',
            'Bash': '.sh',
            'Fortran': '.f95',
            'Scheme': '.scm',
            'Ada': '.ada',
            'awk': '.awk',
            'OCaml': '.ml',
            'Brainfuck': '.bf',
            'Whitespace': '.ws',
            'Tcl': '.tcl',
            'Assembly (32bit)': '.asm',
            'Assembly (32bit)': '.asm',
            'D': '.d',
            'Clojure': '.clj',
            'Rhino': '.js',
            'Cobol': '.cob',
            'SpiderMonkey': '.js',
            'Pike': '.pike',
            'sed': '.sed',
            'Rust': '.rs',
            'Boo': '.boo',
            'Intercal': '.i',
            'bc': '.bc',
            'Nemerle': '.n',
            'Cobra': '.cobra',
            'Algol 68': '.a68',
            'Befunge': '.bf',
            'Haxe': '.hx',
            'LOLCODE': '.lol',
            'VB.NET 4.0': '.vb',
            '아희': '.aheui'
        }
        
        if not language in extensions:
            return True, 'Unknown extension'
        return False, extensions[language]
