class Logger:

    def __init__(self):
        self.message_queue = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message not in self.message_queue :
            self.message_queue[message] = timestamp
            return True
        elif 10 > (timestamp - self.message_queue[message]):
            return False
        elif 10 <= (timestamp - self.message_queue[message]):
            self.message_queue[message] = timestamp
            return True
        

        
# ^^ this worked!!

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


if __name__ == "__main__" :
    obj = Logger()
    message = ""
    timestamp = 0
    param_1 = obj.shouldPrintMessage(timestamp,message)