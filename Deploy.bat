@echo off
setlocal

if "%~1"=="" (
  echo Usage: run_ssh.bat [foo]
  exit /b 1
)

set foo=%~1

ssh david@216.153.61.115 "docker image pull registry.tenant-palatial-platform.lga1.ingress.coreweave.cloud/Scion:test"

ssh david@216.153.61.115 "docker run --detach --name data registry.tenant-palatial-platform.lga1.ingress.coreweave.cloud/Scion:test"

ssh david@216.154.51.115 "docker cp data:/data ./%foo%"

ssh david@216.153.61.115 "C:\Users\david\UnrealEngine\Engine\Binaries\Win64\UnrealEditor-Cmd.exe C:\Users\david\Palatial_V01_UE53\Palatial_V01_UE53.uproject -ExecutePythonScript='C:\Users\david\PythonServer\BuildServer.py %foo% https://abad4791da6f642b2de41deee689ccaa.r2.cloudflarestorage.com/palatial-dev/uploads/projects/%foo%/' -NullRHI -DX12"

endlocal
