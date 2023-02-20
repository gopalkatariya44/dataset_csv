import os

start = 296
end = 494
try_count = 0

if __name__ == '__main__':
    while True:
        if start == end + 1:
            break
        try:
            print("|--------------------------------------|")
            print(f"| {start}'s training start....")
            log = os.system(f"curl -X 'POST' \
                        'http://0.0.0.0:8080/start_training/?exp_id={start}' \
                        -H 'accept: application/json' \
                        -d ''")
            if log == 0:
                start += 1
                print(f"| {start}'s training end.")
                print("|--------------------------------------|")
            elif try_count == 6:
                start += 1
                print(f"| {start}'s training error.")
                print("|--------------------------------------|")
            else:
                try_count += 1
        except Exception as e:
            print(f"| error : {e}")
            print("|--------------------------------------|")
