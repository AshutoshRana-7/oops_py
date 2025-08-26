class v1():
    def __init__(self,chat,audio_call):
        self.chat= chat
        self.audio_call= audio_call
    
    def feature(self):
        print(self.chat)
        print(self.audio_call)

class v2(v1):
    def __init__(self,chat,audio_call,video_call,status):
        v1.__init__(self,chat,audio_call)
        self.video_call= video_call
        self.status= status
        
    def feature(self):
        v1.feature(self)
        print(self.video_call)
        print(self.status)

class v3(v2):
    def __init__(self, chat, audio_call, video_call, status, payments, meta_Ai):
        super().__init__(chat, audio_call, video_call, status, )
        self.payments= payments
        self.meta_Ai= meta_Ai
    
    def feature(self):
        super().feature()
        print(self.payments)
        print(self.meta_Ai)
        
user1 = v3('important stuff', 'possible', 'screenshere', 'upload', 'upi', 'meta_Ai')
user1.feature()