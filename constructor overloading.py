class IPL: 

    def __init__(self,*details):
        self.details = details



    @classmethod
    def net_practice(cls):
        print("Net Practice")

    def play(self):
        print(self.details, 'is playing')

player1 = IPL("dhoni","wk")
player2 = IPL("rohit")
player1.net_practice()
player2.net_practice()
player1.play()
player2.play()
IPL.net_practice()
