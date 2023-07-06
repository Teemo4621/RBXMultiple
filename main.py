import os, sys, requests, time, re, zipfile, subprocess, colorama
from bs4 import BeautifulSoup
import urllib.request

os.system('cls')
os.system('title RBXMultiple')

currentPath = os.getcwd()

def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)

printSlow(f"{colorama.Fore.LIGHTMAGENTA_EX}MakeBy: ZEMONNUB")

count = input(f"{colorama.Fore.WHITE}\nAmount: ")

def getUrl():
    r = requests.post('https://store.rg-adguard.net/api/GetFiles', data={ "type": "url", "url": "https://apps.microsoft.com/store/detail/roblox/9NBLGGGZM6WM", "ring": "RP", "lang": "en-US" })

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")
        a_tags = soup.find_all('a')
        links = []
        if a_tags:
            for tag in a_tags:
                if 'href' in tag.attrs:
                    href = tag['href']
                    links.append(href)
                    
        return links[len(links)-1]
                
def downloadFromUrl(url):
    print('Downloading...')
    if not os.path.exists(f'{currentPath}\\RobloxUWP.msixbundle'):
        urllib.request.urlretrieve(url, "RobloxUWP.msixbundle")
    print('Download RobloxUWP Successfully')
    
def findFileName():
    with zipfile.ZipFile(f"{currentPath}\\RobloxUWP.msixbundle", 'r') as zip_ref:
        allfile = zip_ref.namelist()
        print("Extracted files RobloxUWP.msixbundle")
        for file in allfile:
            searchfile = re.search("Win32", f'{file}')
            if searchfile:
                return file
        
downloadFromUrl(getUrl())

