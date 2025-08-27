# # Approach
# - all message are stored hash map
#   key: message, value: timestamp
# - when the message is comming, check whether new message is or not,
#   if new, return True
# - when the message is known already, check last timestamp under time limnit or nor,
#   if under time limit, return False, else return True

class RequestLogger:
    def __init__(self, time_limit: int):
        self.messages = {}
        self.time_limit = time_limit

    # This function decides whether the message request should be accepted or rejected
    def message_request_decision(self, timestamp: int, request: str) -> bool:
        if request not in self.messages:
            # new message has arrived
            self.messages[request] = timestamp
            return True
        
        # known message has arrived
        last_timestamp = self.messages[request]
        self.messages[request] = timestamp
        if timestamp - last_timestamp > self.time_limit:
            return True
        return False


def main():
    # requests = [
    #     (1, "hello"),
    #     (4, "bye"),
    #     (5, "bye"),
    #     (10, "hello"),
    #     (11, "bye"),
    #     (14, "hello"),
    # ]

    requests = [
        [1,"good morning"],
        [5,"good morning"],
        [9,"i need coffee"],
        [10,"hello world"],
        [11,"good morning"],
        [15,"i need coffee"],
        [17,"hello world"],
        [25,"i need coffee"]
    ]

    request_logger = RequestLogger(7)

    for timestamp, request in requests:
        result = request_logger.message_request_decision(timestamp, request)
        print(f"timestamp: {timestamp},\trequest: {request}\t-> decision: {result}")


if __name__ == "__main__":
    main()