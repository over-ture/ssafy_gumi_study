#!/bin/bash

# 현재 디렉터리의 모든 항목에 대해 루프 실행
for dir in */; do
    # 디렉터리 이름 끝의 '/' 제거
    dir_name="${dir%/}"
    
    # 해당 폴더 안에 파일 생성
    # touch 명령어로 빈 파일을 만듭니다.
    touch "$dir_name/${dir_name}.py"
    touch "$dir_name/${dir_name}_input.txt"
    
    echo "Created files in $dir_name"
done