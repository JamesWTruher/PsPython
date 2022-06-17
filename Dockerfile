FROM mcr.microsoft.com/powershell:lts-7.2-ubuntu-20.04

RUN apt update && apt install -y python3.8-full python3-pip wget vim
RUN pip install pythonnet --pre -U
RUN wget  "https://dotnet.microsoft.com/download/dotnet/scripts/v1/dotnet-install.sh" && \
    chmod +x dotnet-install.sh && \
    ./dotnet-install.sh  -version 6.0.100

ENV DOTNET_ROOT=/root/.dotnet
ENV PATH="$PATH:/root/.dotnet"

# save the profile which says how to demo
RUN mkdir -p /root/.config/powershell
COPY profile /root/.config/powershell/Microsoft.PowerShell_profile.ps1
# save the files needed for the demos
COPY pspython.runtimeconfig.json /root
COPY pspython.py /root
COPY pspar.py /root
COPY psrun.py /root
RUN chmod +x /root/pspython.py && \
    chmod +x /root/pspar.py && \
    chmod +x /root/psrun.py
