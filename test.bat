@echo off
rmdir /s /q "C:\Users\al334\Downloads\TEST"
mkdir "C:\Users\al334\Downloads\TEST"
PowerShell -command "Clear-RecycleBin -Force"