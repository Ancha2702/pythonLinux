import subprocess

def ch_out(command, text):
    try:
        output = subprocess.check_output(command, shell=True,stdout=subprocess.PIPE, encoding='UTF-8')
        if text in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

command = "cat/etc/os-release"
text = "tex"
res = ch_out(command, text)
print(res)
