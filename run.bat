@echo off
setlocal enabledelayedexpansion

set arg1=%1
set arg2=%2

set folder=alg/lab%arg1%/lab%arg1%_%arg2%.py

python %folder%
