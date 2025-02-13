import ctypes
import json
import os

# Load the shared library
lib_path = os.path.join(os.path.dirname(__file__), 'libuseragent.so')
lib = ctypes.CDLL(lib_path)

# Define the function signature
lib.Parse.argtypes = [ctypes.c_char_p]
lib.Parse.restype = ctypes.c_char_p

lib.FreeCString.argtypes = [ctypes.c_char_p]
lib.FreeCString.restype = None

# lib.free.argtypes = [ctypes.c_void_p]


def parse_user_agent(user_agent):
    if not isinstance(user_agent, str):
        return None
    result_ptr = lib.Parse(ctypes.c_char_p(user_agent.encode('utf-8')))
    result_str = result_ptr.decode("utf-8")
    # lib.FreeCString(result_ptr)  # Free memory allocated by Go
    return json.loads(result_str)
    ######
    # try:
    #     result_ptr = lib.Parse(user_agent.encode('utf-8'))
    #     if not result_ptr:
    #         return None
        
    #     result_str = ctypes.string_at(result_ptr).decode('utf-8')
    #     lib.FreeCString(result_ptr)
    #     return json.loads(result_str)
    # except Exception as e:
    #     print(f"Error parsing user agent: {e}")
    #     return None
    ######
    # try:
    #     # Convert the user agent string to bytes
    #     ua_bytes = user_agent.encode('utf-8')
        
    #     # Call the Go function
    #     result_ptr = lib.Parse(ua_bytes)
    #     if not result_ptr:
    #         return None

    #     try:
    #         # Convert the result to a Python string
    #         result_str = ctypes.string_at(result_ptr).decode('utf-8')
    #         # Parse the JSON
    #         return json.loads(result_str)
    #     finally:
    #         # Always free the memory, even if decoding fails
    #         # lib.FreeCString(result_ptr)
    #         # lib.free(result_ptr)
    #         # print('done')
    #         pass
    # except Exception as e:
    #     print(f"Error parsing user agent: {e}")
    #     return None
    pass

# Example usage
if __name__ == "__main__":
    """
    Example Benchmarking test.

    1/26/25
    
    Go Implementation:
    Time taken: 1.3010361194610596 seconds. Average time per call: 0.0013010361194610595 seconds
    Python Implementation:
    Time taken: 48.9687340259552 seconds. Average time per call: 0.0489687340259552 seconds
    Python is 37.63825868742213 times slower than Go
    """
    import time
    user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
    N = 100_000
    start_time = time.time()
    for i in range(N):
        parse_user_agent(user_agent + str(i))
    end_time = time.time()
    go_time = end_time - start_time
    print(f"Go Implementation:\nTime taken: {end_time - start_time} seconds. Average time per call: {(end_time - start_time) / 1000} seconds")

    from user_agents import parse
    start_time = time.time()
    for i in range(N):
        parse(user_agent + str(i))
    end_time = time.time()
    python_time = end_time - start_time
    print(f"Python Implementation:\nTime taken: {end_time - start_time} seconds. Average time per call: {(end_time - start_time) / 1000} seconds")

    print(f"Python is {python_time /go_time} times slower than Go")
    pass