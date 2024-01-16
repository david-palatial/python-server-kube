@echo off 

sps-app deploy .\Saved\StagedBuilds --owner %1 --branch %2 -C
