BOJ-Solutions-Downloader
==========
[![](https://d2gd6pc034wcta.cloudfront.net/images/logo.png)](https://www.acmicpc.net)
----------
 `BOJ-Solutions-Downloader`는 [Baekjoon Online Judge](https://www.acmicpc.net)(이하 BOJ)에서 해결한 다양한 알고리즘 문제의 정답 소스코드를 다운로드 받을 수 있도록 도와줍니다. 이는 자신의 ID를 이용하여 BOJ에서 해결한 문제를 검색 및 분석하고, Local Repository에 해당 문제의 파일이 존재하지 않으면 소스코드를 다운로드 받아 저장합니다. 소스코드를 저장할 때에는 Directory 이름과 파일 이름 포맷을 정할 수 있는 옵션을 사용할 수 있습니다. **만약 소스코드 파일을 [GitHub](https://github.com)에 Push하기를 원한다면 [BOJ-AutoCommit](https://github.com/ISKU/BOJ-AutoCommit)을 추천합니다.**

Installation
----------
``` 
$ git clone https://github.com/ISKU/BOJ-Solutions-Downloader
```

**Dependency**
```
$ pip3 install requests
$ pip3 install bs4
```

How to use
----------
- 아래과 같이 프로그램을 실행합니다.
```
$ python3 main.py
```
- 만약 특정 문제만 다운로드 받기를 원한다면 다음과 같이 문제의 번호를 담은 파일을 명시합니다.
```
$ python3 main.py problems.txt
```
> :bulb: problems.txt에는 다운로드 받기 원하는 문제의 번호가 각 줄마다 있어야 합니다.

<br>

- **Options:**

| **option**      | **Description**
|:----------------|:-------------------------------------------------------------------------------------------
| **mkdir**       | 소스코드 파일을 저장할 때 Directory를 생성할지 결정하니다. (false: dir_name 옵션이 무시됩니다.)
| **dir_name**    | 소스코드 파일을 저장할 때 생성하는 Directory의 이름을 설정합니다.
| **source_name** | 소스코드 파일의 이름을 설정합니다.

> :bulb: [NO]: 만약 내용에 [NO]가 있으면 문제의 번호로 대체됩니다.<br>
> :bulb: [TITLE]: 만약 내용에 [TITLE]이 있으면 문제의 제목으로 대체됩니다.<br>

Default
----------
- 해결한 문제의 모든 정답코드를 검색 및 분석합니다.
- 만약 해결한 문제의 정답코드가 여러개가 있을 경우 **가장 마지막에 제출한 소스코드**를 선택합니다.
- 기본적으로 소스코드마다 Directory는 **생성하지 않습니다.**
- 소스코드 파일의 이름은 해당 **문제의 번호** 입니다.
- 프로그램 종료시 다운로드에 성공, 실패한 문제의 번호 목록이 담긴 파일이 함께 저장됩니다.

License
----------
> - [MIT](LICENSE)

Author
----------
> - Minho Kim ([ISKU](https://github.com/ISKU))
> - https://www.acmicpc.net/user/isku
> - **E-mail:** minho.kim093@gmail.com
