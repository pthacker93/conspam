from subprocess import call

commits = 20
filename = "delete"
extention = ".me"
pusher = "git push https://pthacler93:Peter@g27@github.com/pthacker93/conspam"

def git():
    call(["git", "add", "."])
    call(["git", "commit", "-m",'"commiter auto"']) 
    call(["git", "push", "https://pthacker93:Blackjack1@github.com/pthacker93/conspam"])
   




for i in range(0,commits):
    file = filename + str(i) + extention
    call(["touch", file])
    git()
    
call(["rm", "*.me"])

