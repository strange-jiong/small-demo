@echo off
date /t >> .\3389log.log
time /t >> .\3389log.log
netstat -an | find ":3389" | find "ESTABLISHED" >> .\3389log.log
rem echo 111


