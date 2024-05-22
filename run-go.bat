@echo off
setlocal

pushd "%~dp0"
cd back
cd api
cd go
go run main.go
popd
