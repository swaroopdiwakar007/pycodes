class Session():

    def __init__(self, obj):
        self.user_ip = obj[0]
        self.user_id = obj[1]
        self.user_pwd = obj[2]
        self.user_login = None

    def obj(self):
        self.user_login = pexpect.spawn('ssh ' + self.user_id + '@' + self.user_ip)
        index = self.user_login.expect(['assword:', 'yes/no', pexpect.TIMEOUT])
        if index == 0:
            self.user_login.sendline(self.user_pwd)
        elif index == 1:
            self.user_login.sendline('yes')
            self.user_login.expect('assword:')
            self.user_login.sendline(self.user_pwd)
        self.user_login.expect(prompt)
        print(self.user_login.before.decode('UTF-8', 'ignore') + prompt, end='')

    def send_command(self, command, expect=prompt, before=None, sec=12):
        self.user_login.sendline(command)
        if before:
            self.user_login.expect(before)
        if self.user_login.expect([expect, pexpect.TIMEOUT]) != 0:
            while (self.user_login.expect([expect, pexpect.TIMEOUT]) != 0) and (sec != 0):
                time.sleep(10)
                sec -= 1
        print(self.user_login.before.decode('UTF-8', 'ignore') + expect, end='')
        return (self.user_login.before.decode('UTF-8', 'ignore') + expect)
