import re
from Utils import openCV_util
def get_post_line():
    result = openCV_util.get_line()
    match_regex = re.compile(u'[\u4e00-\u9fa5\\|\u3040-\u30ff。.,，:：《》、\\(\\)（）]{1} +(?<![a-zA-Z])|\\d+ +| +\\d+|[a-z A-Z]+')
    should_replace_list = match_regex.findall(result)
    order_replace_list = sorted(should_replace_list, key=lambda i: len(i), reverse=True)
    for i in order_replace_list:
        if i == u' ':
            continue
        new_i = i.strip()
        result = result.replace(i, new_i)
    print(result)
    print("////////////")
    return result
# result = openCV_util.get_line()
# match_regex = re.compile(u'[\u4e00-\u9fa5\\|\u3040-\u30ff。.,，:：《》、\\(\\)（）]{1} +(?<![a-zA-Z])|\\d+ +| +\\d+|[a-z A-Z]+')
# should_replace_list = match_regex.findall(result)
# order_replace_list = sorted(should_replace_list, key=lambda i: len(i), reverse=True)
# for i in order_replace_list:
#     if i == u' ':
#         continue
#     new_i = i.strip()
#     result = result.replace(i, new_i)
# //////////////////////////////////////////
# lines = result.replace("\n\n","\n")
# lines = lines.splitlines()
# for line in lines:
#     print(line)
# if __name__ == "__main__":
#     get_post_line(
#
#     )