def main(num):
    with zipfile.ZipFile(f"{currentPath}\\RobloxUWP.msixbundle", 'r') as zip_ref:
        zip_ref.extractall(f"{currentPath}")

    print(f'Create File Roblox {num}')

    with zipfile.ZipFile(f"{currentPath}\\{findFileName()}", 'r') as zip_ref:
        zip_ref.extractall(f"{currentPath}\\Roblox{num}")
    
    print(f'Create File Roblox {num} Successfully')
    
    path = f'{currentPath}\\Roblox{num}'
    
    os.remove(f'{path}\\AppxSignature.p7x')

    print('Edit File XML')
    
    headXML = f"""<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<Package IgnorableNamespaces="uap mp rescap build" xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10" xmlns:mp="http://schemas.microsoft.com/appx/2014/phone/manifest" xmlns:uap="http://schemas.microsoft.com/appx/manifest/uap/windows10" xmlns:rescap="http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities" xmlns:desktop="http://schemas.microsoft.com/appx/manifest/desktop/windows10" xmlns:build="http://schemas.microsoft.com/developer/appx/2015/build">
<Identity Name="ROBLOXCORPORATION.ROBLOX.{num}" Publisher="CN=6FEF9772-62F8-4C8B-8DE0-70F628846515" Version="2.581.563.0" ProcessorArchitecture="x86" />
<mp:PhoneIdentity PhoneProductId="880029fb-d4a3-483c-bc85-3879e2129f1a" PhonePublisherId="b9c585ba-231e-4040-918f-836ba9701ea8" />
<Properties>
    <DisplayName>Roblox {num}</DisplayName>
    <PublisherDisplayName>ROBLOX Corporation</PublisherDisplayName>
    <Logo>Assets/Tiles/RobloxStoreLogo50x50.png</Logo>
</Properties>
<Dependencies>
    <TargetDeviceFamily Name="Windows.Desktop" MinVersion="10.0.17763.0" MaxVersionTested="10.0.18362.0" />
    <PackageDependency Name="Microsoft.VCLibs.140.00" MinVersion="14.0.30035.0" Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" />
</Dependencies>
<Resources>
    <Resource Language="EN" />
    <Resource uap:Scale="200" />
</Resources>
<Applications>
    <Application Id="App" Executable="Windows10Universal.exe" EntryPoint="Roblox.App">
    <uap:VisualElements DisplayName="Roblox {num}" Square150x150Logo="Assets\Tiles\RobloxTile150x150.png" Square44x44Logo="Assets\Tiles\RobloxTile44x44.png" Description="Powering Imagination" BackgroundColor="transparent">
        <uap:DefaultTile ShortName="Roblox {num}" Square310x310Logo="Assets/Tiles/RobloxTile310x310.png" Wide310x150Logo="Assets\Tiles\RobloxTile310x150.png" Square71x71Logo="Assets\Tiles\RobloxTile71x71.png">
        <uap:ShowNameOnTiles>
            <uap:ShowOn Tile="square150x150Logo" />
            <uap:ShowOn Tile="square310x310Logo" />
        </uap:ShowNameOnTiles>
        </uap:DefaultTile>
        <uap:SplashScreen Image="Assets/SplashScreen/RobloxSplash620x300.png" BackgroundColor="#F5F5F5" />
        <uap:InitialRotationPreference>
        <uap:Rotation Preference="landscape" />
        </uap:InitialRotationPreference>
    </uap:VisualElements>
    <uap:ApplicationContentUriRules>
        <uap:Rule Match="http://*.roblox.com" Type="include" WindowsRuntimeAccess="none" />
        <uap:Rule Match="https://*.roblox.com" Type="include" WindowsRuntimeAccess="none" />
        <uap:Rule Match="http://*.robloxlabs.com" Type="include" WindowsRuntimeAccess="none" />
        <uap:Rule Match="https://*.robloxlabs.com" Type="include" WindowsRuntimeAccess="none" />
        <uap:Rule Match="http://*.*.robloxlabs.com" Type="include" WindowsRuntimeAccess="none" />
        <uap:Rule Match="https://*.*.robloxlabs.com" Type="include" WindowsRuntimeAccess="none" />
    </uap:ApplicationContentUriRules>
    <Extensions>
        <desktop:Extension Category="windows.fullTrustProcess" Executable="Assets/CrashHandler.exe">
        <desktop:FullTrustProcess />
        </desktop:Extension>
        <uap:Extension Category="windows.protocol">
        <uap:Protocol Name="roblox{num}" />
        </uap:Extension>
    </Extensions>
    </Application>
</Applications>
<Capabilities>
    <rescap:Capability Name="confirmAppClose" />
    <rescap:Capability Name="runFullTrust" />
    <Capability Name="internetClient" />
    <Capability Name="privateNetworkClientServer" />
</Capabilities>
    """
    
    lastXML = """
<build:Metadata>
    <build:Item Name="cl.exe" Version="19.29.30151.0 built by: cloudtest" />
    <build:Item Name="VisualStudio" Version="16.0" />
    <build:Item Name="OperatingSystem" Version="10.0.14393.0 (rs1_release.160715-1616)" />
    <build:Item Name="Microsoft.Build.AppxPackage.dll" Version="16.0.33801.447" />
    <build:Item Name="ProjectGUID" Value="{9D842709-954F-34A6-AC7F-FD7F7C9722D9}" />
    <build:Item Name="OptimizingToolset" Value="None" />
    <build:Item Name="TargetRuntime" Value="Native" />
    <build:Item Name="Microsoft.Windows.UI.Xaml.Build.Tasks.dll" Version="0.0.0.0" />
    <build:Item Name="MakePri.exe" Version="10.0.22000.194 (WinBuild.160101.0800)" />
</build:Metadata>
</Package>
    """
    with open(f'{path}\\AppxManifest.xml', 'w') as file:
        file.write(headXML + lastXML)
        
    print("Edit File XML Success")
    
    print(f"Install Roblox {num}.....")
    
    command = ["powershell", "-Command", "Add-AppxPackage", "-path", f"'{currentPath}\\Roblox{str(num)}\\AppxManifest.xml'", "-register"]
    subprocess.run(command, shell=True, check=True)
    
    print(f"Install Roblox {num} Successfull")

for i in range(int(count)):
    main(i + 1)
    os.system('cls')