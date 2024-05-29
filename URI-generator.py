def generate_uris(strings, predefined_strs):
    # 生成不带预定义字符串和带有预定义字符串的 URI 列表
    uris = []
    for s1 in strings:
        # 添加单独的字符串 URI (不带预定义字符串)
        uris.append(f"/{s1}")
        uris.append(f"/{s1}/")
        
        for predefined_str in predefined_strs:
            # 组合预定义字符串和当前字符串
            combined = f"{s1}{predefined_str}"

            # 添加单独的字符串 URI (带预定义字符串)
            uris.append(f"/{combined}")
            uris.append(f"/{combined}/")

            # 添加带斜杠的预定义字符串到 URI 中
            uris.append(f"/{s1}/{predefined_str}")
            uris.append(f"/{s1}/{predefined_str}/")
            
            for s2 in strings:
                if s1 != s2:
                    # 添加当前字符串和其他字符串的组合 URI (不带预定义字符串)
                    uris.append(f"/{s1}/{s2}")

                    # 添加当前字符串和其他字符串的组合 URI (带预定义字符串)
                    uris.append(f"/{combined}/{s2}")
                    uris.append(f"/{s2}/{combined}")

    # 删除可能重复生成的 URI
    uris = list(set(uris))
    
    return uris

def main():
    # 预定义字符的列表
    predefined_strs = ["pic", "doc", "admin", "login","bak","backup","api","video","log","edit","bbs","tmp","manage","web","upload","txt","editor","inc","images","data","db","v1","image","v2","v3"]

    # 接收用户输入
    user_input = input("请输入多个字符串，用逗号分隔开: ")

    # 根据逗号分割输入字符串
    strings = user_input.split(',')

    # 去除字符串中的首尾空格
    strings = [s.strip() for s in strings]

    # 生成 URI 列表
    uris = generate_uris(strings, predefined_strs)

    # 打印出生成的 URI 列表
    print("包含原始字符串和预定义字符拼接后的 URI 列表如下：")
    for uri in sorted(uris):
        print(uri)

    # 指定输出文件名称
    output_filename = 'diy-dir.txt'

    # 打开（或创建）文件并写入内容，'w'模式会覆盖文件
    with open(output_filename, 'w', encoding='utf-8') as file:
        for uri in sorted(uris):
            file.write(uri + '\n')
    
    # 打印导出成功的消息
    print(f"URI列表已经导出到文件: {output_filename}")

if __name__ == "__main__":
    main()
        