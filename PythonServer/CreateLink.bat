@echo off 

sps-app create-link https://%1.palatialxr.com/%2 -C

REM ssh -tv david@palatial.tenant-palatial-platform.coreweave.cloud sudo -E python3 ~/link-deployment/run_pipeline.py https://%1.palatialxr.com/%2 -C
