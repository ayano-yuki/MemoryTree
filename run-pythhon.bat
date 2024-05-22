@echo off
setlocal

pushd "%~dp0"
cd back
cd api
cd python
uvicorn main:app --reload
popd
