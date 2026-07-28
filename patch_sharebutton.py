import re
import sys

path = sys.argv[1]
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Bo'shliq/joylashuvga chidamli (whitespace-tolerant) qidiruv
pattern = re.compile(
    r"if\s*\(\s*drawSideButton\s*==\s*1\s*\|\|\s*drawSideButton\s*==\s*2\s*\)\s*\{\s*"
    r"info\.addChild\(ChatMessageCell\.this,\s*SHARE\);\s*"
    r"\}"
)

if not pattern.search(content):
    print("OGOHLANTIRISH: ChatMessageCell.java - ulashish tugmasi bloki topilmadi, bu patch o'tkazib yuborildi")
else:
    content = pattern.sub(
        "// TalkBack uchun ulashish tugmasi o'chirilgan - foydalanuvchi so'rovi bo'yicha\n"
        "            // if (drawSideButton == 1 || drawSideButton == 2) {\n"
        "            //     info.addChild(ChatMessageCell.this, SHARE);\n"
        "            // }",
        content,
        count=1
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("ChatMessageCell.java - ulashish tugmasi TalkBack'dan yashirildi")
