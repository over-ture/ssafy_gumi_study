@echo off
set /p words="폴더 이름을 나열하세요 (예: a b c d): "

for %%a in (%words%) do (
    if not exist "%%a" (
        mkdir "%%a"
        echo 폴더 생성: %%a
    ) else (
        echo 이미 존재함: %%a
    )
)
pause